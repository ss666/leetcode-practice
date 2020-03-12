class Solution{
    public int sumOfLeftLeaves(TreeNode root){
        return recrusive_comp(root,false);
    }

    public int recrusive_comp(TreeNode node, Boolean isLeft){
        int sum = 0;
        if(node == null) return 0;
        else if(node.left != null ||node.right != null){
            sum = sum + recrusive_comp(node.left, true);
            sum = sum + recrusive_comp(node.right, false);
        }
        else if (isLeft == true)  
            sum = sum + node.val;  
        
        return sum;
    }
}
