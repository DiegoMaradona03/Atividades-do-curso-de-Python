import pygame, sys

pygame.init()
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Animação")
relogio = pygame.time.Clock()

x, y = 100, 100
vel_x, vel_y = 5, 5
raio = 30
preto = (0, 0, 0)
verde = (0, 255, 0)

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    x += vel_x
    y += vel_y

    if x - raio <= 0 or x + raio >= 800: vel_x *= -1
    if y - raio <= 0 or y + raio >= 600: vel_y *= -1

    tela.fill(preto)
    pygame.draw.circle(tela, verde, (x, y), raio)

    pygame.display.flip()
    relogio.tick(60)