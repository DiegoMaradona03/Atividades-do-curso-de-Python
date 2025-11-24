import pygame, sys
pygame.init()

tela = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Desenhos no Pygame")

preto = (0, 0, 0)
vermelho = (255, 0, 0)
azul = (0, 0, 255)
verde = (0, 255, 0)

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    tela.fill(preto)

    pygame.draw.rect(tela, vermelho, (50, 50, 100, 60))
    pygame.draw.circle(tela, azul, (300, 200), 50)
    pygame.draw.line(tela, verde, (0, 0), (600, 400), 5)

    pygame.display.flip()