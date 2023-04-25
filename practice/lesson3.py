age = int(input("Please enter your age: "))
driver = input("Are you driving? y/n ")
dl_license = input("Do you have an ID? y/n ")


if age < 21:
    ok_to_drink = False
elif driver == 'y':
    ok_to_drink = False
elif dl_license == 'n':
    ok_to_drink = False
else:
    ok_to_drink = True

# legal_age_to_drink = True if age >= 21 else False
#
# if age >= 21:
#     legal_age_to_drink = True
# else:
#     legal_age_to_drink = False

message = "\nYou can drink" if ok_to_drink else "\nNo drinking for you!"
print(message)


ls = ['a', 'b', 'c']
dict1 = {'age': 77, 'driver': driver, 'name': 'James'}
times_to_run = 12

for i in ls:
    print(f'the letter is {i}')

for k, v in dict1.items():
    print(f'the key is {k} with a value of {v}')

for j in range(times_to_run):
    print(f'loop number {j + 1}')




