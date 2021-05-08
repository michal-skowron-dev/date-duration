from datetime import datetime
import time
import os

class Date:
	months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

	calendar_names = ["Gregorian calendar year", "Julian astronomical year", "Calendar common year", "Calendar leap year"]
	calendar_values = [31556952, 31557600, 31536000, 31622400]
	calendar_choice = 1

	def bound(value, low, high):
		return max(low, min(high, value))

	def add_leap_day(year, month):
		if month != 2:
			return 0
		
		if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
			return 1
		
		return 0
  
	def __init__(self, value):
		suffix = ""

		if value == "now":
			value = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
			suffix = " (now)"
		
		list = value.split(" ")

		date = list[0].split(".") if len(list) > 0 else None
		time = list[1].split(":") if len(list) > 1 else None
		
		self.year = Date.bound(int(date[2]), 1, 9999) if date is not None and len(date) > 2 else 1
		self.month = Date.bound(int(date[1]), 1, 12) if date is not None and len(date) > 1 else 1
		self.day = Date.bound(int(date[0]), 1, Date.months[self.month - 1] + Date.add_leap_day(self.year, self.month)) if date is not None and len(date) > 0 else 1
		
		self.hour = Date.bound(int(time[0]), 0, 23) if time is not None and len(time) > 0 else 0
		self.minute = Date.bound(int(time[1]), 0, 59) if time is not None and len(time) > 1 else 0
		self.second = Date.bound(int(time[2]), 0, 59) if time is not None and len(time) > 2 else 0

		self.label = "{:02d}.{:02d}.{:04d} {:02d}:{:02d}{}".format(self.day, self.month, self.year, self.hour, self.minute, suffix)

def convert_to_seconds(past, present):
	days = 0
	hours = 0
	minutes = 0
	seconds = 0

	if (past.year != present.year) or (past.month != present.month):
		days += Date.months[past.month - 1] + Date.add_leap_day(past.year, past.month) - past.day
		hours += 23 - past.hour
		minutes += 59 - past.minute
		seconds += 60 - past.second

		past.month += 1
		past.day = 1
		past.hour = 0
		past.minute = 0
		past.second = 0
	
		if past.month == 13:
			past.year += 1
			past.month = 1
		
		while (past.year != present.year) or (past.month != present.month):
			days += Date.months[past.month - 1] + Date.add_leap_day(past.year, past.month)
			past.month += 1
			
			if past.month == 13:
				past.year += 1
				past.month = 1

	if past.day != present.day:
		days += present.day - past.day - 1
		hours += 23 - past.hour
		minutes += 59 - past.minute
		seconds += 60 - past.second

		hours += present.hour
		minutes += present.minute
		seconds += present.second
	else:
		if past.hour != present.hour:
			hours += present.hour - past.hour - 1
			minutes += 59 - past.minute
			seconds += 60 - past.second

			minutes += present.minute
			seconds += present.second
		else:
			if past.minute != present.minute:
				minutes += present.minute - past.minute - 1
				seconds += 60 - past.second
				seconds += present.second
			else:
				seconds += present.second - past.second

	seconds += days * 86400
	seconds += hours * 3600
	seconds += minutes * 60

	return seconds

def close_frame(text_length):
	spaces = 71 - text_length
	extra_text = ""
	i = 0

	while i < spaces:
		extra_text += " "
		i += 1
	
	extra_text += "|"
	return extra_text

def display_help(message, past_label, present_label):
	print(" ------------------------------------------------------------------------")
	print("| {}{}".format(Date.calendar_names[Date.calendar_choice], close_frame(len(Date.calendar_names[Date.calendar_choice]))))
	print("|									 |")
	print("| {}{}".format(message, close_frame(len(message))))
	print("| {}{}".format(past_label, close_frame(len(past_label))))
	print("| {}{}".format(present_label, close_frame(len(present_label))))
	print("|									 |")
	print("|     Command	Description						 |")
	print("|									 |")
	print("|     q		Quit program						 |")
	print("|     h		Display help						 |")
	print("|     c		Clear console						 |")
	print("|									 |")
	print("|     1 - 9	Choose event						 |")
	print("|     y		Change calendar						 |")
	print("|     d		Display date duration in given format: y m w d H M S	 |")
	print(" ------------------------------------------------------------------------")

def clear_console():
	os.system("cls" if os.name == "nt" else "clear")

def change_calendar():
	print("\n1| {}".format(Date.calendar_names[0]))
	print("2| {}".format(Date.calendar_names[1]))
	print("3| {}".format(Date.calendar_names[2]))
	print("4| {}".format(Date.calendar_names[3]))
	choice = input("Choice: ")

	if choice == "1" or choice == "2" or choice == "3" or choice == "4":
		Date.calendar_choice = int(choice) - 1

def display_menu(message, past_label, present_label, seconds, start_time, inverted):
	display_help(message, past_label, present_label)
	updated_time = 0
	
	while True:
		if start_time != 0:
			if inverted:
				past_label = datetime.now().strftime("%d.%m.%Y %H:%M (now)")
			else:
				present_label = datetime.now().strftime("%d.%m.%Y %H:%M (now)")
			
			updated_time = int(time.time() - start_time)
		
		command = input("Command: ")

		if command == "q":
			return -1
		elif command == "1":
			clear_console()
			return 0
		elif command == "2":
			clear_console()
			return 1
		elif command == "3":
			clear_console()
			return 2
		elif command == "4":
			clear_console()
			return 3
		elif command == "5":
			clear_console()
			return 4
		elif command == "6":
			clear_console()
			return 5
		elif command == "7":
			clear_console()
			return 6
		elif command == "8":
			clear_console()
			return 7
		elif command == "9":
			clear_console()
			return 8
		elif command == "h":
			clear_console()
			display_help(message, past_label, present_label)
		elif command == "c":
			clear_console()
		elif command == "y":
			change_calendar()
			clear_console()
			display_help(message, past_label, present_label)
		elif command == "d":
			_seconds = seconds + updated_time

			format = input("\nFormat: ")
			chosen = format.split(" ")
			output = ""
			i = 0

			while i < len(chosen):
				if chosen[i] == "y":
					years = int(_seconds / Date.calendar_values[Date.calendar_choice])
					_seconds -= years * Date.calendar_values[Date.calendar_choice]
					output += " {} years".format(years)
				elif chosen[i] == "m":
					months = int(_seconds / int(Date.calendar_values[Date.calendar_choice] / 12))
					_seconds -= months * int(Date.calendar_values[Date.calendar_choice] / 12)
					output += " {} months".format(months)
				elif chosen[i] == "w":
					weeks = int(_seconds / 604800)
					_seconds -= weeks * 604800
					output += " {} weeks".format(weeks)
				elif chosen[i] == "d":
					days = int(_seconds / 86400)
					_seconds -= days * 86400
					output += " {} days".format(days)
				elif chosen[i] == "H":
					hours = int(_seconds / 3600)
					_seconds -= hours * 3600
					output += " {} hours".format(hours)
				elif chosen[i] == "M":
					minutes = int(_seconds / 60)
					_seconds -= minutes * 60
					output += " {} minutes".format(minutes)
				elif chosen[i] == "S":
					output += " {} seconds".format(_seconds)
				i += 1
			
			print("Output:" + output + "\n")

def read_values(option):
	with open("dates.txt") as file:
		lines = file.read().splitlines()
	
	if (lines is None) or (len(lines) != 9):
		print("dates.txt is empty or doesn't have 9 lines")
		return -1

	line_values = lines[option].split("\t")
	return line_values

def is_inverted(past, present):
	if past.year > present.year:
		return True
	elif (past.year == present.year) and (past.month > present.month):
		return True
	elif (past.year == present.year) and (past.month == present.month) and (past.day > present.day):
		return True
	elif (past.year == present.year) and (past.month == present.month) and (past.day == present.day) and (past.hour > present.hour):
		return True
	elif (past.year == present.year) and (past.month == present.month) and (past.day == present.day) and (past.hour == present.hour) and (past.minute > present.minute):
		return True
	elif (past.year == present.year) and (past.month == present.month) and (past.day == present.day) and (past.hour == present.hour) and (past.minute == present.minute) and (past.second > present.second):
		return True
	else:
		return False

def main():
	option = 0
	
	while option != -1:
		line_values = read_values(option)

		if line_values == -1:
			return
		elif len(line_values) != 4:
			print("dates.txt has less than 3 tabulators in line {}".format(option + 1))
			return

		message = "{} {}".format(line_values[0], line_values[1])
		past_date = line_values[2]
		present_date = line_values[3]

		past = Date(past_date)
		present = Date(present_date)
		
		inverted = is_inverted(past, present)

		if inverted:
			temp = past
			past = present
			present = temp
		
		start_time = 0

		if present_date == "now":
			start_time = time.time()
		
		seconds = convert_to_seconds(past, present)
		option = display_menu(message, past.label, present.label, seconds, start_time, inverted)

main()