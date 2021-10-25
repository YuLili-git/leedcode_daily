#请你设计一个数据结构，支持 添加新单词 和 查找字符串是否与任何先前添加的字符串匹配 。
#实现词典类 WordDictionary ：
#WordDictionary() 初始化词典对象
#void addWord(word) 将 word 添加到数据结构中，之后可以对它进行匹配
#bool search(word) 如果数据结构中存在字符串与 word 匹配，则返回 true ；否则，返回  false 。word 中可能包含一些 '.' ，每个 . 都可以表示任何一个字母。
#示例：
#输入：
#["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
#[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
#输出：
#[null,null,null,null,false,true,true,true]
#解释：
#WordDictionary wordDictionary = new WordDictionary();
#wordDictionary.addWord("bad");
#wordDictionary.addWord("dad");
#wordDictionary.addWord("mad");
#wordDictionary.search("pad"); // return False
#wordDictionary.search("bad"); // return True
#wordDictionary.search(".ad"); // return True
#wordDictionary.search("b.."); // return True
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            ch = ord(ch) - ord('a')
            if not node.children[ch]:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isEnd = True


class WordDictionary:
    def __init__(self):
        self.trieRoot = TrieNode()

    def addWord(self, word: str) -> None:
        self.trieRoot.insert(word)

    def search(self, word: str) -> bool:
        def dfs(index: int, node: TrieNode) -> bool:
            if index == len(word):
                return node.isEnd
            ch = word[index]
            if ch != '.':
                child = node.children[ord(ch) - ord('a')]
                if child is not None and dfs(index + 1, child):
                    return True
            else:
                for child in node.children:
                    if child is not None and dfs(index + 1, child):
                        return True
            return False

        return dfs(0, self.trieRoot)




# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
