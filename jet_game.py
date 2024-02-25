import pygame
import random

pygame.init()
HEIGHT = 600
WIDTH = 800
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHTBLUE = (115, 215, 255)
BROWN = (123, 63, 0)
YELLOW = (255, 255, 0)
GRASSGREEN = (34, 139, 34)
sc = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("example")
clock = pygame.time.Clock()
score = 0
trigger = True


def gettext(message, color, x, y, size):
    font = pygame.font.SysFont("Impact", size)
    text = font.render(message, True, color)
    place = text.get_rect(center=(x, y))
    sc.blit(text, place)


def gameover():
    global trigger
    sc.fill(RED)
    gettext("GAME OVER", LIGHTBLUE, WIDTH // 2, HEIGHT // 2, 96)
    for g in allsprites:
        g.kill()
    pygame.display.flip()
    playing = True
    while playing:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                playing = False
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_RETURN and not trigger:
                    trigger = True
                    #player = Player()
                    player.rect.left = 0
                    player.rect.centery = HEIGHT // 2
                    draw()
                    return
    pygame.quit()
    exit()


def draw():
    global score, trigger
    if player.update():
        score += 1
    asteroids.update()
    sc.blit(bg, (0, 0))
    for entity in allsprites:
        sc.blit(entity.surf, entity.rect)
    sc.blit(player.surf, player.rect)
    gettext(f"SCORE: {score}", WHITE, WIDTH // 2, 30, 40)

    if player.rect.right < WIDTH and pygame.sprite.spritecollideany(player, asteroids):
        for i in asteroids:
            i.kill()
        player.kill()

        trigger = False
        score = 0

        gameover()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Jet_Game_Images/jetfighter.png").convert_alpha()
        self.surf = pygame.transform.scale(self.image, (50, 40))
        self.rect = self.surf.get_rect(center = (25, HEIGHT // 2))


    def update(self):
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.move_ip(0, -5)
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.move_ip(0, 5)
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5, 0)
        if self.rect.left > WIDTH:
            self.rect.left = 0
            self.rect.y = HEIGHT // 2
            return 1




class Asteroids(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image1 = pygame.image.load("Jet_Game_Images/asteroid_1.png").convert_alpha()
        self.image2 = pygame.image.load("Jet_Game_Images/asteroid_2.png").convert_alpha()
        self.image = random.choice((self.image1, self.image2))
        self.surf = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.surf.get_rect(center=(random.randint(WIDTH + 20, WIDTH + 100), random.randint(0, HEIGHT)))
        self.speed = random.randint(5, 12)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


Add_asteroids = pygame.USEREVENT + 1
pygame.time.set_timer(Add_asteroids, 500)
player = Player()
allsprites = pygame.sprite.Group()
#allsprites.add(player)
asteroids = pygame.sprite.Group()
bg = pygame.image.load("Jet_Game_Images/BGSpace.png").convert()
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

play = True
while play:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == Add_asteroids:
            asteroid = Asteroids()
            allsprites.add(asteroid)
            asteroids.add(asteroid)
    keys = pygame.key.get_pressed()
    draw()
    pygame.display.flip()
pygame.quit()

# restartgame ; find images (asteroids, bg)
