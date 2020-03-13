import globe
import math
import pygame
pygame.init()


class Arm:
    def __init__(self, anchor, touch, length):
        # The position of the shoulder (Where the arm is connected and anchored)
        self.anchor_point = anchor
        # The point towards which the arm is trying to reach
        self.touch = touch
        # Length of each arm piece
        self.length = length

        # Variables the are used in the calculation
        self.joint_point = None
        self.point_test = None
        self.angle_test = None

    def update_touch(self, point):
        self.touch = point

    def draw(self, screen):
        self.calculate()

        self.joint_point = (int(self.joint_point[0]), int(self.joint_point[1]))
        self.touch = (int(self.touch[0]), int(self.touch[1]))
        self.point_test = (int(self.point_test[0]), int(self.point_test[1]))

        # ARM SKELETON FOR DEBUG
        pygame.draw.line(screen, (255, 255, 255), self.anchor_point, self.joint_point, 3)
        pygame.draw.line(screen, (255, 255, 255), self.joint_point, self.touch, 3)

        #pygame.draw.circle(screen, (50, 255, 50), self.anchor_point, 10, 3)
        #pygame.draw.circle(screen, (255, 50, 50), self.joint_point, 10, 3)
        pygame.draw.circle(screen, (255, 255, 255), self.touch, 10, 3)

        #pygame.draw.circle(screen, (50, 50, 255), self.point_test, 10, 3)

    def calculate(self):
        # Assumes that the distance between anchor point and touch destination is the hypotenuse of a triange
        # Calculates hypotenuse, adjacent side, and opposite side
        hyp = globe.distance(self.anchor_point, self.touch)
        adj = self.touch[0] - self.anchor_point[0]
        opp = self.touch[1] - self.anchor_point[1]
        # Checks if the destination is farther than the arms could reach
        if self.length * 2 < hyp:
            # Finds the closest point the arm can reach on the line towards the destination using triangle similarity
            new_y = (opp * (2 * self.length)) / hyp
            new_x = (adj * (2 * self.length)) / hyp
            # Sets destination to the new location
            self.touch = (self.anchor_point[0] + new_x, self.anchor_point[1] + new_y)

        # Recalculates triangle stuff
        hyp = round(globe.distance(self.anchor_point, self.touch), 2)
        if hyp == 0:
            hyp = 0.01
        adj = self.touch[0] - self.anchor_point[0]
        opp = self.touch[1] - self.anchor_point[1]

        # Finds the joint point not regarding the fact that the arm triangle may be at an angle
        if self.touch[0] < self.anchor_point[0]:
            point = (self.anchor_point[0] + (hyp / 2), self.anchor_point[1] - (math.sqrt((self.length ** 2) - ((hyp / 2) ** 2))))
        else:
            point = (self.anchor_point[0] + (hyp / 2), self.anchor_point[1] + (math.sqrt((self.length ** 2) - ((hyp / 2) ** 2))))

        # Finds the angle by which that point has to be rotated
        angle = math.acos(adj/hyp)
        # Accounts for the glitch when the touch point is below anchor
        if self.touch[1] > self.anchor_point[1]:
            angle = (math.pi - angle) + math.pi

        # Calculates the rotated final coordinates
        shift_x = point[0] - self.anchor_point[0]
        shift_y = point[1] - self.anchor_point[1]

        rotated_point = (shift_y * math.sin(angle) + shift_x * math.cos(angle),
                         shift_y * math.cos(angle) - shift_x * math.sin(angle))

        self.point_test = point

        self.angle_test = angle

        self.joint_point = (rotated_point[0] + self.anchor_point[0],
                            rotated_point[1] + self.anchor_point[1])
