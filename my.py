import sys

def interpret(code):
    tokens = code.split()  
    
    memory = [0] * 30000
    pointer = 0
    pc = 0
    loops = {}
    stack = []
    random_simbol = ['(❁◡❁)']  # Морд
    output = ""  
    
    for i, token in enumerate(tokens):
        if token == '😂':  #Начало цикла
            stack.append(i)
        elif token == '😭':  #Конец цикла
            start = stack.pop()
            loops[start] = i
            loops[i] = start
    
    while pc < len(tokens):
        command = tokens[pc]
        
        if command == '👍':  # Увеличить значение
            memory[pointer] += 1
        elif command == '👎':  #Уменьшить
            memory[pointer] -= 1
        elif command == '👉':  #Сдвинуть указатель вправо
            pointer += 1
        elif command == '👈':  #Сдвинуть указатель влево
            pointer -= 1
        elif command == '🤖':  #Вывести символ (ASCII)
            output += chr(memory[pointer])
        elif command == '🔢':  #Вывести число
            output += str(memory[pointer]) + ' '
        elif command == '🍅':  #Ввод числа в текущую ячейку (вывод мордочки)
            output += ''.join(random_simbol)  # Вывод мордочки
        elif command == '😂':  #Цикл: если в ячейке 0, выйти из цикла
            if memory[pointer] == 0:
                pc = loops[pc]
        elif command == '😭':  #Конец цикла
            if memory[pointer] != 0:
                pc = loops[pc]

        pc += 1
    
    if output.endswith(' '):
        output = output[:-1]  #Удалить проб
    return output

if __name__ == "__main__":
    program = "👍" * 65 + "🤖"
    print(interpret(program))

