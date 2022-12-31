#include <iostream>
#include <string>
using namespace std;

// Create a function
void myFunction() {
  cout << "I just got executed!";
}

class MyClass {       // The class
  public:             // Access specifier
    int myNum;        // Attribute (int variable)
    string myString;  // Attribute (string variable)
};



int main() {
    int a = 10;
    float b = 10.0;
    string greeting = "Hello";
    int sum1 = 100 + 50; 
    int time = 22;
    
    cout << "Hello World!";
    
    if (time < 10) {
        cout << "Good morning.";
    } else if (time < 20) {
        cout << "Good day.";
    } else {
        cout << "Good evening.";
    }

    string cars[4] = {"Volvo", "BMW", "Ford", "Mazda"}; 
    int myNum[3] = {10, 20, 30};


    myFunction()


    return 0;
}