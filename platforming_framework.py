##TODO: More Configurable Jumping, Platform side-specific collision, spritesheets/animations, advanced win conditions

import pygame
from pygame import image

all_entities = pygame.sprite.Group()
platforms =  pygame.sprite.Group()
players = pygame.sprite.Group()
goals = pygame.sprite.Group()

class Entity(pygame.sprite.Sprite):

    #constructor: if a default position is supplied, entity will be placed there. else, it will be placed at 0,0
    def __init__(self, sprite, x , y):
        pygame.sprite.Sprite.__init__(self)

        self.sprite = sprite
        self.width, self.height = sprite.get_width(), sprite.get_height()
        self.hitbox = self.sprite.get_rect()
        self.hitbox = self.hitbox.move(x, y)

        self.rect = self.hitbox

        global all_entities
        all_entities.add(self)

        self.var_gravity = 9


    def go(self, x, y):
        #move around
        self.hitbox.move_ip(x, y)
        #keep entities inside screen
        self.hitbox.clamp_ip(pygame.display.get_surface().get_rect())

    def reset(self):
        #move back to reset position
        self.hitbox = self.sprite.get_rect().move(self.default_x, self.default_y)

    def gravity(self):
        #gravity
        self.hitbox.move_ip(0,self.var_gravity)
        #keep entities inside screen
        self.hitbox.clamp_ip(pygame.display.get_surface().get_rect())


    def refresh(self):
        #gravity
        self.gravity()
        #draw sprite
        window = pygame.display.get_surface()
        window.blit(self.sprite, (self.hitbox.x,self.hitbox.y))


class Player(Entity):
    __type__ = "player"

    isJumping = False
    jumpHeight = 10
    goal_reached = False

    def __init__(self, sprite, x = None, y = None):
        super().__init__(sprite, x, y)

        global players
        players.add(self)


    def refresh(self):

        if self.isJumping:
            if self.jumpHeight >= -10:
                self.go(0,-(self.jumpHeight*abs(self.jumpHeight)) * 0.5)
                self.jumpHeight -= 1
            else:
                self.jumpHeight = 10
                self.isJumping = False


        global platforms
        self.platform_list = pygame.sprite.spritecollide(self, platforms, False)
        if(self.platform_list):
            self.hitbox.bottom = self.platform_list[0].rect.top +1
            self.var_gravity = 0
        else:
            self.var_gravity = 9

        global goals
        self.goal_list = pygame.sprite.spritecollide(self, goals, False)
        if(self.goal_list):
            self.goal_reached = True

        #stop on reaching goal
        while self.goal_reached:
            window = pygame.display.get_surface()
            window_size = window.get_size()
            font = pygame.font.Font('freesansbold.ttf', 32)
            text = font.render('You Win!', True, pygame.Color(0, 255, 0), pygame.Color(0, 0, 255))
            text_rect = text.get_rect()
            text_rect.center = (window_size[0]/2, window_size[1]/2)
            window.blit(text, text_rect)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

        super().refresh()
    
    def jump(self):
        if self.isJumping == False:
            self.isJumping = True
    

class Platform(Entity):

    __type__ = "platform"

    # def __init__(self, sprite, x, y):
    #     super().__init__(sprite,x,y)
    #     self.var_gravity = 0

    #     global platforms
    #     platforms.add(self)        

    def __init__(self, color, x, y, w, h):
        platform = pygame.Surface((w, h))
        super().__init__(platform,x,y)
        platform.fill(color)
        self.var_gravity = 0

        global platforms
        platforms.add(self) 


    def refresh(self):
        super().refresh()


class Goal(Entity):

    __type__ = "goal"

    def __init__(self, color, x, y, w, h):
        goal = pygame.Surface((w,h))
        super().__init__(goal,x,y)
        goal.fill(color)
        self.var_gravity = 0

        global goals
        goals.add(self)

    def refresh(self):
        super().refresh()
