# XML to JSON #

### Description ##
This application takes in .xml files containing seatmaps and saves a standard JSON object in a seperate file matching original filename under the directory "json_output"

### Usage ###

```
python3 seatmap_parsey.py [optional:flags] filename1.xml filename2.xml
```
Required:
- Minimum 1 filename

Flags:
- "-C" - returns JSON seatmap sorted by cabins instead of rows

outputs:
```
createdfilename.json
createdfilename2.json
```
saves in "json_output" directory in root folder, is created if doesn't exist


### Reflection / Ideas for imporvement ###
- make parser class based
- impement customer xml parser  
    - import xml file as string
    - make custom node class for xml elements with useful methods such as has/getChildren(), getParent(), childContains(), and mapChildren()
        - parent node retains map of children for easier traversal / item lookup
    - parse xml string creating and mapping a linked node for each element into a tree
- refactor to improve time / space complexity 


