import pygame, sys

pygame.init()
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Colisão de Retângulos")
relogio = pygame.time.Clock()

fonte = pygame.font.Font(None, 48)

jogador = pygame.Rect(100, 100, 50, 50)
alvo = pygame.Rect(400, 300, 50, 50)

vel = 7
branco = (255, 255, 255)
azul = (0, 120, 255)
vermelho = (255, 0, 0)

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]: jogador.x -= vel
    if teclas[pygame.K_RIGHT]: jogador.x += vel
    if teclas[pygame.K_UP]: jogador.y -= vel
    if teclas[pygame.K_DOWN]: jogador.y += vel

    tela.fill(branco)
    pygame.draw.rect(tela, vermelho, jogador)
    pygame.draw.rect(tela, azul, alvo)

    if jogador.colliderect(alvo):
        msg = fonte.render("COLIDIU!", True, (0, 0, 0))
        tela.blit(msg, (315, 50))

    pygame.display.flip()
    relogio.tick(60)