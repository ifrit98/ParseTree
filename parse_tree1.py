from stack import Stack
from BinaryTree import *

def buildParseTree(exp):
    fplist = exp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        if i == '(':
            # If new expression, create new empty left child, push current root onto stack
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            # If a number, set node to it and return to the parent node (reached a leaf node)
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/']:
            # If operator, set node val to it and create empty right child
            # Push current node on stack, descend to right child
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            # If end of expression, pop top of stack
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree

pt = buildParseTree("( ( 10 + 5 ) * 3 )")
pt.height(pt.key)
pt.inorder()
print('Evaluated tree:',evaluate(pt))