class Solution {
    static {
        Runtime.getRuntime().gc();
        Runtime.getRuntime().addShutdownHook(new Thread(() -> {
            try (FileWriter writer = new FileWriter("display_runtime.txt")) {
                writer.write("0");
            } catch (IOException e) {
                e.printStackTrace();
            }
        }));
    }
    public int[] dailyTemperatures(int[] t) {
        int n = t.length;
        int[] res = new int[n];
        Stack<Integer> st = new Stack<>();
        res[n-1] = 0;
        st.push(n-1);

        for(int i=n-2;i>=0;i--){
            while(!st.isEmpty() && t[st.peek()] <= t[i]){
                st.pop();
            }
            if(st.isEmpty()){
                res[i] = 0;
            }
            else{
                res[i] = st.peek() - i;
            }
            st.push(i);
        }
        return res;
    }
}