package addTwoNumbers;

public class ListNode {
    private static int maxId = 0;
    private long id;
    private int value;
    private ListNode next;
    private boolean hasNext;

    public ListNode (int value, ListNode next)
    {
        maxId++;
        id = maxId;
        this.value = value;
        this.next = next;
        this.hasNext = true;
    }

    public ListNode (int value)
    {
        maxId++;
        id = maxId;
        this.value = value;
        // this.next = false;
        this.hasNext = false;
    }

    public int getValue ()
    {
        return value;
    } 

    public void setValue (int value)
    {
        this.value = value;
    }

    public ListNode getNext ()
    {
        return next;
    }

    public void setNext (ListNode next)
    {
        this.next = next;
    }

    public boolean  getHasNext ()
    {
        return hasNext;
    }

    public void setHasNext (boolean x)
    {
        hasNext = x;
    }

    @Override
    public String toString ()
    {
        return 
        //"Id is " + id + ", " + 
        "value is " + value + ", next is " + next;
    }
    
}
