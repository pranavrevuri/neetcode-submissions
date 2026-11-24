using namespace std;

class Solution {
public:
    int maxArea(vector<int>& heights) {
        int left = 0;
        int right = heights.size() - 1;

        int vol = 0;
        int best = 0;
        while (left < right) {
            vol = (right-left)*min(heights[left], heights[right]);
            best = max(best, vol);

            if (heights[right] > heights[left]) {
                left++;
            }
            else if (heights[right] <= heights[left]) {
                right--;
            }
        }

        return best;
    }
};
