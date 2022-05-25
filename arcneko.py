import pygame
class Arcneko:
    """A class to manage Arc Neko."""
    def __init__(self, ai_game):
        """Initialize Arc Neko and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the Arc Neko image and get its rect.
        image = pygame.image.load('images/arcneko.bmp')
        image = pygame.transform.scale(image, (image.get_width()/2,image.get_height()/2))
        self.image = image
        self.rect = self.image.get_rect()

        # Start each arc neko at the center of the screen.
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw Arc Neko at its current location."""
        self.screen.blit(self.image, self.rect)