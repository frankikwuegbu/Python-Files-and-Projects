from converter import validate_and_exe, user_input_message

days_and_unit = ""

while days_and_unit != "end":
    days_and_unit = input(user_input_message)
    days_unit_list = days_and_unit.split(" to ")
    # print(days_unit_list)
    days_unit_dict = {"days": days_unit_list[0], "unit": days_unit_list[1]}
    dict_days = days_unit_dict["days"]
    dict_unit = days_unit_dict["unit"]
    validate_and_exe(dict_days, dict_unit)