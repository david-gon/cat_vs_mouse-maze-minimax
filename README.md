# 🐱🐭 Gato vs Ratón - Minimax Maze Game

## 📋 Descripción

Juego de persecución estratégica donde controlas un ratón que debe escapar de un gato inteligente en un laberinto. 
El gato está programado utilizando el algoritmo Minimax con recursividad de profundidad limitada, permitiéndole predecir y anticipar tus movimientos. 
Tu objetivo: recolectar todo el queso antes de ser atrapado.

---

## 🎮 Reglas del Juego

### Objetivo Principal
- **Eres el ratón** 🐭: Tu misión es recolectar todo el queso disponible en el laberinto
- **El gato te persigue** 🐱: Controlado por IA usando Minimax, intentará capturarte
- **Ganar**: Recolecta todo el queso antes de ser atrapado
- **Perder**: El gato te alcanza antes de completar tu objetivo

### Mecánicas
- Muévete por el laberinto usando las teclas de dirección WASD
- El gato analiza todas las posibles jugadas antes de moverse
- Cada movimiento cuenta - el gato predice tus siguientes pasos
- Planifica tu ruta cuidadosamente para evitar ser capturado

---

## 🧠 ¿Qué es Minimax y por qué es Inteligencia Artificial?

### Definición de Minimax

El **algoritmo Minimax** es una estrategia de toma de decisiones utilizada en teoría de juegos y en inteligencia artificial para juegos de dos jugadores con suma cero (donde la ganancia de uno es la pérdida del otro).

### Principios Fundamentales

**Minimax funciona bajo estos conceptos:**

1. **Maximizar ganancias propias**: El gato busca maximizar sus posibilidades de capturarte
2. **Minimizar ganancias del oponente**: Asume que tú (el ratón) juegas de manera óptima para escapar
3. **Exploración de posibilidades**: Analiza todos los movimientos posibles varios pasos adelante
4. **Decisión óptima**: Elige el movimiento que le da la mejor ventaja asumiendo que juegas perfectamente

### ¿Por qué es IA?

Minimax representa un principio de **Inteligencia Artificial** porque:

- **Simulación de razonamiento**: El algoritmo "piensa" varios movimientos adelante, similar a cómo un humano planifica estrategias
- **Toma de decisiones autónoma**: El gato decide por sí mismo la mejor jugada sin intervención humana
- **Adaptación al oponente**: Reacciona inteligentemente a tus movimientos, no sigue patrones predefinidos
- **Búsqueda en espacio de estados**: Explora un árbol de posibilidades para encontrar la solución óptima
- **Comportamiento racional**: Actúa de manera lógica para maximizar su objetivo (capturarte)

---

## ⚙️ Implementación del Minimax en el Juego

### Funcionamiento Técnico

#### 1. **Árbol de Decisiones**
Cuando es el turno del gato, el algoritmo construye un árbol de posibilidades:
```
Estado Actual
    ├── Movimiento 1 del Gato
    │   ├── Respuesta 1 del Ratón
    │   ├── Respuesta 2 del Ratón
    │   └── Respuesta 3 del Ratón
    ├── Movimiento 2 del Gato
    │   └── ...
    └── Movimiento 3 del Gato
```

#### 2. **Predicción de Movimientos**
- El gato explora **todas las posiciones posibles** a las que puede moverse
- Para cada una, simula **todos los movimientos que TÚ podrías hacer** en respuesta
- Este proceso se repite recursivamente hasta alcanzar la **profundidad límite** configurada
- Cada camino del árbol representa una secuencia completa de jugadas futuras

#### 3. **Evaluación de Posiciones**
Cada nodo terminal del árbol recibe una puntuación basada en:
- **Distancia al ratón**: Qué tan cerca está el gato de capturarte
- **Distancia al queso**: Qué tan cerca estás tú de tu objetivo
- **Posiciones estratégicas**: Bloquear rutas de escape

#### 4. **Selección del Mejor Movimiento**
- El algoritmo **retrocede** desde las hojas del árbol hasta la raíz
- Asume que el ratón elegirá su mejor jugada (minimizar captura)
- El gato elige el camino que maximiza sus posibilidades incluso si juegas perfectamente
- **Resultado**: El gato se mueve a la posición más ventajosa



### Características Clave de la Implementación

✅ **Búsqueda Exhaustiva**: Recorre todo el árbol de posibilidades antes de decidir
✅ **Anticipación Estratégica**: No solo ve tu posición actual, sino dónde podrías estar en varios turnos
✅ **Juego Óptimo**: El gato juega asumiendo que eres un jugador perfecto

---

## 🎚️ Niveles de Dificultad

### 🟢 Nivel 1: Introducción
- **Laberinto**: Pequeño (15x15 celdas aprox.)
- **Objetivo**: Recolectar 1 queso 🧀
- **Ideal para**: Aprender las mecánicas y entender cómo piensa el gato

### 🟡 Nivel 2: Desafío Medio
- **Laberinto**: Pequeño (15x15 celdas aprox.)
- **Objetivo**: Recolectar 3 quesos 🧀🧀🧀
- **Desafío**: Planificar una ruta eficiente sin ser atrapado

### 🟠 Nivel 3: Experto
- **Laberinto**: Grande (30x30celdas aprox.)
- **Objetivo**: Recolectar 10 quesos 🧀×10
- **Desafío**: Navegación compleja con múltiples objetivos

### 🔴 Nivel HARDCORE
- **Laberinto**: Pequeño (30x30 celdas aprox.)
- **Objetivo**: Recolectar 1 queso 🧀
- **Dificultad del Gato**: **¡El gato se mueve 2 pasos por cada movimiento tuyo!** ⚡
- **Desafío**: Velocidad extrema - requiere jugadas perfectas y anticipación absoluta

---

## 💡 Aprendizajes y Descubrimientos

Durante el desarrollo de este proyecto, profundicé en varios conceptos fundamentales de ciencias de la computación e inteligencia artificial:

### 🌲 Estructuras de Datos
- **Árboles de decisión**: Cómo representar y navegar todas las posibilidades de juego
- **Nodos y grafos**: Modelar el laberinto como un grafo donde cada celda es un nodo
- **Exploración de grafos**: Algoritmos para recorrer y evaluar estructuras complejas

### 🔄 Recursividad
- **Pensamiento recursivo**: Resolver problemas dividiéndolos en subproblemas idénticos más pequeños
- **Casos base**: Identificar cuándo detener la recursión (profundidad límite o fin del juego)
- **Backtracking**: Retroceder en el árbol para evaluar todas las opciones antes de decidir
- **Stack de llamadas**: Entender cómo se acumulan y resuelven las llamadas recursivas

### 📏 Cálculo de Distancias
Exploré diferentes métodos para medir distancias en el laberinto:
- **Distancia Manhattan**: `|x1 - x2| + |y1 - y2|` - útil para movimientos en grilla
- **Distancia Euclidiana**: `√((x1-x2)² + (y1-y2)²)` - distancia en línea recta
- **Pathfinding**: Calcular la distancia real considerando obstáculos (A*, BFS)

### 🤖 Dinámica de la IA
- **Predicción de comportamiento**: Cómo la IA anticipa movimientos futuros del jugador
- **Evaluación heurística**: Asignar valores numéricos a posiciones del tablero
- **Trade-offs computacionales**: Balance entre profundidad de búsqueda y tiempo de respuesta
- **Comportamiento emergente**: Cómo reglas simples crean estrategias complejas

### 🎯 Optimización
- **Poda de árbol**: Eliminar ramas que no vale la pena explorar (Alpha-Beta pruning conceptual)
- **Límites de profundidad**: Controlar cuántos movimientos adelante analiza el gato
- **Rendimiento**: Gestionar la complejidad computacional para mantener el juego fluido

---

## 🚀 Tecnologías Utilizadas

- [Especifica aquí tu lenguaje: Python, JavaScript, etc.]
- [Librerías gráficas: Pygame, Canvas, etc.]
- Algoritmo Minimax con recursividad
- [Otras herramientas que usaste]

---

## 📦 Instalación y Uso
```bash
# Clona el repositorio
git clone https://github.com/tu-usuario/cat-mouse-maze-minimax.git

# Navega al directorio
cd cat-mouse-maze-minimax

# Instala dependencias (si aplica)
[Tus comandos de instalación]

# Ejecuta el juego
[Tu comando para ejecutar]
```

---

## 🎮 Controles

- **A W S D**: Mover al ratón


## 🤝 Contribuciones

Las contribuciones son bienvenidas. Si tienes ideas para mejorar el juego o el algoritmo, siéntete libre de abrir un issue o pull request.

---


## 👨‍💻 Autor

David Gonzalez
- GitHub: https://github.com/david-gon
- Linkedin: https://www.linkedin.com/in/david-gonzalez-a3347028a/
- 
---
