import pygame, sys

pygame.init()
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Movimento com Limite")

relogio = pygame.time.Clock()
preto = (0,0,0)
vermelho = (255, 0, 0)

x, y = 100, 100
vel = 7
larg, alt = 60, 60

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_a] and x > 0:
        x -= vel
    if teclas[pygame.K_d] and x < 800 - larg:
        x += vel
    if teclas[pygame.K_w] and y > 0:
        y -= vel
    if teclas[pygame.K_s] and y < 600 - alt:
        y += vel

    tela.fill(preto)
    pygame.draw.rect(tela, vermelho, (x, y, larg, alt))

    pygame.display.flip()
    relogio.tick(60)