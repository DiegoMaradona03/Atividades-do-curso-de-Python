import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Define tamanho da tela
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Meu Primeiro Jogo")

# Define cor de fundo (RGB)
branco = (255, 255, 255)

# Loop principal do jogo
while True:
    # Verifica eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Preenche a tela
    tela.fill(branco)

    # Atualiza a tela
    pygame.display.flip()