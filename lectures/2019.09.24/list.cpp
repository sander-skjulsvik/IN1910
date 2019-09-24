#include <iostream>
#include <vector>

using namespace std;


bool is_prime(int n){
    if (n <= 1 || n == 0){
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

vector<int> get_primes(int N){
    vector<int> primes;

    for (int i=1; i<N; i++){
            if (is_prime(i) == 1){
                primes.push_back(i);
            }
        }

    return primes;
}

int main() {   
    int n = 1000;
    vector<int> primes = get_primes(n);

    // for (int i = 0; i < primes.size(); i++){
    //     cout << primes[i] << " ";
    // }
    cout << primes.size() << endl;
    return 0;

}