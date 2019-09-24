#include <iostream>
#include <stdio.h>

using namespace std;

double F2C(double F)
{
    double C = 5*(F-32)/9;
    return C;
}


int main() 
{
    //auto F = 90.0
    double F = 90;
    double C = F2C(F);

    cout << "F: " << F << " = C: " << C << endl;
    printf("F: %.2f = C: %.2f", F, C);
    return 0;
}