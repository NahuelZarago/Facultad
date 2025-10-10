# Implementar una función que permita cargar una expresión matemática en un árbol binario
# (no balanceado), y resuelva lo siguiente:
# a. determinar cuál de los barridos muestra la expresión en el orden correcto;
# b. resolver la expresión matemática y muestre el resultado.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class ExpressionTree:
    def __init__(self):
        self.root = None

    def in_order(self, node):
        if node is not None:
            if node.left or node.right:
                print("(", end="")
            self.in_order(node.left)
            print(node.value, end=" ")
            self.in_order(node.right)
            if node.left or node.right:
                print("", end="")

    def pre_order(self, node):
        if node is not None:
            print(node.value, end=" ")
            self.pre_order(node.left)
            self.pre_order(node.right)

    def post_order(self, node):
        if node is not None:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.value, end=" ")

    def evaluate(self, node):
        if node is None:
            return 0
        
        if node.left is None and node.right is None:
            return int(node.value)

        
        left_val = self.evaluate(node.left)
        right_val = self.evaluate(node.right)

        if node.value == "+":
            return left_val + right_val
        elif node.value == "-":
            return left_val - right_val
        elif node.value == "*":
            return left_val * right_val
        elif node.value == "/":
            return left_val / right_val



tree = ExpressionTree()
tree.root = Node("*")

tree.root.left = Node("+")
tree.root.left.left = Node("3")
tree.root.left.right = Node("5")

tree.root.right = Node("-")
tree.root.right.left = Node("2")
tree.root.right.right = Node("4")


print("Inorden:", end=" ")
tree.in_order(tree.root)   
print("\nPreorden:", end=" ")
tree.pre_order(tree.root) 
print("\nPostorden:", end=" ")
tree.post_order(tree.root)


print("Resultado de la expresion:", tree.evaluate(tree.root))
