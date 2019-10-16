#include <iostream>
#include <cmath>
#include <vector>
// using forward euler to solve ode

using namespace std;

struct Sulution
{
    vector<double> t;
    vector<double> v;
    vector<double> y;
};

Sulution vertical_throw(double v0, double y0, double dt, double T, double m, double D){
    Sulution sol;

    double g = 9.81;
    double t = 0;
    double v = v0;
    double y = y0;
    
    sol.t = {t};
    sol.y = {y0};
    sol.v = {v0};

    while (t < T){
        v += dt * (-m * g - D * abs(v) * v);
        y += dt*v;
        t += dt;
        sol.v.push_back(v);
        sol.y.push_back(y);
        sol.t.push_back(t);

    }
    return sol;
}

int main(){
    double v0 = 1.0;
    double y0 =1.0;
    double dt = 0.001;
    double T = 1.0;
    double m = 1.0;
    double D = 1.0;
    Sulution sol = vertical_throw(v0, y0, dt, T, m, D);

    return 0;
}