using namespace std;
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<vector<int>, vector<string>> my_map;
        vector<vector<string>> res;

        for (const auto& word : strs) {
            vector<int> freq_arr(26, 0);

            for (char ch : word) {
                int ascii_val = static_cast<int>(static_cast<unsigned char>(ch));
                int base_val = static_cast<int>(static_cast<unsigned char>('a'));
                freq_arr[ascii_val - base_val] += 1;            
            }

            my_map[freq_arr].push_back(word);
        }

        for (auto& [key, group] : my_map) {
            res.push_back(group);
        }

        return res;
    }

};
