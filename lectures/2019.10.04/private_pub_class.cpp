
#include <iostream>
using namespace std;

const double PI = 3.1415;

class Circle {
   private:
    double radius;
    double cx;

   public:
   Circle(){
       cout << "Calling Cirlcle()" << endl;
       radius = 1;
   }
   Circle(double r){
       cout << "Calling Cirlcle()" << endl;
       radius = r;
   }
    double get_radius() {
        return radius;
    }
    void set_radius(double r) {
        radius = r;
    }
    double get_area(){
        return PI*radius*radius;
    }
};

int main() {
    Circle c1;
    cout << c1.get_radius << endl;

    // Circle c2(3.0);
    // cout << c1.get_radius << endl;
    

    


    return 0;
}
