"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""
 
def fn_hack_10():
    result = "fooziman"   
    result2 ="F,0,0,Z,1,M,@,N"
    return result.replace("fooziman",result2).split(",")
final = fn_hack_10()
print(final)
