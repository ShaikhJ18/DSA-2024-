class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self,item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            raise IndexError('pop from empty stack')
        return self.stack.pop()
    
    def peek(self):
        if len(self.stack) == 0:
            raise IndexError('peek from empty stack')
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def __str__(self):
        return str(self.stack)

if __name__ == '__main__':
    games = Stack()
    games.push("Skyrim")
    games.push("Witcher 3")
    games.push("Cyberpunk 2077")
    games.push("GTA V")
    games.push("Red Dead Redemption 2")
    games.push("Assassin's Creed Valhalla")
    games.push("Assassin's Creed Odyssey")

    length = games.size()

    for i in range(length):
        print(games.pop())
        print(str(games))

    string = input("Enter a string: ")

    stringStack = Stack()

    for char in string.lower().replace(" ",""):
        stringStack.push(char)
    
    reversedString = ""

    while not stringStack.isEmpty():
        reversedString += stringStack.pop()

    if string.lower().replace(" ","") == reversedString:
        print("The string is a palindrome")
    else:
        print("The string is not a palindrome")
    