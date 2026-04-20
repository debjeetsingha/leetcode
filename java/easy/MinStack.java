import java.util.Stack;

// Used a stack to implement a stack but operations are all O(1) including getMin()
// Could have used a linked list to implement it from scratch

class MinStack {
    private Stack<Integer> stack;
    private Stack<Integer> minimum;

    public MinStack() {
        stack = new Stack<>();
        minimum = new Stack<>();
    }
    
    public void push(int val) {
        stack.push(val);

        if (minimum.isEmpty() || minimum.peek()>=val) {
            minimum.push(val);
        }
    }
    
    public void pop() {
        // int popped = stack.pop();
        // if (popped==minimum.peek()){ 
        //     minimum.pop();  
        // }

        // stack.pop() returns an Integer. minimum.peek() returns an Integer.
        // We can use .equals() to compare their values safely instead of converting to int
        if (stack.pop().equals(minimum.peek())) {
            minimum.pop();
        }
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return minimum.peek();
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */