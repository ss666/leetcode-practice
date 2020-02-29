class Solution{
    public List<Integer> addToArrayForm(int[] A, int K){
        LinkedList<Integer> res = new LinkedList<Integer>();
        int carry = 0;

        for (int i = A.length -1 ; i >= 0 ; i--){
            int m = A[i] + K % 10 + carry;
            carry = m / 10;
            K /= 10 ;
            res.addFirst(m % 10);
        }

        while(K >= 1) {
            int m = K % 10 + carry;
            carry = m / 10;
            K /= 10 ;
            res.addFirst(m % 10);
        }

        if (carry == 1) res.addFirst(1);

        return res;
    }

}