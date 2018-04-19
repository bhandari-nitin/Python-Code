class stack(object):
    def __init__(self):
        self.stack = []
        self.dic = {
            '}': '{',
            ']': '[',
            ')': '('
        }

    def validator(self, s):
        s = list(s)
        for i in range(0, len(s)):
            self.push(s[i])
        return True if len(self.stack) == 0 else False

    def push(self, char):

        if len(self.stack) == 0:
            self.stack.insert(0, char)
        else:
            if char in self.dic:
                if self.dic[char] == self.peek_stack():
                    self.pop_stack()
        return self.stack

    def pop_stack(self):
        self.stack.pop(0)

    def peek_stack(self):
        return self.stack[0]


if __name__ == '__main__':
    check = stack()
    s = '{{[]}}'
    print check.validator(s)
