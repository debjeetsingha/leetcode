import java.util.Stack;

class Solution {
    public int calPoints(String[] operations) {
        Stack<Integer> record = new Stack<>();
        for(int i=0; i<operations.length; i++){
            if (operations[i].equals("C")){
                record.pop();
            }
            else if (operations[i].equals("D")){
                record.push(2*record.peek());
            }
            else if (operations[i].equals("+")){
                int top_val = record.pop();
                int new_val = record.peek()+top_val;
                record.push(top_val);
                record.push(new_val);
            } else {
                record.push(Integer.parseInt(operations[i]));
            }
        }

        int result = 0;
        for (int score: record ){
            result += score;
        } 
        return result;
    }
}