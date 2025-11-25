"""
Módulo principal do simulador granular.
Gerencia emissor, ferramenta de bloqueio e loop principal.
"""

import sys
import random
import logging
import pygame
from physics import PhysicsEngine
from ui import UI
import config

logging.basicConfig(level=logging.INFO)

class Emissor:
    """
    Classe responsável por emitir grãos de areia.
    """
    def __init__(self, largura: int) -> None:
        self.largura = largura
        self.pos_px: int = largura // 2
        self.spread: int = 6

    def mover_esquerda(self, passo: int = 5) -> None:
        """Move o emissor para a esquerda."""
        self.pos_px = max(10, self.pos_px - passo)

    def mover_direita(self, passo: int = 5) -> None:
        """Move o emissor para a direita."""
        self.pos_px = min(self.largura - 10, self.pos_px + passo)

    def emitir(self, physics: PhysicsEngine, n: int = 1) -> None:
        """Emite n grãos de areia no topo."""
        for _ in range(n):
            x = self.pos_px + random.randint(-self.spread, self.spread)
            physics.criar_grao((x, 5))


class BloqueioTool:
    """
    Ferramenta para desenhar segmentos de bloqueio com o mouse.
    """
    def __init__(self, altura_canvas: int) -> None:
        self.desenhando: bool = False
        self.inicio: tuple[int, int] | None = None
        self.altura_canvas = altura_canvas

    def iniciar(self, pos: tuple[int, int]) -> None:
        """Inicia desenho de segmento."""
        x, y = pos
        if y < self.altura_canvas:
            self.desenhando = True
            self.inicio = (x, y)

    def finalizar(self, pos: tuple[int, int], physics: PhysicsEngine) -> None:
        """Finaliza desenho e cria segmento físico."""
        if not self.desenhando or self.inicio is None:
            return
        x, y = pos
        if y < self.altura_canvas:
            physics.criar_segmento(self.inicio, (x, y), espessura=2)
            logging.info(f"Segmento desenhado de {self.inicio} até {(x,y)}")
        self.desenhando = False
        self.inicio = None


class SimuladorGranular:
    """
    Classe principal que encapsula o simulador granular.
    """
    def __init__(self, largura: int = config.LARGURA_TELA,
                 altura: int = config.ALTURA_TELA,
                 ui_altura: int = config.UI_ALTURA,
                 fps: int = config.FPS) -> None:
        pygame.init()
        self.largura = largura
        self.altura = altura
        self.ui_altura = ui_altura
        self.fps = fps

        self.tela = pygame.display.set_mode((largura, altura + ui_altura))
        pygame.display.set_caption("Simulador Granular (Pymunk, OOP)")
        self.clock = pygame.time.Clock()

        self.physics = PhysicsEngine(largura, altura)
        self.ui = UI(largura, altura, ui_altura)
        self.emissor = Emissor(largura)
        self.bloqueio_tool = BloqueioTool(altura)

        self.rodando: bool = False

    def _handle_mouse_down(self) -> None:
        x, y = pygame.mouse.get_pos()
        if y >= self.altura:
            if self.largura - 180 <= x <= self.largura:
                self.ui.input_ativo = True
                return
            else:
                self.ui.input_ativo = False
                index = x // 180
                if index == 0:
                    self.rodando = True
                    logging.info("Simulação iniciada.")
                elif index == 1:
                    self.rodando = False
                    logging.info("Simulação pausada.")
                elif index == 2:
                    self.physics.reiniciar()
                elif index == 3:
                    self.bloqueio_tool.desenhando = not self.bloqueio_tool.desenhando
        else:
            if self.bloqueio_tool.desenhando:
                self.bloqueio_tool.iniciar((x, y))

    def _handle_mouse_up(self) -> None:
        x, y = pygame.mouse.get_pos()
        if self.bloqueio_tool.desenhando and self.bloqueio_tool.inicio is not None:
            self.bloqueio_tool.finalizar((x, y), self.physics)

    def _handle_keydown(self, evento: pygame.event.Event) -> None:
        if evento.key == pygame.K_LEFT:
            self.emissor.mover_esquerda()
        elif evento.key == pygame.K_RIGHT:
            self.emissor.mover_direita()
        elif self.ui.input_ativo:
            if evento.key == pygame.K_RETURN:
                try:
                    qtd = int(self.ui.texto_input)
                    self.emissor.emitir(self.physics, n=qtd)
                    logging.info(f"{qtd} grãos emitidos manualmente.")
                except ValueError:
                    logging.error("Valor inválido no input de areia.")
                self.ui.texto_input = ""
            elif evento.key == pygame.K_BACKSPACE:
                self.ui.texto_input = self.ui.texto_input[:-1]
            else:
                if evento.unicode.isdigit():
                    self.ui.texto_input += evento.unicode

    def _update(self) -> None:
        if self.rodando:
            self.emissor.emitir(self.physics, n=1)
            dt = 1.0 / self.fps
            substeps = 2
            for _ in range(substeps):
                self.physics.step(dt / substeps)
            self.physics.limpar_fora_da_tela(self.largura, self.altura)

    def _render(self) -> None:
        self.tela.fill(config.COR_FUNDO)
        for s in self.physics.areia_shapes:
            x, y = int(s.body.position.x), int(s.body.position.y)
            if 0 <= x < self.largura and 0 <= y < self.altura:
                pygame.draw.circle(self.tela, s.color, (x, y), int(s.radius))
        for s in self.physics.segmentos_bloqueio:
            p0 = (int(s.a.x), int(s.a.y))
            p1 = (int(s.b.x), int(s.b.y))
            pygame.draw.line(self.tela, s.color, p0, p1, int(s.radius) * 2 or 2)

        self.ui.desenhar_emissor(self.tela, self.emissor.pos_px)
        self.ui.desenhar_botoes(self.tela)
        self.ui.desenhar_input(self.tela)

        pygame.display.flip()

    def run(self) -> None:
        """Loop principal da aplicação."""
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    self._handle_mouse_down()
                elif evento.type == pygame.MOUSEBUTTONUP:
                    self._handle_mouse_up()
                elif evento.type == pygame.KEYDOWN:
                    self._handle_keydown(evento)

            self._update()
            self._render()
            self.clock.tick(self.fps)