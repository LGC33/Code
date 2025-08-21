/************************************************************
* LoanApplication.java
* Author: Guillermo Tonsmann
*
* This class represents a Loan Application.
************************************************************/

public class LoanApplication {

  private String name;			// applicant's lastname
  private double loan;     		// amount requested
  private double collateral; 	// value of collateral

//**********************************************************

  // Constructor

  public LoanApplication(String name, double loan, double collateral) {
    this.setName(name);
    this.setLoan(loan);
    this.setCollateral(collateral);
  } // end constructor

//**********************************************************

  // Accesors

  public String getName() {
    return this.name;
  } // end getName

  public double getLoan() {
    return this.loan;
  } // end getLoan

  public double getCollateral() {
    return this.collateral;
  } // end getCollateral

//**********************************************************

  // Mutators

  public void setName(String name) {
    this.name = name;
  } // end setName

  public void setLoan(double loan) {
    this.loan = loan;
  } // end setName

  public void setCollateral(double collateral) {
    this.collateral = collateral;
  } // end setName

  //*********************************************************

  // Method to calculate fee.

  public double getFee() {
	double fee = 0.0;					// Fee requested
	if ( this.getLoan() > this.getCollateral() ) {
	   fee = .03*this.getLoan() + .05*(this.getLoan() - this.getCollateral());
    }
	else {
	   double fee1 = .05*this.getLoan();
	   double fee2 = .10*this.getLoan() - .02*(this.getCollateral() - this.getLoan());
	   if (fee1 > fee2) {
	       fee = fee1;
	   }
	   else {
	       fee = fee2;
   	   }
    }
    return fee;

  } // end getFee

  //*********************************************************

  // Method to obtain a String with the object's status .

  public String toString() {
    return "\nLoan Applicant        = " + this.getName() + "\n" +
    	   "Loan Amount Requested = " + this.getLoan() + "\n" +
           "Collateral Value      = " + this.getCollateral() + "\n" +
           "Fee Required          = " + this.getFee() + "\n\n";
  } // end display

} // end class LoanApplication
