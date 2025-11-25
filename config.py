"""
Configurações globais do simulador granular.
"""

# Dimensões
LARGURA_TELA: int = 900
ALTURA_TELA: int = 900
UI_ALTURA: int = 40
FPS: int = 60

# Física
GRAVIDADE: tuple[int, int] = (0, 900)
RAIO_GRAO: float = 2.5
MASSA_GRAO: float = 0.02
FRICCAO_GRAO: float = 0.45
RESTITUICAO_GRAO: float = 0.05
DAMPING: float = 0.999
MAX_PARTICULAS: int = 20000

# Cores
COR_FUNDO: tuple[int, int, int] = (10, 10, 12)
COR_TEXTO: tuple[int, int, int] = (240, 240, 240)
COR_BOTAO: tuple[int, int, int] = (60, 60, 70)
COR_INPUT: tuple[int, int, int] = (40, 40, 44)
COR_INPUT_ATIVO: tuple[int, int, int] = (70, 70, 76)
COR_EMISSOR: tuple[int, int, int] = (255, 70, 70)
COR_BLOQUEIO: tuple[int, int, int] = (180, 180, 180)
COR_AREIA1: tuple[int, int, int] = (215, 195, 120)
COR_AREIA2: tuple[int, int, int] = (190, 170, 100)