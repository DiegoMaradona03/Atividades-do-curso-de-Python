import pygame, sys, time, random

pygame.init()
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Quadrado Móvel")

relogio = pygame.time.Clock()
branco = (255, 255, 255)
vermelho = (255, 0, 0)

x, y = 100, 100
vel = 7

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_a]:
        x -= vel
    if teclas[pygame.K_d]:
        x += vel
    if teclas[pygame.K_w]:
        y -= vel
    if teclas[pygame.K_s]:
        y += vel

    tela.fill(branco)
    pygame.draw.rect(tela, vermelho, (x, y, 60, 60))

    pygame.display.flip()
    relogio.tick(60)