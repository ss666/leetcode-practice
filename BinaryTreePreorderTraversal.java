class Solution{
    public List<Integer> preorderTraversal(TreeNode root){
        List<Integer> arr = new ArrayList<>();
        preorderVisit(root, arr);
        return arr; 
    }

    public void preorderVisit(TreeNode node, List<Integer> arr){
        if(node != null){
            arr.add(node.val);
            preorderVisit(node.left,arr);
            preorderVisit(node.right,arr);
        }
    }
}