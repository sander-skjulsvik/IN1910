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

class LinkedList{
  private:
    Node* head;
  public:
    LinkedList(){
        cout << "LinkedList()" << endl;
        head = nullptr;
    }
    ~LinkedList(){
        Node* current;
        Node* next;
        current = head;
        while (current->next != nullptr){
            next = current->next;
            delete current;
            current = next;
        }
        
    }

    int lenght(){
        int len;
        Node* current;
        current = head;
        while (current != nullptr){
            current = current->next;
            len++;
        }
    }

    void append(int val){
        if (head=nullptr){
            head = new Node(val);
        } else {
            Node* current;
            current = head;
            while (current->next != nullptr)
            {
                current = current->next; // (*current)
            }
            current->next = new Node(val);

        }
    }

    void print(){
        Node* current;
        current = head;
        cout << "[";
        while (current->next != nullptr){
                cout << current->val << " ";
                current = current->next;
            }
        cout << current->val;
        cout << "]";
    }
};

int main() {

    LinkedList list;

    // Node n1(47);
    // Node n2(48, &n1);

    // cout << "n1: val: " << n1.val << " , next: " << n1.next << endl;
    // cout << "n2: val: " << n2.val << " , next: " << n2.next << endl;
    list.append(1);
    list.append(10);
    list.append(15);
    list.append(20);
    list.append(100);
    list.print();


    return 0;
}