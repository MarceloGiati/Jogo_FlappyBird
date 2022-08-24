import pygame 
import os
import random

TELA_LARGURA = 500
TELA_AUTURA = 800

IMAGEM_CANO = pygame.trasform.scale2x(pygame.image.load(os.path.join('Imgs', 'pipe.png')))
IMAGEM_CHAO = pygame.trasform.scale2x(pygame.image.load(os.path.join('Imgs', 'base.png')))
IMAGEM_BACKGROUND = pygame.trasform.scale2x(pygame.image.load(os.path.join('Imgs', 'bg.png')))
IMAGENS_PASSARO = [
    pygame.trasform.scale2x(pygame.image.load(os.path.join('Imgs', 'bird1.png'))),
    pygame.trasform.scale2x(pygame.image.load(os.path.join('Imgs', 'bird2.png'))),
    pygame.trasform.scale2x(pygame.image.load(os.path.join('Imgs', 'bird3.png'))),
]

pygam.font.init()
FONTE_PONTOS = pygam.font.SysFont('arial', 50)
