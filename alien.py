import pygame;
from pygame.sprite import Sprite;

class Alien(Sprite):

    """A class to represent a single alien in the fleet."""
    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__();
        self.screen = ai_game.screen;

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