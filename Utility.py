import os.path
import pygame
main_directory = os.path.split(os.path.abspath(__file__))[0]
def load_image(file):
    file = os.path.join(main_directory, "Data", file)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit('Could not lot image')
    return surface.convert()
def load_images(*file_names):
    images = []
    for file_name in file_names:
        image = load_image(file_name)
        images.append(image)
    return images
class DummySound:
    def play(self):
        pass
def load_sound(file):
    