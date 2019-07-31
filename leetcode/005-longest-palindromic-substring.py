# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

def longestPalindrome(s):
    rev = "".join(reversed(s))

    output = ''

    for i in range(len(s)):
        for j in range(i, len(s)):
            rev = "".join(reversed(s[i:j]))
            if s[i:j] == rev:
                if len(rev) > 1:
                    if len(rev) > len(output):
                        output = rev


    print(output)


# longestPalindrome("arkmamra")
# longestPalindrome("skeowworeks")
# longestPalindrome("babad")
# longestPalindrome("cbbd")
# longestPalindrome("skeowworeks")

longestPalindrome("gibbusthebiggusfornibbubbin")
longestPalindrome("makeekamtfaewtollerellot")

