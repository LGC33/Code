/*************************************************************
* BridalRegistry.java* Larry Grace
*
* This makes entries in a bridal registry.
*************************************************************/
import java.util.Scanner;

public class BridalRegistry
{  
  public static void main(String[] args)  
  {    
    Scanner stdIn = new Scanner(System.in);    
    String registry = "";    
    char more;     

    System.out.print(   
      "Do you wish to create a bridal registry list? (y/n): ");   
     more = stdIn.nextLine().charAt(0);    


     while (more == 'y')    
     {      
       System.out.print("Enter item: ");      
       registry += stdIn.nextLine() + " - ";      
       System.out.print("Enter store: ");      
       registry += stdIn.nextLine() + "\n";      
       System.out.print("Any more items? (y/n): ");      
       more = stdIn.nextLine().charAt(0);    
     } // end while    
     if (!registry.equals(""))    
     {      
       System.out.println("\nBridal Registry:\n" + registry);    
     }  
  } // end main
} // end BridalRegistry class