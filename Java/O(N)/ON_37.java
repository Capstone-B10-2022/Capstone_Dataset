// Java implementation to check 
// that a given string can be 
// converted to another string 
// by circular clockwise shift 
// of each character by atmost 
// X times 
import java.io.*;
import java.util.*;
  
class ON_37{
      
// Function to check that all 
// characters of s1 can be 
// converted to s2 by circular 
// clockwise shift atmost X times 
static void isConversionPossible(String s1, 
                                 String s2,
                                 int x) 
{ 
    int diff = 0, n; 
    n = s1.length(); 
      
    // Check for all characters of 
    // the strings whether the 
    // difference between their 
    // ascii values is less than 
    // X or not 
    for(int i = 0; i < n; i++) 
    {
          
       // If both the characters 
       // are same 
       if (s1.charAt(i) == s2.charAt(i))
           continue; 
         
       // Calculate the difference 
       // between the ASCII values 
       // of the characters 
       diff = ((int)(s2.charAt(i) - 
                     s1.charAt(i)) + 26) % 26; 
         
       // If difference exceeds X 
       if (diff > x)
       { 
           System.out.println("NO"); 
           return; 
       } 
    } 
    System.out.println("YES");
} 
      
// Driver Code
public static void main (String[] args)
{
    String s1 = "you"; 
    String s2 = "ara"; 
  
    int x = 6; 
  
    // Function call 
    isConversionPossible(s1, s2, x); 
}
}
