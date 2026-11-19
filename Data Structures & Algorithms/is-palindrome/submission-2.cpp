using namespace std;

class Solution {
public:
    bool isPalindrome(string s) {
        transform(s.begin(), s.end(), s.begin(), [](unsigned char c) { return tolower(c) ; });
        erase_if(s, [](unsigned char c) { return !isalnum(c); });

        int left = 0;
        int right = s.length() - 1;

        while (left <= right) {
            if (s[left] != s[right]) {
                return false;
            }
            left++;
            right--;
        }

        return true;



    }
};
