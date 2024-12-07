from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        ans = []
        minl = [len(wordList) + 1, ]
        if beginWord in wordList:
            wordList.remove(beginWord)
        if endWord not in wordList:
            return []

        def juddge(str1: str, str2: str):
            return sum(1 for c1, c2 in zip(str1, str2) if c1 != c2) == 1

        def dfs(cur: str, target: str, path: List[str], wl: List[str]):
            if len(path) > minl[0]:
                return
            if cur == target:
                minl[0] = min(minl[0], len(path))
                ans.append(path[:])
                return
            for i in range(len(wl)):
                if juddge(cur, wl[i]):
                    word = wl[i]
                    path.append(word)
                    wl.remove(word)
                    dfs(word, target, path, wl)
                    wl.insert(i, word)
                    path.pop()

        dfs(beginWord, endWord, [beginWord, ], wordList)

        i = 0
        while i < len(ans):
            if len(ans[i]) > minl[0]:
                ans.remove(ans[i])
            else:
                i += 1
        return ans


def main():
    # beginWord = "hit"
    # endWord = "cog"
    # wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    # beginWord = "hot"
    # endWord = "dog"
    # wordList = ["hot", "cog", "dog", "tot", "hog", "hop", "pot", "dot"]
    # beginWord = "hog"
    # endWord = "cog"
    # wordList = ["cog"]
    beginWord = "qa"
    endWord = "sq"
    wordList = ["si", "go", "se", "cm", "so", "ph", "mt", "db", "mb", "sb", "kr", "ln", "tm", "le", "av", "sm", "ar",
                "ci", "ca", "br", "ti", "ba", "to", "ra", "fa", "yo", "ow", "sn", "ya", "cr", "po", "fe", "ho", "ma",
                "re", "or", "rn", "au", "ur", "rh", "sr", "tc", "lt", "lo", "as", "fr", "nb", "yb", "if", "pb", "ge",
                "th", "pm", "rb", "sh", "co", "ga", "li", "ha", "hz", "no", "bi", "di", "hi", "qa", "pi", "os", "uh",
                "wm", "an", "me", "mo", "na", "la", "st", "er", "sc", "ne", "mn", "mi", "am", "ex", "pt", "io", "be",
                "fm", "ta", "tb", "ni", "mr", "pa", "he", "lr", "sq", "ye"]

    print(Solution().findLadders(beginWord, endWord, wordList))


if __name__ == '__main__':
    main()
