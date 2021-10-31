#给你一个字符串数组 words ，只返回可以使用在 美式键盘 同一行的字母打印出来的单词。键盘如下图所示。
#美式键盘 中：
#第一行由字符 "qwertyuiop" 组成。
#第二行由字符 "asdfghjkl" 组成。
#第三行由字符 "zxcvbnm" 组成。
#示例 1：
#输入：words = ["Hello","Alaska","Dad","Peace"]
#输出：["Alaska","Dad"]
#示例 2：
#输入：words = ["omk"]
#输出：[]
#示例 3：
#输入：words = ["adsdf","sfd"]
#输出：["adsdf","sfd"]
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = list('qwertyuiopQWERTYUIOP')
        second = list('asdfghjklASDFGHJKL')
        third = list('zxcvbnmZXCVBNM')
        res = []
        for i in range(len(words)):
            f = 0
            s = 0
            t = 0
            if len(words[i]) <= 1:
                res.append(words[i])
            else:
                for j in range(len(words[i])):

                    if words[i][j] in first and words[i][j] not in second and words[i][j] not in third:
                        f += 1
                        if f == len(words[i]):
                            res.append(words[i])
                    elif words[i][j] in second and words[i][j] not in first and words[i][j] not in third:
                        s += 1
                        if s == len(words[i]):
                            res.append(words[i])
                    elif words[i][j] in third and words[i][j] not in second and words[i][j] not in first:
                        t += 1
                        if t == len(words[i]):
                            res.append(words[i])
        return res 


