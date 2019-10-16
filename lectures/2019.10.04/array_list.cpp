#include <iostream>
#include <vector>

using namespace std;

class ArrayList{
  private:
    int capacity;

  public:
    int size;
    int *data;

    ArrayList(){
        size = 0;
        capacity = 1000;
        data = new int[capacity];
        // cout << "data: " << &data << endl;
    }
    ~ArrayList(){
        cout << "calling del array list" << endl;
        delete[] data;
    }

    void append(int x){
        data[size] = x;
        size++;

    }


};

int main()
{
    ArrayList a;
    cout << "a.size: " << a.size << endl;
    a.append(1); a.append(2); a.append(3);

    cout << "s.size" << a.size << endl;

    for (int i=0; i<a.size; i++){
        cout << a.data[i] << ", ";
    }
    cout << endl;
    return 0;
}
