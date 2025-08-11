# DO NOT DELETE... i come here to try out random code blocks and interact with copilot!!!

# def currency_counter(amount):
#     currency = [10, 5, 2, 1]  # Sort denominations from largest to smallest for optimal counting
#     number = {}  # Dictionary to store count of each denomination
#     for c in currency:
#         number[c] = amount // c  # Calculate how many of this denomination are needed
#         amount = amount % c  # Update the remaining amount
#     return number  # Return the dictionary with counts


# result = currency_counter(19)  # Call the function and store the result
# print(result)  # Print the result to see the output



# with open("./PYTHON INTRO/logs/error_int.txt", "r") as file:
#     file_lines = file.readlines()   #.readlines() returns all lines of the txt file as a list of indexed strings
#     header = file_lines[0]  #first line of the file
#     body = file_lines[1:]   #body of the file
#     interface_and_error = {}
#     for line in body:
#         line_index = line.split(",")    #splits each word in each line using a comma
#         interface_and_error[line_index[0]] = int(line_index[3]) #adds the values in each line that fits the index into the empty dictionary
    
#     sorted_intanderr = sorted(interface_and_error.items(), key=lambda x: x[1], reverse=True) #sorts the value entries of the dictionary in descending order(reverse=True)
#     highest_five = sorted_intanderr[:5] #the highest five values are isolated
#     for interface, err in highest_five:
#         print(f"{interface}: {err} errors logged")

english_word = "you are the best man in Nigeria"
words = english_word.split()    #splits the sentence into words
latin_word = ""

for word in words:
    first_letter = word[0]  #first letter needed for vowel or consonant comparison
    # print(first_letter)
    if first_letter in "aeiou": #checking for vowel
        word = word + "ma"  #add 'ma' to end of word using concatenation
        # print(word)
    else:                   #else statement here grabs all non-vowel first letters
        word = word.replace(first_letter, "")   #removes first letter from the word
        word = word + "ma"                      #adds 'ma' to the end
        # print(word)
    latin_word += word + " "         #new latin words are added to the empty string and seperated with a space

print(latin_word)


















