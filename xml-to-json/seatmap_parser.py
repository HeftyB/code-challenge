import sys
import os
import json
import xml.etree.ElementTree as et
from datetime import datetime


"""
returns dictionary of needed data sorted by flight #
"""  
def parseXML(path):

    if not path.lower().endswith(".xml"):
        errors.append(f"the file {path} is not a compatible .xml file")
        return {}

    tree = et.parse(path)
    root = tree.getroot()

    """
    check if root tag matches tags used in known .xml files
    """
    if root.tag == "{http://www.iata.org/IATA/EDIST/2017.2}SeatAvailabilityRS":
        if root.attrib["Version"] != "17.2":
            print(f"File: {path} tag:{root.tag} version:{root.attrib['Version']} is unsupported which may result in errors!")

        return seat_availability_rsV17(root)

    elif root.tag == "{http://schemas.xmlsoap.org/soap/envelope/}Envelope":
        for i in root.iter("{http://www.opentravel.org/OTA/2003/05/common/}OTA_AirSeatMapRS"):
            if i.attrib["Version"] != "1":
                print(f"File {path} tag:{i.tag} version:{i.attrib['Version']} is unsupported which may result in errors!")

            return ota_air_seatmap_rsV1(i)

    return {}


"""
saves python object to .json file
returns created filename
"""
def saveFileJSON(dicts, name):

    if not os.path.exists("./json_output/"):
        try:
            os.mkdir("./json_output")
        except OSError as error:
            print(f"Error creating/accessing output directory '/json_output': {error}")
            sys.exit(1)        

    with open(f"./json_output/{name}.json" , "w") as file:
        json.dump(dicts, file)

    return f"{name}.json"

"""
returns base file stripped of extensions and paths
"""
def filename(path):

    str1 = path.replace(".xml", "")

    """
    check if path contains Windows or other os directories
    """
    if str1.rfind("\\") != -1:
        strarr = str1.split("\\")
    elif str1.rfind("/") != -1:
        strarr = str1.split("/")
    else:
        strarr = [str1]
    
    return strarr[-1]

"""
used for seatmap1.xml
"""
def ota_air_seatmap_rsV1(tree):

    default_type = "Seat"
    default_currency = "USD"
    dicts = {}

    for e in tree.iter("{http://www.opentravel.org/OTA/2003/05/common/}SeatMapResponse"):
        flight_info = e.find("{http://www.opentravel.org/OTA/2003/05/common/}FlightSegmentInfo")
        date_time_obj = datetime.strptime(flight_info.attrib["DepartureDateTime"], "%Y-%m-%dT%H:%M:%S")
        flight_num = flight_info.attrib["FlightNumber"]
        dep_airport = flight_info.find("{http://www.opentravel.org/OTA/2003/05/common/}DepartureAirport").attrib["LocationCode"]
        arr_airport = flight_info.find("{http://www.opentravel.org/OTA/2003/05/common/}ArrivalAirport").attrib["LocationCode"]
        model = flight_info.find("{http://www.opentravel.org/OTA/2003/05/common/}Equipment").attrib["AirEquipType"]

        cabins = {}
        counter = 1
        sort = []

        """
        iterate through cabins
        """
        for c in e.iter("{http://www.opentravel.org/OTA/2003/05/common/}CabinClass"):
            layout = c.attrib["Layout"]

            rows = {}

            """
            iterate through rows
            """
            for r in c.iter("{http://www.opentravel.org/OTA/2003/05/common/}RowInfo"):
                row_num = r.attrib["RowNumber"]
                cabin_type = r.attrib["CabinType"]
                seats = {}
                
                """
                iterate through seats
                """
                for s in r.iter("{http://www.opentravel.org/OTA/2003/05/common/}SeatInfo"):
                    seat_info = []
                    items = s.items()
                    seat_type = default_type
                    column_num = None
                    service = None
                    service_code = None
                    fee = None
                    taxes = None
                    price = {}
                    bulk = False
                    exit_row = False
                    wing = False
                    aisle = False
                    window = False
                    
                    """
                    iterate through seat attributes
                    """
                    for item in items:
                        if item[0] == "ColumnNumber":
                            column_num = int(item[1])
                        elif item[1] == "true":
                            if item[0] == "ExitRowInd":
                                exit_row = True
                            seat_info.append(item[0].replace("Ind", ""))

                        if item[0] == "BulkheadInd":
                            bulk = True


                    summary = s.find("{http://www.opentravel.org/OTA/2003/05/common/}Summary")
                    available = True if summary.attrib["AvailableInd"] == "true" else False
                    seat_num = summary.attrib["SeatNumber"]
                    features = []

                    """
                    iterate through features
                    """
                    for f in s.iter("{http://www.opentravel.org/OTA/2003/05/common/}Features"):
                        if f.text != "Other_":
                            features.append(f.text)
                            if f.text == "Aisle":
                                aisle = True
                            elif f.text == "Overwing":
                                wing = True
                            elif f.text == "Window":
                                window = True
                            elif f.text == "BlockedSeat_Permanent" and bulk:
                                seat_type = "Bulkhead"
                        else:
                            features.append(f.attrib["extension"])
                            if f.attrib["extension"] == "Lavatory":
                                seat_type = "Lavatory"
                                                

                    if available:
                        service = s.find("{http://www.opentravel.org/OTA/2003/05/common/}Service")
                        service_code = service.attrib["CodeContext"]

                        """
                        incase multiple prices / currency
                        """
                        for fee in service.iter("{http://www.opentravel.org/OTA/2003/05/common/}Fee"):
                            taxes = fee.find("{http://www.opentravel.org/OTA/2003/05/common/}Taxes")
                            currency = fee.attrib["CurrencyCode"]
                            price[currency] = float(fee.attrib["Amount"]) + float(taxes.attrib["Amount"])

                    seat = {}
                    seat["seatId"] = seat_num
                    seat["type"] = seat_type
                    seat["class"] = cabin_type
                    seat["features"] = features
                    seat["addInfo"] = seat_info
                    seat["price"] = price[default_currency] if available else None
                    seat["currency"] = default_currency if available else None
                    seat["available"] = available
                    seat["exit"] = exit_row
                    seat["wing"] = wing
                    seat["aisle"] = aisle
                    seat["window"] = window

                    seats[layout[column_num - 1]] = seat



                rows[f"row {row_num}"] = {
                    "cabinType": cabin_type,
                    "seats": seats
                }



            if cabin_format:
                cabins[f"cabin {counter}"] = rows
                counter += 1
            else:
                for key, value in rows.items():
                    sort.append({
                        key: value
                    })
        
        
        """
        sort
        """
        if cabin_format:
            for key, value in cabins.items():
                sort.append({
                    key:value
                })

        sort.sort(key=sort_by_rownum)


        dicts[flight_num] = {
            "flightNum": flight_num,
            "date": str(datetime.date(date_time_obj)),
            "time": str(datetime.time(date_time_obj)),
            "depAirport": dep_airport,
            "arrAirport": arr_airport,
            "model": model,
            "cabins" if cabin_format else "rows": sort
        }

    return dicts


"""
used for seatmap2.xml
"""
def seat_availability_rsV17(tree):
    dicts = {}
    offers = {}
    service_def = {}
    seat_def = {}
    flight_segments = {}
    flight_ref = {}
    cab = {}
    availibility_def = None
    exit_def = None
    wing_def = None
    aisle_def = None
    window_def = None
    default_class = "Economy"
    default_type = "Seat"
    default_currency = "GBP"


    """
    iterate through offers for later reference
    """
    for o in tree.iter("{http://www.iata.org/IATA/EDIST/2017.2}ALaCarteOfferItem"):

        """
        incase offer is for multiple flights
        """
        segment_ref = []
        for ref in o.iter("{http://www.iata.org/IATA/EDIST/2017.2}SegmentRefs"):
            segment_ref.append(ref.text)


        """
        incase offer has multiple prices / currency
        """
        price = {}
        for cur_price in o.iter("{http://www.iata.org/IATA/EDIST/2017.2}SimpleCurrencyPrice"):
            price[cur_price.attrib["Code"]] = cur_price.text


        service_id = o.find("{http://www.iata.org/IATA/EDIST/2017.2}Service").attrib["ServiceID"]
        
        offers[o.attrib["OfferItemID"]] = {
            "price": price,
            "segment_ref": segment_ref,
            "service_id": service_id
        }


    """
    iterate through service definitions for later reference, 
        not used but may be useful for future dev
    """
    """
    for serdef in tree.iter("{http://www.iata.org/IATA/EDIST/2017.2}ServiceDefinition"):
        id = serdef.attrib["ServiceDefinitionID"]
        name = serdef.find("{http://www.iata.org/IATA/EDIST/2017.2}Name")
        descriptions_elm = serdef.find("{http://www.iata.org/IATA/EDIST/2017.2}Descriptions")
        description = get_description(descriptions_elm.find("{http://www.iata.org/IATA/EDIST/2017.2}Description"))

        # for des in serdef.iter("{http://www.iata.org/IATA/EDIST/2017.2}Description"):
        #     descriptions.append(des.find("{http://www.iata.org/IATA/EDIST/2017.2}Text"))

        service_def[id] = {
            "id": id,
            "name": name,
            "description": description
        }
    """


    """
    iterate through seat definitions for later reference
    """
    for seatdef in tree.iter("{http://www.iata.org/IATA/EDIST/2017.2}SeatDefinition"):
        id = seatdef.attrib["SeatDefinitionID"]
        description = get_description(seatdef.find("{http://www.iata.org/IATA/EDIST/2017.2}Description"))

        """
        sets relevent seatdef for flagging seat later
        """
        if description == "AVAILABLE":
            availibility_def = id

        elif description == "EXIT":
            exit_def = id

        elif description == "WING":
            wing_def = id

        elif description == "AISLE_SEAT":
            aisle_def = id

        elif description == "WINDOW":
            window_def = id

        seat_def[id] = description


    """
    iterate through flight segments for reference later
    incase multiple flights
    """
    for f_seg in tree.iter("{http://www.iata.org/IATA/EDIST/2017.2}FlightSegment"):
        departure = f_seg.find("{http://www.iata.org/IATA/EDIST/2017.2}Departure")

        seg_key =  f_seg.attrib["SegmentKey"]
        flight_num = f_seg.find("{http://www.iata.org/IATA/EDIST/2017.2}MarketingCarrier").find("{http://www.iata.org/IATA/EDIST/2017.2}FlightNumber").text
        date = departure.find("{http://www.iata.org/IATA/EDIST/2017.2}Date").text
        time = departure.find("{http://www.iata.org/IATA/EDIST/2017.2}Time").text
        dep_airport = departure.find("{http://www.iata.org/IATA/EDIST/2017.2}AirportCode").text
        arr_airport = f_seg.find("{http://www.iata.org/IATA/EDIST/2017.2}Arrival").find("{http://www.iata.org/IATA/EDIST/2017.2}AirportCode").text
        model = f_seg.find("{http://www.iata.org/IATA/EDIST/2017.2}Equipment").find("{http://www.iata.org/IATA/EDIST/2017.2}AircraftCode").text

        flight_ref[flight_num] = seg_key
        
        flight_segments[seg_key] = {
            "flight_num": flight_num,
            "date": date,
            "time": time,
            "dep_airport": dep_airport,
            "arr_airport": arr_airport,
            "model": model
        }

    
    """
    iterate through seatmaps and store by row / cabin per cabin_format
    """
    ma = {}
    counters = 1
    counter = 1
    
    for m in tree.iter("{http://www.iata.org/IATA/EDIST/2017.2}SeatMap"):
        seg_ref = m.find("{http://www.iata.org/IATA/EDIST/2017.2}SegmentRef").text

        cabins = {}
        
        """
        iterate through each cabin in seat map
        """
        for cabin in m.iter("{http://www.iata.org/IATA/EDIST/2017.2}Cabin"):

            rows = {}

            """
            iterate through each row in cabin
            """
            for row in cabin.iter("{http://www.iata.org/IATA/EDIST/2017.2}Row"):
                row_num = row.find("{http://www.iata.org/IATA/EDIST/2017.2}Number").text

                seats = {}

                """
                iterate through each seat in row
                """
                for seat in row.iter("{http://www.iata.org/IATA/EDIST/2017.2}Seat"):
                    col = seat.find("{http://www.iata.org/IATA/EDIST/2017.2}Column").text
                    seat_offers = []
                    seats_def = []
                    prices = {}
                    available = False
                    e = False
                    wing = False
                    aisle = False
                    window = False

                    """
                    add each offer for seat
                    """
                    for off in seat.iter("{http://www.iata.org/IATA/EDIST/2017.2}OfferItemRefs"):
                        seat_offers.append(offers[off.text])

                        if offers[off.text]["segment_ref"] == segment_ref:
                            prices[default_currency] = offers[off.text]["price"][default_currency]

                    """
                    add each seatdef 
                    """
                    for sdef in seat.iter("{http://www.iata.org/IATA/EDIST/2017.2}SeatDefinitionRef"):

                        if sdef.text == availibility_def:
                            available = True

                        elif sdef.text == exit_def:
                            e = True

                        elif sdef.text == wing_def:
                            wing = True

                        elif sdef.text == aisle_def:
                            aisle= True

                        elif sdef.text == window_def:
                            window = True

                        seats_def.append(seat_def[sdef.text])

                    s = {
                        "seatId": row_num + col,
                        "type": default_type,
                        "class": default_class,
                        "features":  seats_def,
                        "addInfo":  [],
                        "price": price[default_currency] if available == True else None,
                        "currency": default_currency,
                        "available":  available,
                        "exit":  e,
                        "wing": wing,
                        "aisle": aisle,
                        "window": window
                    }

                    seats[col] = s



                rows[f"row {row_num}"] = {
                    "cabinType": default_class,
                    "seats": seats
                }

            rows_sorted = list(rows.keys())
            rows_sorted.sort(key=s_to_int)

            if cabin_format:
                rows_sorted_dicts = {k:rows[k] for k in rows_sorted}
                cabins[f"cabin {counter}"] = rows_sorted_dicts
                counter += 1
            else:
                for r in rows_sorted:
                    cabins[r] = rows[r]
 
        c = cabins.copy() 

        ma[counters] = {
            "cabins": c,
            "seg_ref": seg_ref
        }
        counters += 1


    """
    if multuple flight segments / seat maps this matches cabin to flightNum
    """
    for key,value in ma.items():
        if flight_segments[value["seg_ref"]]["flight_num"] not in cab:
            cab[flight_segments[value["seg_ref"]]["flight_num"]] = []

        cab[flight_segments[value["seg_ref"]]["flight_num"]].append(value["cabins"])


    """
    sort and add
    """
    for keyy, value in cab.items():
        items = []

        if cabin_format:
            value.sort(key=sort_by_rownum)
        else:
            for item in value:
                for keey, value in item.items():
                    items.append({
                        keey: value
                    })

            items.sort(key=sort_by_rownum)


        segstr = flight_ref[keyy]

        seg = flight_segments[segstr]

        dicts[seg["flight_num"]] = {
        "flightNum": seg["flight_num"],
        "date": seg["date"],
        "time": seg["time"],
        "depAirport": seg["dep_airport"],
        "arrAirport": seg["arr_airport"],
        "model": seg["model"],
        "cabins" if cabin_format else "rows": value if cabin_format else items
    }

    return dicts


"""
helper fuction to covert strings to ints
    ex: "row 5" -> 5, "10" -> 10 
"""
def s_to_int(v):
    if not v.isnumeric():
        v = last_digit_st(v)
    return int(v)

"""
helper function to sort dictionaries by key 
    ex: [{"row 11": seats}, {"row 10": seats}] -> [{"row 10": seats}, {"row 11": seats}]
"""
def sort_by_rownum(v):
    for key, value in v.items():
        st = key
        if not st.isnumeric():
            st = last_digit_st(st)
        return int(st)

"""
returns the last numerical chars of a string or -1 if st[-1] not numerical
    ex: "row 10" -> "10" / "row 10R" -> -1
"""
def last_digit_st(st):
    if not st[-1].isnumeric():
        return -1
    final_dex = len(st) - 1

    counter = final_dex

    for i in reversed(st):
        if not i.isnumeric():
            final_dex = counter
            break
        counter -= 1
    
    ret = st[final_dex:]
    return ret

"""
returns text from description node
"""
def get_description(iter):
    return iter.find("{http://www.iata.org/IATA/EDIST/2017.2}Text").text



def main(args):
    """
    check args for minimum of 1
    """
    if len(args) < 1:
        sys.exit("file name is required \nusage: python3 seatmap_parser.py file1.xml")

    files = []

    """
    for multiple files
    """
    for path in args:
        """
        extract data from xml to dictionary
        """
        dicts = parseXML(path)

        """
        extract filename from path
        """
        name = filename(path) 

        if not dicts:
            continue

        files.append(saveFileJSON(dicts, name))

    for e in errors:
        print(f"Parsing error: {e}")

    for f in files:
        print(f"Created: {f}")

    if not files:
        sys.exit("Error!")
        
    sys.exit(0)


if __name__ == "__main__":
    args = None
    cabin_format = False
    errors= []

    if sys.argv[1] == "-C":    
        cabin_format = True
        args = sys.argv[2:]
    else:
        args = sys.argv[1:]
        
    main(args)