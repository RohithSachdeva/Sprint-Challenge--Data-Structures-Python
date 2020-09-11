import time



class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        elif value >= self.value:
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if self.value == target:
            return True
        if self.value != target:
            if self.value < target:
                if self.right is None:
                    return False
                return self.right.contains(target)
            elif self.value > target:
                if self.left is None:
                    return False
                return self.left.contains(target)
            else:
                return False


"""
Remove nested loop... 
So BST cant have duplicate nodes by default... can insert names into a BST and use the contains method to append?
BST runs at o(n) vs o(n^2) (current)

insert and contains method
1. Insert Name 1 into the BST .. making it accessible at o(n) speed when the for loops are not nested... 
2.  If the BST contains that same name (contain method) ... append it to the array duplicates

Review support hours code from last night;  Matt did something similar in lecture 4 video... I think 

5.4 seconds to .08 seconds... pretty cool 
Curious why I had to create a bst variable for BSTNode("None")
"""
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure
bst = BSTNode("None")

# Replace the nested for loops below with your improvements
for name in names_1:
    bst.insert(name)
for name in names_2:
    if bst.contains(name):
         duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
