import sys

def interpret(code):
    tokens = code.replace('.', '').replace('!', '').split()
    
    memory = [0] * 30000
    pointer = 0
    pc = 0
    loops = {}
    stack = []
    
    # Сборка пар циклов для 😂 и 😭
    for i, token in enumerate(tokens):
        if token == '😂':  # начало цикла
            stack.append(i)
        elif token == '😭':  # конец цикла
            start = stack.pop()
            loops[start] = i
            loops[i] = start
    
    output = ""  # Строка для вывода вместо списка
    
    while pc < len(tokens):
        command = tokens[pc]
        
        if command == '👍':  # Увеличить значение
            memory[pointer] += 1
        elif command == '👎':  # Уменьшить
            memory[pointer] -= 1
        elif command == '👉':  # Сдвинуть указатель вправо
            pointer += 1
        elif command == '👈':  # Сдвинуть указатель влево
            pointer -= 1
        elif command == '🤖':  # Вывести символ (ASCII)
            output += chr(memory[pointer])
        elif command == '🔢':  # Вывести число
            output += str(memory[pointer])
        elif command == '⏬':  # Ввод числа в текущую ячейку
            memory[pointer] = int(input())
        elif command == '😂':  # начало цикла: если текущая ячейка = 0, перепрыгнуть
            if memory[pointer] == 0:
                pc = loops[pc]
        elif command == '😭':  # конец цикла: если текущая ячейка ≠ 0
            if memory[pointer] != 0:
                pc = loops[pc]
        elif command == '▶':  
            if memory[pointer] == 0:
                pc = loops.get(pc, pc)
        elif command == '◀': 
            if memory[pointer] != 0:
                pc = loops.get(pc, pc)
        
        pc += 1
    
    return output

if __name__ == "__main__":
    program = "👍" * 65 + "🤖"
    print(interpret(program))
