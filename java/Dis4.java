import java.util.Scanner;
 public class Dis4
 {
   public static void main(String[] args)
   {
     Scanner stdIn = new Scanner(System.in);
     double makes;  // number shots made
     double goal;       // number of shots to make
     System.out.print("how many shots do you have to take before you leave.: ");
     goal = stdIn.nextDouble();
     System.out.print("how many shots did you make: ");
     makes = stdIn.nextDouble();
     if (goal == makes)
     {
      System.out.print("You can leave now:");
     }
     else
     {
    System.out.print("Just keep shooting:");
     }
    } // end main
  } // end class Dis4
