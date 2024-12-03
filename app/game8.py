import calendar

year = int(input("Введите год:"))
month = int(input("Введите месяц (1-12):"))

cal = calendar.TextCalendar(calendar.MONDAY)
month_calendar = cal.formatmonth((year, month))

print(month_calendar)