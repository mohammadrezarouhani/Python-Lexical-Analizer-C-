#include <iostream>
#include <string>
using namespace std;
void myFunction() {
  cout << "I just got executed!";
}
class MyClass {  
  public:            
    int myNum;        
    string myString;  
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
    if (20 > 18) {
        cout << "20 is greater than 18";
    }
    if (x > y) {
        cout << "x is greater than y";
    }
    int i = 0;
    while (i < 5) {
        cout << i << "\n";
        i++;
    }
    for (int i = 0; i < 5; i++) {
        cout << i << "\n";
    }
    cout << "Hello World!";
    return 0;
}