import pygame
pygame.init()

# Carregar som
pygame.mixer.music.load('trilha.mp3')
pygame.mixer.music.play(-1)  # Toca em loop

som_efeito = pygame.mixer.Sound('pulo.wav')
som_efeito.play()