// Example program
#include <iostream>
#include <string>

using namespace std;

int main()
{
    int a = 10;
    int &b = a;
    int* c = &a;
    
    int x = 20;
    int *y = &x;
    
    int *z;

    cout << endl << "Init Data" << endl;
    cout << "a: " << a << ", b: " << b << ", c: " << c << ", *c: " << *c << endl;
    cout << "x: " << x << ", y: " << y << ", *y: " << *y << endl;
    
    b+=2; y+=2; c+=2;

    cout << endl << "Add: " << "b+=2; y+=2; c+=2;" << endl;
    cout << "a: " << a << ", b: " << b << ", c: " << c << ", *c: " << *c << endl;
    cout << "x: " << x << ", y: " << y << ", *y: " << *y << endl;

    x+=3;
    cout << endl << "Add: " << " x+=2;" << endl;
    cout << "x: " << x << ", y: " << y << ", *y: " << *y << endl;




    return 0;

    
}
