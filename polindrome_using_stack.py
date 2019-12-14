class Stack:
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return self.items == []
 
    def push(self, data):
        self.items.append(data)
 
    def pop(self):
        return self.items.pop()
s = Stack()
text = input() 
for character in text:
    s.push(character)
reversed_text = ''
while not s.is_empty():
    reversed_text = reversed_text + s.pop()
if text == reversed_text:
    print("yes")
else:
    print("no")
