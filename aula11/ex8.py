import pygame, sys

pygame.init()
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Clique do Mouse")
relogio = pygame.time.Clock()

fonte = pygame.font.Font(None, 40)
pos_texto = "Clique na tela!"

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.MOUSEBUTTONDOWN:
            pos_texto = f"Posição: {pygame.mouse.get_pos()}"

    tela.fill((20, 20, 20))
    texto = fonte.render(pos_texto, True, (255,255,255))
    tela.blit(texto, (20, 20))

    pygame.display.flip()
    relogio.tick(60)