import time
file = open(input("code file:"),"r")
code = file.read()
stack = []
on = 0

while on < len(code):
    if code[on] == "1":
        push = ""
        on +=1
        while code[on] != ":":
            push += code[on]
            on += 1
        stack.append(int(push))

    if code[on] == "2":
        stack.append(stack[len(stack)-1])

    if code[on] == "3":
        flip = []
        onFlip = len(stack)-1
        while onFlip != -1:
            flip.append(stack[onFlip])
            onFlip -= 1
        stack = flip

    if code[on] == "4":
        stack.append(int(input()))

    if code[on] == "5":
        stack[len(stack)-2] = stack[len(stack)-1] + stack[len(stack)-2]
        stack.pop(len(stack)-1)

    if code[on] == "6":
        print(stack[len(stack)-1])
        stack.pop(len(stack)-1)

    if code[on] == "[":
        loopStart = on

    if code[on] == "]":
        if stack[len(stack)-1] != 0:
            on = loopStart
        
    on += 1
time.sleep(100)
