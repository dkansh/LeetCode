class Solution {
    public int minimumPushes(String word) {
        int[] frequency = new int[26];
        for (int i = 0; i < word.length(); i++) {
            frequency[word.charAt(i) - 'a']++;
        }
        Arrays.sort(frequency);
        int i = 25;
        int count = 0;
        int multiplier = 1;
        int result = 0;
        while (i >= 0 && frequency[i] != 0) {
            result += (multiplier * frequency[i]);
            count++;
            if (count == 8) {
                multiplier++;
                count = 0;
            }
            i--;
        }
        return result;
    }
}