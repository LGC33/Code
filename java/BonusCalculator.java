/***************************************************************** BonusCalculator.java* * This program calculates and prints a person's work bonus.****************************************************************/
public class BonusCalculator
{
  public static void main(String[] args)
    {
        int salary;           // person's salary 
        String bonusMessage;  // specifies work bonus    
        salary = 50000;    
        bonusMessage = "Bonus  $" + (.02 * salary);    
        System.out.println(bonusMessage);  
        } 
       // end main
       } 
       // end class BonusCalculator