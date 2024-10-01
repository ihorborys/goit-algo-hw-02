from collections import deque


def is_palindrome(text) -> bool:
    # Перетворення рядка на нижній регістр та видалення пробілів
    text = text.lower().replace(" ", "")

    # Створення двосторонньої черги та додавання символів
    d = deque(text)

    # Порівняння символів з обох кінців черги
    if len(d) == 0:
        return False
    if len(d) == 1:
        return True
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True


# Приклади використання функції
print(is_palindrome("А баба б а"))
print(is_palindrome("Анна"))
print(is_palindrome("Аннка"))
print(is_palindrome("Аа"))
print(is_palindrome("а"))
print(is_palindrome(""))
