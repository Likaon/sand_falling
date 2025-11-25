"""
Ponto de entrada do simulador granular.
"""

from simulator import SimuladorGranular
import config

if __name__ == "__main__":
    app = SimuladorGranular(largura=config.LARGURA_TELA,
                            altura=config.ALTURA_TELA,
                            ui_altura=config.UI_ALTURA,
                            fps=config.FPS)
    app.run()
