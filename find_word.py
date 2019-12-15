import sys
from itertools import permutations

class TrieNode:
  def __init__(self):
    self.finalWord = None
    self.children = [None] * 26

class Trie:

  parent = TrieNode() 

  def __init__(self):
    self.parent = TrieNode()

  def addWord(self, word):
    current = self.parent
    for c in word:
      i = ord(c)-ord('a')
      if current.children[i] is None:
        current.children[i] = TrieNode()
      current = current.children[i]

    current.finalWord = word

  def hasWord(self, word):
    current = self.parent
    for c in word:
      i = ord(c)-ord('a')
      if current.children[i] is None:
        return False
      current = current.children[i]
    return current.finalWord != None

  def printWords(self):
    self.p(self.parent)

  def p(self, root):
    if root is None:
      return
    if root.finalWord: 
      print(root.finalWord)
    for child in root.children:
      self.p(child)


if __name__ == '__main__':
  print('\n')
  print('\n')
  print('\n')
  print('running...')
  results = {}
  trie = Trie()

  # Load Words
  print('loading words...')
  print('\n')
  f = open("words_alpha.txt", "r")
  for x in f:
    trie.addWord(str(x).strip())

  print('comparing permutations of your inputs...')
  print('\n')

  # Do lookups

  print('\n')
  print('\n')
  print('\n')
  for word in sys.argv[1:]:
    for p in list(permutations(word)):
      perm = ''.join(p)

      if trie.hasWord(perm):
        if word not in results:
          results[word] = []
        results[word].append(perm)
  f.close()

  for key in results:
    print(key + ': ')
    print('   ' + str(results[key]))

  print('\n')
  print('\n')
  print('\n')
