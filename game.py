import globe, arm, pygame


class game:
    def __init__(self):
        self.rightArm = arm.Arm((450, 300), pygame.mouse.get_pos(), 100)
        self.leftArm = arm.Arm((350, 300), pygame.mouse.get_pos(), 100)

        # Stores the velocity at which the arms are lifting
        self.velocity = 0

        # Height lifted in pixels
        self.height = self.rightArm.anchor_point[1]

    def run_game(self, screen):
        self.update()
        self.draw(screen)

    def draw(self, screen):
        # Calls arm draw functions
        self.rightArm.draw(screen)
        self.leftArm.draw(screen)

        # Draws barbell bar
        screen.blit(globe.barbell_bar_image, ((globe.SCREEN_SIZE[0] / 2) - (globe.barbell_bar_image.get_width() / 2),
                                              self.rightArm.touch[1] - 5))

    def update(self):
        # Tests for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                globe.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    self.velocity -= .03
                elif event.button == 5:
                    self.velocity += .03

        # Updates arm touch positions according height
        if pygame.mouse.get_pos()[1] < self.rightArm.anchor_point[1]:
            self.rightArm.update_touch((self.rightArm.anchor_point[0] + globe.BARBELL_GRAB_SHIFT, self.height))

            self.leftArm.update_touch((self.leftArm.anchor_point[0] - globe.BARBELL_GRAB_SHIFT, self.height))

        # Updates velocity
        if self.height > self.rightArm.anchor_point[1] - (self.rightArm.length * 2):
            self.velocity += .001
        else:
            self.velocity += .01

        # Updates height
        self.height += self.velocity
        # Prevents arm from going too low
        if self.height > self.rightArm.anchor_point[1]:
            self.height = self.rightArm.anchor_point[1]
            self.velocity = 0
