#!/usr/bin/env python3
#this program allows a student to complete a registration form


print('Registration Form')
print()

#get input from users

firstname = str(input('First name:\t'))

lastname = str(input('Last name:\t'))

year = int(input('Birth year:\t'))


#display informations
print()
print('Welcome '+firstname+' '+lastname)
print('Your registration is complete')
print('Your temporary password is: '+firstname+'*'+str(year))
