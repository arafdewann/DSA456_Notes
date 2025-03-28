# MD ARAFAT KOYES 
## Remeber those syntax and practice it to achive the best result in the exam.
#DSA456 SENECA COLLEGE - NOTES AND CODES


# Binary Search Tree (BST) Implementation and Exam Practice

class BST:
    class Node:
        # Node's constructor with data and left, right pointers
        def __init__(self, value=None, left=None, right=None):
            self.value = value
            self.left = left
            self.right = right

    # BST's constructor with an empty root
    def __init__(self):
        self.root = None

    # -----------------------------
    # Insert a Node (Iterative)
    # -----------------------------
    def insert(self, data):
        if self.root is None:
            self.root = BST.Node(data)  # Create root if empty
            return
        
        curr = self.root
        while True:
            if data < curr.value:
                if curr.left is None:
                    curr.left = BST.Node(data)  # Insert on left
                    break
                else:
                    curr = curr.left
            else:
                if curr.right is None:
                    curr.right = BST.Node(data)  # Insert on right
                    break
                else:
                    curr = curr.right

    # -----------------------------
    # Recursive Insert
    # -----------------------------
    def ins(self, data, subtree):
        if subtree is None:
            return BST.Node(data)
        elif data < subtree.value:
            subtree.left = self.ins(data, subtree.left)
        else:
            subtree.right = self.ins(data, subtree.right)
        return subtree

    def recursive_insert(self, data):
        self.root = self.ins(data, self.root)

    # -----------------------------
    # Search for a Value (Iterative)
    # -----------------------------
    def search(self, data):
        curr = self.root
        while curr is not None:
            if data < curr.value:
                curr = curr.left  # Go left if smaller
            elif data > curr.value:
                curr = curr.right  # Go right if larger
            else:
                return curr  # Return node if found
        return None  # Return None if not found

    # -----------------------------
    # Recursive Search
    # -----------------------------
    def r_search(self, data, subtree):
        if subtree is None:
            return None
        elif data < subtree.value:
            return self.r_search(data, subtree.left)
        elif data > subtree.value:
            return self.r_search(data, subtree.right)
        else:
            return subtree

    def search_recursive(self, data):
        return self.r_search(data, self.root)

    # -----------------------------
    # Inorder Traversal
    # -----------------------------
    def print_inorder(self, subtree):
        if subtree is not None:
            self.print_inorder(subtree.left)
            print(subtree.value, end=" ")
            self.print_inorder(subtree.right)

    # -----------------------------
    # Preorder Traversal
    # -----------------------------
    def print_preorder(self, subtree):
        if subtree is not None:
            print(subtree.value, end=" ")
            self.print_preorder(subtree.left)
            self.print_preorder(subtree.right)

    # -----------------------------
    # Postorder Traversal
    # -----------------------------
    def print_postorder(self, subtree):
        if subtree is not None:
            self.print_postorder(subtree.left)
            self.print_postorder(subtree.right)
            print(subtree.value, end=" ")

    # -----------------------------
    # Find Minimum Value
    # -----------------------------
    def find_min(self):
        curr = self.root
        while curr.left is not None:
            curr = curr.left
        return curr.value

    # -----------------------------
    # Find Maximum Value
    # -----------------------------
    def find_max(self):
        curr = self.root
        while curr.right is not None:
            curr = curr.right
        return curr.value

    # -----------------------------
    # Delete a Node
    # -----------------------------
    def delete_node(self, subtree, data):
        if subtree is None:
            return subtree  # Node not found

        if data < subtree.value:
            subtree.left = self.delete_node(subtree.left, data)  # Go left
        elif data > subtree.value:
            subtree.right = self.delete_node(subtree.right, data)  # Go right
        else:
            # Node found - 3 possible cases:
            if subtree.left is None:  # Case 1: No left child
                return subtree.right
            elif subtree.right is None:  # Case 2: No right child
                return subtree.left
            else:  # Case 3: Two children
                successor = self.get_min(subtree.right)  # Leftmost of right subtree
                subtree.value = successor.value
                subtree.right = self.delete_node(subtree.right, successor.value)
        return subtree

    # -----------------------------
    # Get Minimum Node for Successor
    # -----------------------------
    def get_min(self, subtree):
        curr = subtree
        while curr.left is not None:
            curr = curr.left
        return curr

    # -----------------------------
    # Inorder Successor
    # -----------------------------
    def inorder_successor(self, value):
        curr = self.root
        successor = None

        while curr is not None:
            if value < curr.value:
                successor = curr
                curr = curr.left
            elif value > curr.value:
                curr = curr.right
            else:
                if curr.right is not None:
                    successor = curr.right
                    while successor.left is not None:
                        successor = successor.left
                break
        return successor

    # -----------------------------
    # Print Values Between Min and Max
    # -----------------------------
    def print_between(self, min, max):
        def inorder_print(subtree):
            if subtree is None:
                return
            if min < subtree.value:
                inorder_print(subtree.left)
            if min <= subtree.value <= max:
                print(subtree.value, end=" ")
            if max > subtree.value:
                inorder_print(subtree.right)

        inorder_print(self.root)
        print("")
