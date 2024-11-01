with open("story.txt","r", encoding="utf-8") as f: #to open any file like txt or json file in the read mode and we can do any file operations on this variable f
    story = f.read()

# print(story)

#enumerate allows us to access the positon as well as the element at that postion

words = set() #we get duplicated words aldo but we want only unique So instead of list we use set to get only unique elements
#for list we simply write words = []
start_of_word = -1
target_start = "<"
target_end = ">"

#find all the different words in the story
for i,char in enumerate(story): #getting the index and along the value
    if char == target_start:
        start_of_word = i
    
    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i+1]
        #slicing (subsection of the string)-->staring character is start_of_word and the ending character is not included but we need to be 
        #included so we put + 1 to i
        words.add(word) #if words is list then we say append instead of add
        start_of_word = -1 #as we found 1 whole word next we will reset it back

# print(words)

# now we have words now we will ask the user to put some values by setting up a dictionary

answers ={} #empty dictionary

for word in words:
    answer = input("Enter a word for " + word + ": ")  #we will use plus in input stmts in order to concate 2 strings
    answers[word] = answer

# print(answers)
# this gives us all the different words and their answers from the user

#Now we should replace these answers within the story

for word in words:
    story = story.replace(word,answers[word]) 
    #replace every single instance of 1 string with another and we know both what to replace and with what
    # we replace the angular brackets with the user input 

print(story)
