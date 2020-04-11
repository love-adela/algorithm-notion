class AdelaQueue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x):
        self.stack_in.append(x)

    def pop(self):
        if not self.stack_out:
            # stack_out is empty
            while self.stack_in:
                item = self.stack_in.pop()
                self.stack_out.append(item)
            # All items of stack_in has moved to stack_out

        return self.stack_out.pop()

    def empty(self):
        return not (self.stack_in or self.stack_out)

    def __len__(self):
        return len(self.stack_in) + len(self.stack_out)

queue = AdelaQueue()
while True:
    print('> ', end='')
    elem = input().split()
    if len(elem) == 0:
        continue

    cmd = elem[0]
    if cmd == 'push':
        if len(elem) != 2:
            print('"push" requires an argument')
            continue
        queue.push(elem[1])
    elif cmd == 'pop':
        print(queue.pop())
    elif cmd  == 'len':
        print(len(queue))
    elif cmd == 'empty':
        print(queue.empty())
    else:
        print('Use one of "push <input>", "pop", "len", "empty"')
