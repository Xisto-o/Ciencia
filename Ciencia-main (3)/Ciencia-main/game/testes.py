"""
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
    "ciencia-main/game/assets/spritesheet3.png"
).convert_alpha()
# ============================================================
# FUNDO
# ============================================================

background = pygame.image.load(
    "ciencia-main/game/assets/background2.png"
).convert()
background = pygame.transform.scale(
    background,
    (
        background.get_width() * 1,
        background.get_height() * 1
    )
)
# ============================================================
# POSIÇÕES DOS SPRITES
# ============================================================

frames = [
    pygame.Rect(0, 0, 512, 512),          # 0 - parado
    pygame.Rect(2000, 30, 512, 512),      # 1 - andando
    pygame.Rect(0, 1050, 512, 512),     # 2 - andando
    pygame.Rect(2350, 1050, 512, 512),    # 3 - andando
    pygame.Rect(650, 2080, 512, 512),     # 4 - andando
    pygame.Rect(3050, 2080, 512, 512),    # 5 - andando
    pygame.Rect(1020, 3100, 512, 512),    # 6 - andando
    pygame.Rect(1950, 3550, 512, 512),    # 7 - andando
    pygame.Rect(0, 4630, 512, 512),       # 8 - subindo
    pygame.Rect(2150, 4650, 512, 512),    # 9 - aterrissando
    pygame.Rect(0, 5000, 800, 800)        # 10 - caindo
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
    300,  # 7 - andando
    300,  # 8 - subindo
    300,  # 9 - aterrissando
    100   # 10 - caindo
]


# ============================================================
# CRIAR OS FRAMES
# ============================================================

sprite_frames = []


for frame_index, frame_rect in enumerate(frames):

    # Recorta o sprite da spritesheet.

    frame = spritesheet.subsurface(
        frame_rect
    ).copy()


    # Altura desejada para esse frame.

    sprite_height = FRAME_SIZES[
        frame_index
    ]


    # Mantém a proporção original.

    new_width = int(
        frame.get_width()
        * sprite_height
        / frame.get_height()
    )


    # Redimensiona.

    frame = pygame.transform.scale(
        frame,
        (
            new_width,
            sprite_height
        )
    )


    # Guarda na lista.

    sprite_frames.append(
        frame
    )


# ============================================================
# CONTROLE DA ANIMAÇÃO
# ============================================================

current_frame = 0

animation_timer = 100
landing_timer = 150

FRAME_DURATION = 100
LANDING_DURATION = 150

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

gravity = 0.75

jump_strength = -25

speed = 4.4

on_ground = False


# ============================================================
# MUNDO
# ============================================================

# ============================================================
# MUNDO
# ============================================================

ground_image = pygame.image.load(
    "ciencia-main/game/assets/chao1.png"
).convert_alpha()

# Posição da imagem no mundo
ground_x = 0
ground_y = -90


# ============================================================
# PLATAFORMAS / COLISÕES
# ============================================================

grounds = [

    # -------------------------
    # PARTE ESQUERDA
    # -------------------------

    pygame.Rect(20, 585 + ground_y, 360, 25),
    pygame.Rect(32, 492 + ground_y, 85, 25),
    pygame.Rect(60, 375 + ground_y, 225, 25),
    pygame.Rect(267, 347 + ground_y, 145, 25),
    pygame.Rect(320, 214 + ground_y, 225, 25),

    pygame.Rect(402, 462 + ground_y, 110, 25),
    pygame.Rect(404, 605 + ground_y, 65, 25),

    # -------------------------
    # CENTRO-ESQUERDA
    # -------------------------

    pygame.Rect(552, 713 + ground_y, 280, 25),
    pygame.Rect(617, 443 + ground_y, 135, 25),
    pygame.Rect(703, 375 + ground_y, 250, 25),
    pygame.Rect(704, 558 + ground_y, 108, 25),

    pygame.Rect(844, 618 + ground_y, 70, 25),
    pygame.Rect(900, 676 + ground_y, 60, 25),

    # -------------------------
    # CENTRO
    # -------------------------

    pygame.Rect(1045, 291 + ground_y, 345, 25),
    pygame.Rect(1160, 157 + ground_y, 195, 25),
    pygame.Rect(1100, 505 + ground_y, 255, 25),
    pygame.Rect(1032, 682 + ground_y, 360, 25),

    # -------------------------
    # DIREITA
    # -------------------------

    pygame.Rect(1437, 60 + ground_y, 210, 25),
    pygame.Rect(1418, 441 + ground_y, 215, 25),
    pygame.Rect(1495, 599 + ground_y, 175, 25),

    pygame.Rect(1655, 357 + ground_y, 325, 25),
    pygame.Rect(1675, 549 + ground_y, 305, 25),

    pygame.Rect(1750, 57 + ground_y, 235, 25),
    pygame.Rect(1630, 688 + ground_y, 355, 25),
]

# ============================================================
# CÂMERA
# ============================================================

camera_x = 0
camera_y = 0


# ============================================================
# FUNÇÃO DO FUNDO
# ============================================================

# ============================================================
# FUNÇÃO DO FUNDO
# ============================================================

def draw_background(camera_x, camera_y):

    # Limpa a tela
    screen.fill(BG)


    # ========================================================
    # PARALLAX DO FUNDO
    # ========================================================

    # Quanto menor esse número,
    # mais devagar o fundo se movimenta.
    #
    # 0.2 = fundo anda 20% da velocidade da câmera.
    # 0.5 = fundo anda 50%.
    # 1.0 = fundo anda junto com a câmera.

   


    # Calcula onde a imagem deve aparecer
    # na tela.

    background_x = -camera_x * 0.1

    background_y = (-camera_y *0.5) - 250


    # Desenha a imagem do fundo.

    screen.blit(
        background,
        (
            background_x,
            background_y
        )
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
on_ground = False

for ground in grounds:

    if (
        player.colliderect(ground)
        and velocity_y >= 0
    ):

        # Se estava no ar, registra
        # o momento da aterrissagem.

        if not on_ground:

            landing_timer = current_time


        # Coloca o jogador exatamente
        # em cima da grama.

        player.bottom = ground.top

        velocity_y = 0

        on_ground = True

        break


    # ========================================================
    # ANIMAÇÃO
    # ========================================================

    # --------------------------------------------------------
    # NO AR
    # --------------------------------------------------------

    if not on_ground:


        # SUBINDO

        if velocity_y < 0:

            current_frame = 8


        # CAINDO

        else:

            current_frame = 10


    # --------------------------------------------------------
    # ATERRISSANDO
    # --------------------------------------------------------

    elif (

        current_time
        - landing_timer

        <

        LANDING_DURATION

    ):

        current_frame = 9


    # --------------------------------------------------------
    # NO CHÃO
    # --------------------------------------------------------

    else:


        # CAMINHANDO

        if moving:


            # Se está vindo de uma animação
            # diferente, começa a caminhada no frame 1.

            if (
                current_frame < 1
                or current_frame > 7
            ):

                current_frame = 1

                animation_timer = current_time


            # Troca o frame quando chega a hora.

            elif (

                current_time
                - animation_timer

                >=

                FRAME_DURATION

            ):

                current_frame += 1


                # Depois do frame 7,
                # volta para o frame 1.

                if current_frame > 7:

                    current_frame = 1


                animation_timer = current_time


        # PARADO

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
    ground_image.get_width() - WIDTH
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

    screen.blit(
    ground_image,
    (
        ground_x - camera_x,
        ground_y - camera_y
    )
)

    


    # ========================================================
    # ESCOLHER IMAGEM
    # ========================================================

    if TEST_MODE:

        image = sprite_frames[
            TEST_FRAME
        ]

    else:

        image = sprite_frames[
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


    # ========================================================
    # AJUSTE DO FRAME DE QUEDA
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

    clock.tick(
        FPS
    )


# ============================================================
# ENCERRAR
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
# FASE
# ============================================================

fase = 2


# ============================================================
# ESCOLHA DOS ARQUIVOS DA FASE
# ============================================================

if fase == 1:

    spritesheet_path = (
        "ciencia-main/game/assets/spritesheet4.png"
    )

    ground_path = (
        "ciencia-main/game/assets/chao.png"
    )

    background_path = (
        "ciencia-main/game/assets/background1.png"
    )


elif fase == 2:

    spritesheet_path = (
        "ciencia-main/game/assets/spritesheet2.png"
    )

    ground_path = (
        "ciencia-main/game/assets/chao2.png"
    )

    background_path = (
        "ciencia-main/game/assets/background2.png"
    )


# ============================================================
# SPRITESHEET
# ============================================================

spritesheet = pygame.image.load(
    spritesheet_path
).convert_alpha()


# ============================================================
# FUNDO
# ============================================================

background = pygame.image.load(
    background_path
).convert()


# ============================================================
# CHÃO / MAPA
# ============================================================

ground_image = pygame.image.load(
    ground_path
).convert_alpha()


# Posição do mapa.

ground_x = 0
ground_y = -90


# ============================================================
# POSIÇÕES DOS SPRITES
# ============================================================

frames = [

    pygame.Rect(
        0,
        0,
        512,
        512
    ),

    pygame.Rect(
        2000,
        30,
        512,
        512
    ),

    pygame.Rect(
        0,
        1050,
        512,
        512
    ),

    pygame.Rect(
        2350,
        1050,
        512,
        512
    ),

    pygame.Rect(
        650,
        2080,
        512,
        512
    ),

    pygame.Rect(
        3050,
        2080,
        512,
        512
    ),

    pygame.Rect(
        1020,
        3100,
        512,
        512
    ),

    pygame.Rect(
        1950,
        3550,
        512,
        512
    ),

    pygame.Rect(
        0,
        4630,
        512,
        512
    ),

    pygame.Rect(
        2150,
        4650,
        512,
        512
    ),

    pygame.Rect(
        0,
        5000,
        800,
        800
    )

]


# ============================================================
# TAMANHO DOS FRAMES
# ============================================================

FRAME_SIZES = [

    240,  # 0 - parado
    240,  # 1 - andando
    240,  # 2 - andando
    240,  # 3 - andando
    240,  # 4 - andando
    240,  # 5 - andando
    240,  # 6 - andando
    300,  # 7 - andando
    300,  # 8 - subindo
    300,  # 9 - aterrissando
    100   # 10 - caindo

]


# ============================================================
# CRIAR OS FRAMES
# ============================================================

sprite_frames = []


for frame_index, frame_rect in enumerate(frames):

    # Recorta o sprite.

    frame = spritesheet.subsurface(
        frame_rect
    ).copy()


    # Tamanho do frame.

    sprite_height = FRAME_SIZES[
        frame_index
    ]


    # Mantém a proporção.

    new_width = int(
        frame.get_width()
        * sprite_height
        / frame.get_height()
    )


    # Redimensiona.

    frame = pygame.transform.scale(
        frame,
        (
            new_width,
            sprite_height
        )
    )


    # Guarda.

    sprite_frames.append(
        frame
    )


# ============================================================
# CONTROLE DA ANIMAÇÃO
# ============================================================

current_frame = 0

animation_timer = 0

landing_timer = 0

FRAME_DURATION = 100

LANDING_DURATION = 150

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

gravity = 0.75

jump_strength = -25

speed = 3.4

on_ground = False


# ============================================================
# PLATAFORMAS DA FASE 1
# ============================================================

grounds_fase1 = [

    pygame.Rect(
        20,
        585 + ground_y,
        360,
        25
    ),

    pygame.Rect(
        32,
        492 + ground_y,
        85,
        25
    ),

    pygame.Rect(
        60,
        375 + ground_y,
        225,
        25
    ),

    pygame.Rect(
        267,
        347 + ground_y,
        145,
        25
    ),

    pygame.Rect(
        320,
        214 + ground_y,
        225,
        25
    ),

    pygame.Rect(
        402,
        462 + ground_y,
        110,
        25
    ),

    pygame.Rect(
        404,
        605 + ground_y,
        65,
        25
    ),

    pygame.Rect(
        552,
        713 + ground_y,
        280,
        25
    ),

    pygame.Rect(
        617,
        443 + ground_y,
        135,
        25
    ),

    pygame.Rect(
        703,
        375 + ground_y,
        250,
        25
    ),

    pygame.Rect(
        704,
        558 + ground_y,
        108,
        25
    ),

    pygame.Rect(
        844,
        618 + ground_y,
        70,
        25
    ),

    pygame.Rect(
        900,
        676 + ground_y,
        60,
        25
    ),

    pygame.Rect(
        1045,
        291 + ground_y,
        345,
        25
    ),

    pygame.Rect(
        1160,
        157 + ground_y,
        195,
        25
    ),

    pygame.Rect(
        1100,
        505 + ground_y,
        255,
        25
    ),

    pygame.Rect(
        1032,
        682 + ground_y,
        360,
        25
    ),

    pygame.Rect(
        1437,
        60 + ground_y,
        210,
        25
    ),

    pygame.Rect(
        1418,
        441 + ground_y,
        215,
        25
    ),

    pygame.Rect(
        1495,
        599 + ground_y,
        175,
        25
    ),

    pygame.Rect(
        1655,
        357 + ground_y,
        325,
        25
    ),

    pygame.Rect(
        1675,
        549 + ground_y,
        305,
        25
    ),

    pygame.Rect(
        1750,
        57 + ground_y,
        235,
        25
    ),

    pygame.Rect(
        1630,
        688 + ground_y,
        355,
        25
    )

]


# ============================================================
# PLATAFORMAS DA FASE 2
# ============================================================

grounds_fase2 = [

    # -------------------------
    # ESQUERDA
    # -------------------------

    pygame.Rect(
        15,
        615 + ground_y,
        175,
        25
    ),

    pygame.Rect(
        180,
        645 + ground_y,
        120,
        25
    ),

    pygame.Rect(
        270,
        585 + ground_y,
        105,
        25
    ),

    pygame.Rect(
        318,
        535 + ground_y,
        150,
        25
    ),

    pygame.Rect(
        478,
        565 + ground_y,
        115,
        25
    ),

    pygame.Rect(
        530,
        435 + ground_y,
        100,
        25
    ),

    pygame.Rect(
        605,
        480 + ground_y,
        75,
        25
    ),

    pygame.Rect(
        640,
        438 + ground_y,
        115,
        25
    ),


    # -------------------------
    # CENTRO-ESQUERDA
    # -------------------------

    pygame.Rect(
        735,
        380 + ground_y,
        90,
        25
    ),

    pygame.Rect(
        805,
        535 + ground_y,
        90,
        25
    ),

    pygame.Rect(
        880,
        210 + ground_y,
        85,
        25
    ),

    pygame.Rect(
        928,
        255 + ground_y,
        150,
        25
    ),


    # -------------------------
    # CENTRO
    # -------------------------

    pygame.Rect(
        1125,
        165 + ground_y,
        115,
        25
    ),

    pygame.Rect(
        1205,
        320 + ground_y,
        50,
        25
    ),

    pygame.Rect(
        1265,
        150 + ground_y,
        160,
        25
    ),

    pygame.Rect(
        1320,
        340 + ground_y,
        125,
        25
    ),

    pygame.Rect(
        1110,
        475 + ground_y,
        65,
        25
    ),

    pygame.Rect(
        1395,
        545 + ground_y,
        80,
        25
    ),

    pygame.Rect(
        1415,
        475 + ground_y,
        75,
        25
    ),


    # -------------------------
    # DIREITA
    # -------------------------

    pygame.Rect(
        1465,
        255 + ground_y,
        135,
        25
    ),

    pygame.Rect(
        1575,
        120 + ground_y,
        200,
        25
    ),

    pygame.Rect(
        1630,
        415 + ground_y,
        145,
        25
    ),

    pygame.Rect(
        1670,
        545 + ground_y,
        130,
        25
    ),

    pygame.Rect(
        1420,
        615 + ground_y,
        105,
        25
    ),

    pygame.Rect(
        1530,
        625 + ground_y,
        110,
        25
    ),

    pygame.Rect(
        1640,
        575 + ground_y,
        150,
        25
    ),

    pygame.Rect(
        1760,
        545 + ground_y,
        165,
        25
    ),

    pygame.Rect(
        1825,
        570 + ground_y,
        155,
        25
    ),


    # -------------------------
    # PARTE INFERIOR
    # -------------------------

    pygame.Rect(
        305,
        705 + ground_y,
        70,
        25
    ),

    pygame.Rect(
        680,
        650 + ground_y,
        110,
        25
    ),

    pygame.Rect(
        820,
        660 + ground_y,
        100,
        25
    ),

    pygame.Rect(
        1045,
        640 + ground_y,
        175,
        25
    ),

    pygame.Rect(
        1200,
        700 + ground_y,
        185,
        25
    ),

    pygame.Rect(
        1300,
        675 + ground_y,
        100,
        25
    ),

    pygame.Rect(
        1625,
        700 + ground_y,
        310,
        25
    ),

    pygame.Rect(
        1880,
        605 + ground_y,
        140,
        25
    )

]


# ============================================================
# OBSTÁCULOS QUE CAUSAM DANO - FASE 2
# ============================================================

hazards_fase2 = [

    # -------------------------
    # ESPINHOS DA ESQUERDA
    # -------------------------

    pygame.Rect(
        475,
        535 + ground_y,
        55,
        25
    ),


    # -------------------------
    # ESPINHOS DA PARTE DE CIMA
    # -------------------------

    pygame.Rect(
        1260,
        145 + ground_y,
        70,
        25
    ),


    # -------------------------
    # ESPINHOS DO CENTRO
    # -------------------------

    pygame.Rect(
        805,
        525 + ground_y,
        60,
        25
    ),


    # -------------------------
    # BOLA DE ESPINHOS 1
    # -------------------------

    pygame.Rect(
        1215,
        390 + ground_y,
        45,
        45
    ),


    # -------------------------
    # BOLA DE ESPINHOS 2
    # -------------------------

    pygame.Rect(
        1770,
        255 + ground_y,
        45,
        45
    )

    ]


# ============================================================
# ESCOLHER AS COLISÕES DA FASE
# ============================================================

if fase == 1:

    grounds = grounds_fase1

    hazards = []


elif fase == 2:

    grounds = grounds_fase2

    hazards = hazards_fase2


# ============================================================
# FUNÇÃO DE DANO
# ============================================================

def take_damage():

    global velocity_y
    global on_ground
    global camera_x
    global camera_y
    global current_frame
    global landing_timer

    # Volta para a posição inicial.

    player.x = 100
    player.y = 400


    # Para a queda.

    velocity_y = 0


    # Ainda não está no chão.

    on_ground = False


    # Volta a câmera para o início.

    camera_x = 0
    camera_y = 0


    # Volta para o sprite de queda.

    current_frame = 10


    # Reinicia o timer de aterrissagem.

    landing_timer = pygame.time.get_ticks()


# ============================================================
# CÂMERA
# ============================================================

camera_x = 0

camera_y = 0


# ============================================================
# FUNÇÃO DO FUNDO
# ============================================================

def draw_background(camera_x, camera_y):

    # Limpa a tela.

    screen.fill(BG)


    # Movimento horizontal.

    background_x = -camera_x * 0.1


    # Movimento vertical.

    background_y = (
        -camera_y * 0.1
    ) - 350


    # Desenha o fundo.

    screen.blit(
        background,
        (
            background_x,
            background_y
        )
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

    previous_bottom = player.bottom


    velocity_y += gravity

    player.y += velocity_y


    # ========================================================
    # COLISÃO COM AS PLATAFORMAS
    # ========================================================

    was_on_ground = on_ground

    on_ground = False


    for ground in grounds:

        # Só verifica plataforma
        # enquanto o jogador está caindo.

        if velocity_y < 0:

            continue


        # Verifica sobreposição horizontal.

        horizontal_overlap = (
            player.right > ground.left
            and
            player.left < ground.right
        )


        # Verifica se passou pelo topo.

        crossed_top = (
            previous_bottom <= ground.top
            and
            player.bottom >= ground.top
        )


        if (
            horizontal_overlap
            and
            crossed_top
        ):

            # Começou uma aterrissagem.

            if not was_on_ground:

                landing_timer = current_time


            # Coloca em cima da plataforma.

            player.bottom = ground.top

            velocity_y = 0

            on_ground = True

            break


    # ========================================================
    # DANO DOS OBSTÁCULOS
    # ========================================================

    for hazard in hazards:

        if player.colliderect(hazard):

            take_damage()

            break


    # ========================================================
    # DANO POR CAIR
    # ========================================================

    # O jogador precisa cair bastante
    # abaixo da área visível.

    if player.top > HEIGHT + 200:

        take_damage()


    # ========================================================
    # ANIMAÇÃO
    # ========================================================

    # --------------------------------------------------------
    # NO AR
    # --------------------------------------------------------

    if not on_ground:

        # SUBINDO

        if velocity_y < 0:

            current_frame = 8


        # CAINDO

        else:

            current_frame = 10


    # --------------------------------------------------------
    # ATERRISSANDO
    # --------------------------------------------------------

    elif (
        current_time
        - landing_timer
        <
        LANDING_DURATION
    ):

        current_frame = 9


    # --------------------------------------------------------
    # NO CHÃO
    # --------------------------------------------------------

    else:

        # CAMINHANDO

        if moving:

            if (
                current_frame < 1
                or
                current_frame > 7
            ):

                current_frame = 1

                animation_timer = current_time


            elif (
                current_time
                - animation_timer
                >=
                FRAME_DURATION
            ):

                current_frame += 1


                if current_frame > 7:

                    current_frame = 1


                animation_timer = current_time


        # PARADO

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
        ground_image.get_width()
        - WIDTH
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
    # DESENHAR MAPA
    # ========================================================

    screen.blit(
        ground_image,
        (
            ground_x - camera_x,
            ground_y - camera_y
        )
    )


    # ========================================================
    # ESCOLHER IMAGEM DO PLAYER
    # ========================================================

    if TEST_MODE:

        image = sprite_frames[
            TEST_FRAME
        ]

    else:

        image = sprite_frames[
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


    # ========================================================
    # AJUSTE DO FRAME DE QUEDA
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

    clock.tick(
        FPS
    )


# ============================================================
# ENCERRAR
# ============================================================

pygame.quit()