#Different ways to capitalizes all words in a string in py3
'''1st -- >> using capwords() method which are in string modules'''
import string
quote = 'The best advice I  ever got was that knowledge is power'
print(string.capwords(quote))
#_______________________________________________________________

'''2nd -- >> calling split(),capitalizing the words in the resulting list,
 and then calling join() to combine the results.'''
print(' '.join([i.capitalize()for i in quote.split(' ')]))

#________________________________________________________________
#3rd using title()
print(quote.title())


'''Note if we have a string like  "they're bill's friends from the UK" 
 and use title() method the output will be like this 
 They'Re Bill'S Friends From The Uk  '''

new_string =  "they're bill's friends from the UK"
print(new_string.title())

#to solve this problem
new_string = "They'Re Bill'S Friends From The Uk"
import re
def titlecase(s):
    return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
                  lambda mo: mo.group(0)[0].upper() +
                             mo.group(0)[1:].lower(), s)

print(titlecase(new_string))


