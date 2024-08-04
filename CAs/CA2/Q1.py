import sys
import re


class Queue:
    def __init__(self):
        self.queue = []
        self.len = 0
        self.head = 0
        self.tail = 0
    def enqueue(self, value):
        self.queue.append(value)
        self.len += 1
        self.tail += 1
    def dequeue(self):
        if self.tail != self.head:
            value = self.queue[self.head]
            self.len -= 1
            self.head += 1
            return value

    def size(self):
        return self.len


    def empty(self):
      if self.len == 0:
        print("True")
      else:
        print("False")

    def one_line_str(self):
        for i in range(self.head,self.tail-1):
            print(self.queue[i], end = ' ')
        print(self.queue[self.tail-1])

class Stack:
    def __init__(self, capacity=10):
      self.top = 0
      self.stack = []
      self.len = capacity

    def push(self, value):
        if self.top <= self.len:
           self.stack.append(value)
           self.top += 1
    def pop(self):
        if self.top != 0:
            value = self.stack[self.top-1]
            self.stack.pop()
            self.top -= 1
            return value

    def put(self, value):
        self.stack.pop()
        self.stack.append(value)

    def peek(self):
        if self.top != 0:
            print(self.stack[self.top-1])

    def expand(self):
        self.len *= 2

    def capacity(self):
        return self.len


    def size(self):
        return self.top
    def empty(self):
      if(self.top == 0):
        print("True")
      else:
        print("False")

    def one_line_str(self):
        if(self.top != 0):
            for i in range(len(self.stack) - 1):
                print(self.stack[i], end = ' ')
            print(self.stack[len(self.stack)-1])


class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.linkedList = []

    def insert_front(self, value):
        self.linkedList.insert(0, value)

    def insert_back(self, value):
        self.linkedList.append(value)

    def reverse(self):
        self.linkedList.reverse()

    def one_line_str(self):
        for i in range (len(self.linkedList)-1):
            print(self.linkedList[i], end = ' ')
        print(self.linkedList[len(self.linkedList)-1])

class Runner:
    ds_map = {'stack': Stack, 'queue': Queue, 'linked_list': LinkedList}
    call_regex = re.compile(r'^(\w+)\.(\w+)\(([\w, ]*)\)$')

    def __init__(self, input_src):
        self.input = input_src
        self.items = {}

    def run(self):
        for line in self.input:
            line = line.strip()
            action, _, param = line.partition(' ')
            action_method = getattr(self, action, None)
            if action_method is None:
                return
            action_method(param)

    def make(self, params):
        item_type, item_name = params.split()
        self.items[item_name] = self.ds_map[item_type]()

    def call(self, params):
        regex_res = self.call_regex.match(params)
        item_name, func_name, args_list = regex_res.groups()
        args = args_list.split(',') if args_list != '' else []

        method = getattr(self.items[item_name], func_name)
        result = method(*args)
        if result is not None:
            print(result)


def main():
    runner = Runner(sys.stdin)
    runner.run()


if __name__ == "__main__":
    main()
