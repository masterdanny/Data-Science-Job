#set up lists and dictionaries that contain the written words of the numbers.
nums_0_19 = ['zero','one','two','three','four','five','six','seven','eight',"nine", 'ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
nums_20_90 =	['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
hundred_2_thousand = {100: "hundred", 1000: "thousand"}

def val2word(val):
	"""Take a number as an input and output the number as its written word"""
	if val < 20:
		return nums_0_19[val]
	elif val < 100:
		a = val % 100 - val % 10 
		return nums_20_90[a // 10 - 2] + ( "" if val % 10 == 0 else " " + nums_0_19[val % 10])

	else:
		a = max([i for i in hundred_2_thousand.keys() if i < val])
		return val2word(val // a) + " " + hundred_2_thousand[a] + ("" if val % a == 0 else " " + val2word(val % a))


#Take an input from 0 to 999 999
user_input = input ("Enter a Number: ")
try:
	val = int(user_input)
	print("Input number is: ", val)
	
	if len(str(val)) <= 6:
		print(str(val) + " --> " + val2word(val))
	else:
		#numbers greater or equal than a million shall not be outputed as words
		print("(Error message)")


except ValueError:
	print("That's not a number!")

