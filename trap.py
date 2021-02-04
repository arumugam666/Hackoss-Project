class trap:
    def __init__(self, x, y, z, slow_value):
        self.x = x
        self.y = y
        self.z = z
        self.slow_value = slow_value
    def check(self):
        if(player.x == self.x):
            print("the player stepped on the vortex!")
            print("the speed was decrease by " + str(self.slow_value))
            player.xspeed -= self.slow_value

class dummy:
    def __init__(self, xspeed, yspeed, zspeed):
        self.x = 0
        self.y = 0
        self.z = 0
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.zspeed = zspeed
    def walk(self):
        self.x += self.xspeed
        print("the player walk, current location: " + str(player.x))
        
vortex = trap(x = 6, y = 0, z = 0, slow_value = 1)
player = dummy(xspeed = 2, yspeed = 0, zspeed = 0)
print("player current position is " + str(player.x) + " and his speed is " + str(player.xspeed))

for steps in range(6):
    player.walk()
    vortex.check()