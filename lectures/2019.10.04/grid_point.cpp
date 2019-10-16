#include <iostream>
#include <vector>

using namespace std;

struct GridPoint{
    int x;
    int y;
    int z;

};

int main(){
    GridPoint start;
    start.x = 1;
    start.y = 2;
    start.z = 3;

    GridPoint *start_ptr;
    start_ptr = &start;

    cout << "start.x: " << start.x << endl;
    cout << "start.y: " << start.y << endl;
    cout << "start.z: " << start.z << endl;

    cout << "start_pr: " << start_ptr << endl;
    cout << "&start: " << &start << endl;
    cout << "start_ptr: " << (*start_ptr).x << endl;

    cout << "start.x: " << start_ptr->x << endl;
    cout << "start.y: " << start_ptr->y << endl;
    cout << "start.y: " << start_ptr->y << endl;


    return 0;
}