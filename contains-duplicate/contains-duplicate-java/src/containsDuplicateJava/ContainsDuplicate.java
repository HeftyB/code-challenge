/*
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true

*/

// # in order to check if an array contains any duplicates:

// # FIRST SOLUTION
// # make a set from the array (set will ignore duplicates)
// # compare length of set to length of array
// # if length is == return true else return false


// # SECOND SOLUTION
// # make a hashtable for the array with each item as the key and a count of occurances as valuus
// # loop through the hashtable and return true if any value is > 0

// # THIRD SOLUTION
// # LOOP THROUGH EACH ITEM IN THE ARRAY
// # FOR EACH ITERATION OF LOOP LOOP THROUGH THE WHOLE ARRAY AGAIN(EXCLUDING CURRENT ITEM) AND RETURN TRUE IF A MATCH IS FOUND


package containsDuplicateJava;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class ContainsDuplicate
{
    public static void main(String[] args) 
    {
        List newList1 = new ArrayList<>();
        List newList2 = new ArrayList<>();
        List newList3 = new ArrayList<>();

        newList1.add(1);
        newList1.add(2);
        newList1.add(3);
        newList1.add(1);

        newList2.add(1);
        newList2.add(2);
        newList2.add(3);
        newList2.add(4);

        newList3.add(1);
        newList3.add(1);
        newList3.add(1);
        newList3.add(3);
        newList3.add(3);
        newList3.add(4);
        newList3.add(3);
        newList3.add(2);
        newList3.add(4);
        newList3.add(2);

        firstSolution(newList1);
        firstSolution(newList2);
        firstSolution(newList3);

    }

    public static boolean firstSolution(List l1) 
    {
        
        Set set1 = new HashSet<>(l1);

        if (set1.size() == l1.size())
        {
            System.out.println("false");
            return false;
        }
        System.out.println("true");
        return true;
    }
}
 