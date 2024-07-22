"""
loop: while [] output => [5,4,3,2,1,0]
"""

def fn_hack_7():
    result = []
    resultado = len(result)
    while resultado < 1:
        result.append(5)
        resultado = len(result)
        if resultado < 2:
            result.append(4)
            resultado = len(result)
        if resultado < 3:
            result.append(3)
            resultado = len(result)
        if resultado < 4:
            result.append(2)
            resultado = len(result)
        if resultado < 5:
            result.append(1)
            resultado = len(result)
        if resultado < 6:
            result.append(0)
            resultado = len(result)
        return result
final = fn_hack_7()
print(final)