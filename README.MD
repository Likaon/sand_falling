# 🏖️ Granular Simulator with Pymunk and Pygame

This project implements a granular simulator in Python, using Pymunk for physics and Pygame for rendering. The goal is to demonstrate how particles (sand grains) can be simulated in real time, interacting with obstacles and forming piles, in a modular and scalable way.

## ⚙️ Installation and Execution
1. Clone the repository: git clone https://github.com/Likaon/Sand_Falling.git and then cd Sand_Falling  
2. Create a virtual environment (optional, recommended): python -m venv venv and activate with venv\Scripts\activate on Windows or source venv/bin/activate on Linux/Mac  
3. Install dependencies: pip install -r requirements.txt  
4. Run the simulator: python main.py  

## 📸 Screenshots / GIFs
Add screenshots or GIFs of the simulation running, for example using ScreenToGif on Windows or Peek on Linux. Example: ![Simulation Screenshot](docs/screenshot.png)

## 🧪 Technical Explanation
- Physics Engine (PhysicsEngine): uses Pymunk to simulate gravity, collisions, and friction. Each grain is a circle with mass, radius, and physical properties. Static segments represent obstacles and boundaries.  
- Interface (UI): implemented with Pygame. Displays control buttons (Start, Stop, Reset, Draw). Allows numeric input for particle emission.  
- Emitter: controls the position at the top of the screen. Can be moved with ← → arrow keys. Continuously emits particles when the simulation is running.  

## 🗂️ Architecture
UI → Simulator → Physics Engine → Render (Pygame)  
- UI: buttons, input, emitter  
- Simulator: main loop, integrates UI and Physics  
- Physics Engine: particles, collisions, gravity (Pymunk)  
- Render: draws particles and obstacles (Pygame)  

## 📊 Results and Performance
- Tested on Intel i7 + 16GB RAM + integrated GPU  
- Capable of simulating 20,000 particles in real time at 60 FPS  
- Scalability: performance depends on GPU/CPU, but the modular design allows adjustments (radius, mass, damping) for optimization  

## ✅ Tests and Quality
- Unit tests with pytest: grain creation (position, radius, mass); removal of particles outside the screen; numeric input in the emitter  
- CI/CD: GitHub Actions configured in .github/workflows/ci.yml to run tests and linting automatically  
- Linting: flake8 and black for style standardization  

## 📌 Next Steps
- Expand performance metrics on different machines  

## 👨‍💻 Author
Project developed by Rodrigo Assarice as a study of granular simulation in Python.  

## 📬 Contact
rodrigo.assarice@hotmail.com

-------------------------------------------------------------------------------------------

# 🏖️ Simulador Granular com Pymunk e Pygame

Este projeto implementa um simulador granular em Python, utilizando Pymunk para física e Pygame para renderização. O objetivo é demonstrar como partículas (grãos de areia) podem ser simuladas em tempo real, interagindo com obstáculos e formando montes, de forma modular e escalável.

## ⚙️ Instalação e Execução
1. Clonar o repositório: git clone https://github.com/Likaon/Sand_Falling.git e depois cd Sand_Falling
2. Criar ambiente virtual (opcional, recomendado): python -m venv venv e ativar com venv\Scripts\activate no Windows ou source venv/bin/activate no Linux/Mac
3. Instalar dependências: pip install -r requirements.txt
4. Executar o simulador: python main.py

## 📸 Screenshots / GIFs


## 🧪 Explicação Técnica
- Motor físico (PhysicsEngine): usa Pymunk para simular gravidade, colisões e atrito. Cada grão é um círculo com massa, raio e propriedades físicas. Segmentos estáticos representam obstáculos e bordas.
- Interface (UI): implementada com Pygame. Exibe botões de controle (Iniciar, Parar, Reiniciar, Desenhar). Permite input numérico para emissão de partículas.
- Emissor: controla a posição no topo da tela. Pode ser movido com setas ← →. Emite partículas continuamente quando a simulação está rodando.

## 🗂️ Arquitetura
UI → Simulator → Physics Engine → Render (Pygame)
- UI: botões, input, emissor
- Simulator: loop principal, integra UI e Física
- Physics Engine: partículas, colisões, gravidade (Pymunk)
- Render: desenho de partículas e obstáculos (Pygame)

## 📊 Resultados e Performance
- Testado em máquina Intel i7 + 16GB RAM + GPU integrada
- Capaz de simular 20.000 partículas em tempo real a 60 FPS
- Escalabilidade: performance depende da GPU/CPU, mas o design modular permite ajustes (raio, massa, damping) para otimizar

## ✅ Testes e Qualidade
- Testes unitários com pytest: criação de grãos (posição, raio, massa); remoção de partículas fora da tela; input numérico no emissor
- CI/CD: GitHub Actions configurado em .github/workflows/ci.yml para rodar testes e linting automaticamente
- Linting: flake8 e black para padronização de estilo

## 📌 Próximos Passos
- Expandir métricas de performance em diferentes máquinas

## 👨‍💻 Autor
Projeto desenvolvido por Rodrigo Assarice como estudo de simulação granular em Python.

## Contato
rodrigo.assarice@hotmail.com