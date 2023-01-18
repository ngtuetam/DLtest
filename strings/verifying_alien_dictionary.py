#leetcode: Verifying an Alien Dictionary
# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
class Solution:
    def isAlienSorted(self, words, order: str) -> bool:
        count = {}
        for i in range(len(order)):
            count[order[i]] = i
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            for j in range(len(w1)):
                # if len(w2) < len(w1)
                if j == len(w2):
                    return False
                if w1[j] != w2[j]:
                    if count[w1[j]] > count[w2[j]]:
                        return False
                    break
        return True
                