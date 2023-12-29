# -*- coding:utf-8 -*-

import numpy as np


def SPMGen(W,pos,node):
    if node.lchild is None and node.rchild is None:
        return W

    if node.value[:3] == "AND":
        W = And(W,pos)
    elif node.value[:2] == "OR":
        W = OR(W,pos)
    else:
        print("Error: Unexpected node value: ",node.value)

    if node.lchild.value[0] == "P":
        pos += 1
    else:
        W,pos = SPMGen(W, pos, node.lchild)

    if node.rchild.value[0] == "P":
        pos += 1
    else:
        W,pos = SPMGen(W, pos, node.rchild)

    return W,pos





def And(W,x):
    r,c = W.shape
    new_W = np.zeros(shape=(r+1, c+1))

    new_W[0:x,:] = np.hstack((W[0:x,:], np.zeros(shape=(x,1))))
    new_W[x+2:,:] = np.hstack((W[x+1:,:], np.zeros(shape=(r-x-1,1))))
    new_W[x:x+2,:] = np.vstack((np.hstack((np.zeros(shape=(1,c)),np.array([1]).reshape(1,1))),
                                np.hstack((W[x,:],-1))))

    return new_W


def OR(W,x):
    r,c = W.shape
    new_W = np.zeros(shape=(r+1,c))
    new_W[0:x, :] = W[0:x, :]
    new_W[x + 2:, :] = W[x + 1:, :]
    new_W[x:x + 2, :] = np.vstack((W[x,:],W[x,:]))

    return new_W