import time,  helpers

if helpers.checkSchedule():
    quit()

while True:
    x = time.localtime()
    current_time = time.strftime("%H:%M", x)
    current_day = helpers.whatDay()
    current_minutes = helpers.time2min(current_time)
    day_of_schedule = helpers.searchForDay()
    next_schedule = helpers.time2min(helpers.whatTime(day_of_schedule))
    sleep = helpers.calculateSleep(current_day, day_of_schedule)
    print("Your next print wil occur in {} minutes".format(sleep))
    time.sleep(sleep*60)
    print("Starting your print...")
    helpers.choosePrintType()
    time.sleep(60)
