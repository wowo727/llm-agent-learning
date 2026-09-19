def add(a,b):
    return a+b

anser=add(10,20)
print(anser)

def get_level(score):
    if score >= 90:
        return "优秀"
    else:
        return "其他"

result = get_level(95)