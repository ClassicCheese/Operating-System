
# This is just a simple tree format
class TreeNode:
    def __init__(self, value):
        self.value = value 
        self.left = None
        self.right = None

    def __repr__(self): 
        return f"({self.value})"


# This function find the last operation
def find_main_operator(n):

    # Initialize the min precedence and the index of the root operator
    min_precedence = 4
    main_operator_index = -1

    # A list of operators and it's precedence values
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    # This loops through the entire statement to determine the root
    for i, char in enumerate(n):
        if char in precedence:
            if precedence[char] <= min_precedence:
                min_precedence = precedence[char]
                main_operator_index = i

    # return the index of the root/last operator 
    return main_operator_index

# This funciton build a tree
def build_tree(n: str) :

    # This to filter out all the spaces
    n = n.replace(" ", "")

    # This make sure that if the statment is just a number,
    # then we just return the number as is
    if n.isdigit():
        return TreeNode(n)
    

    # Find the index of the root value
    index = find_main_operator(n)

    # This to double check if somehow a statement by pass the first if check 
    # and then return the value as is
    if index == -1:
        return TreeNode(n)
    
    # This initialize the root with that value at that index
    root = TreeNode(n[index])

    # This build the subtree from that index
    root.left = build_tree(n[:index])
    root.right = build_tree(n[index+1:])

    # Return the root
    return root


# this fuction calculate the tree
def calcTree(n: TreeNode):

    # Base case, it return the total when the node is none
    if not n:
        return 0
    
    # if this is a leaf node (number node) then return the value
    if not n.left and not n.right:
        return float(n.value)
    
    # These get the left and right subtree recursively
    left = calcTree(n.left)
    right = calcTree(n.right)


    # These are just simple if-else statments to perform the calculations
    if n.value == "+":
        return left + right
    elif n.value == "-":
        return left - right
    elif n.value == "*":
        return left * right
    elif n.value == "/":
        return left / right
    elif n.value == "^":
        return left ** right
    return 0


# This function take in the input and return the result of that math statement
def calcExpression(n: str):

    # This call the function to build a tree and return the root
    root = build_tree(n)

    # Then this call another funciton and the root as parameter and calculate it
    # Then it return the result
    return print(f"The answer is: {round(calcTree(root), 2)}")



# EXAMPLES:

calcExpression("0.4")

calcExpression("3.14-3")

calcExpression("3+5") 

calcExpression("3+5*2") 

calcExpression("9+12-34*4/34^2+12")  

calcExpression("2^3/4")  

calcExpression("9+12-34*4/34^2+12*2") 

calcExpression("7*3+6-4^2/2") 

