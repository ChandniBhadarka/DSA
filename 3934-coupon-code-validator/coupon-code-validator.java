import java.util.*;

class Solution {
    public List<String> validateCoupons(String[] code,
                                    String[] businessLine,
                                    boolean[] isActive)
 {

        // Fixed business line order
        String[] order = {"electronics", "grocery", "pharmacy", "restaurant"};

        // Map to store valid coupons by business line
        Map<String, List<String>> map = new HashMap<>();
        for (String key : order) {
            map.put(key, new ArrayList<>());
        }

        for (int i = 0; i < code.length; i++) {

            // 1. code validation
            if (code[i] == null || code[i].isEmpty() ||
                !code[i].matches("[a-zA-Z0-9_]+")) {
                continue;
            }

            // 2. business line validation
            if (!map.containsKey(businessLine[i])) {
                continue;
            }

            // 3. active check
            if (!isActive[i]) {
                continue;
            }

            // store valid coupon
            map.get(businessLine[i]).add(code[i]);
        }

        // build result in required order
        List<String> result = new ArrayList<>();
        for (String key : order) {
            List<String> list = map.get(key);
            Collections.sort(list);   // sort codes lexicographically
            result.addAll(list);
        }

        return result;
    }
}
