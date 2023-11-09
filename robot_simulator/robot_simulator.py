# Globals for the directions
# Change the values as you see fit
EAST  = 'EAST'   # восток
NORTH = 'NORTH'  # север
WEST  = 'WEST'   # запад
SOUTH = 'SOUTH'  # юг


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.coordinates = (self.x_pos, self.y_pos)


    def move(self, stro):

        for i in stro:
            if i == 'L':
                if self.direction == 'NORTH':
                    self.direction = 'WEST'

                elif self.direction == 'WEST':
                    self.direction = 'SOUTH'

                elif self.direction == 'SOUTH':
                    self.direction = 'EAST'

                elif self.direction == 'EAST':
                    self.direction = 'NORTH'
                
                
            elif i == 'R':
                if self.direction == 'NORTH':
                    self.direction = 'EAST'

                elif self.direction == 'EAST':
                    self.direction = 'SOUTH'

                elif self.direction == 'SOUTH':
                    self.direction = 'WEST'

                elif self.direction == 'WEST':
                    self.direction = 'NORTH'
                    
                    
            elif i == 'A':
                if self.direction == 'NORTH':
                    self.y_pos += 1

                if self.direction == 'SOUTH':
                    self.y_pos -= 1

                if self.direction == 'EAST':
                    self.x_pos += 1

                if self.direction == 'WEST':
                    self.x_pos -= 1

        self.coordinates = (self.x_pos, self.y_pos)


# проверка кода - 
# rob = Robot(WEST, 0, 0)

# rob.move('LAA')

# print(rob.coordinates)
# print(rob.direction)





