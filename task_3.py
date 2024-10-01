def is_symmetric(s):
    stack = []
    opening = "({["
    closing = ")}]"
    matches = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if stack and stack[-1] == matches[char]:
                stack.pop()
            else:
                return "Несиметрично"
    return "Симетрично" if not stack else "Несиметрично"


# Приклади використання
print(is_symmetric("( ){ 1 ( ){ }}"))  # Симетрично
print(is_symmetric("( 23 ( 2 - 3);"))  # Несиметрично
print(is_symmetric("( 11 }"))  # Несиметрично