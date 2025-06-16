#Write a program to return the country code for various countries. Here’s a dictionary of different country codes - {'India' : '0091', 'Australia' : '0025', 'Nepal' : '00977
country_codes={'India' : '0091', 'Australia' : '0025', 'Nepal' : '00977'}
country=str(input('Enter name of country to get its code: '))
# print(country_codes.get('India','not found'))
# print(country_codes.get('North Korea','Your country does not exist or it is not registered in our database.'))
# print(country_codes.get('Australia','not found'))
# print(country_codes.get('Nepal','not found'))
print(f'Code of your entered country: {country_codes.get(country,'Your country does not exist or it is not registered in our database.')}')