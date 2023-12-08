#!/usr/bin/env python
# coding: utf-8

# [![image](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/giswqs/geog-312/blob/master/labs/lab_07.ipynb)
# [![image](https://binder.pangeo.io/badge_logo.svg)](https://gishub.org/geog312-pangeo)
# 
# **Firstname Lastname**

# In[ ]:





# In[ ]:


from datetime import datetime

now = datetime.now()
print(f"Submitted time: {now}")


# ## Question 1
# **Learning Python:** Open a blank file in your text editor and write a few lines summarizing what you’ve learned about Python so far. Start each line with the phrase *In Python you can. . ..* Save the file as *learning_python.txt* in the same directory as your exercises from this chapter. Write a program that reads the file and prints what you wrote three times. Print the contents once by reading in the entire file, once by looping over the file object, and once by storing the lines in a list and then working with them outside the *with* block.

# In[3]:


file_path = '/Users/elliebernstein/Downloads/learning_python.txt'
with open(file_path) as file_object:
  for line in file_object:
        print(line)

with open(file_path) as file_object:
    contents = file_object.read()
print(contents)

with open(file_path) as file_object:
    contents = file_object.read()
    print(contents.rstrip())


# ## Question 2
# **Learning C:** You can use the replace() method to replace any word in a string with a different word. Here’s a quick example showing how to replace 'dog' with 'cat' in a sentence:
# ```
# message = "I really like dogs."
# message.replace('dog', 'cat')
# 'I really like cats.'
# ```
# Read in each line from the file you just created, *learning_python.txt*, and replace the word *Python* with the name of another language, such as *C*. Print each modified line to the screen.

# In[5]:


file_path = '/Users/elliebernstein/Downloads/learning_python.txt'

lines = contents.splitlines()
for line in lines:
    line = line.replace('python', 'C')
    print(line)


# ## Question 3
# **Guest:** Write a program that prompts the user for their name. When they respond, write their name to a file called guest.txt.

# In[7]:


import json
prompt = input("What is your name?")
filename = "guest.txt"
with open(filename, 'w') as f:
    json.dump(prompt, f)


# ## Question 4
# **Guest Book:** Write a while loop that prompts users for their name. When they enter their name, print a greeting to the screen and add a line recording their visit in a file called guest_book.txt. Make sure each entry appears on a new line in the file.

# In[8]:


file_path = '/Users/elliebernstein/Downloads/guest_book.txt'

guest_names = []
while True:
    name = input("What is your name?")
    if name == 'quit':
        break
    print(f"Thanks {name}, you will be added to the guest book.")
    guest_names.append(name)

with open(file_path, 'w') as f:
    json.dump(guest_names, f)


# ## Question 5
# **Programming Poll:** Write a while loop that asks people why they like programming. Each time someone enters a reason, add their reason to a file that stores all the responses.

# In[10]:


file_path = '/Users/elliebernstein/Downloads/program_poll'

reasons = []
while True:
    name = input("Why do you like programming?")
    if name == 'quit':
        break
    reasons.append(name)

with open(file_path, 'w') as f:
    json.dump(reasons, f)


# ## Question 6
# **Addition:** One common problem when prompting for numerical input occurs when people provide text instead of numbers. When you try to convert the input to an int, you’ll get a ValueError. Write a program that prompts for two numbers. Add them together and print the result. Catch the ValueError if either input value is not a number, and print a friendly error message. Test your program by entering two numbers and then by entering some text instead of a number.

# In[14]:


try:
    x = input("give number: ")
    x = int(x)

    y = input("give second number: ")
    y = int(y)
except ValueError:
    print("Error")
else:
    sum = x + y
    print(f"The sum of {x} and {y} is {sum}")


# ### Question 7
# **Addition Calculator:** Wrap your code from Question 6 in a while loop so the user can continue entering numbers even if they make a mistake and enter text instead of a number.

# In[15]:


print("Type Quit at any time")
while True:
    try:
        x = input("give number: ")
        if x == 'Quit':
            break
        x = int(x)
        y = input("give second number: ")
        if y == 'q':
            break
        y = int(y)
    except ValueError:
        print("error.")
    else:
        sum = x + y
        print(f"{x} plus {y} is {sum}")


# ## Question 8
# **Cats and Dogs:** Make two files, *cats.txt* and *dogs.txt*. Store at least three names of cats in the first file and three names of dogs in the second file. Write a program that tries to read these files and print the contents of the file to the screen. Wrap your code in a `try-except` block to catch the `FileNotFound` error, and print a friendly message if a file is missing. Move one of the files to a different location on your system, and make sure the code in the `except` block executes properly.

# In[25]:


dogs = '/Users/elliebernstein/Downloads/dogs.txt'
cats = '/Users/elliebernstein/Downloads/cats.txt'
filenames = [cats,dogs]
for filename in filenames:
    print(f"file: {filename}")
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        print(contents)


# ## Question 9
# **Silent Cats and Dogs:** Modify your except block in Question 8 to fail silently if either file is missing.

# In[26]:


dogs = '/Users/elliebernstein/Downloads/dogs.txt'
cats = '/Users/elliebernstein/Downloads/cats.txt'
filenames = [cats,dogs]
for filename in filenames:
    print(f"file: {filename}")
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        print(contents)


# ## Question 10
# **Common Words:** Visit Project Gutenberg (https://gutenberg.org/) and find a few texts you’d like to analyze. Download the text files for these works, or copy the raw text from your browser into a text file on your computer. You can use the `count()` method to find out how many times a word or phrase appears in a string. For example, the following code counts the number of times 'row' appears in a string:

# In[ ]:


line = "Row, row, row your boat"
line.count('row')


# In[ ]:


line.lower().count('row')


# Notice that converting the string to lowercase using lower() catches all appearances of the word you’re looking for, regardless of how it’s formatted.
# 
# Write a program that reads the files you found at Project Gutenberg and determines how many times the word `the` appears in each text. This will be an approximation because it will also count words such as `then` and `there`. Try counting `the`, with a space in the string, and see how much lower your count is.

# In[32]:


file_path = "/Users/elliebernstein/Downloads/pg72354.epub"
def count_common_words (file_path, word):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        word_count = contents.lower().count(word)
        msg = f"'{word}' appears in {filename} about {word_count} times."
        print(msg)
        
filename = 'pg72354.epub'
count_common_words(filename, 'the')


# ## Question 11
# **Favorite Number:** Write a program that prompts for the user’s favorite number. Use `json.dump()` to store this number in a file. Write a separate program that reads in this value and prints the message, `I know your favorite number! It’s _____.`

# In[ ]:


import json

file_path = "/Users/elliebernstein/Downloads/fav_num"

number = input("What's your favorite number? ")

with open(file_path, 'w') as f:
    json.dump(number, f)


# In[ ]:


import json

file_path = "/Users/elliebernstein/Downloads/fav_num"

with open(file_path, 'w') as f:
    number = json.load(f)

print(f"I know your favorite number! It's {number}.")


# ## Question 12
# **Favorite Number Remembered:** Combine the two programs from Question 10 into one file. If the number is already stored, report the favorite number to the user. If not, prompt for the user’s favorite number and store it in a file. Run the program twice to see that it works.

# In[ ]:


import json

file_path = "/Users/elliebernstein/Downloads/fav_num"

number = input("What's your favorite number? ")

with open(file_path, 'w') as f:
    json.dump(number, f)
    

with open(file_path, 'w') as f:
    numbers = json.load(f)

print(f"I know your favorite number! It's {number}.")


# In[ ]:




