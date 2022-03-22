using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace Palindrom
{
    class Program
    {
        static void Main(string[] args)
        {
            bool checkPalindrom(string s)
            {
                s = s.ToLower();
                s = Regex.Replace(s, @"[^a-züöäß]+", String.Empty);

                for(int i=0, j = s.Length -1 ; i < j ; i++, j-- )
                {
                    if (s[i] != s[j])
                    {
                        Console.WriteLine("The string is not a  palindrom");
                        return false;
                    }
                        
                }
                Console.WriteLine("The string is a palindrom");
                return true;
            }
            
            string testString = Console.ReadLine();
            checkPalindrom(testString); 
            Console.ReadKey();
        }
    }
}
