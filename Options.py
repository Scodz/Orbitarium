'''
    Options are added and controlled here.
'''

def getsettings(SettingsWanted):
    with open('Settings.txt', 'r') as file:
        lines = file.readlines()
        PossibleSettings = {1 : lines[2], #Resolution 
                            }
        return PossibleSettings[SettingsWanted]


class OptionsMenu:
    def __init__(self, pygame):
        self.pygame = pygame
        self.screen = self.pygame.display.set_mode(getsettings(1))
        self.pygame.display.set_caption('Options Menu')
        self.clock = self.pygame.time.Clock()
        self.running = True

    def OptionsMenu(self):
        while self.running:
            for event in self.pygame.event.get():
                if event.type == self.pygame.QUIT:
                    self.running = False
            
            self.screen.fill((0, 0, 0))
            self.pygame.display.flip()
            self.clock.tick(60)

        self.pygame.quit()