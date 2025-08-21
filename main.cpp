//
//  main.cpp
//  HW1_Grace.cpp
//
//  Created by Larry Grace on 10/28/19.
//  Copyright © 2019 Larry Grace. All rights reserved.
//
// Author:Larry Grace
// CS225_F2A_Professor Dewey
// Program to read file with records and ouput them on a seperate file.
//********************************************************************************

#include "pch.h"
#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>

int main()
{
    std::ifstream input;
    std::ofstream output;
    double currentSalary, payIncrease, updatedSalary;
    int count = 0;
    std::string firstName, lastName;
    bool message;   //used to track what message for program to output on screen

    input.open("curSalary.txt");
    output.open("newSalary.txt");

    //sets output format into text file
    std::cout << std::fixed << std::showpoint << std::setprecision(2);

    do
    {
        input >> lastName >> firstName >> currentSalary >> payIncrease; //reads input from text file

        //processes data from text file
        if (lastName == "")
        {
            message = false;
        }
       else if (lastName != "...")
            {
                output << firstName << " " << lastName << " " << currentSalary + currentSalary * (payIncrease / 100) << std::endl;
                count++;
                message = true;
            }
    }while (!input.eof());

    //Outputs on sreen # of messages processed and saved or if empty file was made
    if (message)
        {
            std::cout << count << " records processed and saved in \"newSalary.txt\"." << std::endl
                << "Press any key to continue . . ." << std::endl;
        }
    else
        {
            std::cout << "Warning: empty input file. Output file created but is empty." << std::endl
                << "Press any key to continue . . ." << std::endl;
        }

    input.close();
    output.close();

    return 0;
}   //end main
