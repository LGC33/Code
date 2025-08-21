/*-------------------------------------------------------
* LoanApplicationDriver.java
* Author: Guillermo Tonsmann

* Driver Class for Loan Application
--------------------------------------------------------*/
import java.util.Scanner;

public class LoanApplicationDriver {
  public static void main(String[] args) {
    Scanner stdIn = new Scanner(System.in);

    String applicant="";  		// applicant's last name
    double amount = 0.0;		// amount requested
    double collateral = 0.0;	// value of collateral
    String response=""; 		// Auxiliar sentinel variable
    LoanApplication loan;		// Auxiliar loan object

    do {
		System.out.print("Name of Applicant:");
		applicant = stdIn.nextLine();
		System.out.print("Indicate Requested Amount:");
		amount = stdIn.nextDouble();
		System.out.print("Indicate Collateral Value:");
		collateral = stdIn.nextDouble();
		loan = new LoanApplication(applicant, amount, collateral);
		System.out.println(loan);
		System.out.print("Any other application to process (y|n)?:");
		response = stdIn.next();
	} while (response.equalsIgnoreCase("y"));

  } // end main
} // end class LoanApplicationDriver
