
class Solution:
    def countElements(self, arr):
        counted = dict()
        output = 0

        for i in range(len(arr)):
            if arr[i] not in counted:
                counted[arr[i]] = 1
            else:
                counted[arr[i]] += 1

        sorted(counted)

        for num, count in counted.items():
            if num + 1 in counted.keys():
                output += 1 * count

        return output


s = Solution()
print(s.countElements([1, 2, 3]))
print(s.countElements([1,1,3,3,5,5,7,7]))
print(s.countElements([1,3,2,3,5,0]))
print(s.countElements([1,1,2,2]))
