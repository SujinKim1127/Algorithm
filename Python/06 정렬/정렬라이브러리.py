array = [('바나나', 2), ("사과", 4), ("당근", 3)]

def setting(data):
    return data[1]

result = sorted(array, key=setting)
print(result)