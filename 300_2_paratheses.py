def isValid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)

    return not stack


# Example usage:
#input_string = "{[()]}"
input_string = "()"
if isValid(input_string):
    print(f"The input string '{input_string}' is valid.")
else:
    print(f"The input string '{input_string}' is NOT valid.")
