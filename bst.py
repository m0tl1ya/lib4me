#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import numpy as np
import functools
from collections import defaultdict

from permutation import duplicate_permutation


class TreeNode(object):
    def __init__(self, data, depth):
        self.data = data
        self.depth = depth
        self.left = None
        self.right = None
        self.parent = None

    def set_left_child(self, Node):
        self.left = Node
        Node.parent = self

    def set_right_child(self, Node):
        self.right = Node
        Node.parent = self

    def get_data(self):
        return self.data

    def get_left_child(self):
        return self.left

    def get_left_child(self):
        return self.right

class BinaryTree(object):
    def __init__(self):
        self.root = None
        self.size = 0
        self.max_depth = 0

    def insert_in_order(self, new_data, Node=None, depth=1):
        if Node is None:
            Node = self.root
        if self.root is not None:
            depth += 1
            if new_data <= Node.data:
                if Node.left is None:
                    Node.set_left_child(TreeNode(new_data, depth))
                    self.size += 1
                else:
                    self.insert_in_order(new_data, Node.left, depth)
            else:
                if Node.right is None:
                    Node.set_right_child(TreeNode(new_data, depth))
                    self.size += 1
                else:
                    self.insert_in_order(new_data, Node.right, depth)
        else:
            self.root = TreeNode(new_data, depth)
            self.size += 1

    def search(self, search_key, Node=None):
        "Return Node"
        if Node is None:
            Node = self.root
        result = None
        if search_key == Node.data:
            result = Node
        elif search_key <= Node.data:
            if Node.left is not None:
                result = self.search(search_key, Node.left)
        else:
            if Node.right is not None:
                result = self.search(search_key, Node.right)
        return result

    def get_size(self):
        return self.size

    def insert_data_list(self, data_list):
        for d in data_list:
            self.insert_in_order(d)

    def visit(self, Node):
        print('value:{}'.format(Node.data))
        print('depth:{}'.format(Node.depth))

    def in_order_traversal_values(self, Node=None):
        node_data_list = []
        if Node is None:
            Node = self.root
        if Node.left is not None:
            node_data_list += self.in_order_traversal_values(Node.left)
        # self.visit(Node)
        node_data_list.append(Node.data)
        if Node.right is not None:
            node_data_list += self.in_order_traversal_values(Node.right)
        return node_data_list

    def in_order_traversal(self, Node=None):
        node_list = []
        if Node is None:
            Node = self.root
        if Node.left is not None:
            node_list += self.in_order_traversal(Node.left)
        # self.visit(Node)
        node_list.append(Node)
        if Node.right is not None:
            node_list += self.in_order_traversal(Node.right)
        return node_list

    def create_minimum_tree(self, data_list):
        "."
        len_of_list = len(data_list)
        pivot_id = int(len_of_list / 2)
        self.insert_in_order(data_list[pivot_id])
        if len_of_list >= 3:
            self.create_minimum_tree(data_list[:pivot_id])
            self.create_minimum_tree(data_list[pivot_id+1:])
        if len_of_list == 2:
            self.insert_in_order(data_list[pivot_id-1])

    def create_depth_list(self, full_depth_dict, Node):
        "."
        if Node.left is not None:
            self.create_depth_list(full_depth_dict, Node.left)
        full_depth_dict[Node.depth].append(Node.data)
        if Node.right is not None:
            self.create_depth_list(full_depth_dict, Node.right)

    def compute_depth_list(self, Node=None):
        "."
        if Node is None:
            Node = self.root
        depth_dict = defaultdict(lambda: [])
        self.create_depth_list(depth_dict, Node)
        return depth_dict

    def count_max_depth(self, Node=None, max_depth_list=[]):
        if Node is None:
            Node = self.root
        if Node.left is None and Node.right is None:
            max_depth_list.append(Node.depth)
        else:
            if Node.left is not None:
                self.count_max_depth(Node.left, max_depth_list)
            if Node.right is not None:
                self.count_max_depth(Node.right, max_depth_list)

    def is_balanced_tree(self, Node=None):
        "."
        if Node is None:
            Node = self.root
        max_depth_left = [Node.depth]
        max_depth_right = [Node.depth]
        if Node.left is not None:
            self.count_max_depth(Node.left, max_depth_left)
        if Node.right is not None:
            self.count_max_depth(Node.right, max_depth_right)
        if np.abs(np.max(max_depth_left) - np.max(max_depth_right)) <= 1:
            if Node.left is not None:
                self.is_balanced_tree(Node.left)
            if Node.right is not None:
                self.is_balanced_tree(Node.right)
        else:
            return False
        return True

    def is_bst(self):
        "."
        node_data_list = self.in_order_traversal_values()
        lis = list(map(lambda x, y: x <= y, node_data_list,
                                            node_data_list[1:]))
        if len(list(filter(lambda x: x == True, lis))) \
            == len(node_data_list) - 1:
            print('This tree is a BST.\n')
            return True
        else:
            print('This tree is NOT a BST.\n')
            return False

    def find_next_node(self, d):
        "."
        node_data_list = self.in_order_traversal_values()
        print(node_data_list)
        if d in node_data_list:
            index_of_next = node_data_list.index(d) + 1
            try:
                next_node = self.search(node_data_list[index_of_next])
                return next_node
            except:
                return None
        else:
            return None

    def find_ancester(self, d):
        ""
        src_node = self.search(d)
        if src_node.parent is None:
            return []
        ancesters = []
        for ancester in self.find_ancester(src_node.parent.data):
            ancesters.append(ancester)
        ancesters.append(src_node.parent.data)
        return ancesters

    def list_possible_BST_array(self, Node=None):
        ""
        # print(self.data)
        if Node is None:
            Node = self.root
        if Node.left is not None:
            left_possible_array = self.list_possible_BST_array(Node.left)
        else:
            left_possible_array = [[]]
        if Node.right is not None:
            right_possible_array = self.list_possible_BST_array(Node.right)
        else:
            right_possible_array = [[]]
        if left_possible_array == [[]] and right_possible_array == [[]]:
            return list([[Node.data]])

        possible_BST_array = []
        for itr1 in left_possible_array:
            for itr2 in right_possible_array:
                possible_BST_array += list(duplicate_permutation(itr1, itr2))
        for i, itr in enumerate(possible_BST_array):
            possible_BST_array[i] = list([Node.data]) + itr
        return possible_BST_array

    def get_random_node(self):
        ""
        random_id = np.random.randint(self.size)
        node_data_list = self.in_order_traversal_values()
        return self.search(node_data_list[random_id])

    def search_route_to_descendant(self, Node=None):
        ""
        if Node is None:
            Node = self.root
        if Node.left is not None:
            left_possible_array = \
                self.search_route_to_descendant(Node.left)
        else:
            left_possible_array = [[]]
        if Node.right is not None:
            right_possible_array = \
                self.search_route_to_descendant(Node.right)
        else:
            right_possible_array = [[]]
        possible_route = [[Node.data]]
        if left_possible_array == [[]] and right_possible_array == [[]]:
            return possible_route
        for itr in left_possible_array:
            possible_route.append([Node.data]+itr)
        for itr in right_possible_array:
            possible_route.append([Node.data]+itr)
        # print(possible_route)
        return possible_route

    def find_total_equal_route(self, value):
        ""
        node_data_list = self.in_order_traversal()
        # print(node_data_list)
        matched_route = []
        for node in node_data_list:
            possible_route = self.search_route_to_descendant(node)
            for route in possible_route:
                if functools.reduce(lambda x, y: x + y, route) == value:
                    matched_route.append(route)
        return matched_route






def get_next_node(tree, value):
    next_node = tree.find_next_node(value)
    if next_node is not None:
        print(next_node.data)
    else:
        print('None')

def find_common_ancester(tree, value1, value2):
    ancesters1 = tree.find_ancester(value1)
    ancesters2 = tree.find_ancester(value2)
    if ancesters1 != [] and ancesters2 != []:
        if len(ancesters1) >= len(ancesters2):
            lis = [ancesters1[:i+1] == ancesters2[:i+1] for i in
                range(len(ancesters2))]
            indexes = [i for i, x in enumerate(lis) if x == True]
            last_match_index = indexes.pop()
        else:
            lis = [ancesters1[:i+1] == ancesters2[:i+1] for i in
                range(len(ancesters1))]
            indexes = [i for i, x in enumerate(lis) if x == True]
            last_match_index = indexes.pop()
        return ancesters1[last_match_index]
    else:
        return False


if __name__ == '__main__':
    # root = 4
    data_list = [4,1,43,5,45,6,656,57,4]
    b_tree = BinaryTree()
    b_tree.insert_data_list(data_list)
    print(b_tree.get_size())
    node_data_list = b_tree.in_order_traversal_values()
    print(node_data_list)
    depth_dict = b_tree.compute_depth_list()
    print(sorted(depth_dict.items()))
    print(b_tree.is_balanced_tree())
    b_tree.is_bst()
    # print(b_tree.find_ancester(57))

    data_list2 = [1, 2, 3, 4, 5, 6, 7, 9, 100, 342]
    b_tree2 = BinaryTree()
    b_tree2.create_minimum_tree(data_list=data_list2)
    print(b_tree2.get_size())
    node_data_list2 = b_tree2.in_order_traversal_values()
    print(node_data_list2)
    depth_dict = b_tree2.compute_depth_list()
    print(sorted(depth_dict.items()))
    print(b_tree2.is_balanced_tree())
    b_tree2.is_bst()

    data_list3 = [1, 12, 3, 4, 5, 6, 7, 9, 100, 342]
    b_tree3 = BinaryTree()
    b_tree3.insert_data_list(data_list3)
    node_data_list3 = b_tree3.in_order_traversal_values()
    print(node_data_list3)
    print(b_tree3.search(100))
    get_next_node(b_tree3, 12)
    get_next_node(b_tree3, 4)
    get_next_node(b_tree3, 100)
    get_next_node(b_tree3, 20)
    get_next_node(b_tree3, 342)

    data_list = [4,1,43,5,45,6,656,57,4]
    b_tree = BinaryTree()
    b_tree.insert_data_list(data_list)
    v1 = 45
    v2 = 656
    print(b_tree.find_ancester(v1))
    print(b_tree.find_ancester(v2))
    print(find_common_ancester(b_tree, v1, v2))

    data_list = [4,1,43,5,45,6,656,57]
    b_tree = BinaryTree()
    b_tree.insert_data_list(data_list)
    BST_array = b_tree.list_possible_BST_array()
    for i in BST_array:
        print(i)
    print(len(BST_array))

    data_list = [6, 4, 2, 8, 7, 5, 9, 1]
    b_tree = BinaryTree()
    b_tree.insert_data_list(data_list)
    BST_array = b_tree.list_possible_BST_array()
    for i in BST_array:
        print(i)
    print(len(BST_array))
