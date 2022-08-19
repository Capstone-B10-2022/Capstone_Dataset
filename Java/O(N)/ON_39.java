
// Java program for 
// the above approach
import java.util.*;

class ON_39 {

    // Function to maximize the matching
    // pairs between two permutation
    // using left and right rotation
    static int maximumMatchingPairs(int perm1[],
            int perm2[],
            int n) {
        // Left array store distance of element
        // from left side and right array store
        // distance of element from right side
        int[] left = new int[n];
        int[] right = new int[n];

        // Map to store index of elements
        HashMap<Integer, Integer> mp1 = new HashMap<>();
        HashMap<Integer, Integer> mp2 = new HashMap<>();

        for (int i = 0; i < n; i++) {
            mp1.put(perm1[i], i);
        }
        for (int j = 0; j < n; j++) {
            mp2.put(perm2[j], j);
        }

        for (int i = 0; i < n; i++) {
            // idx1 is index of element
            // in first permutation
            // idx2 is index of element
            // in second permutation
            int idx2 = mp2.get(perm1[i]);
            int idx1 = i;

            if (idx1 == idx2) {
                // If element if present on same
                // index on both permutations then
                // distance is zero
                left[i] = 0;
                right[i] = 0;
            } else if (idx1 < idx2) {
                // Calculate distance from left
                // and right side
                left[i] = (n - (idx2 - idx1));
                right[i] = (idx2 - idx1);
            } else {
                // Calculate distance from left
                // and right side
                left[i] = (idx1 - idx2);
                right[i] = (n - (idx1 - idx2));
            }
        }

        // Maps to store frequencies of elements
        // present in left and right arrays
        HashMap<Integer, Integer> freq1 = new HashMap<>();
        HashMap<Integer, Integer> freq2 = new HashMap<>();

        for (int i = 0; i < n; i++) {
            if (freq1.containsKey(left[i]))
                freq1.put(left[i],
                        freq1.get(left[i]) + 1);
            else
                freq1.put(left[i], 1);
            if (freq2.containsKey(right[i]))
                freq2.put(right[i],
                        freq2.get(right[i]) + 1);
            else
                freq2.put(right[i], 1);
        }

        int ans = 0;

        for (int i = 0; i < n; i++) {
            // Find maximum frequency
            ans = Math.max(ans,
                    Math.max(freq1.get(left[i]),
                            freq2.get(right[i])));
        }

        // Return the result
        return ans;
    }

    // Driver Code
    public static void main(String[] args) {
        // Given permutations P1 and P2
        int P1[] = { 5, 4, 3, 2, 1 };
        int P2[] = { 1, 2, 3, 4, 5 };
        int n = P1.length;

        // Function Call
        System.out.print(maximumMatchingPairs(P1, P2, n));
    }
}