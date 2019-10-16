#include <iostream>
#include <vector>

using namespace std;

class Array
{
  public:
    int *data;
    int size;

    Array(int n){
        data = new int[n]; // dynamisk minne alokering
        int tmp[n];
        for (int i = 0; i<n; i++){
            tmp[i] = 0;
        }
        data = tmp;
        size = n;
    }
        
};

int main()
{
    Array a(10);
    for (int i; i<a.size; i++){
        cout << a.data[i] <<  ", ";
    }
    return 0;
}