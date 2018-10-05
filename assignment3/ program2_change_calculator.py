#! /usr/bin/env python3 

def main():

	print('Change Calculator')
	choice ="y"
	while(choice=="y"):
			cent = int(input('Enter number of cents:'))

			restQuarters = number(cent,'quarters')
			print('Quarters :',(cent-restQuarters)/25)
			
			restDimes = number(restQuarters,'dimes')
			print('Dimes :',(restQuarters-restDimes)/10)
			
			restNickels = number(restDimes,'nickels')
			print('Nickels :',(restDimes-restNickels)/5)

			restPennies = number(restNickels,'pennies')
			print('Pennies :',(restNickels-restPennies)/1)

			print()
			choice = input("Continue? (y/n): ")
        while choice.lower()!="y" and choice.lower!="n":
            choice = input("Wrong input. Continue? (y/n): ")



def number(cent,type):
	rest = 0
	if type == 'quarters':
		rest = cent%25
	elif type == 'dimes':
		rest = cent%10
	elif type == 'nickels':
		rest = cent%5
	elif type == 'pennies':
		rest = cent%1
	else:
		print('type incorrect')

	return rest

if __name__ == "__main__":
    main()