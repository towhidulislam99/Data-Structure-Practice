
def string_reverse(string):
    if len(string) == 0:
        return string
    else: 
        return string_reverse(string[1:]) + string[0]
    
reverse_word = "Hello"
output = string_reverse(reverse_word)

print(output)

    


        