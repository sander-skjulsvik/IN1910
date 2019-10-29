#include<iostream>
#include<random>

using namespace std;

int main(){
    
    // generating random numbers
    mt19937 engine{1234};
    // converting the random numbers to the form i want
    uniform_real_distribution<float> uniform(0,1);

    for (int i=0; i<5; i++){
        cout << uniform(engine) << endl;
    }


    return 0;
}