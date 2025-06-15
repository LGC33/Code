/************************************************************
* Plot.java
* Author: Guillermo Tonsmann
*
* This class represents a Plot.
************************************************************/

public class Plot {
  public static final double USD_PER_ACRE = 40.0;	// Dollars per acre of land
  public static final double USD_PER_HEAD = 110.0;	// Dollars per head of cattle
  public static final double USD_PER_TREE = 79.0;	// Dollars per large tree

  private String id;			// plot ID
  private double size;     		// plot size in acres
  private int headsOfCattle; 	// number of heads of cattle
  private int numberOfTrees;	// number of trees

//**********************************************************

  // Constructor

  public Plot(String id, double size, int heads, int trees) {
    this.setId(id);
    this.setSize(size);
    this.setHeadsOfCattle(heads);
    this.setNumberOfTrees(trees);
  } // end constructor

  // Default Constructor

  public Plot() {
    this("NO ID", 0.0, 0, 0);
  } // end Default Constructor

//**********************************************************

  // Accesors

  public String getId() {
    return this.id;
  } // end getId

  public double getSize() {
    return this.size;
  } // end getSize

  public int getHeadsOfCattle() {
    return this.headsOfCattle;
  } // end getHeadsOfCattle

  public int getNumberOfTrees() {
    return this.numberOfTrees;
  } // end getNumberOfTrees

//**********************************************************

  // Mutators

  public void setId(String id) {
    this.id = id;
  } // end setId

  public void setSize(double size) {
    this.size = size;
  } // end setSize

  public void setHeadsOfCattle(int heads) {
    this.headsOfCattle = heads;
  } // end setHeadsOfCattle

  public void setNumberOfTrees(int trees) {
    this.numberOfTrees = trees;
  } // end setNumberOfTrees

  //*********************************************************

  // Method to calculate plot's worth.

  public double getWorth() {
    return this.getSize()*Plot.USD_PER_ACRE +
    	   this.getHeadsOfCattle()*Plot.USD_PER_HEAD +
    	   this.getNumberOfTrees()*Plot.USD_PER_TREE ;
  } // end getWorth

  //*********************************************************

  // Method to obtain a String with the object's status .

  public String toString() {
    return "\nPlot ID                   = " + this.getId() + "\n" +
    	   "Plot size                 = " + this.getSize() + "\n" +
           "Number of heads of cattle = " + this.getHeadsOfCattle() + "\n" +
           "Number of large trees     = " + this.getNumberOfTrees() + "\n" +
           "Plot's worth (in USD)     = " + this.getWorth() + "\n\n";
  } // end toString

} // end class plot
