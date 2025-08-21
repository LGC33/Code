/***************************************************************   
* Car.java   
* Larry Grace   
* 
 * This class implements copy functionality for a car.  ***************************************************************/  
 public class Car   
 {
     private String make;    // car's make    
     private int year;       // car's manufacturing year    
     private String color;   // car's primary color


    //************************************************************   
    public void setMake(String make)    
    {
      this.make = make;    
    }
    
    public void setYear(int year)   
    {
      this.year = year;    
    }
    
    public void setColor(String color)    
    {                        
      this.color = color;   
    }    
    //************************************************************    
    public Car makeCopy()    
    {      
      Car car = new Car();      
      car.make = this.make;     
      car.year = this.year;     
      car.color = this.color;      
      return car;   
    } // end makeCopy
      //************************************************************

      public void display()    
      {   
        System.out.printf("make= %s\nyear= %s\ncolor= %s\n",        
          this.make, this.year, this.color);    
      } // end display50  
 } // end class Car