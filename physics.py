"""
Módulo responsável pela física granular usando Pymunk.
"""

import random
import logging
import pymunk
import config

logging.basicConfig(level=logging.INFO)


class PhysicsEngine:
    """
    Motor físico que gerencia partículas de areia e bloqueios.
    """

    def __init__(self, largura: int, altura: int) -> None:
        self.largura = largura
        self.altura = altura
        self.space = pymunk.Space()
        self.space.gravity = config.GRAVIDADE
        self.space.damping = config.DAMPING
        self.areia_shapes: list[pymunk.Shape] = []
        self.segmentos_bloqueio: list[pymunk.Shape] = []
        self.criar_bordas()

    def criar_grao(self, pos: tuple[int, int]) -> pymunk.Shape | None:
        """
        Cria um grão de areia na posição especificada.
        """
        if len(self.areia_shapes) >= config.MAX_PARTICULAS:
            logging.warning("Limite máximo de partículas atingido.")
            return None

        body = pymunk.Body(
            mass=config.MASSA_GRAO,
            moment=pymunk.moment_for_circle(
                config.MASSA_GRAO,
                0,
                config.RAIO_GRAO
            )
        )
        body.position = pos

        shape = pymunk.Circle(body, radius=config.RAIO_GRAO)
        shape.friction = config.FRICCAO_GRAO
        shape.elasticity = config.RESTITUICAO_GRAO
        shape.color = random.choice([config.COR_AREIA1, config.COR_AREIA2])

        self.space.add(body, shape)
        self.areia_shapes.append(shape)
        logging.info(f"Grão criado em {pos}")
        return shape

    def criar_segmento(
        self,
        p0: tuple[int, int],
        p1: tuple[int, int],
        espessura: int = 2
    ) -> None:
        """
        Cria um segmento estático (bloqueio).
        """
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        shape = pymunk.Segment(body, p0, p1, espessura)
        shape.friction = 0.7
        shape.elasticity = 0.0
        shape.color = config.COR_BLOQUEIO

        self.space.add(body, shape)
        self.segmentos_bloqueio.append(shape)
        logging.info(f"Segmento criado de {p0} até {p1}")

    def criar_bordas(self) -> None:
        """Cria bordas de contenção (chão e paredes)."""
        self.criar_segmento(
            (0, self.altura - 1),
            (self.largura, self.altura - 1),
            1
        )
        self.criar_segmento((0, 0), (0, self.altura), 1)
        self.criar_segmento(
            (self.largura - 1, 0),
            (self.largura - 1, self.altura),
            1
        )

    def reiniciar(self) -> None:
        """Remove todas as partículas e bloqueios e recria bordas."""
        for s in self.areia_shapes:
            self.space.remove(s, s.body)
        self.areia_shapes = []

        for s in self.segmentos_bloqueio:
            self.space.remove(s, s.body)
        self.segmentos_bloqueio = []

        self.criar_bordas()
        logging.info("Mundo reiniciado.")

    def step(self, dt: float) -> None:
        """Avança a simulação física."""
        self.space.step(dt)

    def limpar_fora_da_tela(self, largura: int, altura: int) -> None:
        """Remove partículas que saíram da tela."""
        vivos = []
        for s in self.areia_shapes:
            x, y = s.body.position
            if -50 <= x <= largura + 50 and -50 <= y <= altura + 200:
                vivos.append(s)
            else:
                self.space.remove(s, s.body)
                logging.info(
                    f"Grão removido fora da tela em {(x, y)}"
                )
        self.areia_shapes = vivos