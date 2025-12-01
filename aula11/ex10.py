import pygame, sys, random

pygame.init()
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Jogo do Quadrado Vermelho")
relogio = pygame.time.Clock()

fonte = pygame.font.Font(None, 50)

jogador = pygame.Rect(380, 280, 50, 50)
alvo = pygame.Rect(random.randint(0, 750), random.randint(0, 550), 50, 50)

vel = 7
pontos = 0
preto = (0, 0, 0)
vermelho = (255, 0, 0)
azul = (0, 100, 255)
branco = (255, 255, 255)

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and jogador.x > 0: jogador.x -= vel
    if teclas[pygame.K_RIGHT] and jogador.x < 750: jogador.x += vel
    if teclas[pygame.K_UP] and jogador.y > 0: jogador.y -= vel
    if teclas[pygame.K_DOWN] and jogador.y < 550: jogador.y += vel

    if jogador.colliderect(alvo):
        pontos += 1
        alvo.x = random.randint(0, 750)
        alvo.y = random.randint(0, 550)

    tela.fill(branco)
    pygame.draw.rect(tela, vermelho, jogador)
    pygame.draw.rect(tela, azul, alvo)

    texto = fonte.render(f"Pontos: {pontos}", True, preto)
    tela.blit(texto, (10, 10))

    pygame.display.flip()
    relogio.tick(60)