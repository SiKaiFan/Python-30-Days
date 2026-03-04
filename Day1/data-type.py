# On this file we will learn only about data types
# number(int, float, complex), boolean(True, False), string, list, 
#ditionary, set, tuple

current_year = 2026
print(current_year)
next_year = current_year + 1
print(next_year)
print(type(next_year))
#using type we can check the data type
print(type(2))
print(type(3.14))
print(type(1+2j))

#Converting float to int

print(int(3.14))
print(round(9.81))
print(float(2))

#Boolean : True or False

enjoying_lesson = True
is_light_on = True
is_single = False
value = 3 < 2
print(value)

#Strings -> strings are text data types

firstname = 'Kai'
print(firstname)
lastname = 'Fan'
fullname = firstname + ' ' + lastname #concatentation
print(fullname)

print(type(firstname))
#We can use different string methods to manipulate the string

country = 'Taiwan'
print(country.upper())
print('i love python because it is awasome'.title())