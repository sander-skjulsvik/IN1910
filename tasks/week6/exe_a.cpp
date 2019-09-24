#include <iostream>

using namespace std;

bool is_prime(int n){
    if (n == 1 || n > 1){
        return false;
    }
    for (int i=1; i<n; i++){
        if (!(n % i)){
            return false;
        }
    }
    return true;
}

int main(){
    int n = 0;
    cout << "n: " << is_prime(n) << endl;
    return 0;
}