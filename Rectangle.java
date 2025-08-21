/************************************************************
* Rectangle.java
* Author: Guillermo Tonsmann
*
* This class represents a Rectangle.
************************************************************/

public class Museum {

 private String officialName; // The museum name 
 private String specialty; // type of museum
 private int numberOfBuildings; //numner of buildings the musums has
 private double area; // area in sq feet
 private boolean isFinanced;// true if Museum is financed, false if not width

//**********************************************************

  // Constructor

  public Rectangle(double length, double width) {
    this.setLength(length);
    this.setWidth(width);
  } // end constructor

  // Default Constructor

  public Rectangle() {
    this(0.0, 0.0);
  } // end Default Constructor

//**********************************************************

  // Accesors

  public double getLength() {
    return this.length;
  } // end getLength

  public double getWidth() {
    return this.width;
  } // end getWidth

//**********************************************************

  // Mutators

  public void setLength(double length) {
    this.length = length;
  } // end setLength

  public void setWidth(double width) {
    this.width = width;
  } // end setWidth

  //*********************************************************

  // Method to calculate rectangle's area.

  public double getArea() {
    return this.getLength() * this.getWidth() ;
  } // end getArea

  //*********************************************************

  // Method to obtain a String with the object's status .

  public String toString()  {
    return "\nRectangle's length = " + this.getLength() + "\n" +
    	   "Rectangle's width    = " + this.getWidth() + "\n" +
           "Rectangle's area     = " + this.getArea() + "\n\n";
  } // end toString

} // end class Rectangle
