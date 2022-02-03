fruits1 = ["banana", "maça", "morango", "melão", "abacaxi"]
fruits2 = ["banana", "mamão", "uva", "melão", "abacaxi"]
i = 0
a = 0
print(len(fruits1))
while i < len(fruits1):
    if fruits1[i] == "morango":
        a+=1     
    i+=1
if a != 0:    
    print("morango faz parte da lista")
else:       
    print("morango não tem")