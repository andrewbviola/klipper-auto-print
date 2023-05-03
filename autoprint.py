import time,  helpers

x = time.localtime()
current_time = time.strftime("%H:%M", x)
current_day = helpers.whatDay()

current_minutes = helpers.time2min(current_time)
current_schedule = helpers.time2min(helpers.whatTime(current_day))
next_day = helpers.nextDay()
new_day = False

if current_schedule < current_minutes:
    new_day = True
    current_schedule = helpers.time2min(helpers.whatTime(next_day))

if new_day == True:
    sleep_time = ((1440-current_minutes) + current_schedule)
else:
    sleep_time = (current_schedule - current_minutes)

while True:
    print("Your next print will occur in {} minutes".format(sleep_time))
    time.sleep(sleep_time*60)
    print("Starting your print...")
    helpers.choosePrintType()
    current_minutes = helpers.time2min(current_time)
    next_day = helpers.nextDay()
    current_schedule = helpers.time2min(helpers.whatTime(next_day))
    sleep_time = ((1440-current_minutes) + current_schedule)