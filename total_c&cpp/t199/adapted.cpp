#include <iostream>
#include <vector>
#include <functional>
#include <fstream>
#include <ctime>

const int DEGREE = 4; // Maximum degree of the B-Tree

class TreeNode {
public:
    bool is_leaf;
    std::vector<int> keys;
    std::vector<TreeNode *> children;
    std::vector<std::string> values; // Only used in leaf nodes

    TreeNode(bool leaf = true) : is_leaf(leaf) {
        if (leaf) {
            values.resize(2 * DEGREE - 1); // Initialize the values vector in leaf nodes
        }
    }
};

class BTree {
public:
    TreeNode *root;

    BTree() {
        root = new TreeNode(); // Initialize the root node
    }

    void insert(int key, const std::string& value) {
        if (root->keys.size() == 2 * DEGREE - 1) {
            TreeNode *new_root = new TreeNode(false);
            new_root->children.push_back(root);
            split_child(new_root, 0);
            insert_non_full(new_root, key, value);
            root = new_root;
        } else {
            insert_non_full(root, key, value);
        }
    }

    bool search(int key) {
        return search_key(root, key);
    }

    std::string search_values(int key) {
        return search_key_value(root, key);
    }

    void remove(int key) {
        if (!root->keys.empty()) {
            remove_from_node(root, key);
            if (root->keys.empty() && !root->is_leaf) {
                TreeNode *new_root = root->children[0];
                delete root;
                root = new_root;
            }
        }
    }

private:
    void insert_non_full(TreeNode *node, int key, const std::string& value) {
        int i = node->keys.size() - 1;
        if (node->is_leaf) {
            node->keys.push_back(0);
            node->values.push_back("");
            while (i >= 0 && key < node->keys[i]) {
                node->keys[i + 1] = node->keys[i];
                node->values[i + 1] = node->values[i];
                i--;
            }
            node->keys[i + 1] = key;
            node->values[i + 1] = value;
        } else {
            while (i >= 0 && key < node->keys[i]) {
                i--;
            }
            i++;
            if (node->children[i]->keys.size() == 2 * DEGREE - 1) {
                split_child(node, i);
                if (key > node->keys[i]) {
                    i++;
                }
            }
            insert_non_full(node->children[i], key, value);
        }
    }

    void split_child(TreeNode *parent, int index) {
        TreeNode *child = parent->children[index];
        TreeNode *new_child = new TreeNode(child->is_leaf);

        parent->keys.insert(parent->keys.begin() + index, child->keys[DEGREE - 1]);
        parent->children.insert(parent->children.begin() + index + 1, new_child);

        new_child->keys.assign(child->keys.begin() + DEGREE, child->keys.end());
        child->keys.resize(DEGREE - 1);

        if (child->is_leaf) {
            parent->values.insert(parent->values.begin() + index, child->values[DEGREE - 1]);
            new_child->values.assign(child->values.begin() + DEGREE, child->values.end());
            child->values.resize(DEGREE - 1);
        } else {
            new_child->children.assign(child->children.begin() + DEGREE, child->children.end());
            child->children.resize(DEGREE);
        }
    }

    bool search_key(TreeNode *node, int key) {
        int i = 0;
        while (i < node->keys.size() && key > node->keys[i]) {
            i++;
        }
        if (i < node->keys.size() && key == node->keys[i]) {
            return true;
        } else if (node->is_leaf) {
            return false;
        } else {
            return search_key(node->children[i], key);
        }
    }

    std::string search_key_value(TreeNode *node, int key) {
        int i = 0;
        while (i < node->keys.size() && key > node->keys[i]) {
            i++;
        }
        if (i < node->keys.size() && key == node->keys[i]) {
            return node->values[i];
        } else if (node->is_leaf) {
            std::cout << "Value not found for key " << key << std::endl;
            return "false";
        } else {
            return search_key_value(node->children[i], key);
        }
    }

    void remove_from_node(TreeNode *node, int key) {
        int idx = 0;
        while (idx < node->keys.size() && key > node->keys[idx]) {
            idx++;
        }

        if (idx < node->keys.size() && key == node->keys[idx]) {
            if (node->is_leaf) {
                node->keys.erase(node->keys.begin() + idx);
                node->values.erase(node->values.begin() + idx);
            } else {
                TreeNode *pred = get_predecessor(node, idx);
                node->keys[idx] = pred->keys.back();
                node->values[idx] = pred->values.back();
                remove_from_node(pred, pred->keys.back());
            }
        } else {
            if (node->is_leaf) {
                std::cout << "Key " << key << " not found in the tree." << std::endl;
                return;
            }

            bool is_last = (idx == node->keys.size());
            TreeNode *child = node->children[idx];

            if (child->keys.size() < DEGREE) {
                fill_child(node, idx);
            }

            if (is_last && idx > node->keys.size()) {
                remove_from_node(node->children[idx - 1], key);
            } else {
                remove_from_node(node->children[idx], key);
            }
        }
    }

    TreeNode *get_predecessor(TreeNode *node, int idx) {
        TreeNode *current = node->children[idx];
        while (!current->is_leaf) {
            current = current->children.back();
        }
        return current;
    }

    void fill_child(TreeNode *node, int idx) {
        if (idx != 0 && node->children[idx - 1]->keys.size() >= DEGREE) {
            borrow_from_prev(node, idx);
        } else if (idx != node->keys.size() && node->children[idx + 1]->keys.size() >= DEGREE) {
            borrow_from_next(node, idx);
        } else {
            if (idx != node->keys.size()) {
                merge_nodes(node, idx);
            } else {
                merge_nodes(node, idx - 1);
            }
        }
    }

    void borrow_from_prev(TreeNode *node, int idx) {
        TreeNode *child = node->children[idx];
        TreeNode *sibling = node->children[idx - 1];

        child->keys.insert(child->keys.begin(), node->keys[idx - 1]);
        node->keys[idx - 1] = sibling->keys.back();
        node->values[idx - 1] = sibling->values.back();

        if (!sibling->is_leaf) {
            child->children.insert(child->children.begin(), sibling->children.back());
            sibling->children.pop_back();
        }

        sibling->keys.pop_back();
        sibling->values.pop_back();
    }

    void borrow_from_next(TreeNode *node, int idx) {
        TreeNode *child = node->children[idx];
        TreeNode *sibling = node->children[idx + 1];

        child->keys.push_back(node->keys[idx]);
        node->keys[idx] = sibling->keys.front();

        if (!sibling->is_leaf) {
            child->children.push_back(sibling->children.front());
            sibling->children.erase(sibling->children.begin());
        }

        sibling->keys.erase(sibling->keys.begin());
    }

    void merge_nodes(TreeNode *node, int idx) {
        TreeNode *child = node->children[idx];
        TreeNode *sibling = node->children[idx + 1];

        child->keys.push_back(node->keys[idx]);
        child->values.push_back(node->values[idx]);

        child->keys.insert(child->keys.end(), sibling->keys.begin(), sibling->keys.end());
        child->values.insert(child->values.end(), sibling->values.begin(), sibling->values.end());

        if (!child->is_leaf) {
            child->children.insert(child->children.end(), sibling->children.begin(), sibling->children.end());
        }

        node->keys.erase(node->keys.begin() + idx);
        node->values.erase(node->values.begin() + idx);
        node->children.erase(node->children.begin() + idx + 1);

        delete sibling;
    }
};

void generateDot(TreeNode *node, std::ofstream &dot_file) {
    dot_file << "digraph G {" << std::endl;

    std::function<void(TreeNode *, int)> generate_node = [&](TreeNode *node, int id) {
        dot_file << "  " << id << " [label=\"";
        for (int key : node->keys) {
            dot_file << key << "\\l";
        }
        dot_file << "\"];" << std::endl;

        if (!node->is_leaf) {
            for (int i = 0; i < node->children.size(); i++) {
                generate_node(node->children[i], id * 10 + i + 1);
                dot_file << "  " << id << " -> " << id * 10 + i + 1 << ";" << std::endl;
            }
        }
    };

    generate_node(node, 1);

    dot_file << "}" << std::endl;
}

std::string generateRandomValue() {
    const int length = 6; // Length of the generated value
    const std::string charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    std::string value;
    for (int i = 0; i < length; i++) {
        value += charset[rand() % charset.length()];
    }
    return value;
}

int main() {
    BTree b_tree;

    // Insert 851 keys with random values into the B-Tree
    for (int key = 1; key <= 851; key++) {
        b_tree.insert(key, generateRandomValue());
    }

    // Testing search and search_values functions
    std::cout << std::boolalpha;
    std::cout << b_tree.search(5) << std::endl; 
    std::cout << b_tree.search_values(5) << std::endl;     

    std::cout << b_tree.search_values(20) << std::endl;    

    std::cout << b_tree.search_values(38) << std::endl;    
    std::cout << b_tree.search(10001) << std::endl;        

    // Removing keys
    b_tree.remove(500);
    b_tree.remove(10001);

    // Checking results after removal
    std::cout << b_tree.search(5) << std::endl;  
    std::cout << b_tree.search_values(5) << std::endl;       
    std::cout << b_tree.search(10001) << std::endl;          

    return 0;
}
