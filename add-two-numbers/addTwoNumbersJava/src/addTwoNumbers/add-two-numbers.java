/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

package addTwoNumbers;

import java.lang.Math;
public class Main
{
	private static void main(String []

	args)

	{

	}


	class Solution
	{
		public ListNode addTwoNumbers(
		{
			ListNode l1,
			ListNode l2)

			int counter = 1;

			ListNode current = l1;

			while current.next
			{
				current = current.next;
				counter++;
			}

			System.out.println(counter);

		}
	}

}