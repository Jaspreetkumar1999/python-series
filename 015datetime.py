import datetime

# # d = datetime.datetime(2016,5,3,12,15,30)
# #year, month,date,timehr,min,sec
# # print(d)
# # today =datetime.date.today()
# # to get todays date
# # print(today)
# # print(today.year)
# # print(today.day)
# # to get only year
# # print(today.weekday())
# #for week day monday =0 and sunday =6
# # print(today.isoweekday())
# # for isoweekday monday =1 and sunday =7
# # tdelta = datetime.timedelta(days=7)
# # timedelta function is used to print the time difference bw selective dayes
# # tdelta = datetime.timedelta(days=100)
# # print(today + tdelta)
# #-------------date2 = date1 +- timedelta
# #-------------timedelta = date1 +-date2
# bday = datetime.date(2020,11,13)
# #it never accept day and month as 02,04 etc format it always accept it in the form of 2,4,
# till_bday = bday-today
# # print(till_bday)
# # print(till_bday.days)
# # print(till_bday.total_seconds())
# t = datetime.time(7,45,32,100000)
# whenever we are working with date time we are working on the year month and days but in time we are going
# to work on hours minutes and seconds microseconds

# print(t)
# t = datetime.datetime(2020,12,4,7,45,32,100000)
# both date and time
# print(t)
# print(t.year)
# print(t.time())
# tdelta = datetime.timedelta(days= 7)
# tdelta = datetime.timedelta(hours= 7)

# print(t +tdelta)
# dt_today = datetime.datetime.today()
# #curent time zone
# dt_now = datetime.datetime.now()
# #current time zone with option
# dt_utcnow = datetime.datetime.utcnow()
#
# #current utctime
# print(dt_today)
#
# print(dt_utcnow)
# print(dt_now)
#--------------------pytz package is recommended while using the timezone function------
import pytz
# dt = datetime.datetime(2015,3,5,14,54,45, tzinfo=pytz.utc)
# whenever you using pytz always use utc
# print(dt)
dt1 = datetime.datetime.now(tz =pytz.utc)
# dt2 = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)
print(dt1)
# print(dt2)
dt_mtn = dt1.astimezone(pytz.timezone('Asia/kolkata'))
# # it will show indian timezone
#
print(dt_mtn)
# for tz in pytz.all_timezones:  --------------timezone list
#     print(tz)
#=======naive time  means which donnt have time zone
