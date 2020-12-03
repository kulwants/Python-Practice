import datetime
import os

date = int(input('Enter Date (DD) : '))
month = int(input('Enter Month (MM) : '))
year = int(input('Enter Year (YYYY) : '))

if date > 31:
    print('Enter Date is Not Valid.')
elif date == 0:
    print('Date cannot be 0')
else:
    pass

if month > 12:
    print ('Invalid Month Input.')
elif month == 1:
    if date <= 31:
        print (date, 'January', year)
elif month == 2:
    if date <= 28 or date <= 29:
        print (date, 'February',  year)
elif month == 3:
    if date <= 31:
        print (date, 'March', year)
elif month == 4:
    if date <= 30:
        print (date, 'April', year)
elif month == 5:
    if date <= 31:
        print (date, 'May', year)
elif month == 6:
    if date <= 30:
        print (date, 'June', year)
elif month == 7:
    if date <= 31:
        print (date, 'July', year)
elif month == 8:
    if date <= 31:
        print (date, 'August', year)
elif month == 9:
    if date <= 30:
        print (date, 'September', year)
elif month == 10:
    if date <= 31:
        print (date, 'October', year)
elif month == 11:
    if date <= 30:
        print (date, 'November', year)
elif month == 12:
    if date <= 31:
        print (date, 'December', year)

os.system('powershell.exe (Get-Date -Year {} -Month {} -Day {}).DayOfWeek',year,month,date)

weekday = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
day_of_week = datetime.date(year, month, date)
week = day_of_week.weekday()
x = int(print(week))
y = int(x)
print (weekday[y])























# dd = input('Enter Date (DD) : ')
# if dd > '31':
#     print('Entered Date is Invalid.')
#     exit()
    
# mm = input('Enter Month (MM) : ')
# #mm = int(input(' Press 1 for January \n Press 2 for February \n Press 3 for March \n Press 4 for April \n Press 5 for May \n Press 6 for June \n Press 7 for July \n Press 8 for August \n Press 9 for September \n Press 10 for October \n Press 11 for November \n Press 12 for December \n'))

# # if mm == 2:
# #     if dd > '28' or dd > '29':
# #         print('Entered Data is Incorrect.')
# #         exit()
# #     else:
# #         print('February')
# # if mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12:
# #     if dd > '31':
# #         print('Entered Data is Incorrect.')
# #         exit()
# #     else:
# #         print('Month')
# # if mm == 4 or mm == 6 or mm == 9 or mm == 11:
# #     if dd > '30':
# #         print('Entered Data is Incorrect.')
# #         exit()
# #     else:
# #         print('Month')

# yy = input('Enter Year (YYYY) : ')


# if mm > '12':
#     print('Month is Invalid.')
#     exit
# elif mm == 1:
#     if dd <= '31':
#         print (dd, 'January', yy)
# elif mm == 2:
#     if dd <= '28' or dd <= '29':
#         print (dd, 'February',  yy)
# elif mm == 3:
#     if dd <= '31':
#         print (dd, 'March', yy)
# elif mm == 4:
#     if dd <= '30':
#         print (dd, 'April', yy)
# elif mm == 5:
#     if dd <= '31':
#         print (dd, 'May', yy)
# elif mm == 6:
#     if dd <= '30':
#         print (dd, 'June', yy)
# elif mm == 7:
#     if dd <= '31':
#         print (dd, 'July', yy)
# elif mm == 8:
#     if dd <= '31':
#         print (dd, 'August', yy)
# elif mm == 9:
#     if dd <= '30':
#         print (dd, 'September', yy)
# elif mm == 10:
#     if dd <= '31':
#         print (dd, 'October', yy)
# elif mm == 11:
#     if dd <= '30':
#         print (dd, 'November', yy)
# elif mm == 12:
#     if dd <= '31':
#         print (dd, 'December', yy)
# else:
#     print ('Enter the correct option')



# print('Input DD / MM / YYYY is : ', dd,'/',mm,'/',yy)
