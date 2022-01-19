#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Love score calculator with Python
#This simple program calculates your love score from your names
#It reads your full name and your crush's full name in English.
#Then it finds out how many alphabets in both names match the alphabets in the word "TRUE" and "LOVE" (1 point for each match)
#It then constucts the love score by putting together the score from "TRUE" and "LOVE" together in 2 digit-integer

#conditions:
#If the love score is less than 10 and more than 90:
#print: "Your score is **love_score**, you go together like Coke and Mentos."
#If the love score is between 40 and 50:
#print: "Your score is **love_score**, you are alright together."
#For any other love score, only print: "Your score is **love_score**."

#-----------There is no logic or reason behind the calculation of the love score---------------
#-----------The calculation could have also been something else-----------------

print("Welcome to the Love Calculator!")
name1 = input("What is your full name in English? \n")
name2 = input("What is your crush's full name in English? \n")

names = name1 + name2
t_score = 0
r_score = 0
u_score = 0
e1_score = 0
l_score = 0
o_score = 0
v_score = 0
e2_score = 0

true_score = 0
love_score = 0

#-----------------------find "TRUE" score
for i in range(len(names)):
    if names[i] == "T" or names[i] == "t":
        t_score += 1
    
    if names[i] == "R" or names[i] == "r":
        r_score += 1

    if names[i] == "U" or names[i] == "u":
        u_score += 1

    if names[i] == "E" or names[i] == "e":
        e1_score += 1

true_score = t_score + r_score + u_score + e1_score

#-----------------------find "LOVE" score
for n in range(len(names)):
    if names[n] == "L" or names[n] == "l":
        l_score += 1
    
    if names[n] == "O" or names[n] == "o":
        o_score += 1

    if names[n] == "V" or names[n] == "v":
        v_score += 1

    if names[n] == "E" or names[n] == "e":
        e2_score += 1

love_score = l_score + o_score + v_score + e2_score

total_score = int(str(true_score)+str(love_score))

if total_score < 10 or total_score > 90:
    print(f"Your score is {total_score}, you go together like coke and mentos.")
elif total_score >= 40 and total_score <= 50:
    print(f"Your score is {total_score}, you are alright together.")
else:
    print(f"Your score is {total_score}.")


# In[ ]:




