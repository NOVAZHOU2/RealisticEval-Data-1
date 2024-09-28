import { TreeNode, BinaryTree } from './yourBinaryTreeModule'; // Replace with the actual path to your module

describe('BinaryTree', () => {
    let tree: BinaryTree;

    beforeEach(() => {
        // Setup basic tree structure for testing
        // Tree structure:
        //      1
        //     / \
        //    2   3
        //   / \
        //  4   5
        tree = new BinaryTree(new TreeNode(1));
        tree.root!.left = new TreeNode(2, new TreeNode(4), new TreeNode(5));
        tree.root!.right = new TreeNode(3);
    });

    test('preorder traversal', () => {
        const result = tree.preorderTraversal(tree.root);
        expect(result).toEqual([1, 2, 4, 5, 3]);
    });

    test('inorder traversal', () => {
        const result = tree.inorderTraversal(tree.root);
        expect(result).toEqual([4, 2, 5, 1, 3]);
    });

    test('postorder traversal', () => {
        const result = tree.postorderTraversal(tree.root);
        expect(result).toEqual([4, 5, 2, 3, 1]);
    });

    test('traversals on an empty tree', () => {
        const emptyTree = new BinaryTree();
        expect(emptyTree.preorderTraversal(emptyTree.root)).toEqual([]);
        expect(emptyTree.inorderTraversal(emptyTree.root)).toEqual([]);
        expect(emptyTree.postorderTraversal(emptyTree.root)).toEqual([]);
    });

    test('traversals on a single node tree', () => {
        const singleNodeTree = new BinaryTree(new TreeNode(10));
        expect(singleNodeTree.preorderTraversal(singleNodeTree.root)).toEqual([10]);
        expect(singleNodeTree.inorderTraversal(singleNodeTree.root)).toEqual([10]);
        expect(singleNodeTree.postorderTraversal(singleNodeTree.root)).toEqual([10]);
    });
});