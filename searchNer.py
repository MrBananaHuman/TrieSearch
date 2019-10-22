data = open('ne_dic.txt', 'r', encoding='utf-8')
lines = data.readlines()

class Node(object):
    def __init__(self, text, tag=None, data=None):
        self.text = text
        self.tag = tag
        self.data = data
        self.children = {}

class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, text, tag):
        current_node = self.head
        for char in text:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char] 
            current_node.tag = tag
        current_node.data = text

    def search(self, text):
        current_node = self.head
        for char in text:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return False
            if current_node.data != None:
                return current_node.tag
            
t = Trie()

tags = ['PS', 'OG', 'LC', 'PL', 'EV', 'PR', 'QT', 'DT', 'OC', 'TI']
for line in lines:
    line = line.replace('\n', '')
    text = line.split(' ')[0]
    tag = line.split(' ')[1]
    if tag in tags:
        t.insert(text, tag)

while(True):
    print('input')
    a = input()
    print('\n', t.search(a))

