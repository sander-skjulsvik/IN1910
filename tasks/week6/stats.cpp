#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;


void stats(vector<double> data, double &mean, double &median){
    // mean
    mean = accumulate(data.begin(), data.end(), 0.0)/data.size();

    //median
    sort(data.begin(), data.end());
    median = data[data.size()/2];
    
}

int main()
{
    vector<double> data = {1.2, 5.3, 7.1, -2.4, 9.2};
    cout << "data: ";
    for (int i = 0; i < data.size(); i++){
        cout << "data: " << data[i] << ", ";
    }
    double mean;
    double median;
    stats(data, mean, median);
    cout << endl << mean << endl;

}


