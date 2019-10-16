#include <iostream>
#include <vector>
using namespace std;



vector<int> range(int start, int N){
    vector<int> list;

    for (int i = start; i<N; i++){
        list.push_back(i);
    }
    return list;
}

vector<int> range(int N){
    vector<int> list = range(1, N);
    return list;
}
// vector<int> range(int N){
    //     vector<int> list;

    //     for (int i = 1; i<N; i++){
    //         list.push_back(i);
    //     }
    //     return list;
// }

int main()
{
    vector<int> list1 = range(10);
    for (int x: list1){
        cout << " " << x;
    }
    cout << endl;
    return 0;
}
