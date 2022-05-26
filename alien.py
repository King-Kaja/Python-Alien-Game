import pygame;
from pygame.sprite import Sprite;

class Alien(Sprite):

    """A class to represent a single alien in the fleet."""
    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__();
        self.screen = ai_game.screen;
        self.settings = ai_game.settings


        scale = 2.5;

        # Load the alien image and set its rect attribute.
        image = pygame.image.load('images/alienCrop.bmp');
        image = pygame.transform.scale(image, (image.get_width()/scale,image.get_height()/scale));
        
        self.image = image;
        self.rect = self.image.get_rect();

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width/scale;
        self.rect.y = self.rect.height/scale;

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x);

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect);

    def update(self):
        """Move the alien right or left."""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction);
        self.rect.x = self.x;


    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect();
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True;