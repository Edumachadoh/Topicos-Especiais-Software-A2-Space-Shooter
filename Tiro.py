import pygame

from ElementoJogo import ElementoJogo


class Tiro(ElementoJogo):
    def __init__(self, x_nave, y_nave, largura_tela, altura_tela, velocidade=25):
        self.largura_tela = largura_tela
        self.altura_tela = altura_tela

        super().__init__(
            x=x_nave,
            y=y_nave,
            largura=50,
            altura=50,
            velocidade=velocidade,
        )

    def mover(self):
        self.rect.y -= self.velocidade

    def desenhar(self, tela):
        # Polimorfismo: desenha o asteroide como círculo
        pygame.draw.rect(tela, self.cor, self.rect.center, self.largura)
