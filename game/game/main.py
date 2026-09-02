
import pygame
pygame.init()


# ============================================================
# CONFIGURAÇÕES DA JANELA
# ============================================================

WIDTH = 1000
HEIGHT = 600
FPS = 60

# Cria a janela usando a largura e altura que definimos acima
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Nome que aparece na barra da janela
pygame.display.set_caption("Ciência Delas")

# Cria um relógio para controlar a velocidade do jogo
clock = pygame.time.Clock()


BG = (25, 25, 35)
WHITE = (240, 240, 240)
GREEN = (80, 200, 120)


# ============================================================
# JOGADOR
# ============================================================

player = pygame.Rect(100, 400, 64, 80)

# Carrega a spritesheet inteira
spritesheet = pygame.image.load(
    "assets/spritesheet1.png"
).convert_alpha()

# Pega o primeiro frame da spritesheet
player_image = spritesheet.subsurface(
    pygame.Rect(0, 0, 512, 512)
)

# Redimensiona o frame para o tamanho que queremos no jogo
player_image = pygame.transform.scale(
    player_image,
    (230, 230)
)

# Cria uma versão da imagem virada horizontalmente
# para quando o personagem estiver olhando para a esquerda.
player_image_left = pygame.transform.flip(
    player_image,
    True,
    False
)

# Começamos olhando para a direita
facing_right = True


# ============================================================
# FÍSICA DO JOGADOR
# ============================================================

velocity_y = 0

gravity = 0.8

jump_strength = -30

speed = 5

on_ground = False


# ============================================================
# MUNDO
# ============================================================

ground = pygame.Rect(
    0,      # posição X
    500,    # posição Y
    3000,   # largura
    100     # altura
)


# ============================================================
# CÂMERA
# ============================================================

camera_x = 0


# ============================================================
# FUNÇÃO DO FUNDO
# ============================================================

def draw_background(camera_x):

    # --------------------------------------------------------
    # CÉU
    # --------------------------------------------------------

    # Limpa a tela a cada frame.
    screen.fill(BG)


    # --------------------------------------------------------
    # MONTANHAS DISTANTES
    # --------------------------------------------------------

    # As montanhas se movem mais devagar que a câmera.
    # Isso cria o efeito de profundidade chamado PARALLAX.

    mountain_offset = int(camera_x * 0.2)


    for x in range(-500, 4000, 500):

        x_screen = x - mountain_offset

        points = [
            (x_screen, 450),
            (x_screen + 250, 250),
            (x_screen + 500, 450)
        ]

        pygame.draw.polygon(
            screen,
            (45, 45, 65),
            points
        )


    # --------------------------------------------------------
    # MONTANHAS MAIS PRÓXIMAS
    # --------------------------------------------------------

    mountain_offset = int(camera_x * 0.4)


    for x in range(-2000, 4000, 700):

        x_screen = x - mountain_offset

        points = [
            (x_screen, 500),
            (x_screen + 350, 300),
            (x_screen + 700, 500)
        ]

        pygame.draw.polygon(
            screen,
            (60, 60, 80),
            points
        )


# ============================================================
# LOOP PRINCIPAL
# ============================================================

running = True

while running:


    # ========================================================
    # EVENTOS
    # ========================================================

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False


    # ========================================================
    # TECLADO
    # ========================================================

    keys = pygame.key.get_pressed()


    # ========================================================
    # MOVIMENTO HORIZONTAL
    # ========================================================

    if keys[pygame.K_a] or keys[pygame.K_LEFT]:

        player.x -= speed

        # Agora o personagem passa a olhar para a esquerda
        facing_right = False


    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:

        player.x += speed

        # Agora o personagem passa a olhar para a direita
        facing_right = True


    # ========================================================
    # PULO
    # ========================================================

    if (
        (keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP])
        and on_ground
    ):

        velocity_y = jump_strength

        on_ground = False


    # ========================================================
    # GRAVIDADE
    # ========================================================

    velocity_y += gravity

    player.y += velocity_y


    # ========================================================
    # COLISÃO COM O CHÃO
    # ========================================================

    if player.colliderect(ground):

        player.bottom = ground.top

        velocity_y = 0

        on_ground = True


    # ========================================================
    # CÂMERA
    # ========================================================

    # A câmera acompanha o jogador horizontalmente.
    camera_x = player.centerx - WIDTH // 2


    # A câmera só começa a subir quando o jogador
    # chega perto do topo da tela.
    camera_y = player.y - 400


    # --------------------------------------------------------
    # LIMITES DA CÂMERA
    # --------------------------------------------------------

    # A câmera nunca pode mostrar uma região
    # que não existe à esquerda do mundo.
    camera_x = max(0, camera_x)

    # A câmera nunca pode passar do final do mundo.
    camera_x = min(camera_x, ground.width - WIDTH)


    # A câmera vertical não pode ficar positiva.
    # Valores negativos significam que o mundo
    # está sendo deslocado para baixo na tela.
    camera_y = min(0, camera_y)
    # ========================================================
    # DESENHAR
    # ========================================================

    # Primeiro desenhamos o fundo.

    draw_background(camera_x)


    # --------------------------------------------------------
    # CHÃO
    # --------------------------------------------------------

    pygame.draw.rect(
        screen,
        GREEN,
        (
            ground.x - camera_x,
            ground.y,
            ground.width,
            ground.height
        )
    )


    # --------------------------------------------------------
    # JOGADOR
    # --------------------------------------------------------

    # Escolhe qual imagem usar dependendo
    # da direção que o personagem está olhando.

    if facing_right:
        image = player_image
    else:
        image = player_image_left


    # Desenha o personagem na posição correta da tela.

    screen.blit(
        image,
        (
            player.x - camera_x,
            player.y
        )
    )


    # ========================================================
    # ATUALIZAÇÃO DA TELA
    # ========================================================

    pygame.display.flip()


    # ========================================================
    # FPS
    # ========================================================

    clock.tick(FPS)


# ============================================================
# ENCERRAMENTO
# ============================================================

pygame.quit()

