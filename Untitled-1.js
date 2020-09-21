function test (str) {
    // console.log("It's working!")
    // console.log(str[0])
    returnString = "";
    counter = 0;
    char = ""
    // console.log(str[0].length)
    for (let i = 0; i < str[0].length; i++) {
        // console.log("loop")
        // console.log(i)
        for (j = 1; j < str.length; j++) {
            // console.log(str[0])
            counter = 0
            if (str[0][i] == str[j][i]) {
                
                counter++;
                char = str[0][i];
            }
        if (counter == str.length) {
            returnString = returnString + char;
        }
        }
    }
    if (returnString.length == 0) {
        return "NO LENGTH"
    } else {
        return returnString;
    }
}


arry = ["flower" , "flow", "flight"]


console.log(test(arry));