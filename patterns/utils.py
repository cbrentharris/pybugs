def is_return_true(node):
    return isinstance(node, ast.Return) and node.value.id == "True"

def is_return_false(node):
    return isinstance(node, ast.Return) and node.value.id == "False"