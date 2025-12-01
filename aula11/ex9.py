import pygame, sys

pygame.init()
pygame.mixer.init()

tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Som no Espaço")
relogio = pygame.time.Clock()

som = pygame.mixer.Sound("aula11/som.wav")

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
            som.play()

    tela.fill((50,50,50))
    pygame.display.flip()
    relogio.tick(60)