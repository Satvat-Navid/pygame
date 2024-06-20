import pygame.font
class button:
    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect
        #set dimention for the button
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0) 
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 0)
        #get the rect object of the button and center in
        self.rect = pygame.Rect(0, 0 ,self.width, self.height)
        self.rect.center = self.screen_rect.center
        #Button massage needs to be prepped only once
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """render the msg on the button and center it"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center