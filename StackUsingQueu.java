import java.util.*;
class MyStack{
    Queue<Integer> q1 = new LinkedList<>();
    Queue<Integer> q2 = new LinkedList<>();

    public void push(int x){
            q1.offer(x);
    }

    public int pop(){
        if(!q1.isEmpty()){
            int size=q1.size();
            for(int i=0; i<size-1; i++)
                q2.offer(q1.poll());
            return q1.poll();
        }
        else if(!q2.isEmpty()){
            int size=q2.size();
            for(int i=0; i<size-1; i++)
                q1.offer(q2.poll());
            return q2.poll();
        }
        else return -1;
    }

}

class MyStack2<T>{
    Queue<T> q3 = new LinkedList<>();

    public void push(T data){
        q3.offer(data);
    }

    public T pop(){
        if(!q3.isEmpty()){
            int size=q3.size();
            for(int i=0; i<size-1; i++){
                q3.offer(q3.poll());
            }
            return q3.poll();
        }
        else return null;
    }

}