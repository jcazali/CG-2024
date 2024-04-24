import sys
import pygame
import random

pygame.init()

# Configurações da tela
largura = 800
altura = 600

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Pygame")

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)
AMARELO = (255, 255, 0)
VERDE = (0, 255, 0)

tamanho_fonte = 50
fonte = pygame.font.SysFont(None, tamanho_fonte)

texto = fonte.render("DVD", True, BRANCO)

# Posicionamento do texto
texto_rect = texto.get_rect(center=(largura/2, altura/2)) 

clock = pygame.time.Clock() 

velocidade_x = random.randint(-1, 1)
velocidade_y = random.randint(-1, 1)

while velocidade_x == 0:
    velocidade_x = random.randint(-1, 1)
while velocidade_y == 0:
    velocidade_y = random.randint(-1, 1)

# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    texto_rect.x += velocidade_x
    texto_rect.y += velocidade_y

    if texto_rect.right >= largura:
        velocidade_x = random.randint(-1, 0)
        velocidade_y = random.randint(-1, 1)
        cor_texto = (
                    random.randint(0, 255),
                    random.randint(0, 255), 
                    random.randint(0, 255)
                    )
        texto = fonte.render("DVD", True, cor_texto)

    if texto_rect.bottom >= altura:
        velocidade_x = random.randint(-1, 1)
        velocidade_y = random.randint(-1, 0)
        cor_texto = (
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255)
                    )
        texto = fonte.render("DVD", True, cor_texto)

    if texto_rect.left <= 0:
        velocidade_x = random.randint(0, 1)
        velocidade_y = random.randint(-1, 1)
        cor_texto = (
                    random.randint(0, 255),
                    random.randint(0, 255), 
                    random.randint(0, 255)
                    )
        texto = fonte.render("DVD", True, cor_texto)

    if texto_rect.top <= 0:
        velocidade_x = random.randint(-1, 1)
        velocidade_y = random.randint(0, 1)
        cor_texto = (
                    random.randint(0, 255), 
                    random.randint(0, 255),
                    random.randint(0, 255)
                    )
        texto = fonte.render("DVD", True, cor_texto)

    clock.tick(180)
    tela.fill(PRETO)
    tela.blit(texto, texto_rect)
    pygame.display.flip()