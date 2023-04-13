input_str = "This is a program experiment for fun in python"
char_count = {}
for char in input_str:
    if char != " ":
        char_count[char] = char_count.get(char, 0)+1
print(char_count)