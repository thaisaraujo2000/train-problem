import pygame
import pygame_gui
import sys
import time
import threading

pygame.init()
clock = pygame.time.Clock()

# Cores
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARELO = (255, 255, 0)
CINZA_CLARO = (200, 200, 200)

# Tamanho da tela
LARGURA_TELA = 800
ALTURA_TELA = 600

# Tamanho dos trilhos e trens
LARGURA_TRILHO = 200
ALTURA_TRILHO = 100
LARGURA_TREM = 15
ALTURA_TREM = 15

# Deslocamento
DESL = 0

tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))

# Criação da interface de usuário
manager = pygame_gui.UIManager((LARGURA_TELA, ALTURA_TELA))


# Criação das labels
label1 = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((30, ALTURA_TELA - 150), (150, 20)), 
                                     text='Trem Vermelho:', 
                                     manager=manager)
label2 = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((30, ALTURA_TELA - 120), (150, 20)), 
                                     text='Trem Verde:', 
                                     manager=manager)
label3 = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((30, ALTURA_TELA - 90), (150, 20)), 
                                     text='Trem Azul:', 
                                     manager=manager)
label4 = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((30, ALTURA_TELA - 60), (150, 20)), 
                                     text='Trem Amarelo:', 
                                     manager=manager)

# Criação dos controles deslizantes
slider1 = pygame_gui.elements.UIHorizontalSlider(
    relative_rect=pygame.Rect((200, ALTURA_TELA - 150), (150, 20)),
    start_value=0.0,
    value_range=(0.0, 10.0),
    manager=manager
)

slider2 = pygame_gui.elements.UIHorizontalSlider(
    relative_rect=pygame.Rect((200, ALTURA_TELA - 120), (150, 20)),
    start_value=0.0,
    value_range=(0.0, 10.0),
    manager=manager
)

slider3 = pygame_gui.elements.UIHorizontalSlider(
    relative_rect=pygame.Rect((200, ALTURA_TELA - 90), (150, 20)),
    start_value=0.0,
    value_range=(0.0, 10.0),
    manager=manager
)

slider4 = pygame_gui.elements.UIHorizontalSlider(
    relative_rect=pygame.Rect((200, ALTURA_TELA - 60), (150, 20)),
    start_value=0.0,
    value_range=(0.0, 10.0),
    manager=manager
)

class Trem:
    def __init__(self, x, y, cor, trilho, name):
        self.x = x
        self.y = y
        self.cor = cor
        self.name = name
        self.velocidade = 1  # Adiciona o atributo velocidade
        self.trilho = trilho  # Adiciona o atributo trilho
        self.direcao = "DIREITA"  # Adiciona o atributo direção
        self.deve_continuar = True  # Adiciona um atributo para indicar se o trem deve continuar ou não
        self.aceleracao = 0


    def desenhar(self, tela):
        pygame.draw.rect(tela, self.cor, (self.x, self.y, LARGURA_TREM, ALTURA_TREM))

    def mover(self):
        
        if self.direcao == "DIREITA":
            if self.x + LARGURA_TREM + self.velocidade <= self.trilho.x + LARGURA_TRILHO + DESL:
                self.x += self.velocidade
            else:
                if self.name == "Trem 1":
                    # faz o lock no semáforo 1
                    if semaphore1.acquire(blocking=True):
                        lock4.acquire()
                        lock1.acquire()
                    else:
                        self.direcao = "DIREITA"
                    
                if self.name == "Trem 3":
                    lock3.acquire()
                    # unlock lock4
                    if lock4.locked():
                        semaphore1.release()
                        # libera o trilho 4
                        lock4.release()

                if self.name == "Trem 4":
                    if lock2.locked():
                        # libera o semáforo 1
                        semaphore1.release()
                        # libera o trilho 2
                        lock2.release()

                self.direcao = "BAIXO"
        elif self.direcao == "BAIXO":
            if self.y + ALTURA_TREM + self.velocidade <= self.trilho.y + ALTURA_TRILHO + DESL:
                self.y += self.velocidade
            else:
                if self.name == "Trem 1":
                    if lock1.locked():
                        # semaphore1.release() # talvez precise tirar
                        lock1.release()

                if self.name == "Trem 2":
                    if semaphore1.acquire(blocking=True):
                        # faz o lock no trilho 2
                        lock2.acquire()
                    else:
                        self.direcao = "BAIXO"
                if self.name == "Trem 3":
                    if lock3.locked():
                        # libera o semáforo 1
                        semaphore1.release()
                        # libera o trilho 3
                        lock3.release()
                self.direcao = "ESQUERDA"
        elif self.direcao == "ESQUERDA":
            if self.x - self.velocidade >= self.trilho.x - DESL:
                self.x -= self.velocidade
            else:
                if self.name == "Trem 1":
                    if lock4.locked():
                        # libera o semáforo 4
                        semaphore1.release()
                        # libera o trilho 4
                        lock4.release()
                if self.name == "Trem 2":
                    lock1.acquire()
                    if lock2.locked():
                        # libera o semáforo 1
                        semaphore1.release()
                        # libera o trilho 2
                        lock2.release()
    
                if self.name == "Trem 4":
                    if semaphore1.acquire(blocking=True):
                        # faz o lock no trilho 3
                        lock3.acquire()
                    else:
                        self.direcao = "ESQUERDA"
                self.direcao = "CIMA"
        elif self.direcao == "CIMA":
            if self.y - self.velocidade >= self.trilho.y - DESL:
                self.y -= self.velocidade
            else:            
                if self.name == "Trem 2":
                    if lock1.locked():
                        # libera o semáforo 1
                        semaphore1.release()
                        # libera o trilho 1
                        lock1.release()
                if self.name == "Trem 3":
                    if semaphore1.acquire(blocking=True):
                        # faz o lock no trilho 4
                        lock4.acquire()
                    else:
                        self.direcao = "CIMA"
                if self.name == "Trem 4":
                    # bloqueia o trilho 2
                    lock2.acquire()
                    if lock3.locked():
                        # libera o semáforo 1
                        semaphore1.release()
                        # libera o trilho 3
                        lock3.release()
                self.direcao = "DIREITA"
            

    def mover_thread(self):
        while self.deve_continuar:
                self.mover()
                time.sleep(0.02)

    def parar(self):
        self.deve_continuar = False

class Trilho:
    def __init__(self, x, y, cor):
        self.x = x
        self.y = y
        self.cor = cor

    def desenhar(self, tela):
        pygame.draw.rect(tela, self.cor, (self.x, self.y, LARGURA_TRILHO, ALTURA_TRILHO), 15)

# Instâncias de Trilho
trilho1 = Trilho(LARGURA_TELA//2 - LARGURA_TRILHO + 15, ALTURA_TELA//2 - ALTURA_TRILHO + 15, CINZA_CLARO)
trilho2 = Trilho(LARGURA_TELA//2, ALTURA_TELA//2 - ALTURA_TRILHO + 15, CINZA_CLARO)
trilho3 = Trilho(LARGURA_TELA//2 - LARGURA_TRILHO + 15, ALTURA_TELA//2, CINZA_CLARO)
trilho4 = Trilho(LARGURA_TELA//2, ALTURA_TELA//2, CINZA_CLARO)

# Crie os locks.
lock1 = threading.Lock() # para trilho compartilhado entre trem 1 e trem 2
lock2 = threading.Lock() # para trilho compartilhado entre trem 2 e trem 4
lock3 = threading.Lock() # para trilho compartilhado entre trem 3 e trem 4
lock4 = threading.Lock() # para trilho compartilhado entre trem 1 e trem 3

# Crie os semáforos.
semaphore1 = threading.Semaphore(3)  # Semáforo para controlar a bifucação

# Crie as instâncias de Trem.
trem1 = Trem(LARGURA_TELA//2 - LARGURA_TRILHO + DESL, ALTURA_TELA//2 - ALTURA_TRILHO + 15, VERMELHO, trilho1, "Trem 1")
trem2 = Trem(LARGURA_TELA//2 + DESL, ALTURA_TELA//2 - ALTURA_TRILHO + 15, VERDE, trilho2, "Trem 2")
trem3 = Trem(LARGURA_TELA//2 - LARGURA_TRILHO + DESL, ALTURA_TELA//2 + DESL, AZUL, trilho3, "Trem 3")
trem4 = Trem(LARGURA_TELA//2 + DESL, ALTURA_TELA//2 + DESL, AMARELO, trilho4, "Trem 4")

# Agora, inicie as threads, como você já fez.
thread_trem1 = threading.Thread(target=trem1.mover_thread)
thread_trem2 = threading.Thread(target=trem2.mover_thread)
thread_trem3 = threading.Thread(target=trem3.mover_thread)
thread_trem4 = threading.Thread(target=trem4.mover_thread)

thread_trem1.start()
thread_trem2.start()
thread_trem3.start()
thread_trem4.start()

trens = [trem1, trem2, trem3, trem4]
trilhos = [trilho1, trilho2, trilho3, trilho4]

def atualizar_tela():
    tela.fill((0, 0, 0))  # Preenche a tela com preto
    for trilho in trilhos:
        trilho.desenhar(tela)
    for trem in trens:
        trem.desenhar(tela)
    manager.draw_ui(tela)  # Desenha a interface do usuário
    pygame.display.update()  # Atualiza a tela

while True:
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            for trem in trens:
                trem.parar()
            pygame.quit()
            sys.exit()

        # Atualiza a interface do usuário
        manager.process_events(event)

        # Atualiza a velocidade do trem com base no valor do slider
        if event.type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
            if event.ui_element == slider1:
                trem1.velocidade = slider1.get_current_value() * 1.02 + 0.5  # Multiplica a proporção do valor do controle deslizante por 1.2 para obter um valor de velocidade razoável
            elif event.ui_element == slider2:
                trem2.velocidade = slider2.get_current_value() * 1.02 + 0.5
            elif event.ui_element == slider3:
                trem3.velocidade = slider3.get_current_value() * 1.02 + 0.5
            elif event.ui_element == slider4:
                trem4.velocidade = slider4.get_current_value() * 1.02 + 0.5

    # Atualiza a interface do usuário
    manager.update(time_delta)

    atualizar_tela()