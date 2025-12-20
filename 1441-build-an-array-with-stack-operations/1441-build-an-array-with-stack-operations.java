class Solution {
    public List<String> buildArray(int[] target, int n) {

        List<String> result = new ArrayList<>();
        int index = 0; // pointer for target array

        for (int i = 1; i <= n; i++) {

            // always push the number from stream
            result.add("Push");

            // if current number matches target, move to next target
            if (index < target.length && i == target[index]) {
                index++;
            } 
            // otherwise pop it
            else {
                result.add("Pop");
            }

            // stop once target is built
            if (index == target.length) {
                break;
            }
        }

        return result;
    }
}
