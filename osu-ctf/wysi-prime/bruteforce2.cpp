#include <iostream>
#include <fstream>
#include <string>
#include <boost/multiprecision/cpp_int.hpp>
#include "script.h" // Assuming you have implemented getNthWYSIprime in script.h

using namespace std;
using namespace boost::multiprecision;

int main() {
    ifstream inputFile("output.txt");
    if (!inputFile.is_open()) {
        cerr << "Error: Couldn't open the input file." << endl;
        return 1;
    }

    cpp_int n;
    string line;
    getline(inputFile, line);
    n = cpp_int(line.substr(line.find('=') + 1)); // Extracting n from the file
    inputFile.close();

    bool found = false;
    int num_prime = 1; // Start from the 1st prime
    while (!found) {
        cpp_int curr = getNthWYSIprime(num_prime); // Assuming getNthWYSIprime is implemented in script.h
        if (n % curr == 0) {
            cpp_int potential = n / curr;
            string s_potential = potential.str();
            if (s_potential.find_first_not_of("27") == string::npos) { // Checking if all digits are either 2 or 7
                found = true;
            }
        }
        num_prime++;
        if (to_string(curr).length() > 544) {
            cout << "bro you suck" << endl;
            break;
        }
        cout << curr << endl;
    }

    cout << "The WYSI prime that divides n evenly is: " << getNthWYSIprime(num_prime - 1) << endl; // The last successful value of curr
    return 0;
}
