"""
list: [1,3,5,7,9] output => [3,5,7]
"""

def fn_hack_8():
    result = [1,3,5,7,9]
    result.pop(0)
    result.pop(3)
    return result
resultado = fn_hack_8()
print(resultado)