import java.util.*;
class MyQueue{
    Stack<Integer> stack1 = new Stack<Integer>();
    Stack<Integer> stack2 = new Stack<Integer>();
    
    public void add(int x){
        stack1.push(x);
    }
    public void change(){
        while(!stack1.empty()){
            int x = stack1.pop();
            stack2.push(x);
        }
    }
    public int remove(){
        if(stack2.empty())
            change();
        return stack2.pop();
    }
    public int peek(){
        if(stack2.empty())
            change();
        return stack2.peek();
    }

}

