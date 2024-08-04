import sys
import re


INVALID_INDEX = 'invalid index'
OUT_OF_RANGE_INDEX = 'out of range index'
EMPTY = 'empty'


class MinHeap:
    class Node:
        pass

    def __init__(self):
        self.tree = []
    def bubble_up(self, index):
        if not isinstance(index, int):
            raise Exception(INVALID_INDEX)
        elif index > len(self.tree) or index < 0:
            raise Exception(OUT_OF_RANGE_INDEX)
        elif len(self.tree) == 0:
            raise Exception(EMPTY)
        parent_index = int((index - 1) / 2)
        parent = self.tree[int((index - 1) / 2)]
        if self.tree[index] < parent:
            self.tree[int((index - 1) / 2)] = self.tree[index]
            self.tree[index] = parent
            self.bubble_up(int((index - 1) / 2))
    def bubble_down(self, index):
        if not isinstance(index, int):
            raise Exception(INVALID_INDEX)
        elif index > len(self.tree) or index < 0:
            raise Exception(OUT_OF_RANGE_INDEX)
        elif len(self.tree) == 0:
            raise Exception(EMPTY)

        if index * 2 + 2 < len(self.tree):
            left = self.tree[index * 2 + 1]
            right = self.tree[index * 2 + 2]
            if right < left:
                if right < self.tree[index]:
                    temp = self.tree[index]
                    self.tree[index] = self.tree[index * 2 + 2]
                    self.tree[index * 2 + 2] = temp
                    self.bubble_down(index * 2 + 2)
            else:
                if left < self.tree[index]:
                    temp = self.tree[index]
                    self.tree[index] = self.tree[index * 2 + 1]
                    self.tree[index * 2 + 1] = temp
                    self.bubble_down(index * 2 + 1)
        elif index * 2 + 1 < len(self.tree):
            left = self.tree[index * 2 + 1]
            if left < self.tree[index]:
                temp = self.tree[index]
                self.tree[index] = self.tree[index * 2 + 1]
                self.tree[index * 2 + 1] = temp
                self.bubble_down(index * 2 + 1)

    def heap_push(self, value):
        self.tree.append(value)
        self.bubble_up(len(self.tree) - 1)
    def heap_pop(self):
        if len(self.tree) == 0:
            raise Exception(EMPTY)
        root = self.tree[0]
        if len(self.tree) > 1:
            self.tree[0] = self.tree.pop()
            self.bubble_down(0)
        else:
            self.tree.pop()
        return root
    
    def find_min_child(self, index):
        if not isinstance(index, int):
            raise Exception(INVALID_INDEX)
        elif index > len(self.tree) or index < 0:
            raise Exception(OUT_OF_RANGE_INDEX)
        elif len(self.tree) == 0:
            raise Exception(EMPTY)
        left_i = 2 * index + 1
        right_i = 2 * index + 2
        length = len(self.tree)
        if right_i < length:
            if self.tree[right_i] < self.tree[left_i]:
                return right_i
            else:
                return left_i
        elif left_i < length:
            return left_i

    def heapify(self, *args):
        for argument in args:
            self.heap_push(argument)



class HuffmanTree:
    class Node:
        def __init__(self, symb, freq, left=None, right=None):
            self.frq = freq
            self.symb = symb
            self.left = left
            self.right = right
            self.dir = ""

        def __str__(self) -> str:
            out = "Symbol: " + str(self.symb) + "\tFreq: " + str(self.frq)
            return out

    def __init__(self):
        self.root = None
        self.letter = []
        self.freq = []
        self.let_freq = {}
        self.nodes = []
        # self.let_freq_dict = {}
        self.encoded = {}

    def set_letters(self, *args):
        for i in args:
            self.letter.append(i)

    def set_repetitions(self, *args):
        for i in args:
            self.freq.append(i)
        self.let_freq = dict(zip(self.letter, self.freq))

    def build_huffman_tree(self):
        if len(self.let_freq) == 0:
            raise Exception(EMPTY)
        for letter in self.let_freq:
            self.nodes.append(self.Node(letter, self.let_freq[letter]))

        while not len(self.nodes) == 1:
            self.nodes.sort(key=lambda x: x.frq)
            right_n = self.nodes[0]
            right_n.dir = "0"
            left_n = self.nodes[1]
            left_n.dir = "1"
            self.nodes.append(
                self.Node(
                    left_n.symb + right_n.symb,
                    left_n.frq + right_n.frq,
                    left_n,
                    right_n,
                )
            )
            self.nodes = self.nodes[2:]
        self.root = self.nodes[0]
        self.generate_encode_dict(self.root)

    def generate_encode_dict(self, node, code=""):
        adr = code + node.dir
        if node.right == None and node.left == None:
            self.encoded[node.symb] = adr
            return
        self.generate_encode_dict(node.right, adr)
        self.generate_encode_dict(node.left, adr)

    def get_huffman_code_cost(self):
        cost = int(0)
        for letter in self.let_freq:
            cost += len(self.encoded[letter]) * int(self.let_freq[letter])
        return cost

    def text_encoding(self, text):
        for char in text:
            if char in self.let_freq:
                self.let_freq[char] += 1
            else:
                self.let_freq[char] = 1
        self.build_huffman_tree()


class Bst:
    class Node:
        def __init__(self, key):
            self.l_child = None
            self.r_child = None
            self.key = key

    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root == None:
            self.root = self.Node(key)
            return
        else:
            self.inner_insert(self.root, key)

    def inner_insert(self, node, key):
        if key <= node.key:
            if node.l_child is None:
                node.l_child = self.Node(key)
            else:
                self.inner_insert(node.l_child, key)
        else:
            if node.r_child is None:
                node.r_child = self.Node(key)
            else:
                self.inner_insert(node.r_child, key)

    def inorder(self):
        return self.recursive_inorder(self.root)[1:]

    def recursive_inorder(self, node):
        if node == None:
            return ""
        else:
            out = ""
            out += str(self.recursive_inorder(node.l_child)) + " "
            out += str(node.key)
            out += str(self.recursive_inorder(node.r_child))
        return out

class Runner:
    dsMap = {'min_heap': MinHeap, 'bst': Bst, 'huffman_tree': HuffmanTree}
    callRegex = re.compile(r'^(\w+)\.(\w+)\(([\w, \-"\']*)\)$')

    def __init__(self, inputSrc):
        self.input = inputSrc
        self.items = {}

    def run(self):
        for line in self.input:
            line = line.strip()
            action, _, param = line.partition(' ')
            actionMethod = getattr(self, action, None)
            if actionMethod is None:
                return
            actionMethod(param)

    def make(self, params):
        itemType, itemName = params.split()
        self.items[itemName] = self.dsMap[itemType]()

    def call(self, params):
        regexRes = self.callRegex.match(params)
        itemName, funcName, argsList = regexRes.groups()

        args = [x.strip() for x in argsList.split(',')] if argsList != '' else []
        args = [x[1:-1] if x[0] in ('"', "'") else int(x) for x in args]

        method = getattr(self.items[itemName], funcName)
        try:
            result = method(*args)
        except Exception as ex:
            print(ex)
        else:
            if result is not None:
                print(result)


def main():
    runner = Runner(sys.stdin)
    runner.run()


if __name__ == "__main__":
    main()
