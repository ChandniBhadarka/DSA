class Solution {
    public int[] finalPrices(int[] prices) {

        int n = prices.length;
        int[] answer = prices.clone(); // copy prices
        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < n; i++) {

            // apply discount to previous items -->While the current price can give a discount to earlier items, keep popping and applying the discount.
            while (!stack.isEmpty() && prices[i] <= prices[stack.peek()]) {
                int index = stack.pop();
                answer[index] = prices[index] - prices[i];
            }

            // current item waits for discount
            stack.push(i);
        }

        return answer;
    }
}
