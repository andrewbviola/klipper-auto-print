URL = "http://localhost/" # Default: http://localhost, set to the address of your drawing machine

grabGcode = "{}server/files/list?root=gcodes".format(URL)

# Set your schedule in 24 hour format ie 8:42 PM is "20:42"
# If it is set to "0", it will not run for that day
# Default is set to "1" to remind you to change them
# Edit Below 
Monday = "1"
Tuesday = "1"
Wednesday = "1"
Thursday = "1"
Friday = "1"
Saturday = "1"
Sunday = "1"

# Only one of these can be selected true. If multiple were to be selected,
# iteratedListPrint will take precedence, then memoryPrint and then trueRandom

iteratedListPrint = False # Print your g-code in order
memoryPrint = True # Print your g-code randomly, but the print won't be repeated
trueRandom = False # Print your g-code randomly

# Don't touch
startingIndex = 0
previousIndex = 0
