class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

    def print_tree(self, level=0):
        if self.right:
            self.right.print_tree(level + 1)
        print('     ' * level + f'{self.val}/{level}')
        if self.left:
            self.left.print_tree(level + 1)


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        new_node = Node(val)
        if not self.root:
            self.root = new_node
        else:
            current = self.root
            while True:
                if val < current.val:
                    if not current.left:
                        current.left = new_node
                        break
                    else:
                        current = current.left
                elif val > current.val:
                    if not current.right:
                        current.right = new_node
                        break
                    else:
                        current = current.right

    def print_tree(self):
        if self.root:
            self.root.print_tree()

# first, if the node has no child:
        if self.right is None and self.left is None:
            retour = "%s" % self.value
            width = len(retour)
            height = 1
            middle = width // 2
            return str([retour]), width, height, middle

        # the node has only a right child:
        if self.left is None:
            retour, n, p, x = self.right.display_node_hardway()
            next = '%s' % self.value
            len_next = len(next)
            first_line = next + x * ' ' + (n - x) * ' '
            second_line = (len_next + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [len_next * ' ' + line for line in retour]
            return str([first_line, second_line]) + str(shifted_lines), n + len_next, p + 2, len_next//2

        # the node has only a left child:
        if self.right is None:
            retour, n, p, x = self.left.display_node_hardway()
            next = '%s' % self.value
            len_next = len(next)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + next
            second_line = x * ' ' + ' ' + (n - x - 1 + len_next) * ' '
            shifted_lines = [line + len_next * ' ' for line in retour]
            return str([first_line, second_line]) + str(shifted_lines), n + len_next, p + 2, n + len_next // 2

        # the node has two child
        else:
            left, n, p, x = self.left.display_node_hardway()
            right, m, q, y = self.right.display_node_hardway()
            next = '%s' % self.value
            len_next = len(next)
            first_line = (x + 1) * ' ' + (n - x - 1) * ' ' + next + y * ' ' + (m - y) * ' '
            second_line = x * ' ' + ' ' + (n - x - 1 + len_next + y) * ' ' + ' ' + (m - y - 1) * ' '
            if p < q:
                left += [n * ' '] * (q - p)
            elif q < p:
                right += [m * ' '] * (p - q)
            zipped_lines = zip(left, right)
            lines = [first_line, second_line] + [a + len_next * ' ' + b for a, b in zipped_lines]
            return lines, n + m + len_next, max(p, q) + 2, n + len_next // 2


########################################
from asciitree.drawing import BoxStyle, render_tree
from asciitree.node import Node, CLOSE_BRANCH, LEAF, OPEN_BRANCH


# Define a node class to hold the data and children of each node
class MyNode(Node):
    def __init__(self, name, children=None):
        super().__init__(name, children)


# Create the root node and its children
root = MyNode("root", [
    MyNode("left", [
        MyNode("left.left"),
        MyNode("left.right"),
    ]),
    MyNode("right"),
])

# Render the tree and print it
print(render_tree(root, node_factory=MyNode,
                  box_style=BoxStyle(gfx=OPEN_BRANCH, horiz_len=1)))


#######################################
print(f"\t {self}")
        max_value = 8
        for _ in range(0,max_value):
            # first, if the node has no child:
            if self.right is None and self.left is None:
                line = str(self)
                return line

            # the node has only a right child:
            if self.left is None:
                line += str(self.right.display_node_hardaway())
                return line

            # the node has only a left child:
            if self.right is None:
                line += str(self.left.display_node_hardway())
                return line

            # the node has two child
            else:
                line = str(self.left.display_node_hardway()) + "\t" + str(self.right.display_node_hardaway())
                return line




# usage
tree = BinaryTree()
tree.insert(5)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(6)
tree.insert(7)
tree.insert(8)
tree.print_tree()
