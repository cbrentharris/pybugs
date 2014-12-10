import ast
import astunparse
from utils import *

class IfVisitor(object):
    u"""The If Vistor visits a BugNode, traverses it, and tests for common
    antipatterns or dead code if the node is an If node
    """

    def visit(self, node):
        u"""runs all of the tests on the node"""
        self.test_program_doesnt_have_if_true_else(node.ast_node)
        self.test_program_doesnt_have_if_false(node.ast_node)
        self.test_program_doesnt_return_true_after_if(node.ast_node)
        self.test_program_doesnt_return_false_after_if(node.ast_node)

    def test_program_doesnt_have_if_true_else(self, node):
        u"""checks that the node does not resemble the block of code such as
        if True:
            ...
        """
        if not isinstance(node, ast.If):
            return 
        if not node.test.id == "True":
            return         
        if not hasattr(node,'orelse'):
            print "Unecessary if True statement - line {}".format(node.lineno)
        else:
            print "Dead code in else block - line {}".format(node.lineno)
        print astunparse.unparse(node)

    def test_program_doesnt_have_if_false(self, node):
        u"""checks that the node does not resemble the block of code such as
        if False:
            ...
        """
        if not isinstance(node, ast.If):
            return 
        if not node.test.id == "False":
            return         
        if not hasattr(node,'test'):
            print "Unecessary if False statement - line {}".format(node.lineno)
        else:
            print "Dead code in if block - line {}".format(node.lineno)
        print astunparse.unparse(node)

    def test_program_doesnt_return_true_after_if(self, node):
        u"""checks that the node does not resemble the block of code such as
        if (some boolean expression):
            return True
        else:
            return False
        """
        if not isinstance(node, ast.If):
            return
        if return_true_in_if_body(node.body) and return_false_in_else_body(node.orelse):
            print "Unnecessary conditional - simply return test - line {}".format(node.lineno)
            print astunparse.unparse(node)

    def test_program_doesnt_return_false_after_if(self, node):
        u"""checks that the node does not resemble the block of code such as
        if (some boolean expression):
            return False
        else:
            return True
        """
        if not isinstance(node, ast.If):
            return
        if self.return_false_in_if_body(node.body) and self.return_true_in_else_body(node.orelse):
            print "Unnecessary conditional - simply return negation of test - line {}".format(node.lineno)
            print astunparse.unparse(node)

    def return_true_in_if_body(self, _list):
        for subnode in _list:
            if is_return_true(subnode):
                return True
            for child in ast.walk(subnode):
                if isinstance(child, ast.For) or isinstance(child, ast.While):
                    break
                if is_return_true(child):
                    return True
        return False

    def return_false_in_if_body(self, _list):
        for subnode in _list:
            if is_return_false(subnode):
                return True
            for child in ast.walk(subnode):
                if isinstance(child, ast.For) or isinstance(child, ast.While):
                    break
                if is_return_false(child):
                    return True
        return False

    def return_true_in_else_body(self, _list):
        for subnode in _list:
            if is_return_true(subnode):
                return True
            for child in ast.walk(subnode):
                if isinstance(child, ast.For) or isinstance(child, ast.While):
                    break
                if is_return_true(child):
                    return True
        return False

    def return_false_in_else_body(self, _list):
        for subnode in _list:
            if is_return_false(subnode):
                return True
            for child in ast.walk(subnode):
                if isinstance(child, ast.For) or isinstance(child, ast.While):
                    break
                if is_return_false(child):
                    return True
        return False



