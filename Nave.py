import pygame
from ElementoJogo import ElementoJogo
from Projetil import Projetil


class Nave(ElementoJogo):
    def __init__(self, largura_tela, altura_tela, velocidade=15, cor=(0, 255, 100)):
        # Inicializa a classe base com posição inicial centralizada embaixo
        super().__init__(
            x=largura_tela // 2 - 20,
            y=altura_tela - 180,
            largura=40,
            altura=40,
            cor=cor,
            velocidade=velocidade
        )

        # definir imagem da nave
        self.image = pygame.image.load('Image\Spaceship.png').convert_alpha()
        self.largura_tela = largura_tela
        self.altura_tela = altura_tela
        self.vel_x = 0
        self.tiros = []  # Lista que guardará os tiros ativos

    def processar_evento(self, evento):
        """Controla os eventos de teclado para movimentação e disparo."""
        if evento.type == pygame.KEYDOWN:
            if evento.key in (pygame.K_LEFT, pygame.K_a):
                self.vel_x = -self.velocidade
            elif evento.key in (pygame.K_RIGHT, pygame.K_d):
                self.vel_x = self.velocidade
            elif evento.key == pygame.K_SPACE:
                self.atirar()

        elif evento.type == pygame.KEYUP:
            if evento.key in (pygame.K_LEFT, pygame.K_a) and self.vel_x < 0:
                self.vel_x = 0
            elif evento.key in (pygame.K_RIGHT, pygame.K_d) and self.vel_x > 0:
                self.vel_x = 0

        elif evento.type == pygame.KEYDOWN:
            if evento.key in pygame.K_SPACE:
                self.atirar()

    def mover(self):
        """Aplica o deslocamento horizontal e trava nas bordas da tela."""
        self.rect.x += self.vel_x

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > self.largura_tela:
            self.rect.right = self.largura_tela

    def atirar(self):
        # =========================================================================
        # TODO 1 (Alunos): Criar um projétil (pygame.Rect) saindo da ponta da nave
        # (ex: largura 4, altura 10) e adicioná-lo à lista self.tiros
        # =========================================================================

        projetil = Projetil(self.rect.x, self.rect.y,self.largura_tela, self.altura_tela)

        self.tiros.append(projetil)


    def atualizar_tiros(self):
        # =========================================================================
        # TODO 2 (Alunos):
        # - Mover cada tiro da lista para cima (diminuir tiro.y)
        # - Remover da lista os tiros que saírem pelo topo da tela (tiro.bottom < 0)
        # =========================================================================

        # O [:] cria uma cópia da lista para o loop.
        # Isso é fundamental porque não devemos modificar (remover itens) de uma lista enquanto a percorremos diretamente.
        for tiro in self.tiros[:]:

            # 1. Movimentação:
            # No Pygame, o ponto (0,0) é o canto superior esquerdo.
            # Para o tiro subir, a coordenada Y precisa diminuir.
            # A velocidade do tiro é herdada de Projetil, pois o mesmo tem esse parâmetro em seu método construtor
            tiro.rect.y -= tiro.velocidade

            # 2. Limpeza de memória:
            # Verifica se a base do retângulo passou do topo da tela
            if tiro.rect.y < 0:
                # Remove o tiro da lista original de tiros ativos
                self.tiros.remove(tiro)

    def atualizar(self):
        self.mover()
        self.atualizar_tiros()

    def desenhar(self, tela):
        tela.blit(self.image, self.rect)

        # Desenha os tiros ativos na cor branca
        for tiro in self.tiros:
            pygame.draw.rect(tela, (255, 255, 255), tiro)