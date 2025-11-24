import pygame, sys

pygame.init()
tela = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Movimento com o Teclado")

preto = (0, 0, 0)
branco = (255, 255, 255)
x, y = 300, 200
velocidade = 5

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        x -= velocidade
    if teclas[pygame.K_RIGHT]:
        x += velocidade
    if teclas[pygame.K_UP]:
        y -= velocidade
    if teclas[pygame.K_DOWN]:
        y += velocidade

    tela.fill(preto)
    pygame.draw.rect(tela, branco, (x, y, 50, 50))
    pygame.display.flip()