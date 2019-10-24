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
        last_tag = None
        tagged_text = None
        for char in text:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                break
            if current_node.data != None and current_node.tag != None :
                last_tag = current_node.tag
                tagged_text = current_node.data
        return last_tag, tagged_text

    def featureExtractor(self, text):
        output_sent = []
        start_idx = 0
        end_idx = len(text)-1
        while(start_idx < end_idx):
            model_text = text[start_idx:end_idx].replace(' ', '')
            results = self.search(model_text)
            if results[0] != None:
                term = results[1]
                start_idx += len(term)
                for i in range(0, len(term)):
                    output_sent.append(1)
            split_idx = text[start_idx:end_idx].find(' ')
            if split_idx != -1:
                start_idx += split_idx + 1
                for i in range(0, split_idx):
                    output_sent.append(0)
            else:
                for i in range(start_idx, end_idx):
                    start_idx += 1
                    output_sent.append(0)
        return output_sent


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

