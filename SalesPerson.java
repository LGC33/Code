/************************************************************
* SalesPerson.java
* Author: Guillermo Tonsmann
*
* This class represents a SalesPerson.
************************************************************/

public class SalesPerson {
  public static final double BASE_PAY = 900.0;		// Salesperson's base pay (USD)
  public static final double CEILING_1 =   500.0;	// Salesperson's first ceiling to cross (USD)
  public static final double CEILING_2 = 10000.0;	// Salesperson's second ceiling to cross (USD)

  public static final double RATE_1 = 4.0;			// First Compensation rate (%)
  public static final double RATE_2 = 10.0;			// Second Compensation rate (%)

  private String name;			// Salesperson's name
  private double sales;    		// salesperson's sales

//**********************************************************

  // Constructor

  public SalesPerson(String name, double sales) {
    this.setName(name);
    this.setSales(sales);
  } // end constructor

  // Default Constructor

  public SalesPerson() {
    this("NN", 0.0);
  } // end Default Constructor

//**********************************************************

  // Accesors

  public String getName() {
    return this.name;
  } // end getName

  public double getSales() {
    return this.sales;
  } // end getSales

//**********************************************************

  // Mutators

  public void setName(String name) {
    this.name = name;
  } // end setName

  public void setSales(double sales) {
    this.sales = sales;
  } // end setSales

  //*********************************************************

  // Method to calculate plot's worth.

  public double getPayment() {
	double totalPay;

	if (this.getSales() < CEILING_1) {
	   totalPay = BASE_PAY;
	}
	else if (this.getSales() < CEILING_2) {
	   totalPay = BASE_PAY + RATE_1 * this.getSales() / 100.0;
	}
	else {
	   totalPay = (1.0 + RATE_2 / 100.0) *
	              (BASE_PAY + RATE_1 * this.getSales() / 100.0);
   }

    return totalPay ;
  } // end getPayment

  //*********************************************************

  // Method to obtain a String with the object's status .

  public String toString() {
    return "\nSalesperson name : " + this.getName() + "\n" +
    	   "Total sales (USD): " + this.getSales() + "\n" +
           "Payment (USD)    : " + this.getPayment() + "\n\n";
  } // end toString

} // end class SalesPerson
