from hashlib import blake2b
from sqlite3 import IntegrityError
import string
from tokenize import Number, String


name = "Blake"
country = "U.S."
age = 23
hourly_wage = 19
satisifed = False
daily_wage = (hourly_wage * 8)
print(name + " lives in " + country)
print(name+" is "+str(age)+" years old.")
print(f"He makes {daily_wage} per day.")
print("Are you satisfied with your current wage?" + " " +str(satisifed))
