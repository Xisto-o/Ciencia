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

FRAME_DURATION = 120

facing_right = True

landing_timer = 0


# ============================================================
# TESTE DE FRAME
# ============================================================

# Use isso SOMENTE se quiser testar um frame parado.
#
# Depois coloque TEST_MODE = False.

TEST_MODE = False

TEST_FRAME = 0


# ============================================================
# FÍSICA DO JOGADOR
# ============================================================

velocity_y = 0

gravity = 0.85

jump_strength = -20

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
# TAMANHO DE CADA FRAME
# ============================================================

FRAME_SIZES = [
    240,  # 0 - parado
    240,  # 1 - andando
    240,  # 2 - andando
    240,  # 3 - andando
    240,  # 4 - andando
    240,  # 5 - andando
    240,  # 6 - andando
    240,  # 7 - andando
    240,  # 8 - subindo
    240,  # 9 - aterrissando
    100   # 10 - caindo
]


# ============================================================
# CRIAR OS FRAMES
# ============================================================

walk_frames = []

for frame_index, frame_rect in enumerate(frames):

    frame = spritesheet.subsurface(
        frame_rect
    ).copy()

    sprite_height = FRAME_SIZES[
        frame_index
    ]

    new_width = int(
        frame.get_width()
        * sprite_height
        / frame.get_height()
    )

    frame = pygame.transform.scale(
        frame,
        (
            new_width,
            sprite_height
        )
    )

    walk_frames.append(
        frame
    )


# ============================================================
# CONTROLE DA ANIMAÇÃO
# ============================================================

current_frame = 0

animation_timer = 0
landing_timer = 0

FRAME_DURATION = 120
LANDING_DURATION = 100

facing_right = True


# ============================================================
# TESTE DE FRAME
# ============================================================

TEST_MODE = False
TEST_FRAME = 0


# ============================================================
# FÍSICA DO JOGADOR
# ============================================================

velocity_y = 0

gravity = 0.85

jump_strength = -20

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

def draw_background(camera_x, camera_y):

    screen.fill(BG)


    # ========================================================
    # MONTANHAS DISTANTES
    # ========================================================

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
            - mountain_offset_x
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


    # ========================================================
    # MONTANHAS PRÓXIMAS
    # ========================================================

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
            - mountain_offset_x
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
    # TEMPO
    # ========================================================

    current_time = pygame.time.get_ticks()


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


    if (
        keys[pygame.K_a]
        or keys[pygame.K_LEFT]
    ):

        player.x -= speed

        facing_right = False

        moving = True


    if (
        keys[pygame.K_d]
        or keys[pygame.K_RIGHT]
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
            or keys[pygame.K_w]
            or keys[pygame.K_UP]
        )

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

    if (

        player.colliderect(ground)

        and velocity_y >= 0

    ):

        # Só inicia a aterrissagem
        # se estava no ar antes.

        if not on_ground:

            landing_timer = current_time


        player.bottom = ground.top

        velocity_y = 0

        on_ground = True


    # ========================================================
    # ANIMAÇÃO
    # ========================================================

    # --------------------------------------------------------
    # NO AR
    # --------------------------------------------------------

    if not on_ground:

        # Subindo

        if velocity_y < 0:

            current_frame = 8


        # Caindo

        else:

            current_frame = 10


    # --------------------------------------------------------
    # ATERRISSAGEM
    # --------------------------------------------------------

    elif (
        current_time
        - landing_timer
        < LANDING_DURATION
    ):

        current_frame = 9


    # --------------------------------------------------------
    # NO CHÃO
    # --------------------------------------------------------

    else:

        # Caminhando

        if moving:

            if (

                current_time
                - animation_timer
                >= FRAME_DURATION

            ):

                current_frame += 1


                # Caminhada: frames 1 até 7

                if (
                    current_frame < 1
                    or current_frame > 7
                ):

                    current_frame = 1


                animation_timer = current_time


        # Parado

        else:

            current_frame = 0


    # ========================================================
    # CÂMERA HORIZONTAL
    # ========================================================

    camera_x = (
        player.centerx
        - WIDTH // 2
    )

    camera_x = max(
        0,
        camera_x
    )

    camera_x = min(
        camera_x,
        ground.width - WIDTH
    )


    # ========================================================
    # CÂMERA VERTICAL
    # ========================================================

    camera_y = min(
        0,
        player.y - 400
    )


    # ========================================================
    # DESENHAR FUNDO
    # ========================================================

    draw_background(
        camera_x,
        camera_y
    )


    # ========================================================
    # DESENHAR CHÃO
    # ========================================================

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


    # ========================================================
    # ESCOLHER IMAGEM
    # ========================================================

    if TEST_MODE:

        image = walk_frames[
            TEST_FRAME
        ]

    else:

        image = walk_frames[
            current_frame
        ]


    # ========================================================
    # VIRAR PARA A ESQUERDA
    # ========================================================

    if not facing_right:

        image = pygame.transform.flip(
            image,
            True,
            False
        )


    # ========================================================
    # POSIÇÃO DA IMAGEM
    # ========================================================

    image_x = (

        player.centerx
        - image.get_width() // 2
        - camera_x

    )


    image_y = (

        player.bottom
        - image.get_height()
        - camera_y
        + 160

    )


    # ========================================================
    # AJUSTE EXCLUSIVO DO FRAME 10
    # ========================================================

    if current_frame == 10:

        image_y -= 160


    # ========================================================
    # DESENHAR JOGADOR
    # ========================================================

    screen.blit(

        image,

        (
            image_x,
            image_y
        )

    )


    # ========================================================
    # ATUALIZAR TELA
    # ========================================================

    pygame.display.flip()


    # ========================================================
    # FPS
    # ========================================================

    clock.tick(FPS)


# ============================================================
# ENCERRAR
# ============================================================

pygame.quit()