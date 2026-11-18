class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> suffix(n, 1);
        vector<int> prefix(n, 1);
        vector<int> product(n, 1);

        int running = 1;
        for (int i = 0 ; i < n ; i++) {
            prefix[i] = running;
            running *= nums[i];
        }

        running = 1;
        for (int i = n - 1 ; i >= 0 ; i--) {
            suffix[i] = running;
            running *= nums[i];
        }

        for (int i = 0 ; i < n ; i++) {
            product[i] = suffix[i] * prefix[i];
        }

        return product;
    }
};
