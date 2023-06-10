def likes(names):
    result = 'no one likes this'
    if 1 > len(names) > 0:
        result = f'{names[0]} likes this'
        return result
    elif len(names) >= 2 and len(names) < 3:
        result = f'{names[0]} and {names[1]} likes this'
        return result
    elif len(names) >= 3 and len(names) < 4:
        result = f'{names[0]}, {names[1]} and {names[2]} likes this'
        return result
    elif len(names) >= 4:
        result = f'{names[0]}, {names[1]} and 2 others like this'
        return result
    elif len(names) == 0:
        return result


names = ['Jacob', 'Alex', 'Mark', 'Tom']
print(likes(names))
