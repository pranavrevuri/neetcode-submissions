using namespace std;

class Solution {
public:

    string encode(vector<string>& strs) {
        string encoded_string;

        for (const auto& word : strs) {
            string word_len = to_string(word.length());
            encoded_string += word_len + '#' + word;
        }

        return encoded_string;
    }

    vector<string> decode(string s) {
        string num;
        vector<string> vec;
        for (int i = 0 ; i < s.length() ; i++) {
            while (s[i] != '#') {
                num += s[i];
                i++;
            }
            int len = stoi(num);

            string word;
            for (int j = i + 1 ; j < len + i + 1 ; j++) {
                word += s[j];
            }

            i += len;
            vec.push_back(word);
            num = "";
        }
        return vec;
    }
};
