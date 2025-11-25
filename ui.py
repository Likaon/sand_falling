"""
Interface gráfica: botões, input e emissor.
"""

import pygame
import config

class UI:
    """Classe responsável por desenhar elementos da interface."""

    def __init__(self, largura: int, altura: int, ui_altura: int = 40) -> None:
        self.largura = largura
        self.altura = altura
        self.ui_altura = ui_altura
        self.fonte = pygame.font.SysFont("Arial", 16)
        self.input_ativo: bool = False
        self.texto_input: str = ""

    def desenhar_botoes(self, tela: pygame.Surface) -> None:
        botoes = ['Iniciar', 'Parar', 'Reiniciar', 'Desenhar']
        for i, texto in enumerate(botoes):
            rect = pygame.Rect(i * 180, self.altura, 180, self.ui_altura)
            pygame.draw.rect(tela, config.COR_BOTAO, rect)
            label = self.fonte.render(texto, True, config.COR_TEXTO)
            tela.blit(label, (rect.x + 10, rect.y + 10))

    def desenhar_input(self, tela: pygame.Surface) -> None:
        rect = pygame.Rect(self.largura - 180, self.altura + 5, 170, self.ui_altura - 10)
        cor = config.COR_INPUT_ATIVO if self.input_ativo else config.COR_INPUT
        pygame.draw.rect(tela, cor, rect, border_radius=4)
        label = self.fonte.render(f"Qtd Areia: {self.texto_input}", True, config.COR_TEXTO)
        tela.blit(label, (rect.x + 10, rect.y + 7))

    def desenhar_emissor(self, tela: pygame.Surface, pos_emissor_px: int) -> None:
        pygame.draw.rect(tela, config.COR_EMISSOR, (pos_emissor_px - 3, 0, 6, 6))