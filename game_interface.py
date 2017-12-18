# this is the first screen shown, should be a game chooser
# tutorial here http://www.nebelhom.com/2013/08/14/create-a-simple-game-menu-with-pygame-pt-1-writing-the-menu-options-to-the-screen/
"""
this module is the game interface where you can choose which game to play
"""
import os
import sys
import pygame

pygame.init()


# make a menu item closs to recognize mouse clicks on target menu item
# inherits from parent class pygame.font.Font
class MenuItem(pygame.font.Font):
    """
    describes the behavior and placement of each item in the menu
    """
    def __init__(self, text, font=None, font_size=30, font_color=(255, 255, 255), xy=(0, 0)):
        #super(MenuItem, self).__init__()
        """
        set the desired font appearance of the menu items
        """
        # use parent __init__
        pygame.font.Font.__init__(self, font, font_size)
        self.text = text
        self.font_size = font_size
        self.font_color = font_color
        self.label = self.render(self.text, 1, self.font_color)
        self.width = self.label.get_rect().width
        self.height = self.label.get_rect().height
        self.x_pos, self.y_pos = xy
        self.position = xy

    def set_position(self, x, y):
        """
        location of the text, default to center
        """
        self.position = (x, y)
        self.x_pos = x
        self.y_pos = y

    def mouse_selection(self, xy):
        """
        behavior of item when mouse hovers or clicks
        """
        x_pos, y_pos = xy
        # are the mouse coords between the x and y borders of he menu item?
        if (x_pos >= self.x_pos and x_pos <= self.x_pos + self.width) \
                and (y_pos >= self.y_pos and y_pos <= self.y_pos + self.height):
            return True
        return False

    def mouse_select_font_color(self, rgb_tup):
        """
        changes the color of the hovered over text
        """
        # changes selected item text color
        self.font_color = rgb_tup
        self.label = self.render(self.text, 1, self.font_color)


# make a menu class, set a bunch of values to default
class GameMenu():
    """
    this is the menu itself
    """
    def __init__(self, screen, items, funcs, bg_color=(0, 0, 0), font=None, font_size=30,
                 font_color=(255, 255, 255)):
        """
        set up screen defaults
        """
        self.screen = screen
        # screen size is set down at the bottom in the create the screen section
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        self.bg_color = bg_color
        # clock sets the screen-updates per second
        self.clock = pygame.time.Clock()
        # making things pretty-maybe later
        self.font = pygame.font.SysFont(font, font_size)
        self.font_color = font_color
        self.items = []
        # these will be the open game trigger on click
        self.funcs = funcs

        # adding lists to the list of items
        # enumerate() The enumerate() function adds a counter to an iterable.
        # So for each element in cursor , a tuple is produced with (counter, element)
        for index, item in enumerate(items):
            menu_item = MenuItem(item)
            # th=total height of text block
            th = len(items) * menu_item.height
            # math to place each item at a different centered position on the screen
            x_pos = (self.screen_width / 2) - (menu_item.width / 2)
            y_pos = (self.screen_height / 2) - (th / 2) + (index * 2) + index * menu_item.height
            menu_item.set_position(x_pos, y_pos)
            self.items.append(menu_item)

    # instruction for how the screen should run and update, may add more events in here
    def run(self):
        """
        this method collects and interprets mous events and how the screen responds
        """
        mainloop = True
        while mainloop:
            # limit frame speed to 50 fps
            # this is how many times the screen is redrawn in a second
            self.clock.tick(50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainloop = False
                # is mouse button pressed
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # get the mouse position
                    mouse_pos = pygame.mouse.get_pos()
                    for item in self.items:
                        # if the mouse position is over our menu item
                        if item.mouse_selection(mouse_pos):
                            # exit the main loop and run the associated function
                            mainloop = False
                            self.funcs[item.text]()

            # redraw the background
            self.screen.fill(self.bg_color)

            for item in self.items:
                # this is what makes selected text change color
                if item.mouse_selection(pygame.mouse.get_pos()):
                    item.mouse_select_font_color((255, 0, 0))
                else:
                    item.mouse_select_font_color((255, 255, 255))
                self.screen.blit(item.label, item.position)

            pygame.display.flip()


# This section actually creates the Screen
if __name__ == '__main__':
    def gm_1():
        """
        opens game_1: maze game
        """
        os.system('python game_1.py')


    def gm_2():
        """
        opens game_2: triangle eats circle game
        """
        os.system('python game_2.py')

    def hs():
        """
        opens high score code
        """
        os.system('python high_score.py')

    funcs = {'Game 1': gm_1, 'Game 2': gm_2, 'High Score': hs, 'Quit': sys.exit}
    # Creating the screen, setting sizes
    screen = pygame.display.set_mode((640, 480), 0, 32)
    # menu_items gets passed to the GameMenu class as 'items'
    menu_items = ('Game 1', 'Game 2','High Score', 'Quit')
    # words on the screen header
    pygame.display.set_caption('Game Menu')
    # new instance of GameMenu
    gm = GameMenu(screen, funcs.keys(), funcs)
    gm.run()
