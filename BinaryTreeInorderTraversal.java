class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> arr = new ArrayList<>();
        inordervisit(root, arr);
        return arr;
    }
    
    public void inordervisit(TreeNode node, List<Integer> arr){
        if(node !=null){
            inordervisit(node.left, arr);
            arr.add(node.val);
            inordervisit(node.right,arr);
        }
    }
}