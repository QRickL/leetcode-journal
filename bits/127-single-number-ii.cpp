// Initial solution: O(1) space and O(n) time

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        
        vector<int> bit_count(32,0);
        for (int i : nums)
        {
            for (int p = 0; p < 32; p++)
            {
                unsigned int t = (1 << p);
                if (i & t) bit_count[p]++;
            }
        }

        unsigned int ans = 0;
        for (int p = 0; p < 32; p++)
        {
            if ((bit_count[p] % 3) == 1)
            {
                ans = (ans | (1 << p));
            }
        }
        return static_cast<int>(ans);
    }
};

// Refined solution: O(1) space (but no need for allocation of vector) and O(n) time

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        
        int ans = 0;
        for (int p = 0; p < 32; p++) {
            int bit_count = 0;
            for (int i : nums) {
                unsigned int t = 1 << p;
                if (i & t) bit_count++;
            }
            if (bit_count % 3) ans = (ans | (1 << p));
        }
        return ans;
    }
};