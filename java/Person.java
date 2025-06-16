/************************************************************
* Tech.java
* Author: Larry Grace
*
* This class represents a Tech.
************************************************************/

public class Tech {

  private String firstName;    	// Tech's first name
  private String lastName;     	// Tech's last name
  private String title; 	    	// Tech's title
  private int age; 		    	// Tech's age

//**********************************************************

  // Constructor

  public Tech(String firstName, String lastName, String title, int age) {
    this.setFirstName(firstName);
    this.setLastName(lastName);
    this.settitle(title);
    this.setAge(age);
  } // end constructor

  // Default Constructor

  public Tech() {
    this("", "", "", 0);
  } // end Default Constructor

//**********************************************************

  // Accesors

  public String getFirstName() {
    return this.firstName;
  } // end getFirstName

  public String getLastName() {
    return this.lastName;
  } // end getLastName

  public String getTitle() {
    return this.title;
  } // end gettitle

  public int getAge() {
    return this.age;
  } // end getAge

//**********************************************************

  // Mutators

  public void setFirstName(String firstName) {
    this.firstName = firstName;
  } // end setFirstName

  public void setLastName(String lastName) {
    this.lastName = lastName;
  } // end setLastName

  public void settitle(String title) {
    this.title = title;
  } // end settitle

  public void setAge(int age) {
    this.age = age;
  } // end setAge

  //*********************************************************

  // Method to obtain the Tech's initials

  public String getInitials() {
    return ""+this.getFirstName().charAt(0) + "."+ this.getLastName().charAt(0) + "." ;
  } // end getInitials

  //*********************************************************

  // Method to obtain a String with the object's status .

  public String toString() {
    return "\nTech's first name = " + this.getFirstName() + "\n" +
    	   "Tech's last name    = " + this.getLastName() + "\n" +
    	   "Tech's initials    = " + this.getInitials() + "\n" +
    	   "Tech's title    = " + this.getTitle() + "\n" +
           "Tech's age     = " + this.getAge() + "\n\n";
  } // end toString

} // end class Tech
