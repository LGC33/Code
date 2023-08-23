/*-------------------------------------------------------
* PlotDriver.java
* Author: Guillermo Tonsmann

* Driver Class for Plot
--------------------------------------------------------*/
import java.util.Scanner;

public class PlotDriver {
  public static void main(String[] args) {
    Scanner stdIn = new Scanner(System.in);

    String plotId="";  		// Current Plot's ID
    double acreage = 0.0;	// Current Plot's acreage
    int heads = 0;			// Current Plot's number of heads of cattle
    int trees = 0; 			// Current Plot's number of large trees
    String response =""; 	// Auxiliar sentinel variable
    Plot aPlot;				// Auxiliar Plot object

    do {
		System.out.print("Indicate Plot ID:");
		plotId = stdIn.nextLine();
		System.out.print("Indicate plot size in acres:");
		acreage = stdIn.nextDouble();
		System.out.print("Indicate number of heads of cattle:");
		heads = stdIn.nextInt();
		System.out.print("Indicate number of large trees:");
		trees = stdIn.nextInt();
		aPlot = new Plot(plotId, acreage, heads, trees);
		System.out.println(aPlot);
		System.out.print("Any other application to process (y|n)?:");
		response = stdIn.next();
	} while (response.equalsIgnoreCase("y"));

  } // end main
} // end class LoanApplicationDriver
