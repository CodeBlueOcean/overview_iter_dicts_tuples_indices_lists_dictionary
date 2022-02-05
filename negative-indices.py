awesome = "awesome"

print(len(awesome)) 
# prints out 7 letters, index of 0-6
print(awesome[-1]) 
# prints out letter e at the end of word
print(awesome[-3])
# prints out the letter o at the end of the word
print(awesome[::-1]) 
# prints backwords emosewa
print(awesome[-1::-1]) 
# prints backwords emosewa
print(awesome[-1:-7:-1]) 
# indicates start, stop, step, goes backwards of the word, stop at the end of the letter and skip "a". 
print(awesome[-1:-100:-1]) 
# prints backwords emosewa
print(awesome[-1:-3:-1]) 
# prints em, backwards, em 
print(awesome[-1::-2]) 
# prints eoea 

