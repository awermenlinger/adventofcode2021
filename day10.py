import time
lines = open('files\day10.txt', 'r').read().rstrip().split('\n')

dict_stack_check = {")": "(", "}": "{", "]": "[", ">": "<"}
illegal_chars_values = {")": 3, "}": 1197, "]": 57, ">": 25137}
reduced_lines = []
illegal_chars = []
illegal_lines = []
legal_stacklist = []
for line in lines:   
    stack = []
    for char in line:
        if char in ["(", "[", "{", "<"]:
            stack.append(char)

        else:
            if char in dict_stack_check:
                if stack[-1] == dict_stack_check[char]:
                    stack.pop()
                else:
                    illegal_chars.append(illegal_chars_values[char])
                    illegal_lines.append(line)
                    break

print("Part 1: ", sum(illegal_chars))

legal_lines = [line for line in lines if line not in illegal_lines]

stack = []
for line in legal_lines:   
    stack = []
    for char in line:
        if char in ["(", "[", "{", "<"]:
            stack.append(char)

        else:
            if char in dict_stack_check:
                if stack[-1] == dict_stack_check[char]:
                    stack.pop()
                else:
                    illegal_chars.append(illegal_chars_values[char])
                    illegal_lines.append(line)
                    break
    legal_stacklist.append(stack)

reversed_stacklist = [stack[::-1] for stack in legal_stacklist]
closing_values = {"(": 1, "{": 3, "[": 2, "<": 4}
result_values = []
for r_stack in reversed_stacklist:
    result = 0
    for ele in r_stack:
        result = result * 5 + closing_values[ele]
    result_values.append(result)
result_values.sort()
middleIndex = (len(result_values) - 1)/2
print("Part 2: ", result_values[int(middleIndex)])
