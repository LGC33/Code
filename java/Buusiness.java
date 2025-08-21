public class Business
	{
		private String name;  	   	        // Auxiliar Business name
		private String stockTicker;         // Aux Business Stock Ticker
		private int numberOfEmployees;	    // Aux Number of Employees
		private double netWorth; 			// Aux net worth

		// Acessors

		// This method assigns the business name
		public String getName()
		{
			return this.name;
		}// end business names

		// This method assigns the business stock ticker
		public String getStockTicker()
		{
			return this.stockTicker;
		}// end business stock ticker

		// This method assigns the number of employees
		public int numberOfEmloyees()
		{
			return this.numberOfEmployees;
		}// end number of employees

		// This method assigns the net worth
		public double netWorth()
		{
			return this.netWorth;
		}// end networth

		//Mutator Methods
		public void setName(String newName)
		{
			this.name = newName;
		}
		public void setStockTicker(String newStockTicker)
		{
			this.stockTicker = newStockTicker;
		}
		public void setNumberOfEmployees(int newNumberOfEmployees)
		{
			this.numberOfEmployees = newNumberOfEmployees;
		}
		public void setNetWorth(double newNetWorth)
		{
			this.netWorth = newNetWorth;
		}

		// Two constructor methods
		public Business (String newName, String newStockTicker, int newNumberOfEmployees, double newNetWorth)
		{
			this.setName(newName);
			this.setStockTicker(newStockTicker);
			this.setNumberOfEmployees(newNumberOfEmployees);
			this.setNetWorth(newNetWorth);
		}
		public Business()
		{
			this("NN","NN",4,0.0);
		}// end two constructor methods

		// toString method
		public String toString(String name, String stockTicker, int numberOfEmployees, double netWorth)
		{
			this.name = name;
			this.stockTicker = stockTicker;
			this.numberOfEmployees = numberOfEmployees;
			this.netWorth = netWorth;

			return this.name + "" + stockTicker + "" + numberOfEmployees + "" + netWorth;
		}// end toString method

		// grow method
		public Business grow(double percentage)
		{
			// numberOfEmployees
			// netWorth
			percentage = .01 * percentage;
			this.numberOfEmployees += (this.numberOfEmployees * percentage);
			this.netWorth += (this.netWorth * percentage * .01);
			return this;
		}// end grow method

		// branchOut method c = b.grow(20).branchOut
		public Business branchOut(String name, double percentage)
		{
			Business c = new Business();
			percentage = .01 * percentage;
			this.stockTicker = this.name.charAt(0) + "-" + this.name.charAt(name.length()-1);
			this.numberOfEmployees += (this.numberOfEmployees * percentage);
			this.netWorth = this.netWorth * percentage;
			return this;
		}// end branchOut method

		// joinVenture method d= a.joinVenture(c,10)
		public Business joinVenture(Business c, double percentage)
		{
			Business d = new Business();
			percentage = .01 * percentage;
			this.stockTicker = this.name.charAt(0) + "&" + this.name.charAt(0);
			this.name = this.name + "-" + name;
			return this;
		}// end joinVenture method

		// takeOver method b.takeOver(a);
		public Business takeOver(Business a)
		{
			this.numberOfEmployees = numberOfEmployees;
			this.netWorth = netWorth;
			netWorth = 0;
			return this;
		}// end takeOver method

}// end class Business.java
