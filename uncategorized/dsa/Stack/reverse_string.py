from stack import Stack


def reverse_string(input_str):
    s = Stack()
    for i in range(len(input_str)):
        s.push(input_str[i])
    reversed_str = ""
    while not s.is_empty():
        reversed_str += s.pop()

    return reversed_str


input_str = "!emoh yM ot emocleW"
print(reverse_string(input_str))