class Solution {
    public long getDescentPeriods(int[] prices) {
        long count = 1;      // first day
        long curr = 1;       // current descent length

        for (int i = 1; i < prices.length; i++) {
            if (prices[i] == prices[i - 1] - 1) {
                curr++;
            } else {
                curr = 1;
            }
            count += curr;
        }

        return count;
    }
}