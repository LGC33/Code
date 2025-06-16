/*-------------------------------------------------------
* RectangleDriver.java
* Author: Guillermo Tonsmann

* Driver Class for Rectangle
--------------------------------------------------------*/
import java.util.Scanner;

public class RectangleDriver {
  public static void main(String[] args) {
    Scanner stdIn = new Scanner(System.in);

    double userLength = 0.0;	// Length given by user
    double userWidth  = 0.0;	// Width given by user
    String response =""; 		// Auxiliar variable to get responses
    Rectangle aRectangle;		// Auxiliar Rectangle object

    do {
		System.out.print("Indicate rectangle's length: ");
		userLength = stdIn.nextDouble();
		System.out.print("Indicate rectangle's width: ");
		userWidth = stdIn.nextDouble();

		aRectangle = new Rectangle(userLength,userWidth);
		System.out.println(aRectangle);
		System.out.print("Any other rectangle to process (y|n)?:");
		response = stdIn.next();
	} while (response.equalsIgnoreCase("y"));

  } // end main
} // end class RectangleDriver
