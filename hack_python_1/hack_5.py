"""
text: "fooziman" output => "f00z1m@n"
"""

def fn_hack_5():
    result = "fooziman"
    result = result.replace("ooziman","00z1m@n")
    return result  
resultado = fn_hack_5()

print(resultado)