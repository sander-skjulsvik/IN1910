#include <iostream>
#include <vector>
using namespace std;

struct Node {
    int key;
    Node *left;
    Node *right;

    Node(int value) {
        key = value;
        left = nullptr;
        right = nullptr;
    }
};

class BinarySearchTree {
   private:
    Node *root;
    int count;

    Node *insert(Node *subroot, int x) {
        // If subtree is empty
        if (subroot == nullptr) {
            return new Node(x);
        }
 
        // Subtree isn't empty, have to go deeper (recursively)
        if (x <= subroot->key) {
            subroot->left = insert(subroot->left, x);
        } else {
            subroot->right = insert(subroot->right, x);
        }
        return subroot;
    }

    void print(Node *subroot) {
        if (subroot != nullptr) {
            print(subroot->left);
            cout << subroot->key << endl;
            print(subroot->right);
        }
    }

    bool contains(Node *subroot, int value) {
        if (subroot == nullptr){
            return false;
        }
        if (subroot->key == value){
            return true;
        }
        else if (subroot->key < value){
                return contains(subroot->right, value);
        }
        else{
            return contains(subroot->left, value);
        }
        

    }

    Node* find_min(Node* subroot){

        Node* current = subroot;
        while (current->left != nullptr){
            current = current->left;
        }
        return current;
    }

    Node* remove(Node *subroot, int value){
        
        if (subroot == nullptr){
            throw runtime_error("element not in tree");
        }
        

        if (subroot->key > value){
            subroot->left = remove(subroot->left, value);
        }
        else if (subroot->key < value){
            subroot->right = remove(subroot->right, value);
        }
        else{
            // We have found the correct node. Now we check children

            // No children
            if (subroot->left == nullptr && subroot->right == nullptr){
                delete subroot;
                return nullptr;
            }
            // One child
            else if(subroot->left == nullptr){
                Node* right = subroot->right;
                delete subroot;
                return right;

            }
            else if(subroot->right == nullptr){
                Node* left = subroot->left;
                delete subroot;
                return left;

            }
            else{
                Node* successor = find_min(subroot->right);

                // Move the successor to the node that we want to delete
                subroot->key = successor->key;
                // We need to remove the successor (which will be to the right subtree of subroot)
                subroot->right = remove(subroot->right, successor->key);

            }

        }
        return subroot;
    }


   public:
    BinarySearchTree() {
        root = nullptr;
        count = 0;
    }

    BinarySearchTree(vector<int> list) {
        root = nullptr;
        count = 0;
        insert(list);
    }

    bool contains(int value) {
        return contains(root, value);
    }

    int length() {
        return count;
    }

    void insert(int x) {
        root = insert(root, x);
        count++;
    }

    void insert(vector<int> numbers) {
        for (int n : numbers) {
            insert(n);
        }
    }

    void insert_iterative(int value) {
        count++;
        if (root == nullptr) {
            root = new Node(value);
        }

        // Iterate to bottom of tree
        Node *parent = nullptr;
        Node *current = root;

        while (current != nullptr) {
            parent = current;
            if (value <= current->key) {
                current = current->left;
            } else
                current = current->right;
        }

        // Do actual insertion
        if (value <= parent->key) {
            parent->left = new Node(value);
        } else
            parent->right = new Node(value);
    }

    void print() {
        if (root == nullptr) {
            cout << "Empty tree." << endl;
        } else {
            print(root);
        }
    }

    void remove(int value){
        cout << "Root before: " << root->key << endl;
        root = remove(root, value);
        cout << "Root after: " << root->key << endl;
        count--;

    }
};

int main() {
    BinarySearchTree tree({4, 1, 3, 8, 5, 10,6});

    cout << "Before deletion" << endl;
    tree.print();
    tree.remove(4);
    cout << "After deletion" << endl;
    tree.print();

    cout << "tree.contains(1): " << tree.contains(1) <<endl;
    cout << "tree.contains(6): " << tree.contains(6) <<endl;
    cout << "tree.contains(5): " << tree.contains(5) <<endl;


    return 0;
}