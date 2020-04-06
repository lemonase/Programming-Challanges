#!/usr/bin/env python3

class Solution:
    """
    The accepted O(n) solution
    """
    def maxProfit(self, prices: [int]) -> int:
        # gets profit from a linear algo looking back 1 element, or 0 if no profit
        return sum(max(0, prices[i] - prices[i-1]) for i in range(1, len(prices)))



class mySolution:
    """
    My solution became way too involved.
    Started taking all kinds of averages
    turns out the problem was way more
    simple than I was making it.
    """
    def get_avg(self, nums):
        if len(nums) == 0:
            return 0
        return int(sum(nums)/len(nums))
    def maxProfit(self, prices: List[int]) -> int:
        avg = self.get_avg(prices)
        prange = (max(prices) - min(prices))

        profit = 0
        buy_price = 0

        # print("---")
        # print(f"Average: {avg}")
        # print(f"Range: {prange}")
        # print(prices)
        # print()

        for day, cur_price in enumerate(prices):
            day_avg = self.get_avg(prices[day:])
            max_dev = max(prices) - day_avg 
            min_dev = min(prices) + day_avg 

            if cur_price < day_avg and buy_price == 0:
                buy_price = cur_price
                # print(f"buy: at {buy_price} on day: {day + 1} with a profit of {profit}")

            # print(max(prices), prices[day:])
            if max(prices) in prices[day:] and max(prices) != prices[day]:
                continue

            if cur_price > avg and buy_price != 0:
                profit += cur_price - buy_price
                buy_price = 0
                # print(f"sell: at {cur_price} on day: {day + 1} with a profit of {profit}")

        # print("Profit: ", profit)
        return profit
        

s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
print(s.maxProfit([1, 2, 3, 4, 5]))
print(s.maxProfit([7, 6, 4, 3, 1]))
print(s.maxProfit([6, 1, 3, 2, 4, 7]))

