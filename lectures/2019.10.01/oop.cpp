// struct oop
// class oop
/*
struct kan ha metoder, og er sedeles lik class
class er ganske like python
structs er i c++ siden c++ skulle være kompatibelt med C




*/
#include <iostream>
#include <cmath>

using namespace std;

struct Position{
    /* data */
    double y;
    double x;
};

double distance(Position p1, Position p2){
    double dx = p1.x - p2.x;
    double dy = p1.y - p2.y;

    return sqrt(pow(dx, 2) + pow(dy, 2));

}



int main(){
    Position p1{1.0, 2.1};
     Position p2{2.3, 4.1};

    double d = distance(p1, p2);

    // cout << p.x << p.y << endl;

    return 0;
}

