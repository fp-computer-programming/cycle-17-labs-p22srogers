# Author: SMR (AMDG) 04/29/22
# Defining the Class
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

    
    def turn_on(self):
        self.on = True
    

    def turn_off(self):
        self.on = False
    

    def volume_up(self, value):
        self.volume_level += value
    

    def volume_down(self, value):
        self.volume_level -= value
    

    def channel_up(self, value):
        self.channel += value
    

    def channel_down(self, value):
        self.channel -= value
    
my_remote = tv_remote()
my_remote.on = True
my_remote.turn_on()
my_remote.turn_off()
my_remote.turn_on()
my_remote.volume_up(38)
my_remote.volume_up(64)
my_remote.channel_up(32)
my_remote.volume_down(63)
my_remote.channel_down(10)
my_remote.turn_off()
print(my_remote)