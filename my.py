import sys

def interpret(code):
    tokens = code.replace('.', '').replace('!', '').split()
    
    memory = [0] * 30000
    pointer = 0
    pc = 0
    loops = {}
    stack = []
    for i, token in enumerate(tokens):
        if token == '😂':#wbrk
            stack.append(i)
        elif token == '😭':#цикл
            start = stack.pop()
            loops[start] = i
            loops[i] = start
    random_simbol=['(❁◡❁)']
    output = ""  # Строка для вывода вместо списка
    
    while pc < len(tokens):
        command = tokens[pc]
        
        if command == '👍': # Увеличить значение
            memory[pointer] += 1
        elif command == '👎': #Уменьшить
            memory[pointer] -= 1
        elif command == '👉':#Сдвинуть указатель вправо
            pointer += 1
        elif command == '👈':#Сдвинуть указатель влево
            pointer -= 1
        elif command == '🤖':
            output = output + chr(memory[pointer])
        elif command == '🔢':
            output = output + str(memory[pointer]) + ' '
        elif command == '🍅️':#Ввод числа в текущую ячейку
            memory[pointer] = random_simbol
        elif command == '😂':#Цикл: если в ячейке 0, выйти из цикла
            if memory[pointer] == 0:
                pc = loops[pc]
        elif command == '😭':#Конец цикла
            if memory[pointer] != 0:
                pc = loops[pc]
        
        pc += 1
    
    if output.endswith(' '):
        output = output[:-1]
    return output
if __name__ == "__main__":
    program = "👍" * 65 + "🤖"
    print(interpret(program))

