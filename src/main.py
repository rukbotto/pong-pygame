import os, sys, pygame


class Pad(pygame.sprite.Sprite):
    def __init__(self, pos=(0, 0)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((12, 30)).convert()
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center=pos)
        self.max_speed = 5
        self.speed = 0

    def move_up(self):
        self.speed = self.max_speed * -1

    def move_down(self):
        self.speed = self.max_speed * 1

    def stop(self):
        self.speed = 0

    def update(self):
        self.rect.move_ip(0, self.speed)


def main():
    pygame.init()

    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Pong Pygame')

    try:
        filename = os.path.join(
            os.path.dirname(__file__),
            'assets',
            'graphics',
            'background.png')
        background = pygame.image.load(filename)
        background = background.convert()
    except pygame.error as e:
        print ('Cannot load image: ', filename)
        raise SystemExit(str(e))

    pad_left = Pad((width/6, height/4))
    pad_right = Pad((5*width/6, 3*height/4))

    sprites = pygame.sprite.Group(pad_left, pad_right)

    clock = pygame.time.Clock()
    fps = 60

    pygame.key.set_repeat(1, 1000/fps)

    while 1:
        clock.tick(fps)

        pad_left.stop()
        pad_right.stop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                pad_left.move_up()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                pad_left.move_down()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                pad_right.move_up()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                pad_right.move_down()

        sprites.update()

        screen.blit(background, (0, 0))
        sprites.draw(screen)
        pygame.display.flip()


if __name__ == '__main__':
    main()
