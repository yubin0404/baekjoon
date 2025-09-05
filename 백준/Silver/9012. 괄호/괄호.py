class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        if self.top == None:
            self.top = Node(data)
        else:
            curr = Node(data)
            curr.next = self.top
            self.top = curr

    def pop(self):
        # 가장 윗 노드 제거, 해당 data 반환
        if self.top == None:
            return None
        else:
            curr = self.top
            self.top = self.top.next
            return curr.data
    def peek(self):
        # 가장 윗 노드의 data 반환
        if self.top == None:
            return None
        else:
            curr = self.top
            return curr.data

    def is_empty(self):
        return self.top == None

    def __str__(self):
        result = ""

        curr = self.top

        while True:
            result += str(curr.data)
            if curr.next == None:
                break
            curr = curr.next
            result += " -> "
            
        return result

def is_valid(valid):
    is_vps = True
    
    braket = Stack()
    for ps in valid:
        if ps == "(":
            braket.push(ps)
        else:
            if braket.pop() == "(":
                continue
            else:
                is_vps = False
                break
    if not braket.is_empty():
        is_vps = False
    print("YES" if is_vps else "NO")

T = int(input())
for _ in range(T):
    valid = input()
    is_valid(valid)