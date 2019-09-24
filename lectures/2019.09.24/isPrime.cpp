#include <iostream>

using namespace std;

bool isPrime(int n){
    if (n == 1){
        return false;
    }
    else{
        for (int d = 2; d < n; d++){
            if (!(n % d)){
                return false;
            }
        }
    }
    return true;
}

int main(){
    int n = 3;

    string output;
    
    if (isPrime(n)){
        output = "False";
    } else {
        output = "True";
    }
    cout << "N = " << n << " is prime: " << isPrime(n) << endl;
    return 0;
}