from datetime import datetime


def deadline_counter():
        if days_left > 2:
            return f"User, the time left to achieve your {goal} goal is {days_left} days"
        else:
              return f"User, the time left to achieve your {goal} goal is {hours_left} hours"

def validate_deadline_date():
    if deadline_date > today_date:
        print(deadline_counter())
    else:
        print(f"User, your deadline day must be AT LEAST a day after today: {today}")


user_input = input("Enter your goal and deadline seperated by a colon \ngoal:d.m.y> ")
input_list = user_input.split(":")
goal = input_list[0]
deadline = input_list[1]
deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.today()
today = today_date.date()
days = deadline_date - today_date
days_left = days.days
hours_left = int(days.total_seconds()/60/60)
validate_deadline_date()