# Problem-solving practice 2 (competition / LeetCode style) - a step up in difficulty.
#
# Most of these are natural fits for a STACK or a QUEUE (this week's data structures).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def eval_rpn(tokens):
   # my plan is to create a stack and loop through every token and if it's a number convert it to int and add it 
   # to the stack if it's operator pop the second number and pop the first number, perform the operation and push 
   # the result back to the stack


    stack = []

    for token in tokens:
        if token not in ["+", "-", "*", "/"]:
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()

            if token == "+":
                result = a + b
            elif token == "-":
                result = a - b
            elif token == "*":
                result = a * b
            elif token == "/":
                result = int(a / b)

            stack.append(result)

    return stack.pop()



def decode_string(s):
    # so i'll create empty stack loop through each character in the string, if the character is
    #  in the digit build the repeat number, if it's [ push both the repeat count and string onto
    #  the string if it's a letter add it to the current string and if it's ] pop the previous string 
    # and repeat count, repeat the current string by that count and attach it to the previous string

    stack = []
    current = ""
    count = 0

    for char in s:
        if char.isdigit():
            count = count * 10 + int(char)

        elif char == "[":
            stack.append((current, count))
            current = ""
            count = 0

        elif char == "]":
            previous, repeat = stack.pop()
            current = previous + current * repeat

        else:
            current += char

    return current


def daily_temperatures(temps):

    #this is more striaght forward than the rest imo, all i have to do is create empty
    #  stack like the rest to store day indexes and after looping thgough the tempreture
    #  using their indexes pop the previous day from the stack, calculate how many days we
    #  waited, store that number in the result list and the previous day's index and filally
    #  push didays index onto the stack  and return the list


    result = [0] * len(temps)
    stack = []

    for i in range(len(temps)):
        while stack and temps[i] > temps[stack[-1]]:
            previous_day = stack.pop()
            result[previous_day] = i - previous_day

        stack.append(i)

    return result

def num_islands(grid):   # Part 4 - stretch (optional)
    # Outline:
    #   ...
    # TODO: `grid` is a list of equal-length strings of "1" (land) and "0" (water).
    #   Count the islands - groups of "1"s connected up/down/left/right (not diagonally).
    #   Example: ["11000","11000","00100","00011"]  ->  3
    pass


def main():
    # Optional scratch space - try your functions here, then run: python lab10.py
    # print(eval_rpn(["2", "1", "+", "3", "*"]))   # 9
    pass


if __name__ == "__main__":
    main()
