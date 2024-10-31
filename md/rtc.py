import uasyncio as asyncio
from machine import RTC


## NEED TO CHANGE FOR OTHER HOUSE
     #_1 =
async def current_rtc(var):
    while True:
     print("RTC___________________________________IS RUNNIGN")
     rtc = RTC()
     year, month, day, week, hour, minute, second, *_ = rtc.datetime()
     # print("this is in rtc module:-",year,":", month,":", day,":", week,":", hour,":", minute,":", second)

     var.c_hour_1 = hour
     var.c_min_1 = minute
     print(f'H:{hour} M:{minute}')
     await asyncio.sleep(1)

