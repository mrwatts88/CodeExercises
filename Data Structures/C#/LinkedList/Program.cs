using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace myNamespace
{
    class Program
    {
        static void Main(string[] args)
        {
            LinkedList ll = new LinkedList(new int[] { 3, 4, 3, 5, 5 });

            ll.addToStart(99);
            ll.addToEnd(88);
            int[] llArray = ll.toArray();
            foreach (int x in llArray)
                Console.WriteLine(x);

            try
            {
                Console.WriteLine(ll.get(6).value);
            }
            catch (Exception e)
            {
                Console.WriteLine(e);
            }

            try
            {
                ll.remove(2);
            }
            catch (Exception e)
            {
                Console.WriteLine(e);
            }

            int[] llArray2 = ll.toArray();

            foreach (int x in llArray2)
                Console.WriteLine(x);

            try
            {
                ll.insert(4,666);
            }
            catch (Exception e)
            {
                Console.WriteLine(e);
            }

            int[] llArray3 = ll.toArray();

            foreach (int x in llArray3)
                Console.WriteLine(x);

            Console.ReadKey();
        }
    }
}
