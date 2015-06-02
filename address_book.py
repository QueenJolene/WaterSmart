import sys

phone_number_dict = {}
name_dict = {}

class Contact():

	def __init__(self, name):
		self.name = name
		self.mobile = None
		self.home = None
		self.work = None

	def add_mobile(self, number):
		self.mobile = number

	def add_home(self, number):
		self.home= number

	def add_work(self, number):
		self.work = number

	def print_contact(self):
		print "Name: %s" % self.name
		print "Mobile: %s" % self.mobile
		print "Work: %s" % self.work
		print "Home: %s" % self.home

	def edit_contact(self):
		print "This is where you would edit the contact. Not functioning currently."


def add_number(number, contact):
		phone_number_dict[number]=contact

def add_name (name, contact):
		name = name.upper()
		name_dict[name]=contact

def add_contact():
	name = raw_input("What is your contact person's first and last name? > ").upper()
	contact = name_dict.get(name)
	while contact != None:
		print "That person is already in the address book.\n\n"
		contact.print_contact()
		answer = raw_input("\n\nWould you like to edit this record? 'YES' or 'NO'? > ").upper()
		if answer == "YES":
			contact.edit_contact()
			return
		else:
			return
		name = raw_input("What is your contact person's first and last name? > ")
	type_num = ""
	command = ""
	c = Contact(name)
	while command != "NO":
		type_num = raw_input("Please enter the number type: 'MOBILE', 'HOME', 'WORK' > ")
		type_num = type_num.upper()

		if type_num == "MOBILE":
			phone_number = raw_input("What is their phone number? > ")
			c.add_mobile(phone_number)
			add_number(phone_number,c)


		elif type_num =="HOME":
			phone_number = raw_input("What is their phone number? > ")
			c.add_home(phone_number)
			add_number(phone_number,c)

		elif type_num == "WORK":
			phone_number = raw_input("What is their phone number? > ")
			c.add_work(phone_number)
			add_number(phone_number,c)
		else:
			print "I'm sorry that is not a valid phone number type."

		command = raw_input("Would you like to add another different phone number? 'YES' or 'NO' > ").upper()

	add_name(name, c)

def find_contact():
	command = raw_input("Would you like to search by 'NAME' or 'PHONE'? > ").upper()
	if command == "NAME":
		name = raw_input("What is the person's name? > ").upper()
		contact = name_dict.get(name)
		if contact !=  None:
			contact.print_contact()
		else:
			print "That name is not in the phone book."

	if command == "PHONE":
		phone_number = raw_input("What is the phone number you'd like to look up? > ")
		contact = phone_number_dict.get(phone_number)
		if contact != None:
			contact.print_contact()
		else:
			print "That number is not in the phone book."


def main():
	command = ""
	while command != "QUIT":
		command = raw_input("Would you like to 'ADD' or 'FIND' a contact? Enter 'QUIT' to exit. > ").upper()
		if command.strip() == 'FIND':
			find_contact()
		elif command.strip() == 'ADD':
			add_contact()
		elif command.strip() == 'QUIT':
			sys.exit()
		else:
			print "That is not a valid command."

if __name__ == '__main__':
	main()
