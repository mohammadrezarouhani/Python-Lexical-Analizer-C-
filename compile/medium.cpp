#include <iostream>
#include <string>
using namespace std;

int main() {
    int a = 10;
    float b = 10.0;
    string greeting = "Hello";
    int sum1 = 100 + 50; 
    int x = 20;
    int y = 18;

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