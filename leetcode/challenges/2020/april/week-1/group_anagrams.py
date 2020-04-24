import collections


class Solution:
    def groupAnagrams(self, strs):
        output = collections.defaultdict(list)
        
        for s in strs:
            output[tuple(sorted(s))].append(s)
        
        return output.values()

        
input_arr = ["eat", "tea", "tan", "ate", "nat", "bat"]

s = Solution()
print(s.groupAnagrams(input_arr))

# print(s.check_anagram("eat", "tea"))

