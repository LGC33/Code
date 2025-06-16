#include <iostream>
#include <vector>
using namespace std;

double GetCorrespondingTableValue(int search, vector<int> baseTable, vector<double> valueTable) {
   int baseTableLength;
   double value;
   int i;
   bool keepLooking;

   baseTableLength = baseTable.size();
   i = 0;
   keepLooking = true;

   while ((i < baseTableLength) && keepLooking) {
      if (search <= baseTable.at(i)) {
         value = valueTable.at(i);
         keepLooking = false;
      }
      else {
         ++i;
      }
   }

   return value;
}

int main() {
   int annualSalary;
   double taxRate;
   int taxToPay;
   vector<int> salaryBase(5);
   vector<double> taxBase(5);

   salaryBase.at(0) = 0;
   salaryBase.at(1) = 20000;
   salaryBase.at(2) = 50000;
   salaryBase.at(3) = 100000;
   salaryBase.at(4) = 99999999;

   taxBase.at(0) = 0.0;
   taxBase.at(1) = 0.10;
   taxBase.at(2) = 0.20;
   taxBase.at(3) = 0.30;
   taxBase.at(4) = 0.40;

   // FIXME: Change the input to come from a function
   cout << "\nEnter annual salary (0 to exit): " << endl;
   cin >> annualSalary;

   while (annualSalary > 0) {
      taxRate = GetCorrespondingTableValue(annualSalary, salaryBase, taxBase);

      taxToPay = static_cast<int>(annualSalary * taxRate);  // Truncate tax to an integer amount
      cout << "Annual salary: " << annualSalary <<
              "\nTax rate: " << taxRate << 
              "\nTax to pay: " << taxToPay << endl;

      // Get the next annual salary
      // FIXME: Change the input to come from a function
      cout << "\nEnter annual salary (0 to exit): " << endl;
      cin >> annualSalary;
   }

   return 0;
} 
