#include <iostream>
#include <vector>

using namespace std;


int main(){
    int x[100];

    for (int i = 0; i < 5; i++){
        cout << &x[i] << endl;
    }
    cout << "x: " << x << endl;
    cout << "&x: " << &x << endl;

    cout << endl << "----------" << endl;

    int z[] = {2,4,6,8,10,12};
    int *y = &z[0];
    // int *y = z;

    for (int i = 0; i < 5; i++){
        cout << *(y + i) << endl;
    }
    return 0;
}