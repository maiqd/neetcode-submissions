public class LinkedList {
    private class Node {
        public Node(int value,Node next) {
            this.Value = value;
            this.Next = next;
        }
        public int Value { get; set; }
        public Node Next { get; set; }
    }
    private Node head;

    public LinkedList() {
        head = new Node(-1, null);
    }

    public int Get(int index) {
        var cur = head;
        var i = 0;
        while (i <= index) {
            cur = cur.Next;
            if (cur == null) {
                return -1;
            }
            i++;
        }
        return cur.Value;
    }

    public void InsertHead(int val) {
        var next = head.Next;
        head.Next = new Node(val, next);
    }

    public void InsertTail(int val) {
        var cur = head;
        while (cur.Next != null) {
            cur = cur.Next;
        }
        cur.Next = new Node(val, null);
    }

    public bool Remove(int index) {
        var preCur = head;
        var i = 0;
        while (i < index) {
            preCur = preCur.Next;
            if (preCur == null) {
                return false;
            }
            i++;
        }
        if (preCur.Next == null) {
            return false;
        }
        preCur.Next = preCur.Next.Next;
        return true;
    }

    public List<int> GetValues() {
        var res = new List<int>();
        var cur = head.Next;
        while (cur != null) {
            res.Add(cur.Value);
            cur = cur.Next;
        }
        return res;
    }
}