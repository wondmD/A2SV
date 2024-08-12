from sys import stdin
from collections import defaultdict, deque, Counter
from bisect import bisect_left, bisect_right

class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        cur = self.root
        for w in word:
            if not w in cur:
                cur[w] = {}
            cur = cur[w]
        cur['*'] = ''

    def search(self, word: str) -> bool:
        cur = self.root
        for w in word:
            if not w in cur:
                return False
            cur = cur[w]
        return True if '*' in cur else False

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for w in prefix:
            if not w in cur:
                return False
            cur = cur[w]
        return True
    def delete(self, word: str) -> None:
        # your code goes here
        cur  = self.root
        leng = len(word)
        def dl(tr,word,ind):
            nonlocal leng
            
            if not tr:
                return None
            if ind == leng:
                tr.is_end = False
                if not self.has_children(tr):
                    return None
                
            if not self.has_children(tr) and not tr.is_end:
                return None
            tr.children[ord(word[ind])-ord("a")] = dl(tr.children[ord(word[ind])-ord("a")],word,ind+1)
            return tr
        dl(cur,word,0)

def sol():
    num = int(stdin.readline())
    lis = list(map(int, stdin.readline().split()))
    
  
  
    lis.sort()
    
    my_trie = Trie()
    
    ans = []
    for num in lis:
        ch = False
        x = int('1'*num, 2)
        
        for i in range(1, x+1):
          
            bnr = bin(i)[2:]
            
            bnr = '0'*(num-len(bnr)) + bnr
   
            if not my_trie.startsWith(bnr):
                ch = True
                my_trie.insert(bnr)
                ans.append(bnr)
                break
        if not ch:
            print("NO")
            return
    print('YES')
    for i in ans:
        print(i)   

sol()
