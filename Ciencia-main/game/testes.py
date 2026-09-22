"""
import pygame

pygame.init()


# ============================================================
# CONFIGURAÇÕES DA JANELA
# ============================================================

WIDTH = 1200
HEIGHT = 720
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
# FASE
# ============================================================

fase = 1


# ============================================================
# JOGADOR
# ============================================================

# Posição inicial de cada fase.

spawn_points = {

    1: (100, 400),

    2: (100, 400),

    3: (100, 175)

}


player = pygame.Rect(
    spawn_points[fase][0],
    spawn_points[fase][1],
    64,
    80
)


# ============================================================
# POSIÇÃO DO MAPA
# ============================================================

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
# OBSTÁCULOS DA FASE 2
# ============================================================

hazards_fase2 = [

    # Espinhos

    pygame.Rect(
        475,
        535 + ground_y,
        55,
        25
    ),

    pygame.Rect(
        1260,
        145 + ground_y,
        70,
        25
    ),

    pygame.Rect(
        805,
        525 + ground_y,
        60,
        25
    ),

    # Bola de espinhos 1

    pygame.Rect(
        1215,
        390 + ground_y,
        45,
        45
    ),

    # Bola de espinhos 2

    pygame.Rect(
        1770,
        255 + ground_y,
        45,
        45
    )

]


# ============================================================
# PLATAFORMAS DA FASE 3
# ============================================================

grounds_fase3 = [

    # -------------------------
    # ESQUERDA
    # -------------------------

    pygame.Rect(
        5,
        200 + ground_y,
        225,
        22
    ),

    pygame.Rect(
        5,
        345 + ground_y,
        230,
        22
    ),

    pygame.Rect(
        220,
        366 + ground_y,
        335,
        22
    ),

    pygame.Rect(
        445,
        527 + ground_y,
        110,
        22
    ),

    pygame.Rect(
        535,
        538 + ground_y,
        90,
        22
    ),

    pygame.Rect(
        560,
        418 + ground_y,
        170,
        22
    ),

    # -------------------------
    # PARTE SUPERIOR
    # -------------------------

    pygame.Rect(
        670,
        230 + ground_y,
        260,
        22
    ),

    pygame.Rect(
        910,
        370 + ground_y,
        100,
        22
    ),

    # -------------------------
    # CENTRO
    # -------------------------

    pygame.Rect(
        770,
        468 + ground_y,
        140,
        22
    ),

    pygame.Rect(
        1015,
        468 + ground_y,
        180,
        22
    ),

    pygame.Rect(
        1100,
        292 + ground_y,
        180,
        22
    ),



    pygame.Rect(
        1220,
        504 + ground_y,
        165,
        22
    ),



    # -------------------------
    # DIREITA-CENTRO
    # -------------------------

    pygame.Rect(
        1430,
        530 + ground_y,
        180,
        22
    ),

    pygame.Rect(
        1605,
        366 + ground_y,
        105,
        22
    ),

    pygame.Rect(
        1635,
        515 + ground_y,
        170,
        22
    ),

    pygame.Rect(
        1740,
        402 + ground_y,
        75,
        22
    ),

    # -------------------------
    # EXTREMA DIREITA
    # -------------------------

    pygame.Rect(
        1815,
        312 + ground_y,
        220,
        22
    ),

    pygame.Rect(
        1835,
        458 + ground_y,
        205,
        22
    )

]


# ============================================================
# OBSTÁCULOS DA FASE 3
# ============================================================

hazards_fase3 = []


# ============================================================
# PORTAS DA FASE 1
# ============================================================

doors_fase1 = [

    # Porta de acesso para a Fase 2.
    # É a porta no centro do mapa.

    pygame.Rect(
        1170,
        180 + ground_y,
        130,
        120
    )
]


# ============================================================
# PORTAS DA FASE 2
# ============================================================

doors_fase2 = [

    pygame.Rect(
        1610,
        25 + ground_y,
        110,
        130
    )

]


# ============================================================
# PORTAS DA FASE 3
# ============================================================

doors_fase3 = [

    pygame.Rect(
        75,
        375 + ground_y,
        130,
        110
    )

]


# ============================================================
# VARIÁVEIS DA FASE
# ============================================================

spritesheet = None
background = None
ground_image = None

sprite_frames = []

grounds = []
hazards = []
doors = []


# ============================================================
# CRIAR OS FRAMES
# ============================================================

def create_sprite_frames():

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


    return sprite_frames


# ============================================================
# CARREGAR FASE
# ============================================================

def load_phase(new_phase):

    global fase
    global spritesheet
    global background
    global ground_image
    global sprite_frames
    global grounds
    global hazards
    global doors


    # ========================================================
    # FASE 1
    # ========================================================

    if new_phase == 1:

        spritesheet = pygame.image.load(
            "ciencia-main/game/assets/spritesheet4.png"
        ).convert_alpha()

        ground_image = pygame.image.load(
            "ciencia-main/game/assets/chao.png"
        ).convert_alpha()

        background = pygame.image.load(
            "ciencia-main/game/assets/background1.png"
        ).convert()

        grounds = grounds_fase1

        hazards = []

        doors = doors_fase1


    # ========================================================
    # FASE 2
    # ========================================================

    elif new_phase == 2:

        spritesheet = pygame.image.load(
            "ciencia-main/game/assets/spritesheet2.png"
        ).convert_alpha()

        ground_image = pygame.image.load(
            "ciencia-main/game/assets/chao2.png"
        ).convert_alpha()

        background = pygame.image.load(
            "ciencia-main/game/assets/background2.png"
        ).convert()

        grounds = grounds_fase2

        hazards = hazards_fase2

        doors = doors_fase2


    # ========================================================
    # FASE 3
    # ========================================================

    elif new_phase == 3:

        spritesheet = pygame.image.load(
            "ciencia-main/game/assets/spritesheet3.png"
        ).convert_alpha()

        ground_image = pygame.image.load(
            "ciencia-main/game/assets/chao3.png"
        ).convert_alpha()

        background = pygame.image.load(
            "ciencia-main/game/assets/background3.png"
        ).convert()

        grounds = grounds_fase3

        hazards = hazards_fase3

        doors = doors_fase3


    # Atualiza a fase.

    fase = new_phase


    # ========================================================
    # CRIA NOVAMENTE OS SPRITES
    # ========================================================

    sprite_frames = create_sprite_frames()


# ============================================================
# ANIMAÇÃO
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
# FÍSICA
# ============================================================

velocity_y = 0

gravity = 0.75

jump_strength = -25

speed = 3.4

on_ground = False


# ============================================================
# DANO
# ============================================================

def take_damage():

    global velocity_y
    global on_ground
    global camera_x
    global camera_y
    global current_frame
    global landing_timer
    global animation_timer


    # Volta para o spawn da fase atual.

    player.x = spawn_points[fase][0]

    player.y = spawn_points[fase][1]


    # Para a queda.

    velocity_y = 0


    # Ainda não está no chão.

    on_ground = False


    # Volta a câmera.

    camera_x = 0
    camera_y = 0


    # Reinicia a animação.

    current_frame = 10

    animation_timer = pygame.time.get_ticks()

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

    background_x = (
        -camera_x
        * 0.1
    )


    # ========================================================
    # POSIÇÃO VERTICAL DO BACKGROUND
    # ========================================================

    if fase == 1:

        background_y = (
            -camera_y
            * 0.1
        ) - 100


    elif fase == 2:

        background_y = (
            -camera_y
            * 0.1
        ) - 50


    elif fase == 3:

        background_y = (
            -camera_y
            * 0.1
        ) - 50


    # Desenha.

    screen.blit(
        background,
        (
            background_x,
            background_y
        )
    )


# ============================================================
# TRANSIÇÃO ENTRE FASES
# ============================================================

transitioning = False

transition_alpha = 0

transition_direction = 1

next_phase = None

FADE_SPEED = 12


# ============================================================
# CARREGAR A FASE INICIAL
# ============================================================

load_phase(
    fase
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
    # JOGO
    # ========================================================

    # Durante a transição,
    # congelamos o personagem.

    if not transitioning:

        # ====================================================
        # TECLADO
        # ====================================================

        keys = pygame.key.get_pressed()


        # ====================================================
        # MOVIMENTO HORIZONTAL
        # ====================================================

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


        # ====================================================
        # PULO
        # ====================================================

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


        # ====================================================
        # GRAVIDADE
        # ====================================================

        previous_bottom = player.bottom

        velocity_y += gravity

        player.y += velocity_y


        # ====================================================
        # COLISÃO COM PLATAFORMAS
        # ====================================================

        was_on_ground = on_ground

        on_ground = False


        for ground in grounds:

            # Só colide enquanto está caindo.

            if velocity_y < 0:

                continue


            # Sobreposição horizontal.

            horizontal_overlap = (
                player.right > ground.left
                and
                player.left < ground.right
            )


            # Passou pelo topo.

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

                # Acabou de pousar.

                if not was_on_ground:

                    landing_timer = (
                        current_time
                    )


                # Coloca em cima da plataforma.

                player.bottom = ground.top

                velocity_y = 0

                on_ground = True

                break


        # ====================================================
        # DANO
        # ====================================================

        took_damage = False


        for hazard in hazards:

            if player.colliderect(
                hazard
            ):

                take_damage()

                took_damage = True

                break


        # ====================================================
        # DANO POR QUEDA
        # ====================================================

        if (
            player.top
            >
            HEIGHT + 200
        ):

            take_damage()

            took_damage = True


        # ====================================================
        # PORTA
        # ====================================================

        if not took_damage:

            for door in doors:

                if player.colliderect(
                    door
                ):

                    # Só existe uma próxima fase
                    # até a fase 3.

                    if fase < 3:

                        next_phase = (
                            fase + 1
                        )

                        transitioning = True

                        transition_alpha = 0

                        transition_direction = 1


                    break


        # ====================================================
        # ANIMAÇÃO
        # ====================================================

        # ----------------------------------------------------
        # NO AR
        # ----------------------------------------------------

        if not on_ground:

            # SUBINDO

            if velocity_y < 0:

                current_frame = 8


            # CAINDO

            else:

                current_frame = 10


        # ----------------------------------------------------
        # ATERRISSANDO
        # ----------------------------------------------------

        elif (
            current_time
            -
            landing_timer
            <
            LANDING_DURATION
        ):

            current_frame = 9


        # ----------------------------------------------------
        # NO CHÃO
        # ----------------------------------------------------

        else:

            # CAMINHANDO

            if moving:

                if (
                    current_frame < 1
                    or
                    current_frame > 7
                ):

                    current_frame = 1

                    animation_timer = (
                        current_time
                    )


                elif (
                    current_time
                    -
                    animation_timer
                    >=
                    FRAME_DURATION
                ):

                    current_frame += 1


                    if current_frame > 7:

                        current_frame = 1


                    animation_timer = (
                        current_time
                    )


            # PARADO

            else:

                current_frame = 0


    # ========================================================
    # TRANSIÇÃO ENTRE FASES
    # ========================================================

    if transitioning:

        # ----------------------------------------------------
        # ESCURECER
        # ----------------------------------------------------

        if transition_direction == 1:

            transition_alpha += FADE_SPEED


            if transition_alpha >= 255:

                transition_alpha = 255


                # Troca a fase completamente
                # enquanto a tela está preta.

                load_phase(
                    next_phase
                )


                # Novo spawn.

                player.x = spawn_points[
                    fase
                ][0]

                player.y = spawn_points[
                    fase
                ][1]


                # Reseta física.

                velocity_y = 0

                on_ground = False


                # Reseta animação.

                current_frame = 0

                animation_timer = current_time

                landing_timer = current_time


                # Começa a aparecer.

                transition_direction = -1


        # ----------------------------------------------------
        # CLAREAR
        # ----------------------------------------------------

        else:

            transition_alpha -= FADE_SPEED


            if transition_alpha <= 0:

                transition_alpha = 0

                transitioning = False

                next_phase = None


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
        max(
            0,
            ground_image.get_width()
            -
            WIDTH
        )
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
    # ESCOLHER SPRITE
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
    # VIRAR PARA ESQUERDA
    # ========================================================

    if not facing_right:

        image = pygame.transform.flip(
            image,
            True,
            False
        )


    # ========================================================
    # POSIÇÃO DO SPRITE
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
    # DESENHAR PLAYER
    # ========================================================

    screen.blit(
        image,
        (
            image_x,
            image_y
        )
    )


    # ========================================================
    # FADE PRETO
    # ========================================================

    if transition_alpha > 0:

        fade_surface = pygame.Surface(
            (
                WIDTH,
                HEIGHT
            )
        )


        fade_surface.fill(
            (0, 0, 0)
        )


        fade_surface.set_alpha(
            int(transition_alpha)
        )


        screen.blit(
            fade_surface,
            (
                0,
                0
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

chao_rects = [
    pygame.Rect(0, 218, 225, 24),
    pygame.Rect(0, 378, 242, 26),
    pygame.Rect(304, 277, 84, 22),
    pygame.Rect(298, 383, 145, 24),
    pygame.Rect(426, 312, 94, 22),
    pygame.Rect(409, 496, 168, 24),
    pygame.Rect(568, 263, 177, 24),
    pygame.Rect(645, 414, 145, 24),
    pygame.Rect(754, 319, 95, 22),
    pygame.Rect(753, 503, 120, 24),
    pygame.Rect(892, 374, 146, 24),
    pygame.Rect(894, 523, 74, 22),
    pygame.Rect(895, 353, 143, 22),
    pygame.Rect(1068, 540, 70, 22),
    pygame.Rect(1180, 403, 83, 22),
    pygame.Rect(1250, 480, 181, 24),
    pygame.Rect(1285, 311, 150, 24),
    pygame.Rect(1418, 416, 145, 24),
    pygame.Rect(1514, 502, 136, 24),
    pygame.Rect(1545, 530, 120, 22),
    pygame.Rect(1610, 419, 137, 24),
    pygame.Rect(1650, 585, 115, 22),
    pygame.Rect(1768, 582, 126, 24),
    pygame.Rect(1837, 566, 132, 24),
    pygame.Rect(1922, 507, 112, 24),
    pygame.Rect(1982, 337, 190, 25),
    pygame.Rect(1917, 590, 132, 24),
]

hazard_rects = [
    pygame.Rect(267, 460, 48, 48),
    pygame.Rect(538, 333, 52, 52),
    pygame.Rect(563, 421, 43, 48),
    pygame.Rect(603, 470, 46, 48),
    pygame.Rect(876, 561, 50, 48),
    pygame.Rect(1110, 433, 50, 50),
    pygame.Rect(1161, 522, 49, 50),
    pygame.Rect(1480, 332, 53, 53),
    pygame.Rect(306, 267, 80, 20),
    pygame.Rect(354, 372, 84, 20),
    pygame.Rect(643, 404, 100, 20),
    pygame.Rect(1254, 470, 177, 20),
    pygame.Rect(1610, 407, 135, 20),
    pygame.Rect(1760, 572, 130, 20),
    pygame.Rect(1058, 386, 20, 167),
    pygame.Rect(1739, 420, 20, 171),
]

def checar_colisao_chao(player_rect):
    return any(player_rect.colliderect(rect) for rect in chao_rects)

def checar_hazard(player_rect):
    return any(player_rect.colliderect(rect) for rect in hazard_rects)

# Exemplo:
# if checar_hazard(player.rect):
#     player.morrer()  # ou reiniciar a fase

# ============================================================
# ENCERRAR
# ============================================================

pygame.quit()"""
import pygame

pygame.init()


# ============================================================
# CONFIGURAÇÕES DA JANELA
# ============================================================

WIDTH = 1200
HEIGHT = 720
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
# FASE
# ============================================================

fase = 1


# ============================================================
# POSIÇÃO DO MAPA
# ============================================================

ground_x = 0
ground_y = -90


# ============================================================
# PONTOS DE NASCIMENTO
# ============================================================

spawn_points = {

    1: (100, 400),

    2: (100, 400),

    3: (100, 175),

    4: (100, 400)

}


# ============================================================
# JOGADOR
# ============================================================

player = pygame.Rect(
    spawn_points[fase][0],
    spawn_points[fase][1],
    64,
    80
)


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
# OBSTÁCULOS DA FASE 2
# ============================================================

hazards_fase2 = [

    # Espinhos

    pygame.Rect(
        475,
        535 + ground_y,
        55,
        25
    ),

    pygame.Rect(
        1260,
        145 + ground_y,
        70,
        25
    ),

    pygame.Rect(
        805,
        525 + ground_y,
        60,
        25
    ),

    # Bola de espinhos 1

    pygame.Rect(
        1215,
        390 + ground_y,
        45,
        45
    ),

    # Bola de espinhos 2

    pygame.Rect(
        1770,
        255 + ground_y,
        45,
        45
    )

]


# ============================================================
# PLATAFORMAS DA FASE 3
# ============================================================

grounds_fase3 = [

    # -------------------------
    # ESQUERDA
    # -------------------------

    # Ilha superior esquerda

    pygame.Rect(
        0,
        204 + ground_y,
        242,
        24
    ),

    # Ilha grande esquerda

    pygame.Rect(
        0,
        349 + ground_y,
        242,
        24
    ),

    # Plataforma grande à direita da ilha

    pygame.Rect(
        235,
        367 + ground_y,
        320,
        22
    ),

    # Plataformas inferiores

    pygame.Rect(
        235,
        518 + ground_y,
        130,
        22
    ),

    pygame.Rect(
        395,
        540 + ground_y,
        82,
        20
    ),

    pygame.Rect(
        485,
        542 + ground_y,
        90,
        20
    ),

    # Plataforma do telescópio

    pygame.Rect(
        530,
        414 + ground_y,
        202,
        22
    ),


    # -------------------------
    # PARTE SUPERIOR
    # -------------------------

    # Ilha flutuante grande

    pygame.Rect(
        668,
        226 + ground_y,
        268,
        22
    ),


    # Ilha pequena

    pygame.Rect(
        914,
        368 + ground_y,
        96,
        21
    ),


    # -------------------------
    # CENTRO
    # -------------------------

    # Plataforma do terrário

    pygame.Rect(
        778,
        470 + ground_y,
        132,
        21
    ),

    # Plataforma do átomo

    pygame.Rect(
        1015,
        470 + ground_y,
        181,
        22
    ),

    # Ilha superior com cachoeira

    pygame.Rect(
        1102,
        285 + ground_y,
        181,
        23
    ),

    # Ilha pequena

    pygame.Rect(
        1292,
        329 + ground_y,
        80,
        21
    ),

    # Plataforma inferior central

    pygame.Rect(
        1220,
        507 + ground_y,
        165,
        21
    ),

    # Ilha pequena

    pygame.Rect(
        1407,
        410 + ground_y,
        76,
        21
    ),


    # -------------------------
    # DIREITA-CENTRO
    # -------------------------

    # Plataforma com equipamento

    pygame.Rect(
        1434,
        529 + ground_y,
        180,
        22
    ),

    # Ilha superior

    pygame.Rect(
        1605,
        366 + ground_y,
        107,
        21
    ),

    # Plataforma do painel solar

    pygame.Rect(
        1635,
        512 + ground_y,
        170,
        22
    ),

    # Ilha pequena

    pygame.Rect(
        1740,
        402 + ground_y,
        76,
        21
    ),


    # -------------------------
    # EXTREMA DIREITA
    # -------------------------

    # Plataforma do laboratório

    pygame.Rect(
        1815,
        310 + ground_y,
        225,
        23
    ),

    # Plataforma inferior direita

    pygame.Rect(
        1837,
        457 + ground_y,
        210,
        22
    )

]


# ============================================================
# OBSTÁCULOS DA FASE 3
# ============================================================

# Os Rects que estavam aqui anteriormente
# pertenciam a posições erradas.
#
# Como a imagem da fase 3 não apresenta
# aqueles obstáculos naquelas coordenadas,
# deixamos a fase sem hazards por enquanto.

hazards_fase3 = []



doors_fase1 = [

    # PORTA DE SAÍDA DA FASE 1.
    #
    # Esta NÃO é a porta grande
    # da entrada da esquerda.

    pygame.Rect(
        1170,
        180 + ground_y,
        130,
        120
    )

]


# ============================================================
# PORTAS DA FASE 2
# ============================================================

doors_fase2 = [

    # Porta no topo da estrutura direita.

    pygame.Rect(
        1610,
        25 + ground_y,
        110,
        130
    )

]


# ============================================================
# PORTAS DA FASE 3
# ============================================================

doors_fase3 = [

    # Porta do laboratório na extrema direita.

    pygame.Rect(
        1950,
        270 + ground_y,
        60,
        70
    )

]


# ============================================================
# PORTAS DA FASE 4
# ============================================================


# ============================================================
# CRIAR OS FRAMES
# ============================================================

def create_sprite_frames():

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
            *
            sprite_height
            /
            frame.get_height()
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


    return sprite_frames


# ============================================================
# CARREGAR FASE
# ============================================================

def load_phase(new_phase):

    global fase

    global spritesheet

    global background

    global ground_image

    global sprite_frames

    global grounds

    global hazards

    global doors


    # ========================================================
    # FASE 1
    # ========================================================

    if new_phase == 1:

        spritesheet = pygame.image.load(
            "ciencia-main/game/assets/spritesheet1.png"
        ).convert_alpha()


        ground_image = pygame.image.load(
            "ciencia-main/game/assets/chao.png"
        ).convert_alpha()


        background = pygame.image.load(
            "ciencia-main/game/assets/background1.png"
        ).convert()


        grounds = grounds_fase1

        hazards = []

        doors = doors_fase1


    # ========================================================
    # FASE 2
    # ========================================================

    elif new_phase == 2:

        spritesheet = pygame.image.load(
            "ciencia-main/game/assets/spritesheet2.png"
        ).convert_alpha()


        ground_image = pygame.image.load(
            "ciencia-main/game/assets/chao2.png"
        ).convert_alpha()


        background = pygame.image.load(
            "ciencia-main/game/assets/background2.png"
        ).convert()


        grounds = grounds_fase2

        hazards = hazards_fase2

        doors = doors_fase2


    # ========================================================
    # FASE 3
    # ========================================================

    elif new_phase == 3:

        spritesheet = pygame.image.load(
            "ciencia-main/game/assets/spritesheet3.png"
        ).convert_alpha()


        ground_image = pygame.image.load(
            "ciencia-main/game/assets/chao3.png"
        ).convert_alpha()


        background = pygame.image.load(
            "ciencia-main/game/assets/background3.png"
        ).convert()


        grounds = grounds_fase3

        hazards = hazards_fase3

        doors = doors_fase3


    # ========================================================

    # Atualiza a fase.

    fase = new_phase


    # ========================================================
    # CRIA OS SPRITES
    # ========================================================

    sprite_frames = create_sprite_frames()


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
# FÍSICA
# ============================================================

velocity_y = 0

gravity = 0.75

jump_strength = -25

speed = 3.4

on_ground = False


# ============================================================
# DANO
# ============================================================

def take_damage():

    global velocity_y

    global on_ground

    global camera_x

    global camera_y

    global current_frame

    global animation_timer

    global landing_timer


    # Volta para o início da fase atual.

    player.x = spawn_points[fase][0]

    player.y = spawn_points[fase][1]


    # Para a queda.

    velocity_y = 0


    # Ainda não está no chão.

    on_ground = False


    # Volta a câmera.

    camera_x = 0

    camera_y = 0


    # Reinicia animação.

    current_frame = 10

    animation_timer = pygame.time.get_ticks()

    landing_timer = pygame.time.get_ticks()


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

    # Limpa a tela.

    screen.fill(BG)


    # Movimento horizontal.

    background_x = (
        -camera_x
        *
        0.1
    )


    # ========================================================
    # POSIÇÃO VERTICAL
    # ========================================================

    if fase == 1:

        background_y = (
            -camera_y
            *
            0.1
        ) - 100


    elif fase == 2:

        background_y = (
            -camera_y
            *
            0.1
        ) - 50


    elif fase == 3:

        background_y = (
            -camera_y
            *
            0.1
        ) - 50


    elif fase == 4:

        background_y = (
            -camera_y
            *
            0.1
        ) - 50


    # Desenha.

    screen.blit(
        background,
        (
            background_x,
            background_y
        )
    )


# ============================================================
# TRANSIÇÃO ENTRE FASES
# ============================================================

transitioning = False

transition_alpha = 0

transition_direction = 1

next_phase = None

FADE_SPEED = 12


# ============================================================
# CARREGAR A FASE INICIAL
# ============================================================

load_phase(
    fase
)


# ============================================================
# LOOP PRINCIPAL
# ============================================================

running = True


while running:

    # ========================================================
    # TEMPO
    # ========================================================

    current_time = (
        pygame.time.get_ticks()
    )


    # ========================================================
    # EVENTOS
    # ========================================================

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False


    # ========================================================
    # JOGO
    # ========================================================

    if not transitioning:

        # ====================================================
        # TECLADO
        # ====================================================

        keys = pygame.key.get_pressed()


        # ====================================================
        # MOVIMENTO HORIZONTAL
        # ====================================================

        moving = False


        if (
            keys[pygame.K_a]
            or
            keys[pygame.K_LEFT]
        ):

            player.x -= speed

            facing_right = False

            moving = True


        if (
            keys[pygame.K_d]
            or
            keys[pygame.K_RIGHT]
        ):

            player.x += speed

            facing_right = True

            moving = True


        # ====================================================
        # PULO
        # ====================================================

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


        # ====================================================
        # GRAVIDADE
        # ====================================================

        previous_bottom = player.bottom


        velocity_y += gravity

        player.y += velocity_y


        # ====================================================
        # COLISÃO COM PLATAFORMAS
        # ====================================================

        was_on_ground = on_ground

        on_ground = False


        for ground in grounds:

            # Só colide caindo.

            if velocity_y < 0:

                continue


            # Sobreposição horizontal.

            horizontal_overlap = (
                player.right > ground.left
                and
                player.left < ground.right
            )


            # Cruzou o topo.

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

                # Acabou de pousar.

                if not was_on_ground:

                    landing_timer = (
                        current_time
                    )


                # Coloca exatamente
                # no topo da plataforma.

                player.bottom = ground.top

                velocity_y = 0

                on_ground = True

                break


        # ====================================================
        # DANO DOS OBSTÁCULOS
        # ====================================================

        took_damage = False


        for hazard in hazards:

            if player.colliderect(
                hazard
            ):

                take_damage()

                took_damage = True

                break


        # ====================================================
        # DANO POR QUEDA
        # ====================================================

        if (
            player.top
            >
            HEIGHT + 200
        ):

            take_damage()

            took_damage = True


        # ====================================================
        # PORTA
        # ====================================================

        if not took_damage:

            for door in doors:

                if player.colliderect(
                    door
                ):

                    # Existe próxima fase
                    # enquanto não chegou
                    # na fase 4.

                    if fase < 4:

                        next_phase = (
                            fase + 1
                        )

                        transitioning = True

                        transition_alpha = 0

                        transition_direction = 1


                    break


        # ====================================================
        # ANIMAÇÃO
        # ====================================================

        # ----------------------------------------------------
        # NO AR
        # ----------------------------------------------------

        if not on_ground:

            # SUBINDO

            if velocity_y < 0:

                current_frame = 8


            # CAINDO

            else:

                current_frame = 10


        # ----------------------------------------------------
        # ATERRISSANDO
        # ----------------------------------------------------

        elif (
            current_time
            -
            landing_timer
            <
            LANDING_DURATION
        ):

            current_frame = 9


        # ----------------------------------------------------
        # NO CHÃO
        # ----------------------------------------------------

        else:

            # CAMINHANDO

            if moving:

                if (
                    current_frame < 1
                    or
                    current_frame > 7
                ):

                    current_frame = 1

                    animation_timer = (
                        current_time
                    )


                elif (
                    current_time
                    -
                    animation_timer
                    >=
                    FRAME_DURATION
                ):

                    current_frame += 1


                    if current_frame > 7:

                        current_frame = 1


                    animation_timer = (
                        current_time
                    )


            # PARADO

            else:

                current_frame = 0


    # ========================================================
    # TRANSIÇÃO ENTRE FASES
    # ========================================================

    if transitioning:

        # ----------------------------------------------------
        # ESCURECER
        # ----------------------------------------------------

        if transition_direction == 1:

            transition_alpha += (
                FADE_SPEED
            )


            if transition_alpha >= 255:

                transition_alpha = 255


                # Troca a fase enquanto
                # a tela está totalmente preta.

                load_phase(
                    next_phase
                )


                # Novo spawn.

                player.x = spawn_points[
                    fase
                ][0]

                player.y = spawn_points[
                    fase
                ][1]


                # Zera física.

                velocity_y = 0

                on_ground = False


                # Reinicia animação.

                current_frame = 0

                animation_timer = (
                    current_time
                )

                landing_timer = (
                    current_time
                )


                # Agora começa a clarear.

                transition_direction = -1


        # ----------------------------------------------------
        # CLAREAR
        # ----------------------------------------------------

        else:

            transition_alpha -= (
                FADE_SPEED
            )


            if transition_alpha <= 0:

                transition_alpha = 0

                transitioning = False

                next_phase = None


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
        max(
            0,
            ground_image.get_width()
            -
            WIDTH
        )
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
    # ESCOLHER SPRITE
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
    # POSIÇÃO DO SPRITE
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
    # DESENHAR PLAYER
    # ========================================================

    screen.blit(
        image,
        (
            image_x,
            image_y
        )
    )


    # ========================================================
    # FADE PRETO
    # ========================================================

    if transition_alpha > 0:

        fade_surface = pygame.Surface(
            (
                WIDTH,
                HEIGHT
            )
        )


        fade_surface.fill(
            (0, 0, 0)
        )


        fade_surface.set_alpha(
            int(
                transition_alpha
            )
        )


        screen.blit(
            fade_surface,
            (
                0,
                0
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