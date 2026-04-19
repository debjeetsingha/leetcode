import java.util.HashMap;
import java.util.Stack;
import java.util.Map;

class Solution {
    public boolean isValid(String s) {
        Map<Character, Character> pairs = new HashMap<>();
        pairs.put(')','(');
        pairs.put('}','{');
        pairs.put(']','[');

        Stack<Character> stack = new Stack<>();

        for (int i = 0; i<s.length(); i++) {
            char c = s.charAt(i);

            if (pairs.containsKey(c)) {
                char topElement = stack.isEmpty() ? '#' : stack.pop();
                if (topElement != pairs.get(c)){
                    return false;
                }
            } else {
                stack.push(c);
            }
        }

        return stack.isEmpty();
    }
}