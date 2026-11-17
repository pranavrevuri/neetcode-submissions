using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int> res;
        vector<vector<int>> vec(nums.size() + 1);
        unordered_map<int, int> freq;

        for (int num : nums) {
            freq[num]++;
        }

        for (const auto& [key, val] : freq) {
            vec[val].push_back(key);
        }

        for (int i = vec.size() - 1; i >= 0 ; i--) {
            for (auto n : vec[i]) {
                res.push_back(n);
                if (res.size() == k) {
                    return res;
                }
            }
        }

        return res;
    }
};
