from collections import defaultdict
from typing import List


class Solution:
    # O(M*N) Time | O(M) Space
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for letter in word:
                count[ord(letter) - ord("a")] += 1

            tuple_count = tuple(count)
            res[tuple_count].append(word)

        return list(res.values())


if __name__ == '__main__':
    sol = Solution()


    strs = ["eat","tea","tan","ate","nat","bat"]
    print(sol.groupAnagrams(strs))

