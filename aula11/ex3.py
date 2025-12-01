import pygame, sys

pygame.init()
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Desenhando Formas")

preto = (0, 0, 0)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    tela.fill(preto)

    pygame.draw.rect(tela, vermelho, (50, 50, 100, 60))
    pygame.draw.circle(tela, azul, (400, 300), 60)
    pygame.draw.line(tela, verde, (0, 0), (800, 600), 5)

    pygame.display.flip()