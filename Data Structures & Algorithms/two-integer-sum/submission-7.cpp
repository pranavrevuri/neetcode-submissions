class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> val_ind;
        int diff;

        for (int i = 0 ; i < nums.size() ; i++) {
            diff = target - nums[i];
            if (val_ind.count(diff) != 0) {
                return {val_ind[diff], i};
            }
            val_ind[nums[i]] = i;
        }
    }
};
