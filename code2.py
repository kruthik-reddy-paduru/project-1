input_str = "This is a program experiment for fun in python"
char_count = {}
for i, char in enumerate(input_str):
    if char.isalpha():
        count = char_count.get(char, 0)
        if count > 0:
            next_char = chr(ord(char) + count)
            input_str = input_str[:i] + next_char + input_str[i+1:]
        char_count[char] = count + 1
print(input_str)