# Assignment1
for the first question:
first I created a variable named change to store the change amount (substracting cost from tendered amount)
I used the floor division to get the number of bills/coins for each category then i will substract the result number of bills from the change(for ex: change//50 will give the number of 50 bills I have to give to customer, then substract that number (times 50 ) from change redo the same process with 20s,10s...until the change is 0.

#2nd question
For the username, I used the first six letters of the last name (last_name[0:6]), followed by the first letter of the first name (first_name[0]) and the first letter of the middle name (middle_name[0]).

For the password, I used the first two letters of the first name (first_name[0:2]). For the first three even-positioned letters of the middle name, I created a new variable, even_letters [middle_name[1::2] started indexing from 1 (in human language it's 2nd letter which is an even number))
, to store the letters in the even positions, and then used the first three letters of that variable (even_letters[0:3]). For Adele, since she does not have a middle name, I left out the middle-name portion of the password. Finally, I added the last four digits of the phone number using phone[-4:], which gets the last four characters of a string.
