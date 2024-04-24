import pygame
import sys

pygame.init()

PRETO = (0,0,0)
BRANCO = (255,255,255)

#Define o tamanho da tela do jogo
largura = 800
altura = 600

#Cria a tela com os parâmetros pré-definodos
screen = pygame.display.set_mode((largura,altura)) 
#Nomeia a tela
pygame.display.set_caption("Pong") 

#Define o tamanho da raquete
raquete_largura = 10
raquete_altura = 60
tamanho_bola = 20

#Define a posição da raquete do pc - centralizada a esquerda
pc_x = 10
pc_y = altura // 2 - raquete_altura // 2

#Define a posição da raquete do player 1 - centralizada a direita
player_1_x = largura - 20
player_1_y = altura // 2 - raquete_altura // 2

#Define a posição da bola - centralizada 
bola_x = largura // 2 - tamanho_bola // 2
bola_y = altura // 2 - tamanho_bola // 2

#Define a velocidade das raquetes
raquete_player_1_dy = 5
raquete_pc_dy = 5

#Define a velocidade da bola
velocidade_bola_x = 3 
velocidade_bola_y = 3 

#Define o Score 
score_player_1 = 0 
score_pc = 0 

#Configuração da fonte
font_file = 'Pong/font/PressStart2P-Regular.ttf' 
font = pygame.font.Font(font_file, 20)

#Objeto para manupular FPS
clock = pygame.time.Clock()

rodando = False

#Função que define o menu principal 
def menu_principal():
    global rodando
    while True:         
        #Se o usuário clicar em fechar a janela, o jogo é encerrado
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit() 
                sys.exit()
            #Se clicar na tecla espaço, o jogo é iciciado
            elif event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_SPACE: 
                    rodando = True
                    return                    

        #Define o nome do jogo na tela
        screen.fill(PRETO) 
        texto_menu = font.render("Pong", True, BRANCO)
        text_menu_rect = texto_menu.get_rect(center=(largura //2, altura // 2))
        screen.blit(texto_menu, text_menu_rect) 

        #Retorna o número de milissegundos que se passaram desde que o pygame.init() foi chamado
        tempo = pygame.time.get_ticks()

        #Define um texto que ficará piscando abaixo do nome do jogo
        if tempo % 2000 < 1000:
            texto_iniciar = font.render("Pressione Espaço", True, BRANCO)
            texto_iniciar_rect = texto_iniciar.get_rect(center=(largura // 2, 450))
            screen.blit(texto_iniciar, texto_iniciar_rect)

        #Atualiza o conteúdo da tela
        pygame.display.flip()

menu_principal()    

while rodando:  # Loop principal do jogo que roda enquanto a variável "rodando" for True
    for event in pygame.event.get():  # Loop para verificar eventos do Pygame
        if event.type == pygame.QUIT:  # Verifica se o evento é o fechamento da janela
            rodando = False  # Define "rodando" como False para sair do loop principal

    #Define a cor da tela
    screen.fill(PRETO)  

    #amenta a velocidade da bola no eixo x
    bola_x += velocidade_bola_x 
    #aumenta a velocidade da nola no eixo y
    bola_y += velocidade_bola_y 

    #Cria o retângulo de colisão da bola
    bola_rect = pygame.Rect(bola_x, bola_y, tamanho_bola, tamanho_bola) 
    
    #Cria o retângulo de colisão da raquete do pc e do player 1
    raquete_pc_rect = pygame.Rect(pc_x, pc_y, raquete_largura, raquete_altura)     
    raquete_player_1_rect = pygame.Rect(player_1_x, player_1_y, raquete_largura, raquete_altura) 

    #Se a bola colidir com a raquete do pc ou do player
    if bola_rect.colliderect(raquete_pc_rect) or bola_rect.colliderect(raquete_player_1_rect): 
        #Inverte a direção da bola 
        velocidade_bola_x = -velocidade_bola_x

    #Se a bola bater em cima ou em baixo da tela
    if bola_y <= 0 or bola_y >= altura - tamanho_bola:
        #Inverte a direção da bola 
        velocidade_bola_y = -velocidade_bola_y 

    #Se a bola bater no lado esquerdo da tela
    if bola_x <= 0:
        #Volta ao centro da tela
        bola_x = largura // 2 - tamanho_bola // 2 
        bola_y =  altura // 2 - tamanho_bola // 2 
        #Inverte a direção para qual irá ao iniciar novamente o jogo, pro lado oposto de quem marcou ponto
        velocidade_bola_x = -velocidade_bola_x  
        #Adiciona 1 ponto ao score do player 1
        score_player_1 += 1
        print(f"Score Player_1: {score_player_1}")

    #Se a bola bater do lado direito da tela
    if bola_x >= largura - tamanho_bola:
        #Volta ao centro da tela
        bola_x = largura // 2 - tamanho_bola // 2 
        bola_y =  altura // 2 - tamanho_bola // 2
        #Inverte a direção para qual irá ao iniciar novamente o jogo, pro lado oposto de quem marcou ponto
        velocidade_bola_x = -velocidade_bola_x  
        #Adiciona 1 ponto ao score do pc
        score_pc += 1
        print(f"Score PC: {score_pc}")

    #Move a raquete do pc para seguir a bola
    if pc_y + raquete_altura // 2 < bola_y:
        pc_y += raquete_pc_dy
    elif pc_y + raquete_altura // 2 > bola_y:
        pc_y -= raquete_pc_dy

    #Move a raquete do player 1 para seguir a bola
    '''if player_1_y + raquete_altura // 2 < bola_y:
        player_1_y += raquete_player_1_dy
    elif player_1_y + raquete_altura // 2 > bola_y:
        player_1_y -= raquete_player_1_dy'''

    #Evita que a raquete do pc saia fora da tela
    if pc_y < 0:
        pc_y = 0
    elif pc_y > altura - raquete_altura:
        pc_y = altura - raquete_altura

    #Evita que a raquete do player saia fora da tela
    if pc_y < 0:
        pc_y = 0
    elif pc_y > altura - raquete_altura:
        pc_y = altura - raquete_altura

    #Mostre o score no jogo
    fonte_score = pygame.font.Font(font_file, 24)
    score_texto = font.render(
        f"Score PC: {score_pc}       Score Player_1: {score_player_1}", True, BRANCO
    )
    score_rect = score_texto.get_rect(center=(largura //2, 30))
    screen.blit(score_texto, score_rect)

    #Desenha as raquetes e a bola na tela
    pygame.draw.rect(screen, BRANCO, (pc_x, pc_y, raquete_largura, raquete_altura))  
    pygame.draw.rect(screen, BRANCO, (player_1_x, player_1_y, raquete_largura, raquete_altura))  
    pygame.draw.ellipse(screen, BRANCO, (bola_x, bola_y, tamanho_bola, tamanho_bola))  
    pygame.draw.aaline(screen, BRANCO, (largura //2, 0), (largura //2, altura)) 

    #Captura as teclas pressionadas
    keys = pygame.key.get_pressed()  

    #Se a tecla 'seta para cima' estiver pressionada,Momove a raquete do player 1 para cima
    if keys[pygame.K_UP] and player_1_y > 0:  
        player_1_y -= raquete_player_1_dy  

    #Se a tecla 'seta para baixo' estiver pressionada,Momove a raquete do player 1 para baixo
    if keys[pygame.K_DOWN] and player_1_y < altura - raquete_altura:  
        player_1_y += raquete_player_1_dy  

    #Atualiza a tela 
    pygame.display.flip() 

    #Limita a taxa de FPS
    clock.tick(60)  

#Encerra o Pygame
pygame.quit()

#Encerra o programa
sys.exit()  