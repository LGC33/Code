/*-------------------------------------------------------
* SalesPersonDriver.java
* Author: Guillermo Tonsmann

* Driver Class for SalesPerson
--------------------------------------------------------*/
import java.util.Scanner;

public class SalesPersonDriver {
  public static void main(String[] args) {
    Scanner stdIn = new Scanner(System.in);

    String name="";  		// Salesperson's name
    double sales = 0.0;	    // Salesperson's total sales
    String response =""; 	// Auxiliar sentinel variable
    SalesPerson aPerson;	// Auxiliar SalesPerson object

    do {
		System.out.print("Indicate salesman name:");
		name = stdIn.next();
		System.out.print("Indicate amount of sales (USD):");
		sales = stdIn.nextDouble();
		aPerson = new SalesPerson(name, sales);
		System.out.println(aPerson);
		System.out.print("Any other application to process (y|n)?:");
		response = stdIn.next();
	} while (response.equalsIgnoreCase("y"));

  } // end main
} // end class SalesPersonDriver
