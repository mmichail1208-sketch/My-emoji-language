import sys

def interpret(code):
    tokens = code.split()
    
    memory = [0] * 30000
    pointer = 0
    pc = 0
    loops = {}
    stack = []
    
    for i, token in enumerate(tokens):
        if token == '😂':
            stack.append(i)
        elif token == '😭':
            if stack:
                start = stack.pop()
                loops[start] = i
                loops[i] = start
    
    output = ""
    
    while pc < len(tokens):
        command = tokens[pc]
        
        if command == '👍':
            memory[pointer] += 1
        elif command == '👎':
            memory[pointer] -= 1
        elif command == '👉':
            pointer += 1
        elif command == '👈':
            pointer -= 1
        elif command == '🤖':
            output += chr(memory[pointer])
        elif command == '🔢':
            output += str(memory[pointer])
        elif command == '⏬':
            memory[pointer] = int(input())
        elif command == '😂':
            if memory[pointer] == 0:
                if pc in loops:
                    pc = loops[pc]
        elif command == '😭':
            if memory[pointer] != 0:
                if pc in loops:
                    pc = loops[pc]
        
        pc += 1
    
    return output
