import datetime
x = datetime.datetime.now()
print(x.month)
print(x.strftime("%A"))     #   current day full
print(x.strftime("%B"))     #   current month full
print(x.strftime("%C"))     #   current date full
print(x.strftime("%D"))     #   m/d/Y
print(x.strftime("%F"))     #  Y-m-d
print(x.strftime("%G"))     #  Y
print(x.strftime("%H"))     #  hour (24 hr format)
print(x.strftime("%I"))     #  hour (12 hr format)
print(x.strftime("%M"))     #  end of month day
print(x.strftime("%R"))     #  HH:MM
print(x.strftime("%S"))     #  SS (seconds)
print(x.strftime("%T"))     #  HH:MM:SS
print(x.strftime("%U"))     #  Week number of year