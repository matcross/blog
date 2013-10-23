#!/usr/bin/env python
"""
The class for nodes in a k-ary circularly linked tree from
http://matcross.wordpress.com/2013/01/02/python-arborealis/
"""
class TreeNode(object):
    """
    A node in a k-ary circularly linked tree.
    """
    def __init__(self,
                 body=None,
                 nprev=None,
                 nnext=None,
                 nup=None,
                 ndown=None):
        self.body = body
        self.nprev = nprev
        self.nnext = nnext
        self.nup = nup
        self.ndown = ndown

    def __repr__(self):
        return get_repr(self)

    def __str__(self):
        return str(self.body)

    def is_leaf(self):
        "Is the node a leaf?"
        return (self.ndown is None)

    def traverse(self,
                 process_node=None):
        """
        Depth-first traversal of the node.
        process_node may be specified as the visitor function,
        defaulting to 'write'.
        """
        depth = 0
        node = self

        while (node is not None):

            if (process_node is None):
                import sys
                sys.stdout.write(' '*depth*2 + str(node) + '\n')
            else:
                process_node(node)

            if (node.is_leaf()):

                while (node is not None and
                       node != self and
                       node.nnext is None):
                    node = node.nup
                    depth = depth - 1

                if (node is None or
                    node == self):
                    break

                node = node.nnext
            else:
                node = node.ndown
                depth = depth + 1

def get_repr(self,
             depth=0):
    """
    Recursive pretty-printing function for any class.
    Output is elided for recursive structures.
    """
    keys = list(self.__dict__.keys())
    keys.sort()

    fields = []

    for key in keys:

        if (isinstance(self.__dict__[key], self.__class__)):

            if (depth < 1):
                value = get_repr(self.__dict__[key], depth=depth+1)
            else:
                value = ''.join(['<',
                                 self.__class__.__name__,
                                 '(...)>'])

        else:
            value = str(self.__dict__[key])

        fields.append(''.join([key,
                               '=',
                               value]))

    return ''.join([self.__class__.__name__,
                    '(',
                    ', '.join(fields),
                    ')'])

def example():
    """
    Populates a small tree for the expression "7 = 1 + 2 * 3".
    Demonstrates the self-truncating recursive repr and the traversal method.
    """
    root = TreeNode()

    asgn = TreeNode('=')
    root.ndown = asgn
    asgn.nup = root

    lhs = TreeNode(7)
    asgn.ndown = lhs
    lhs.nup = asgn

    plus = TreeNode('+')
    lhs.nnext = plus
    plus.nprev = lhs
    plus.nup = asgn

    one = TreeNode(1)
    plus.ndown = one
    one.nup = plus

    times = TreeNode('*')
    one.nnext = times
    times.nprev = one
    times.nup = plus

    two = TreeNode(2)
    times.ndown = two
    two.nup = times

    three = TreeNode(3)
    two.nnext = three
    three.nprev = two
    three.nup = times

    end = TreeNode('end')
    asgn.nnext = end
    end.nprev = asgn

    print(repr(root))
    root.traverse()

if (__name__=='__main__'):
    example()
