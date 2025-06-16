//int  newSales; 
//int totalSales;
//numCars = 99;
#include <iostream>
using namespace std;

int main() {
   int litterSize;
   int yearlyLitters;
   int annualMice;

   litterSize    = 3; // Low end of litter size range
   yearlyLitters = 5; // Low end of litters per year

   cout << "One female mouse may give birth to ";
   annualMice = litterSize * yearlyLitters;
   cout << annualMice << " mice " << endl;

   cout << "and up to ";
   annualMice = litterSize * yearlyLitters;
   cout <<  << " mice, in a year." << endl;
   
   return 0;
}