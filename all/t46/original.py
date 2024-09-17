# code generated by chatgpt
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def __str__(self):
        return self._in_order_traversal(self.root)
        # return self._middle_first_traversal(self.root)
        # return self._post_order_traversal(self.root)
        # return self._pre_order_traversal(self.root)

    def _in_order_traversal(self, node):
        if node is None:
            return ''
        else:
            result = ''
            result += self._in_order_traversal(node.left)
            result += str(node.value) + ' '
            result += self._in_order_traversal(node.right)
            return result

    def _pre_order_traversal(self, node):
        if node is None:
            return ''
        else:
            result = ''
            result += str(node.value) + ' '
            result += self._pre_order_traversal(node.left)
            result += self._pre_order_traversal(node.right)
            return result
    # def _middle_first_traversal(self, node):
    #     if node is None:
    #         return ''
    #     else:
    #         model_answer_result = ''
    #         model_answer_result += self._middle_first_traversal(node.left)
    #         model_answer_result += str(node.value) + ' '
    #         model_answer_result += self._middle_first_traversal(node.right)
    #         return model_answer_result

    def _post_order_traversal(self, node):
        if node is None:
            return ''
        else:
            result = ''
            result += self._post_order_traversal(node.left)
            result += self._post_order_traversal(node.right)
            result += str(node.value) + ' '
            return result

# Exemplo de uso
if __name__ == "__main__":
    # Construindo a árvore
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    # Criando a instância da árvore
    tree = BinaryTree(root)

    # Imprimindo a representação da árvore
    print(tree)