# Author: SMR (AMDG) 04/29/22
# Defining the class
class tv_remote:

    # Default Values for the tv (channel, volume, and power) 
    def __init__(self, channel=0, volume_level=0, on=False):
        self.channel = channel
        self.volume_level = volume_level
        self.on = on
    # Function that tells user what channel and volume they are on. If not, TV is powered off.    
    def __str__(self):
        if self.on == True:
            return "You are watching on channel {0} at {1}% volume.".format(self.channel, self.volume_level)
        else:
            return "The TV is powered off."

# final calling of the function
my_remote = tv_remote()
my_remote.on = True
print(my_remote)