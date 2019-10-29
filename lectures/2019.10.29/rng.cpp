#include<iostream>
#include<time.h>

using namespace std;

int main(){
    cout << "Rand max: " << RAND_MAX << endl;
    // srand(time(nullptr));
    
    for (int i = 0; i<5; i++){
        
        cout << rand() << endl;
    }

    return 0;
}