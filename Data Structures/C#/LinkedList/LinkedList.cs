using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace myNamespace
{
    public class Node
    {
        public int value;
        public Node next = null;

        public Node(int value)
        {
            this.value = value;
        }
    }

    class LinkedList
    {

        Node head = null;

        public LinkedList(int[] input)
        {
            foreach (int x in input)
                this.addToEnd(x);
        }

        public void addToStart(int val)
        {
            Node n = new Node(val);
            n.next = this.head;
            this.head = n;
        }

        public void addToEnd(int val)
        {
            Node n = this.head;
            if(n == null)
            {
                this.head = new Node(val);
            }else
            {
                while (n.next != null)
                {
                    n = n.next;
                }

                n.next = new Node(val);
            }
        }

        public int[] toArray()
        {
            Node n = this.head;
            if (n == null)
            {
                return new int[] { };
            }
            else
            {
                int[] arr = new int[100];
                int index = 0;

                while (n.next != null)
                {
                    arr[index] = n.value;
                    index++;
                    n = n.next;
                }

                arr[index] = n.value;
                int[] shortArr = new int[index + 1];

                for (int i = 0; i <= index; i++)
                    shortArr[i] = arr[i];           

                return shortArr;
            }
        }

        public Node get(int index)
        {
            if (this.head == null)
                throw new Exception("The list is empty.");
            Node n = this.head;
            for(int i = 0; i < index; i++)
            {
                n = n.next;
                if (n == null)
                    throw new Exception("Index out of bounds");
            }

            return n;
        }

        public Node remove(int index)
        {
            Node n = this.head;
            if (n == null)
                throw new Exception("The list is empty.");
            if (index == 0)
            {               
                this.head = n.next;
                return n;
            }
            else
            {
                Node previous = new Node(0);
                previous.next = n;
                for (int i = 0; i < index; i++)
                {
                    previous = previous.next;
                    n = n.next;
                    if (n == null)
                        throw new Exception("Index out of bounds");
                }   

                previous.next = n.next;

                return n;
            }            
        }

        public void insert(int index, int val)
        {
            Node n = this.head;
            Node previous = new Node(0);
            previous.next = n;
            for (int i = 0; i < index; i++)
            {
                previous = previous.next;
                n = n.next;
                if (n == null)
                    throw new Exception("Index out of bounds");
            }

            Node newNode = new Node(val);
            previous.next = newNode; 
            newNode.next = n;                        
        }
    }
}