URL = "http://localhost/" # Default: http://localhost, adjust if connection issues occur

grabGcode = "{}server/files/list?root=gcodes".format(URL)

# Set your schedule in 24 hour format ie 8:42 PM is 20:42 - Edit these!
Monday = 
Tuesday = 
Wednesday = 
Thursday = 
Friday = 
Saturday = 
Sunday = 

# Only one of these can be selected true. If multiple were to be selected,
# iteratedListPrint will take precedence, then memoryPrint and then trueRandom

iteratedListPrint = False # Print your g-code in order
memoryPrint = True # Print your g-code randomly, but the print won't be repeated
trueRandom = False # Print your g-code randomly

# Don't touch
startingIndex = 0
previousIndex = 0
