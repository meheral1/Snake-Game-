# 🐍 Snake Game

A robust, classic Snake game implementation using Python's **Turtle Graphics**. This version is designed for an "infinite" play experience by removing boundary collisions and adding persistent data storage.

## 🌟 Key Features

### 1. **Screen Wrap-Around (No-Borders)**
Unlike the traditional Snake game where hitting a wall results in "Game Over," this version implements **teleportation logic**. When the snake head reaches the boundary ($x$ or $y = \pm 300$), it is instantly repositioned to the opposite side, allowing for continuous, uninterrupted gameplay.

### 2. **Persistent High Score System**
The game features a local data-logging mechanism using Python’s File I/O.
* **On Startup:** The game reads `highscore.txt` to load your lifetime record.
* **On Update:** If the current score surpasses the record, the file is updated in real-time.

### 3. **Directional Input Validation**
To prevent "instant self-collision" (where the snake turns 180 degrees into its own body), the code includes conditional checks for every directional input. For example, if moving **Up**, the **Down** command is ignored.

### 4. **Optimized Collision Detection**
The game uses a `list` to manage body segments. Collision detection is optimized using **slicing** (`body[1:]`) to ensure the head only triggers a reset when it hits a tail segment, preventing false collisions with the neck.

### 5. **Memory-Safe Reset**
When a collision occurs, the program uses `hideturtle()` and moves old segments to off-screen coordinates ($1000, 1000$) to prevent "ghost" segments from cluttering the game window and ensuring performance stability.

---

## 🎮 Controls

| Key | Action |
| :--- | :--- |
| `Up Arrow` | Move Up |
| `Down Arrow` | Move Down |
| `Left Arrow` | Move Left |
| `Right Arrow` | Move Right |

---

## 🛠️ Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/snake-game.git](https://github.com/your-username/snake-game.git)
