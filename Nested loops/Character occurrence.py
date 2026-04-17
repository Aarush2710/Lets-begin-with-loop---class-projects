word = input("Enter the word : ")
character = input("Enter the character : ")
count = 0
i = 0
while i < len(word):
    if  word[i] == character:
        
        count = count + 1
    i = i + 1
print("Number of character occurrences:", count)