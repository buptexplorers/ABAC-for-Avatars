# -*- coding:utf-8 -*-

import tree

testTreeSingleAttr = tree.Tree()
testTreeSingleAttr.root = tree.Node("P1", None, None)


testTreeAnd = tree.Tree()
testTreeAnd.root = tree.Node("AND", None, None)
testTreeAnd.root.lchild = tree.Node("P1", None, None)
testTreeAnd.root.rchild = tree.Node("P2", None, None)

testTreeOr = tree.Tree()
testTreeOr.root = tree.Node("OR", None, None)
testTreeOr.root.lchild = tree.Node("P1", None, None)
testTreeOr.root.rchild = tree.Node("P2", None, None)