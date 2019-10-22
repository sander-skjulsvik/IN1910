#include<iostream>
#include<vector>

using namespace std;

struct Node{
    int key; //val
    Node* left;
    Node* right;

    Node(int value){ // starten på noden
        key = value;
        left = nullptr;
        right = nullptr;
    }
};

class BinarySearchTree{
// -- private
  private:
    Node* root;
    int count;

// modifiers
    // recursive insert
    Node* insert(Node* subroot, int value){
        if (subroot == nullptr){
            return new Node(value);
        } else{
            if (subroot->key < value){
                subroot->right = insert(subroot->right, value);
            } else{
                subroot->left = insert(subroot->left, value);
            }    
            return subroot;
        }
        
    }
// methods
    void print(Node* subroot){
        if  (subroot != nullptr){
            print(subroot->left);
            cout << subroot->key << ", ";
            print(subroot->right);
        }

    }
    bool contains(Node* subroot, int value){
        if (subroot == nullptr){
            cout << "Tree is empty" << endl;
            return false;
        }
        cout << "path " << subroot->key << endl;
        if (subroot->key == value){
            cout << "Found " << value << endl;
            return true;
        } else if (subroot->key > value){
            return contains(subroot->left, value);
        } else {
            return contains(subroot->right, value);
        }        
    }
    Node* find_min(Node* subroot){
        if (subroot == nullptr){
            return nullptr;
        }
        while (subroot->left != nullptr){
            subroot = subroot->left;
        }
        return subroot;
        
    }
// -- public
  public:
// constructor
    BinarySearchTree(){
        root = nullptr;
        count = 0;
    }
// properties
    int length(){
        return count;
    }

// modifiers
    // recursie insert
    void insert(int value){
        root = insert(root, value);;
        count++;
    }
    void insert(vector<int> values){
        for (int value : values){
            insert(value);
        }
    }
  // iterative sulution non complete
    // void insert(int value){
    //     if (root == nullptr){
    //         root = new Node(value);
    //     }

    //     Node* parent = nullptr;
    //     Node* current = root;
    //     while (current != nullptr)
    //     {
    //         parent = current;
    //         if (x <= current->key){
    //             current = current->left
    //         } else {
    //             current = current->right
    //         }
    //     }
        
    // }
// methods
    void print(){
        print(root);
    }
    bool contains(int value){
        return contains(root, value);
    }
};

int main(){
    
    BinarySearchTree tree; // 
    tree.insert({3,1,2,6,4,7});
    // BinarySearchTree tree;
    // tree.insert(3);
    // tree.insert(1);
    // tree.insert(2);
    // tree.insert(6);
    // tree.insert(4);
    // tree.insert(7);
    // tree.insert(20);
    tree.contains(7);
    // tree.print();

    return 0;
};