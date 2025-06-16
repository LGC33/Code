/*-------------------------------------------------------
* TechDriver.java
* Author: Larry Grace

* Driver Class for Tech
--------------------------------------------------------*/
import java.util.Scanner;

public class TechDriver {
  public static void main(String[] args) {
    Scanner stdIn = new Scanner(System.in);

    String techFirstName = "";	// current tech's first name
    String techLastName = "";		// current tech's last name
    String techTitle = "";			// current tech's Title
    int	   techAge = 0;			// current tech's age

    String response =""; 			// Auxiliar variable to get responses
    tech atech;					// Auxiliar tech object

    do {
		System.out.print("Indicate tech's first name: ");
		techFirstName = stdIn.nextLine();
		System.out.print("Indicate tech's last name: ");
		techLastName = stdIn.nextLine();
		System.out.print("Indicate tech's Title: ");
		techTitle = stdIn.nextLine();
		System.out.print("Indicate tech's age: ");
		techAge = Integer.parseInt(stdIn.nextLine());

		atech = new tech(techFirstName, techLastName, techTitle, techAge);
		System.out.println(atech);
		System.out.print("Any other tech to process (y|n)?:");
		response = stdIn.nextLine();
	} while (response.toUpperCase().charAt(0)=='y');

  } // end main
} // end class TechDriver
