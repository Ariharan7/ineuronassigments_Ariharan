#!/usr/bin/env python
# coding: utf-8

# 1.What are the two values of the Boolean data type? How do you write them?
# 
# Answer1: True, False

# 2. What are the three different types of Boolean operators?
# 
# Answer2: And, or, Not

# 3. Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean values for the operator and what it evaluate ).
# 
# Answer3: True is 1, False is 0
# 
# And truth table: 
# A	B	Output	Explanation 
# 0	0	0	   False and False is False
# 0	1	0	   False and True is False
# 1	0	0	   True and False is False
# 1	1	1	   True and True is True
# 
# Or truth table: 
# A	B	Output	Explanation 
# 0	0	0	   False or False is False
# 0	1	1	   False or True is True
# 1	0	1	   True or False is True
# 1	1	1	   True or True is True
# 
# Not truth table: 
# A	Output	Explanation 
# 0	1	    Not False is True
# 1	0	    Not True is False

# 4. What are the values of the following expressions?
# (5 > 4) and (3 == 5) 
# not (5 > 4)
# (5 > 4) or (3 == 5)
# not ((5 > 4) or (3 == 5))
# (True and True) and (True == False)
# (not False) or (not True)

# In[3]:


print((5>4) and (3==5))
print(not(5>4))
print((5>4) or (3==5))
print(not((5>4) or (3==5)))
print((True and True) and (True==False))
print((not False) or (not True))


# 5. What are the six comparison operators?
# 
# Answer5: <, >, ==, !=, <=, >=

# 6. How do you tell the difference between the equal to and assignment operators?Describe a condition and when you would use one.
# 
# Answer6: equal to(==) is the operator that compares two values which gives a result as Boolean whereas assignement(=) assigns a value and stores it in a variable.

# 7. Identify the three blocks in this code:
# spam = 0
# if spam == 10:
# print('eggs')
# if spam > 5:
# print('bacon')
# else:
# print('ham')
# print('spam')
# print('spam')

# In[6]:


spam = 0
if spam == 10: #block1
    print('eggs') 
if spam > 5: #block2
    print('bacon')
else: #block3
    print('ham')
    print('spam')
    print('spam')


# 8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

# In[1]:


spam = int(input("Enter a number : "))
if spam == 1:
    print("Hello")
elif spam == 2:
    print("Howdy")
else:
    print("Greetings!")


# 9. If your programme is stuck in an endless loop, what keys you’ll press?
# 
# Answer : Ctrl + C should be pressed if programme is stuck in an endless loop.

# 10. How can you tell the difference between break and continue?
# 
# Answer :  	
# 
# Break : It eliminates the execution of remaining iteration of loop
# Continue : It will terminate only the current iteration of loop.

# 11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?
# 
# Answer : As per the below outputs we can confirm that there is no difference in provided set of ranges.

# In[2]:


for i in range(10):
    print(i)


# In[3]:


for i in range(0,10):
    print(i)


# In[4]:


for i in range(0,10,1):
    print(i)


# 12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

# In[5]:


for i in range(1,11):
    print(i)


# In[1]:


a = 1
b = 10

while a<=b:
    print(a)
    a+=1


# 13. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
# 
# Answer13 : It can be called as spam.bacon() after importing the spam. 
