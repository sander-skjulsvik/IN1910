#include <iomanip>
#include <iostream>


using namespace std;

struct Node{
    int val;
    Node* next;

    Node(int v){
        val = v;
        next = nullptr;
    }

    Node(int v, Node* n){
        val = v;
        next = n;
    }

};

int main() {

    Node n1(47);
    Node n2(48, &n1);

    cout << "n1: val: " << n1.val << " , next " << n1.next << endl;
    cout << "n2: val: " << n2.val << " , next " << n2.next << endl;


    return 0;
}