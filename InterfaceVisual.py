import pygame


class InterfaceVisual:
    def __init__(self):
        #adicionando fonte para o placar
        self.fonte = pygame.font.Font(None, 36)

    # método para desenhar os pontos
    def __desenhar_pontos__(self, pontos, tela):
        texto = self.fonte.render(f"Pontos: {pontos}", True, (255, 255, 255))
        tela.blit(texto, (10, 10))

    def __desenhar_fim_de_jogo__(self, pontos, altura_tela, largura_tela, tela):
        texto = self.fonte.render(f"FIM DE JOGO\nPontos: {pontos}\nPressione R para tentar novamente", True, (255, 255, 255))
        tela.blit(texto, (int(altura_tela/2), int(largura_tela/2)))


    def desenhar(self, pontos,altura_tela, largura_tela, tela, fim_de_jogo):
        self.__desenhar_pontos__(pontos, tela)

        if fim_de_jogo:
            self.__desenhar_fim_de_jogo__(pontos,altura_tela, largura_tela, tela)

    #fiz um match para ver se o usuário clicou algo
    # 0 -> não acontece nada
    # 1 -> recomeçar
    # 2 -> fechar jogo
    def processar_evento(self, evento) -> int:
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_r:
                return 1
            elif evento.key == pygame.K_ESCAPE:
                return 2
        return 0