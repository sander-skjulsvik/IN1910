#include <iostream>
#include <vector>
#include <ctime>
#include <cassert> // for assert()
#include <math.h> // sqrt

using namespace std;

bool is_prime(int n){
    if (n == 1 || n < 1){
        return false;
    }
    int m = sqrt(n)+1;
    for (int i=2; i<m; i++){
        if (!(n % i)){
            return false;
        }
    }
    return true;
}

double test_set_prime_time(int N = 1000*3,int n=1000*2){
    double time = 0;

    for (int i=0; i<N; i++){
        clock_t c_start = clock();
        for (int j=0; j<n; j++){
            // cout << "j: " << j << ", ";
            is_prime(j);
        }
        time += clock() - c_start;   
    }
    double average_time = time/((double)N);

    cout << "Average time: " << average_time << " t/N " << endl 
    << "- Parameters: " << "N: " << N << " n:" << n
    << endl;
    return average_time;
}

void test_set_prime_corect(bool (*f)(int)){
    vector<int> known_primes{
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 
        277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 
        839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997   
    };
    int n = 1000;
    int counter = 0;
    for (int i=0; i<n; i++){
        if ((*f)(i)){
            bool val = (known_primes[counter] == i);
            if (!val){
                cout << "known_prime: " << known_primes[counter]
                << " - i: " << i
                << " - counter: " << counter << endl;
                assert(val);
            }
            counter += 1;
        }  
    }
}

int main(){ 
    test_set_prime_time();
    test_set_prime_corect(is_prime);
    return 0;
}
