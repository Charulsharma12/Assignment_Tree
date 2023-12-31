#Implement_Binary_Tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None 
        self.right = None 
from collections import deque

class BinaryTree:
    def __init__(self, root_value):
        self.root = Node(root_value)

# Function to find the height of a given tree
        def height(self, node):
            if node is None:
                return 0 
            return 1 + max(self.height(node.left), self.height(node.right))
        
# Perform Pre-order traversal (Root-Left-Right)
        def preorder_traversal(self, node):
            if node:
                print(node.value, end = " ")
                self.preorder_traversal(node.left)
                self.preorder_traversal(node.right)
# Perform Post-order traversal (Left-Right-Root)
        def postorder_traversal(self, node):
            if node:
                self.preorder_traversal(node.left)
                self.preorder_traversal(node.right
                print(node.value, end = " ")
# Perform In-order traversal (Left-Root-Right)

def inorder_traversal(self, node):
    if node:
        self.inorder_traversal(node.left)
        print(node.value, end = " ")
        self.inorder_traversal(node.right)

# Function to print all the leaves in a given binary tree
def print_leaves(self, node):
    if node:
        if node.left is None and node.right is None 
            print(node.value, end = " ")
        self.print_leaves(node.left)
        self.print_leaves(node.right)

# Implement BFS (Breath First Search)

def bfs(self):
    if not self.root:
        return 
    queue = deque([self.root])
    while queue:
        node = queue.popleft()
        print(node.value, end = " ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Implement DFS (Depth First Search)

def dfs(self):
    if not self.root:
        return
    stack = [self.root]
    while stack:
        node = stack.pop()
        print(node.value, end = " ")
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

 # Find sum of all left leaves in a given Binary Tree

 def sum_left_leaves(self, node, is_left = False):
     if not node:
         return 0 
     if not node.left and not node.right and is_left:
         return node.value 
     return (
         self.sum_left_leaves(node.left, True) 
         + self.sum_left_leaves(node.right, False)
     )
# Find sum of all nodes of the given perfect binary tree
def sum_all_nodes(self, node):
    if not node:
        return 0 
    return (
        node.value
        + self.sum_all_nodes(node.left)
        + self.sum_all_nodes(node.right)
    )

# Count subtrees that sum up to a given value x in a binary tree

def count_subtress_with_sum(self, node, x):
    count = 0 
    def subtree_sum(root):
        nonlocal count
        if not root:
            return 0 
        current_sum = (
            root.value + 
            subtree_sum(root.left)
            + subtree_sum(root.right)
        )
        if current_sum == x:
            count += 1 
        return current_sum

        subtree_sum(node)
        return count 

# # Print the nodes at odd levels of a tree

def print_odd_level_nodes(self, node, level = 1):
    if not node:
        return 
    if level %2 != 0 
        print(node.value end = " ")
    self.print_odd_level_nodes(node.left, level+1)
    self.print_odd_level_nodes(node.right, level+1)

# Find maximum level sum in Binary Tree

def max_level_sum(self):
    if not self.root:
        return 0 
    max_sum = float("-inf")
    queue = deque([self.root])

    while queue:
        level_sum = 0 
        level_size = len(queue)

        for i in range(level_size):
            node = queue.popleft()
            level_sum += node.value 

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)
        max_sum = max(max_sum, level_sum)

    return max_sum 