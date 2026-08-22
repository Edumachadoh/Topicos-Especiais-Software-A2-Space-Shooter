import pygame

from Asteroid import Asteroid
from InterfaceVisual import InterfaceVisual
from Nave import Nave


class Jogo:
    def __init__(self, largura=800, altura=600):
        # Iniciando o pygame
        pygame.init()

        # Configurações da tela
        self.largura = largura
        self.altura = altura
        self.tela = pygame.display.set_mode((self.largura, self.altura))

        # mudando o icone e o título da tela
        pygame.display.set_caption("Space Shooter - Projeto Base")
        icone = pygame.image.load("./Image/Spaceship.png").convert()
        pygame.display.set_icon(icone)

        self.clock = pygame.time.Clock()
        self.fps = 30
        self.rodando = True
        self.fim_de_jogo = False
        self.pontos = 0

        # Elementos do jogo
        self.inteface_visual = InterfaceVisual()
        self.nave = Nave(self.largura, self.altura)
        self.asteroide = Asteroid(self.largura, self.altura)

    def processar_eventos(self):
        for evento in pygame.event.get():   
            if evento.type == pygame.QUIT:
                self.rodando = False

            #se não for fim de jogo ele recebe inputs
            # se ele apertar R ele recomeça
            # se apertar esc fecha o jogo
            if not self.fim_de_jogo:
                self.nave.processar_evento(evento)
            else:
                match(self.inteface_visual.processar_evento(evento)):
                    case 1:
                        self.fim_de_jogo = False
                        self.pontos = 0
                    case 2:
                        self.rodando = False



    def checar_colisoes(self):
        #checagem de colisões

        #vendo em cada tiro da nave se ele colidiu com o asteroide
        for tiro in self.nave.tiros[:]:
            if tiro.rect.colliderect(self.asteroide.rect):
                self.nave.tiros.remove(tiro)
                self.asteroide.iniciar_status()
                self.pontos += 1

        #se a nave acertar o asteroide, fim de jogo
        if self.nave.rect.colliderect(self.asteroide.rect):
            self.fim_de_jogo = True

    def atualizar(self):
        self.nave.atualizar()
        self.asteroide.mover()
        self.checar_colisoes()

    def desenhar(self):
        self.tela.fill((15, 15, 25))# fundo

        self.inteface_visual.desenhar(self.pontos, self.altura, self.largura, self.tela, self.fim_de_jogo)
        self.nave.desenhar(self.tela)
        self.asteroide.desenhar(self.tela)
        pygame.display.flip()

    def executar(self):

        while self.rodando:
            self.clock.tick(self.fps)
            self.processar_eventos()
            self.atualizar()
            self.desenhar()

        pygame.quit()



if __name__ == "__main__":
    jogo = Jogo()
    jogo.executar()
