Simple Data Address Book
----------------

Details to this coding challenge:
A product manager comes	to you with a specification	for	a phonebook	application.
She	wants	to	be	able efficiently store a large set of numbers of different types	
(home, mobile, work, etc).	She	would also like	to	be	able to	access	the	phonebook entries 
by both numbers	and	names.	Assume that	there is no	persistent	backend	storage. Design	an	
interface and write out	the	code that you would	use	to implement that interface.	
Provide	samples	of usage of	your interface,	and	explain	why	you	think your data structures are a good fit.


###### Functionality

Takes arguments from user via a commandline prompt.

To run:

Clone repository and type the following command:

	python address_book.py


###### Assumptions:
1.) Data does not need to persist after program closes.

For simplicity:
1.) Cannot have multiple contacts with the same name.
2.) Contacts cannot share phone numbers.  Code could be modified to accommodate number sharing, but since
the directions did not specify, I kept it simple.

###### Data Structure Choice:

Each contact record is stored as an object "Contact".
The addressbook is stored in two dictionaries. One with key's that are names, and one with keys that are phone numbers, with values pointing to the same objects.  I chose to use dictionaries for their fast look up time.  

I chose to store Contact records as objects in order to not duplicate data storage in the dictionaries. I use the dictionaries a simple pointers to the same objects.

###### Technology
Python
