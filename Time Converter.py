h = int(input('Enter Hours: '))
if h>12:
    print ('Enter hours between 0-12')
    exit()
m = int(input('Enter Minutes: '))
if m>59:
    print ('Enter minutes between 0-59')
    exit()
t = int(input(' Press 1 for AM: \n Press 2 for PM: \n'))

if t == 1:
    if m <= 59:
        if h <= 12:
            print ('Time is :\t',h,':',m,':00')
elif t == 2:
    if m <= 59:
        if h == 0:
            print ('Time is :\t12:',m,':00')
        elif h == 1:
            print ('Time is :\t13:',m,':00')
        elif h == 2:
            print ('Time is :\t14:',m,':00')
        elif h == 3:
            print ('Time is :\t15:',m,':00')
        elif h == 4:
            print ('Time is :\t16:',m,':00')
        elif h == 5:
            print ('Time is :\t17:',m,':00')
        elif h == 6:
            print ('Time is :\t18:',m,':00')
        elif h == 7:
            print ('Time is :\t19:',m,':00')
        elif h == 8:
            print ('Time is :\t20:',m,':00')
        elif h == 9:
            print ('Time is :\t21:',m,':00')
        elif h == 10:
            print ('Time is :\t22:',m,':00')
        elif h == 11:
            print ('Time is :\t23:',m,':00')
        elif h == 12:
            print ('Time is :\t24:',m,':00')
else:
    print ('Enter te correct option')

# if x[-2:] == "AM" and x[:2] == "12":
#         return "00" + x[2:-2]
#     elif x[-2:] == "AM":
#         return x[:-2]
#     elif x[-2:] == "PM" and x[:2] == "12":
#         return x[:-2]
#     else:
#         return str(int(x[:2]) + 12) + x[2:8]


# # import datetime
# # def time24(str1):
# #     if str1[-2:] == "AM" and str1[:2] == "12":
# #         return "00" + str1[2:-2]
# #     elif str1[-2:] == "AM":
# #         return str1[:-2]
# #     elif str1[-2:] == "PM" and str1[:2] == "12":
# #         return str1[:-2]
# #     else:
# #         return str(int(str1[:2]) + 12) + str1[2:8]
# # dt = datetime.datetime.now()
# # print("Conversion Of Time ::",time24(dt.strftime("%H:%M:%S")))




# # def time24(str1): 
# #     if str1[-2:] == "AM" and str1[:2] == "12": 
# #         return "00" + str1[2:-2] 
# #     elif str1[-2:] == "AM": 
# #         return str1[:-2] 
# #     elif str1[-2:] == "PM" and str1[:2] == "12": 
# #         return str1[:-2] 
# #     else: 
# #         return str(int(str1[:2]) + 12) + str1[2:8] 

# # #hh = int(input('Enter Hours: '))
# # #mm = int(input('Enter Minutes: '))
# # #tt = str(input('Enter AM/PM:  '))

# # print(time24('04:12:48PM')) 