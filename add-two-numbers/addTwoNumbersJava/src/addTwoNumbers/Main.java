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
import java.util.ArrayList;
import java.util.List;

import addTwoNumbers.ListNode;

public class Main
{
	public static ListNode addTwoNumbers(ListNode l1, ListNode l2)
	{

		int counter = 1;

		List<ListNode> list1 = new ArrayList<>();
		List<ListNode> list2 = new ArrayList<>();		

		ListNode current = l1;

		list1.add(l1);

		while (current.getHasNext())
		{	list1.add(current.getNext());
			current = current.getNext();
			counter++;
		}

		ListNode currents = l2;

		list2.add(l2);

		while (currents.getHasNext())
		{
			list2.add(currents.getNext());
			currents = currents.getNext();
		}
		System.out.println(counter);
		System.out.println(l1);
		System.out.println(l2);
		return l1;
	}

	public static void main(String []

	args)

	{
		ListNode l11 = new ListNode(3);
		ListNode l12 = new ListNode(4, l11);
		ListNode l13 = new ListNode(2, l12);

		ListNode l21 = new ListNode(4);
		ListNode l22 = new ListNode(6, l21);
		ListNode l23 = new ListNode(5, l22);

		addTwoNumbers(l13, l23);
	}
}