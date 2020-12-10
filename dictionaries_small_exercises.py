#Small Exercise #1 Phonebook dictionary
phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}

#Print Elizabeth's phone number
print(phonebook_dict['Elizabeth'])

#Add an entry to the dictionary: Kareem's number is 938-489-1234
phonebook_dict['Kareem'] = '938-489-1234'
print(phonebook_dict)

#Delete Alice's Entry
del(phonebook_dict['Alice'])
print(phonebook_dict)

#Change Bob's phone number to 968-345-2345'
phonebook_dict['Bob'] = '968-345-2345'
print(phonebook_dict)

#Print all the phone entries
phonebook_dict.values()
print(phonebook_dict.values())





#Small Exercise #2 Nested dictionaries
ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

#Write a python expression that gets the email address of Ramit
print (ramit['email'])

#Write a python expression that gets the first of Ramit's interests.
print (ramit['interests'][0])

#Write a python expression that gets the email address of Jasmine.
print (ramit['friends'][0]['email'])

#Write a python expression that gets the second of Jan's two interests.
print (ramit['friends'][1]['interests'][1])




#Small Exercise #3 Friend counter
