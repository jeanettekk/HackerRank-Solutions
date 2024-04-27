# 20. Valid Parentheses | Easy
def isValid(s):
    stack = []
    bracket_dict = {'(': ')', '[': ']', '{': '}'}
    open_count = 0
    close_count = 0

    if len(s) % 2 != 0 or s[len(s) - 1] in bracket_dict or s[0] in bracket_dict.values():
        return False

    for index, character in enumerate(s):
        if character in bracket_dict:
            stack.append(character)
            open_count += 1

        else:
            close_count += 1
            if stack:
                if bracket_dict[stack[len(stack) - 1]] == character:
                    stack.pop()
                else:
                    return False

    if stack or open_count != close_count:
        return False
    else:
        return True

