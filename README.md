# Love_Score_Calculator_with_Python
This fun, simple Python program calculates a love score based on your and your crush's full names in English. There is no logic or reason in the calculation behind the love score. The calculation could have been anything different from what's shown in this code.

The calculation of the Love Score:
1. The program reads your and your crush's full names in English.
2. It then finds out how many alphabets in both names that match the alphabets in the words "TRUE" and "LOVE" (case insensitive).
3. The program gives 1 point for each match. For example, the name "Elon Musk" and "Grimes" will together have 4 points for the word "TRUE", and 4 points for the word "LOVE".
4. The program constructs the love score by putting together the score from the word "TRUE" and "LOVE" in a 2-digit integer format. In this case, Elon and Grimes' score is 44.
5. Then the program uses that score to predict how the two fit together with the following conditions:
    - If the score is less than 10 or more than 90, the program prints: "Your score is **love_score**, you go together like Coke and Mentos."
    - If the score is between 40 and 50, the program prints: "Your score is **love_score**, you are alright together."
    - For any other love score, only prints: "Your score is **love_score**."

*There is no reason or logic behind the calculation of the love score. It's just for fun!

Credit: This program is a modification of a Python program found in Angela Yu's "100 Days of Code: The Complete Python Pro Bootcamp" on Udemy. You can go to the course's page by clicking the following link (not a ref. link): https://www.udemy.com/course/100-days-of-code/
