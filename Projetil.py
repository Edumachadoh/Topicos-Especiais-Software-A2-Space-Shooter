import pygame
from ElementoJogo import ElementoJogo


class Projetil(ElementoJogo):
    def __init__(self, x_nave, y_nave, largura_tela, altura_tela, velocidade=10):
        self.largura_tela = largura_tela
        self.altura_tela = altura_tela
        self.raio = 20

        super().__init__(
            x=x_nave,
            y=y_nave,
            largura=self.raio * 2,
            altura=self.raio * 2,
            velocidade=velocidade
        )

    def mover(self):
        self.rect.y += self.velocidade

    def desenhar(self, tela):
        # Polimorfismo: desenha o asteroide como círculo
        pygame.draw.circle(tela, self.cor, self.rect.center, self.raio)