#include <iostream>
#include <cctype>
#include <vector>
#include <string>
using namespace std;

const int MAX_NUMS = 4;  // Global variable used for vector sizes

// ***********************************************************************
// GetPeriodPosition - Pass a string and return the position of the period
// ***********************************************************************
int GetPeriodPosition(string stringToSearch) {
   int periodCounter;
   int periodPosition;
   unsigned int i;

   periodCounter = 0;
   periodPosition = -1;
 
   for (i = 0; i < stringToSearch.size(); ++i) {
     if (stringToSearch[i] == '.') {
        ++periodCounter;
        periodPosition = i;
     }
   }
 
   // If there are zero or two or more periods, indicate an incorrect domain name
   // by setting variable periodPosition to -1
   if (periodCounter != 1) {
      periodPosition = -1;
   }
   return periodPosition;
}
 
// *********************************************************************************   
// HasValidSecondLevel  - Returns true if second-level domain is valid, false if not
// *********************************************************************************
// A valid second-level domain:
// 1. Is between 1 and 63 characters long
// 2. Contains only upper- and lower-case letters, digits 0-9 and the dash
// 3. Cannot begin or end with a dash
 
bool HasValidSecondLevel(string secondLevel) {
   const int MAX_SECONDLEVEL_LENGTH = 63;
   const char DASH = '-';
 
   bool isValidSecondLevel;           
   int secondLevelLength;
   char nextChar;
   int i;
   
   isValidSecondLevel = true;              // Assume valid second-level domain
   secondLevelLength = secondLevel.size();
   nextChar = '?';

   // Disqualify the second-level domain if it is too short or too long, or
   // if it begins or ends with a dash
   if ((secondLevelLength >= 1) &&
       (secondLevelLength <= MAX_SECONDLEVEL_LENGTH)) {
      if ((secondLevel[0] == DASH) ||
          (secondLevel[secondLevelLength - 1] == DASH)) {
         isValidSecondLevel = false;
      }
   }
   else {
      isValidSecondLevel = false;
   }
 
   // Disqualify the second-level domain if any character is not a letter,
   // digit, or a dash
   i = 0;
   while ((i < secondLevelLength) && (isValidSecondLevel)) {
      nextChar = secondLevel[i];
      if ((!isalnum(nextChar)) && (nextChar != DASH)) {
         isValidSecondLevel = false;
      }
      ++i;
   }
 
   return isValidSecondLevel;
}

// ***********************************************************************
// HasValidTld - Returns true if top-level domain is valid, false if not
// ***********************************************************************
// A valid top-level domain begins with a period and then contains only
// upper- and lower-case letters, or digits 0-9.
  
bool HasValidTld(string theTld) {
   bool isValidTopLevel;           
   int topLevelLength;
   char nextChar;
   int i;

   isValidTopLevel = true;           // Assume valid top-level domain
   topLevelLength = theTld.size();
   nextChar = '?';
 
   // Disqualify the top-level domain if it is the empty string or
   // the first character is not a period
 
   if ((topLevelLength <= 0) || (theTld[0] != '.')) {
      isValidTopLevel = false;
   }
 
   // Disqualify the top-level domain if any character is not a letter or a digit
   i = 1;
   while ((i < topLevelLength) && (isValidTopLevel)) {
      nextChar = theTld[i];
      if (!isalnum(nextChar)) {
         isValidTopLevel = false;
      }
      ++i;
   }
 
   return isValidTopLevel;
}
 
// *****************************************************************************
// IsSpecialGtld - Takes a vector of special gTLD names and a tld candidate.
//                 Returns true if the candidate is a special gTLD, false if not
// ***************************************************************************** 
bool IsSpecialGtld(vector<string> specialGtld, string tld) {
   bool isSpecial;
   int i;
 
   isSpecial = false;
   i = 0;

   while ((i < MAX_NUMS) && (!isSpecial)) {
      if (specialGtld.at(i) == tld) {
         isSpecial = true;
      }
      else {
         ++i;
      }
   }
   return isSpecial;
}
 
// ***********************************************************************
 
// FIXME: Write a function GetString that prompts the user for an input string.
//        It takes the prompt as a parameter and returns the input string.
  
// FIXME: Insert the GetString function here
 
// ***********************************************************************
 
int main() {
   const string PROMPT_DOMAIN_NAME = "\nEnter the next domain name (Enter to exit): ";
  
   // Define the list of valid core gTLDs and restricted gTLDs
   vector<string> validCoreGtld(MAX_NUMS);
   vector<string> validRestrictedGtld(MAX_NUMS);
   string inputName;
   string searchName;
   string secondLevel;       // In aaa.bbb, the aaa part, aka second-level domain
   string theTld;            // In aaa.bbb, the bbb part, aka top-level domain
   int periodPosition;
   bool isCoreGtld;
   bool isPeriodPositionValid;
   bool isRestrictedGtld;
   bool isDomainValid;
   unsigned int i;

   isCoreGtld            = false;
   isPeriodPositionValid = false;
   isRestrictedGtld      = false;
   isDomainValid         = false;

   validCoreGtld.at(0) = ".com";
   validCoreGtld.at(1) = ".net";
   validCoreGtld.at(2) = ".org";
   validCoreGtld.at(3) = ".info";
   validRestrictedGtld.at(0) = ".biz";
   validRestrictedGtld.at(1) = ".name";
   validRestrictedGtld.at(2) = ".pro";

   // Get the first domain name to process
   // FIXME: Rewrite the prompt for an input of the next domain
   //        name as a call to a function named GetString. The function
   //        has parameter of a string prompt to display to the user.

   cout << PROMPT_DOMAIN_NAME << endl;
   cin >> inputName;

   while (inputName.size() > 0) {
      searchName = inputName;
      for (i = 0; i < inputName.size(); ++i) {
         searchName[i] = tolower(inputName[i]);
      }
      isCoreGtld     = false;
      isDomainValid  = false;
      periodPosition = GetPeriodPosition(searchName);
      isPeriodPositionValid = (periodPosition >= 1);

      // The domain name is valid if there is exactly one period in the
      // domain name (at location periodPosition) and the domain name does
      // not start or end with a period. Note that a period position of 0 means
      // the first character is a period, rendering the domain name invalid

      if ((periodPosition > 0) && (searchName[searchName.size() - 1] != '.')) {
         isPeriodPositionValid = true;
      }
      else {
         isPeriodPositionValid = false;
      }
      if (isPeriodPositionValid) {

         // Extract the second-level domain and the top-level domain
         secondLevel   = searchName.substr(0, periodPosition);
         theTld        = searchName.substr(periodPosition);
         isDomainValid = HasValidSecondLevel(secondLevel) && HasValidTld(theTld);

         // If the domain name is valid see if there is a core gTLD or a restricted gTLD
         if (isDomainValid) {
            isCoreGtld = IsSpecialGtld(validCoreGtld, theTld);
            if (!isCoreGtld) {
               // FIXME: Using function IsSpecialGtld with the vector
               //        validRestrictedGtld, set isRestrictedGtld to
               //        true or false based on whether the gTLD is a
               //        restricted gTLD.

            }
         }
      }

      // Display the results
      cout << "\"" << inputName << "\" ";
      if (isDomainValid) {
         cout << "is a valid domain name and ";
         if (isCoreGtld) {
            cout << "has a core gTLD of \"" << theTld << "\"." << endl;
         }
         else if (isRestrictedGtld) {
            cout << "has a restricted gTLD of \"" << theTld << "\"." << endl;
         }
         else {
            cout << "has a TLD of \"" << theTld << "\"." << endl;
         }
      }
      else {
         cout << "is not a valid domain name." << endl;
      }

      // Get the next domain name to process
      // FIXME: Use the GetString function described above to prompt for and 
      //        input the next candidate domain name
      cout << PROMPT_DOMAIN_NAME << endl;
      inputName = "";
      cin >> inputName;
   }

   return 0;
}