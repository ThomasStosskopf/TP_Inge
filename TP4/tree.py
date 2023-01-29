# encode : utf8
"""
training to understand binary tree
"""

class Binanytree:
    """
    Binary tree
    """
    def __init__(self) -> None:
        """
        Initiation of our class Binarytree
        """
        self.root = None
        self.node = None

    def print_tree(self):
        """
        display the node and all the nodes under it
        """
        return self.root.display_node()


class Node:
    """
    class to create object node that can be add in a
    binary tree
    """

    def __init__(self, value):
        """
        method to init our Node with
        value: integer value
        left: other node object that comes after this one
        right: other node object that comes after this one
        depth: depth of the node in the ninary tree
        """
        self.value: int = value
        self.left= None
        self.right= None
        self.depth: int = 0

    def __str__(self):
        """
        method to return these value when we print
        """
        return f"V:{str(self.value)}/D:{str(self.depth)}"

    def display_node(self):
        """
        display the node and all the nodes under it
        """
        space = ""
        # '_' is used instead of i to iterate by convention
        # when you're not using the variable
        for _ in range(0,self.depth):
            # for a depth = n, we add n "\n" to the variable space
            space += "\t"
        retour = str(space) + str(self) + "\n"
        if self.right:
            retour += self.right.display_node()
        if self.left:
            retour += self.left.display_node()
        return retour


    def display_node_hardway(self):
        """Method to display the tree verticaly"""
        # first, if the node has no child:
        if self.right is None and self.left is None:
            retour = "%s" % self.value
            width = len(retour)
            middle = width // 2
            return retour, middle
        # the node has only a right child:
        if self.left is None:
            pass
        # the node has only a left child:
        if self.right is None:
            pass
        # the node has two child
        else:
            left = self.left.display_node_hardway()
            right = self.right.display_node_hardway()


    def is_leaf(self):
        """
        boolean method to return true if a node is a leaf
        and False if it is not a leaf
        a leaf is a node has no left or right node
        """
        return self.left is None and self.right is None

    def add_node(self, left = None, right = None):
        """
        methode to add a new node to the tree with
        two possible parameters
        :param left: the new node that will be on the left side
        :param right: new node on the right side
        """
        self.left = left
        self.right = right
        if self.left:
            left.depth = self.depth + 1
            left.update_children_depth()
        if self.right:
            right.depth = self.depth + 1
            right.update_children_depth()

    def update_children_depth(self):
        """
        method to update the depth of the nodes
        everytime we had a new node
        """
        if self.left:
            self.left.depth = self.depth + 1
            self.left.update_children_depth()
        if self.right:
            self.right.depth = self.depth + 1
            self.right.update_children_depth()

    def depth_max(self, max_depth):
        """
        method to know the max depth of a tree
        """
        if self.is_leaf():
            if self.depth > max_depth:
                return self.depth
            else:
                return max_depth
        # if i'm a node note a leaf
        else:
            if self.right:
                max_depth = self.right.depth_max(max_depth)

            if self.left:
                max_depth = self.left.depth_max(max_depth)
            return max_depth


if __name__ == "__main__":
    node1 = Node(value=0)
    node2 = Node(value=2)
    node3 = Node(value=3)
    node4 = Node(value=4)
    node1.add_node(node2, node3)
    tree1 = Binanytree()
    tree1.root = node1
    node3.add_node(node4)
    # print("Node1:\n", node1)
    # print("Node2:\n", node2)
    # print("Node3:\n", node3)
    #
    # print("leaf2 ??", node2.is_leaf())
    # print("leaf3 ??", node3.is_leaf())
    # print(node1.display_node())
    #
    # print(node4)

    node5 = Node(value=5)
    node6 = Node(value=6)
    node7 = Node(value=7)
    node8 = Node(value=8)
    node5.add_node(node6, node7)
    # print(node5.display_node())
    node4.add_node(node5)
    node7.add_node(node8)
    print(tree1.print_tree())
    print(node1.display_node_hardway())



# avoir un joli affichage en mode "arbre" dans le terminal
# utilise une récursive
