"""import pygame
pygame.init()


# ============================================================
# CONFIGURAÇÕES DA JANELA
# ============================================================

WIDTH = 1000
HEIGHT = 600
FPS = 60


screen = pygame.display.set_mode(
    (WIDTH, HEIGHT)
)


pygame.display.set_caption(
    "Ciência Delas"
)


clock = pygame.time.Clock()


# ============================================================
# CORES
# ============================================================

BG = (25, 25, 35)

GREEN = (80, 200, 120)


# ============================================================
# JOGADOR
# ============================================================

# Esse Rect é o "corpo físico" do jogador.
#
# A imagem pode ser maior que ele.
# O Rect é usado principalmente para:
#
# - posição
# - colisão
# - física

player = pygame.Rect(
    100,
    400,
    64,
    80
)


# ============================================================
# SPRITESHEET
# ============================================================

spritesheet = pygame.image.load(
    "assets/spritesheet1.png"
).convert_alpha()


# ============================================================
# POSIÇÕES DOS SPRITES
# ============================================================

# Cada Rect representa:
#
# Rect(X, Y, largura, altura)

frames = [
    pygame.Rect(0, 0, 512, 512),
    pygame.Rect(2000, 30, 512, 512),
    pygame.Rect(140, 1050, 512, 512),
    pygame.Rect(2450, 1050, 512, 512),
    pygame.Rect(750, 2080, 512, 512),
    pygame.Rect(3150, 2080, 512, 512),
    pygame.Rect(1120, 3100, 512, 512),
    pygame.Rect(2050, 3600, 512, 512),
    pygame.Rect(0, 4630, 512, 512),
    pygame.Rect(2300, 4730, 512, 512),
    pygame.Rect(0, 5000, 800, 800)
]


# ============================================================
# ANIMAÇÃO DE CAMINHADA
# ============================================================

walk_frames = []


# Altura padrão dos sprites.

SPRITE_HEIGHT = 240


# ============================================================
# TAMANHO INDIVIDUAL DE CADA FRAME
# ============================================================

# Aqui você pode ajustar cada sprite separadamente.
#
# Frame 0 = 240
# Frame 1 = 240
# Frame 2 = 240
# etc.

FRAME_SIZES = [
    240,  # frame 0
    240,  # frame 1
    240,  # frame 2
    240,  # frame 3
    240,  # frame 4
    240,  # frame 5
    240,  # frame 6
    240,  # frame 7
    240,  # frame 8
    240,  # frame 9
    100   # frame 10
]


# ============================================================
# CRIAÇÃO DOS FRAMES
# ============================================================

for frame_index, frame_rect in enumerate(frames):

    # --------------------------------------------------------
    # RECORTAR O SPRITE
    # --------------------------------------------------------

    frame = spritesheet.subsurface(
        frame_rect
    ).copy()


    # --------------------------------------------------------
    # TAMANHO DESTE FRAME
    # --------------------------------------------------------

    sprite_height = FRAME_SIZES[
        frame_index
    ]


    # --------------------------------------------------------
    # MANTER A PROPORÇÃO
    # --------------------------------------------------------

    new_width = int(

        frame.get_width()
        *
        sprite_height
        /
        frame.get_height()

    )


    # --------------------------------------------------------
    # REDIMENSIONAR
    # --------------------------------------------------------

    frame = pygame.transform.scale(

        frame,

        (
            new_width,
            sprite_height
        )

    )


    # --------------------------------------------------------
    # GUARDAR FRAME
    # --------------------------------------------------------

    walk_frames.append(
        frame
    )


# ============================================================
# CONTROLE DA ANIMAÇÃO
# ============================================================

# Qual frame está sendo mostrado agora.

current_frame = 0


# Momento da última troca de frame.

animation_timer = 0


# Tempo entre cada frame.
#
# 100 ms = 0.1 segundo.

FRAME_DURATION = 100


# O personagem começa olhando para a direita.

facing_right = True


# ============================================================
# TESTE DE FRAME
# ============================================================

# Enquanto estiver ajustando os sprites,
# coloque aqui o número do frame que quer visualizar.
#
# 0 até 10.

TEST_FRAME = 10


# ============================================================
# FÍSICA DO JOGADOR
# ============================================================

velocity_y = 0


gravity = 0.85


jump_strength = -30


speed = 5


on_ground = False


# ============================================================
# MUNDO
# ============================================================

ground = pygame.Rect(

    0,

    500,

    31000,

    100

)


# ============================================================
# CÂMERA
# ============================================================

camera_x = 0

camera_y = 0


# ============================================================
# FUNÇÃO DO FUNDO
# ============================================================

def draw_background(
    camera_x,
    camera_y
):


    # --------------------------------------------------------
    # CÉU
    # --------------------------------------------------------

    screen.fill(
        BG
    )


    # --------------------------------------------------------
    # MONTANHAS DISTANTES
    # --------------------------------------------------------

    mountain_offset_x = int(
        camera_x * 0.2
    )


    mountain_offset_y = camera_y


    for x in range(
        -500,
        4000,
        500
    ):

        x_screen = (
            x
            -
            mountain_offset_x
        )


        points = [

            (
                x_screen,
                450 - mountain_offset_y
            ),

            (
                x_screen + 250,
                250 - mountain_offset_y
            ),

            (
                x_screen + 500,
                450 - mountain_offset_y
            )

        ]


        pygame.draw.polygon(

            screen,

            (45, 45, 65),

            points

        )


    # --------------------------------------------------------
    # MONTANHAS MAIS PRÓXIMAS
    # --------------------------------------------------------

    mountain_offset_x = int(
        camera_x * 0.4
    )


    for x in range(
        -2000,
        4000,
        700
    ):

        x_screen = (
            x
            -
            mountain_offset_x
        )


        points = [

            (
                x_screen,
                500 - mountain_offset_y
            ),

            (
                x_screen + 350,
                300 - mountain_offset_y
            ),

            (
                x_screen + 700,
                500 - mountain_offset_y
            )

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

    moving = False


    # --------------------------------------------------------
    # ESQUERDA
    # --------------------------------------------------------

    if (
        keys[pygame.K_a]
        or
        keys[pygame.K_LEFT]
    ):

        player.x -= speed

        facing_right = False

        moving = True


    # --------------------------------------------------------
    # DIREITA
    # --------------------------------------------------------

    if (
        keys[pygame.K_d]
        or
        keys[pygame.K_RIGHT]
    ):

        player.x += speed

        facing_right = True

        moving = True


    # ========================================================
    # PULO
    # ========================================================

    if (

        (
            keys[pygame.K_SPACE]
            or
            keys[pygame.K_w]
            or
            keys[pygame.K_UP]
        )

        and

        on_ground

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

    if player.colliderect(
        ground
    ):

        player.bottom = ground.top

        velocity_y = 0

        on_ground = True


    # ========================================================
    # ANIMAÇÃO
    # ========================================================

    current_time = pygame.time.get_ticks()

    # ========================================================
# ANIMAÇÃO DO PULO
# ========================================================

if not on_ground:

    if velocity_y < 0:
        # Está subindo
        jump_animation = 8

    else:
        # Está caindo
        jump_animation = 10
        
    if moving:

        if (

            current_time
            -
            animation_timer

            >=

            FRAME_DURATION

        ):

            current_frame += 1


            if current_frame >= len(
                walk_frames
            ):

                current_frame = 1


            animation_timer = current_time


    else:

        current_frame = 0


    # ========================================================
    # CÂMERA HORIZONTAL
    # ========================================================

    camera_x = (

        player.centerx
        -
        WIDTH // 2

    )


    camera_x = max(
        0,
        camera_x
    )


    camera_x = min(

        camera_x,

        ground.width
        -
        WIDTH

    )


    # ========================================================
    # CÂMERA VERTICAL
    # ========================================================

    camera_y = min(

        0,

        player.y - 400

    )


    # ========================================================
    # DESENHAR
    # ========================================================

    draw_background(

        camera_x,

        camera_y

    )


    # --------------------------------------------------------
    # CHÃO
    # --------------------------------------------------------

    pygame.draw.rect(

        screen,

        GREEN,

        (

            ground.x - camera_x,

            ground.y - camera_y,

            ground.width,

            ground.height

        )

    )


    # --------------------------------------------------------
    # JOGADOR
    # --------------------------------------------------------

    # Durante os testes, usamos TEST_FRAME.
    #
    # Depois que terminar os ajustes, basta trocar
    # TEST_FRAME por current_frame.

    if not on_ground:
        image = walk_frames[
            jump_animation
        ]
    else:
        image = walk_frames[
            current_frame
        ]
    # --------------------------------------------------------
    # INVERTER PARA A ESQUERDA
    # --------------------------------------------------------

    if not facing_right:

        image = pygame.transform.flip(

            image,

            True,

            False

        )


    # --------------------------------------------------------
    # ALINHAMENTO DA IMAGEM
    # --------------------------------------------------------

    image_x = (

        player.centerx
        -
        image.get_width() // 2
        -
        camera_x

    )


    image_y = (

        player.bottom
        -
        image.get_height()
        -
        camera_y
        +
        160
        

    )
    if TEST_FRAME == 10:
        image_y -= 160


    # --------------------------------------------------------
    # DESENHAR SPRITE
    # --------------------------------------------------------

    screen.blit(

        image,

        (

            image_x,

            image_y

        )

    )


    # ========================================================
    # ATUALIZAÇÃO DA TELA
    # ========================================================

    pygame.display.flip()


    # ========================================================
    # FPS
    # ========================================================

    clock.tick(
        FPS
    )


# ============================================================
# ENCERRAMENTO
# ============================================================

pygame.quit()"""
import pygame
pygame.init()


# ============================================================
# CONFIGURAÇÕES DA JANELA
# ============================================================

WIDTH = 1000
HEIGHT = 600
FPS = 60


screen = pygame.display.set_mode(
    (WIDTH, HEIGHT)
)


pygame.display.set_caption(
    "Ciência Delas"
)


clock = pygame.time.Clock()


# ============================================================
# CORES
# ============================================================

BG = (25, 25, 35)

GREEN = (80, 200, 120)


# ============================================================
# JOGADOR
# ============================================================

player = pygame.Rect(
    100,
    400,
    64,
    80
)


# ============================================================
# SPRITESHEET
# ============================================================

spritesheet = pygame.image.load(
    "assets/spritesheet1.png"
).convert_alpha()


# ============================================================
# POSIÇÕES DOS SPRITES
# ============================================================

frames = [
    pygame.Rect(0, 0, 512, 512),
    pygame.Rect(2000, 30, 512, 512),
    pygame.Rect(140, 1050, 512, 512),
    pygame.Rect(2450, 1050, 512, 512),
    pygame.Rect(750, 2080, 512, 512),
    pygame.Rect(3150, 2080, 512, 512),
    pygame.Rect(1120, 3100, 512, 512),
    pygame.Rect(2050, 3600, 512, 512),
    pygame.Rect(0, 4630, 512, 512),
    pygame.Rect(2300, 4730, 512, 512),
    pygame.Rect(0, 5000, 800, 800)
]


# ============================================================
# ANIMAÇÃO
# ============================================================

walk_frames = []


# Altura padrão

SPRITE_HEIGHT = 240


# ============================================================
# TAMANHO DE CADA FRAME
# ============================================================

FRAME_SIZES = [
    240,  # frame 0
    240,  # frame 1
    240,  # frame 2
    240,  # frame 3
    240,  # frame 4
    240,  # frame 5
    240,  # frame 6
    240,  # frame 7
    240,  # frame 8
    240,  # frame 9
    100   # frame 10
]


# ============================================================
# CRIAÇÃO DOS FRAMES
# ============================================================

for frame_index, frame_rect in enumerate(frames):

    # Recorta o sprite

    frame = spritesheet.subsurface(
        frame_rect
    ).copy()


    # Pega o tamanho específico desse frame

    sprite_height = FRAME_SIZES[
        frame_index
    ]


    # Mantém a proporção

    new_width = int(

        frame.get_width()
        *
        sprite_height
        /
        frame.get_height()

    )


    # Redimensiona

    frame = pygame.transform.scale(

        frame,

        (
            new_width,
            sprite_height
        )

    )


    # Guarda

    walk_frames.append(
        frame
    )


# ============================================================
# CONTROLE DA ANIMAÇÃO
# ============================================================

current_frame = 0

animation_timer = 0

FRAME_DURATION = 600

facing_right = True


# ============================================================
# TESTE DE FRAME
# ============================================================

# Use isso SOMENTE se quiser testar um frame parado.
#
# Depois coloque TEST_MODE = False.

TEST_MODE = False

TEST_FRAME = 10


# ============================================================
# FÍSICA DO JOGADOR
# ============================================================

velocity_y = 0

gravity = 0.85

jump_strength = -30

speed = 5

on_ground = False


# ============================================================
# MUNDO
# ============================================================

ground = pygame.Rect(

    0,
    500,
    31000,
    100

)


# ============================================================
# CÂMERA
# ============================================================

camera_x = 0

camera_y = 0


# ============================================================
# FUNÇÃO DO FUNDO
# ============================================================

def draw_background(
    camera_x,
    camera_y
):


    # --------------------------------------------------------
    # CÉU
    # --------------------------------------------------------

    screen.fill(
        BG
    )


    # --------------------------------------------------------
    # MONTANHAS DISTANTES
    # --------------------------------------------------------

    mountain_offset_x = int(
        camera_x * 0.2
    )


    mountain_offset_y = camera_y


    for x in range(
        -500,
        4000,
        500
    ):

        x_screen = (
            x
            -
            mountain_offset_x
        )


        points = [

            (
                x_screen,
                450 - mountain_offset_y
            ),

            (
                x_screen + 250,
                250 - mountain_offset_y
            ),

            (
                x_screen + 500,
                450 - mountain_offset_y
            )

        ]


        pygame.draw.polygon(

            screen,

            (45, 45, 65),

            points

        )


    # --------------------------------------------------------
    # MONTANHAS MAIS PRÓXIMAS
    # --------------------------------------------------------

    mountain_offset_x = int(
        camera_x * 0.4
    )


    for x in range(
        -2000,
        4000,
        700
    ):

        x_screen = (
            x
            -
            mountain_offset_x
        )


        points = [

            (
                x_screen,
                500 - mountain_offset_y
            ),

            (
                x_screen + 350,
                300 - mountain_offset_y
            ),

            (
                x_screen + 700,
                500 - mountain_offset_y
            )

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

    moving = False


    # --------------------------------------------------------
    # ESQUERDA
    # --------------------------------------------------------

    if (
        keys[pygame.K_a]
        or
        keys[pygame.K_LEFT]
    ):

        player.x -= speed

        facing_right = False

        moving = True


    # --------------------------------------------------------
    # DIREITA
    # --------------------------------------------------------

    if (
        keys[pygame.K_d]
        or
        keys[pygame.K_RIGHT]
    ):

        player.x += speed

        facing_right = True

        moving = True


    # ========================================================
    # PULO
    # ========================================================

    if (

        (
            keys[pygame.K_SPACE]
            or
            keys[pygame.K_w]
            or
            keys[pygame.K_UP]
        )

        and

        on_ground

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

    if player.colliderect(
        ground
    ):

        player.bottom = ground.top

        velocity_y = 0

        on_ground = True


    # ========================================================
    # ANIMAÇÃO
    # ========================================================

    current_time = pygame.time.get_ticks()


    # --------------------------------------------------------
    # JOGADOR NO AR
    # --------------------------------------------------------

    if not on_ground:
        current_frame = 8 if velocity_y < 0 else 10

    elif current_frame == 10:
        current_frame = 9
        landing_timer = current_time
    


    # --------------------------------------------------------
    # JOGADOR NO CHÃO
    # --------------------------------------------------------

    else:

        if moving:

            if (

                current_time
                -
                animation_timer

                >=

                FRAME_DURATION

            ):

                current_frame += 1


                # Só usamos os frames 1 até 7
                # para caminhada.

                if current_frame >= 7:

                    current_frame = 1


                animation_timer = current_time


        else:

            current_frame = 0


    # ========================================================
    # CÂMERA HORIZONTAL
    # ========================================================

    camera_x = (

        player.centerx
        -
        WIDTH // 2

    )


    camera_x = max(
        0,
        camera_x
    )


    camera_x = min(

        camera_x,

        ground.width
        -
        WIDTH

    )


    # ========================================================
    # CÂMERA VERTICAL
    # ========================================================

    camera_y = min(

        0,

        player.y - 400

    )


    # ========================================================
    # DESENHAR
    # ========================================================

    draw_background(

        camera_x,

        camera_y

    )


    # --------------------------------------------------------
    # CHÃO
    # --------------------------------------------------------

    pygame.draw.rect(

        screen,

        GREEN,

        (

            ground.x - camera_x,

            ground.y - camera_y,

            ground.width,

            ground.height

        )

    )


    # --------------------------------------------------------
    # JOGADOR
    # --------------------------------------------------------

    # Se estiver no modo de teste,
    # escolhe manualmente o frame.

    if TEST_MODE:

        image = walk_frames[
            TEST_FRAME
        ]


    # Caso contrário,
    # usa a animação normal.

    else:

        image = walk_frames[
            current_frame
        ]


    # --------------------------------------------------------
    # INVERTER PARA A ESQUERDA
    # --------------------------------------------------------

    if not facing_right:

        image = pygame.transform.flip(

            image,

            True,

            False

        )


    # --------------------------------------------------------
    # ALINHAMENTO DA IMAGEM
    # --------------------------------------------------------

    image_x = (

        player.centerx
        -
        image.get_width() // 2
        -
        camera_x

    )


    image_y = (

        player.bottom
        -
        image.get_height()
        -
        camera_y
        +
        160

    )


    # --------------------------------------------------------
    # AJUSTE EXCLUSIVO DO FRAME 10
    # --------------------------------------------------------

    if current_frame == 10:

        image_y -= 160


    # --------------------------------------------------------
    # DESENHAR SPRITE
    # --------------------------------------------------------

    screen.blit(

        image,

        (
            image_x,
            image_y
        )

    )


    # ========================================================
    # ATUALIZAÇÃO DA TELA
    # ========================================================

    pygame.display.flip()


    # ========================================================
    # FPS
    # ========================================================

    clock.tick(
        FPS
    )


# ============================================================
# ENCERRAMENTO
# ============================================================

pygame.quit()