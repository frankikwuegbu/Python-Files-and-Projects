def days_to_units(days, unit):
        if unit == "hrs":
            return f"Converted!\n{days} days has {days * 24} hours"
        elif unit == "mins":
             return f"Converted!\n{days} days has {days * 24 * 60} minutes"
        else:
             return "!error: unit can only be hrs / mins"

#function to ensure that entries are positive integers only! and execute the conversion    
def validate_and_exe(dict_days, dict_unit):
    try:
        number_of_days = int(dict_days)
        if number_of_days > 0:
            conversion = days_to_units(number_of_days, dict_unit)
            print(conversion)
        elif number_of_days == 0:
            print("!ERROR: days input cannot be zero")
        else:
             print("!ERROR: cannot resolve negative integer")
    except ValueError:
        print("!ERROR: days input can only be int")

user_input_message = "-Welcome to my converter.\n-Use 'end' to close the program.\n-Format: days to unit(hrs / mins)\n> "