import pygame

from Asteroid import Asteroid
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
        self.nave = Nave(self.largura, self.altura)
        self.asteroide = Asteroid(self.largura, self.altura)

    def processar_eventos(self):
        for evento in pygame.event.get():   
            if evento.type == pygame.QUIT:
                self.rodando = False
            self.nave.processar_evento(evento)

    def checar_colisoes(self):
        #checagem de colisões
        for tiro in self.nave.tiros[:]:
            if tiro.rect.colliderect(self.asteroide.rect):
                self.nave.tiros.remove(tiro)
                self.asteroide.iniciar_status()
                self.pontos += 1

        if self.nave.rect.colliderect(self.asteroide.rect):
            self.fim_de_jogo = True

    def atualizar(self):
        self.nave.atualizar()
        self.asteroide.mover()
        self.checar_colisoes()

    def desenhar(self):
        self.tela.fill((15, 15, 25))  # fundo
        self.nave.desenhar(self.tela)
        self.asteroide.desenhar(self.tela)
        pygame.display.flip()
        # =========================================================================
        # TODO 5 (Alunos): Implementar a exibição de pontos na tela
        # =========================================================================

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
