"""
text: "fooziman" output => "Fooziman"
"""

def fn_hack_3():
    result = "fooziman"
    result = result.capitalize()
    return result
resultado = fn_hack_3()

print(resultado)