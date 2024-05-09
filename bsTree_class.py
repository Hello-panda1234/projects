from collections import deque
import math
import sys

class Tree(object):
    class Node(object):
        def __init__(self, v, l=None, r=None):
            self.value = v
            self.left = l
            self.right = r

    def __init__(self):
        self.root = None


    def add(self, value):
        self.root = self.add_util(self.root, value)

    def add_util(self, node, value):
        if node == None:
            node = self.Node(value)
        else:
            if node.value > value:
                node.left = self.add_util(node.left, value)
            else:
                node.right = self.add_util(node.right, value)
        return node


    def print_pre_order(self):
        self.print_pre_order_util(self.root)
        print()


    def print_pre_order_util(self, node):
        # pre order  
        if node != None:
            print(node.value, end=' ')
            self.print_pre_order_util(node.left)
            self.print_pre_order_util(node.right)


    def print_post_order(self):
        self.print_post_order_util(self.root)
        print()

    def print_post_order_util(self, node):
        # post order  
        if node != None:
            self.print_post_order_util(node.left)
            self.print_post_order_util(node.right)
            print(node.value, end=' ')
    def print_in_order(self):
        self.print_in_order_util(self.root)
        print()


    def print_in_order_util(self, node):
        # In order  
        if node != None:
            self.print_in_order_util(node.left)
            print(node.value, end=' ')
            self.print_in_order_util(node.right)
    def find(self, value):
        curr = self.root
        while curr != None:
            if curr.value == value:
                return True
            elif curr.value > value:
                curr = curr.left
            else:
                curr = curr.right
        return False


    def find_min(self):
        node = self.root
        if node == None:
            raise RuntimeError("ListEmptyException")
        while node.left != None:
            node = node.left
        return node.value


    def find_max(self):
        node = self.root
        if node == None:
            raise RuntimeError("ListEmptyException")
        while node.right != None:
            node = node.right
        return node.value

    def find_max_util(self, curr):
        node = curr
        if node == None:
            return None
        while node.right != None:
            node = node.right
        return node

    def find_min_util(self, curr):
        node = curr
        if node == None:
            return None
        while node.left != None:
            node = node.left
        return node

    def free(self):
        self.root = None


    def tree_depth(self):
        return self.tree_depth_util(self.root)

    def tree_depth_util(self, root):
        if root == None:
            return 0
        else:
            lDepth = self.tree_depth_util(root.left)
            rDepth = self.tree_depth_util(root.right)
            if lDepth > rDepth:
                return lDepth + 1
            else:
                return rDepth + 1

    def is_equal(self, T2):
        return self.is_equal_util(self.root, T2.root)

    def is_equal_util(self, node1, node2):
        if node1 == None and node2 == None:
            return True
        elif node1 == None or node2 == None:
            return False
        else:
            return (self.is_equal_util(node1.left, node2.left) and self.is_equal_util(node1.right, node2.right) and (node1.value == node2.value))

    def copy_tree(self):
        tree2 = Tree()
        tree2.root = self.copy_tree_util(self.root)
        return tree2

    def copy_tree_util(self, curr):
        if curr != None:
            temp = self.Node(curr.value)
            temp.left = self.copy_tree_util(curr.left)
            temp.right = self.copy_tree_util(curr.right)
            return temp
        else:
            return None


    def copy_mirror_tree(self):
        tree2 = Tree()
        tree2.root = self.copy_mirror_tree_util(self.root)
        return tree2

    def copy_mirror_tree_util(self, curr):
        if curr != None:
            temp = self.Node(curr.value)
            temp.right = self.copy_mirror_tree_util(curr.left)
            temp.left = self.copy_mirror_tree_util(curr.right)
            return temp
        else:
            return None


    def num_nodes(self):
        return self.num_nodes_util(self.root)

    def num_nodes_util(self, curr):
        if curr == None:
            return 0
        else:
            return (1 + self.num_nodes_util(curr.right) + self.num_nodes_util(curr.left))


    def num_full_nodes_bt(self):
        return self.num_full_nodes_bt_util(self.root)

    def num_full_nodes_bt_util(self, curr):
        if curr == None:
            return 0
        count = self.num_full_nodes_bt_util(curr.right) + self.num_full_nodes_bt_util(curr.left)
        if curr.right != None and curr.left != None:
            count += 1
        return count


    def max_length_path_bt(self):
        return self.max_length_path_bt_util(self.root)

    def max_length_path_bt_util(self, curr):
        # diameter
        if curr == None:
            return 0
        leftPath = self.tree_depth_util(curr.left)
        rightPath = self.tree_depth_util(curr.right)
        maxpath = leftPath + rightPath + 1
        leftMax = self.max_length_path_bt_util(curr.left)
        rightMax = self.max_length_path_bt_util(curr.right)
        if leftMax > maxpath:
            maxpath = leftMax
        if rightMax > maxpath:
            maxpath = rightMax
        return maxpath


    def num_leaf_nodes(self):
        return self.num_leaf_nodes_util(self.root)

    def num_leaf_nodes_util(self, curr):
        if curr == None:
            return 0
        if curr.left == None and curr.right == None:
            return 1
        else:
            return (self.num_leaf_nodes_util(curr.right) + self.num_leaf_nodes_util(curr.left))


    def sum_all_bt(self):
        return self.sum_all_bt_util(self.root)

    def sum_all_bt_util(self, curr):
        if curr == None:
            return 0
        rightSum = self.sum_all_bt_util(curr.right)
        leftSum = self.sum_all_bt_util(curr.left)
        finalsum = rightSum + leftSum + curr.value
        return finalsum


    def print_all_path(self):
        stk = []
        self.print_all_path_util(self.root, stk)

    def print_all_path_util(self, curr, stk):
        if curr == None:
            return
        stk.append(curr.value)
        if curr.left == None and curr.right == None:
            print(stk)
            stk.pop()
            return
        self.print_all_path_util(curr.right, stk)
        self.print_all_path_util(curr.left, stk)
        stk.pop()

    def print_in_range(self, minval, maxval):
        self.print_in_range_util(self.root, minval, maxval)
        print()

    def print_in_range_util(self, root, minval, maxval):
        if root == None:
            return
        self.print_in_range_util(root.left, minval, maxval)
        if root.value >= minval and root.value <= maxval:
            print(root.value, end=' ')
        self.print_in_range_util(root.right, minval, maxval)


    def search_bt(self, value):
        return self.search_bt_util(self.root, value)

    def search_bt_util(self, root, value):
        if root == None:
            return False
        
        if root.value == value or self.search_bt_util(root.left, value) or self.search_bt_util(root.right, value):
            return True

        return False
