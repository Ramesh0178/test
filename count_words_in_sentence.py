# method1
count = 1
sentence = input("enter a sentence:")
for letter in sentence:
    if letter ==" ":
        count = count+1
print("words in sentence:",count)   

# method2
sentence1=input("Enter a sentence:")
list = sentence1.split()
print("words in sentence:",len(list))  
