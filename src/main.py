import sys, pygame


def main():
    pygame.init()

    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Pong Pygame')

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()


if __name__ == '__main__':
    main()
