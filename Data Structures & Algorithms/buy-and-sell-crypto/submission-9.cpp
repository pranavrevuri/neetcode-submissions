using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int left = 0;
        
        int best = 0;
        int profit;

        for (int right = 1 ; right < prices.size() ; right++) {
            profit = prices[right] - prices[left];
            best = max(profit, best);
            if (prices[right] < prices[left]) {
                left = right;
            }
        }

        return best;
    }
};
