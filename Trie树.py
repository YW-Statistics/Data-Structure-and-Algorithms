# Title: Trie Tree
# Time: 2020/10/22
# Author: Vincent

class Trie:

    def __init__(self):
        self.lookup = {}
    
    # 插入单词
    def insert(self, word):
        tree = self.lookup # 游标
        for c in word:
            # 如果结点中不存在字符c，那么新开辟一个字符存储空间
            if c not in tree:
                tree[c] = {'count':1}
            else:
                tree[c]['count'] += 1
            # 游标下移
            tree = tree[c]
        tree['#'] = '#' # 结束标识
        print(tree)
    
    # 检查单词
    def search(self, word):
        tree = self.lookup
        for c in word:
            if tree.get(c) is None or tree[c]['count'] == 0:
                return False
            tree = tree[c]
        # 如果前面所有字符都匹配成功，那么就剩下两种结果：
        # 1.word为前缀树字符串中的一个子串；2.word恰好与前缀树的一个字符串重合
        return False if '#' not in tree else True
    
    # 检查前缀
    def startsWith(self, prefix):
        tree = self.lookup
        for c in prefix:
            if tree.get(c) is None or tree[c]['count'] == 0:
                return False
            tree = tree[c]
        # 如果前面所有字符都匹配成功，那么就剩下一种结果：word恰好与前缀树的一个字符串重合
        return True
    
    # 删除单词
    def delete(self, word):
        if not self.search(word):
            raise ValueError('Trie树中不存在该单词！')
        tree = self.lookup
        for c in word:
            tree[c]['count'] -= 1
            tree = tree[c]
        del tree['#']
        

if __name__ == '__main__':
    sample = Trie()
    sample.insert('IloveYiYi')
    sample.insert('IloveAKai')
    print(sample.lookup)
    
    print(sample.search('Ilove'))
    print(sample.search('IloveYiYi'))
    
    print(sample.startsWith('Ilove'))
    
    sample.delete('IloveYiYi')
    
    print(sample.lookup)
    
    print(sample.search('Ilove'))
    print(sample.search('IloveYiYi'))
    
    print(sample.startsWith('Ilove'))
