import java.util.Scanner;
 public class Discussion
 {  
   public static void main(String[] args)  
   {    
     Scanner stdIn = new Scanner(System.in);    
     double deposit;  // number of money to deposit    
     double withdraw;       // number of moeny withdrawn

     System.out.print("How much you want to deposit: ");   
     deposit = stdIn.nextDouble();    
     System.out.print("How much money you want to withdraw: ");    
     withdraw = stdIn.nextDouble();    
     System.out.print("Amount of money left in your account = $" + (deposit -withdraw)); 
    } // end main
  } // end class PrintPO