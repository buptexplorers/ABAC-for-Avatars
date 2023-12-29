# -*- coding:utf-8 -*-

class Node:
    """节点类"""
    def __init__(self, value, lchild=None, rchild=None):
        self.value = value
        self.lchild = lchild
        self.rchild = rchild


class Tree:
    """树类"""
    def __init__(self, root=None):
        self.root = root


