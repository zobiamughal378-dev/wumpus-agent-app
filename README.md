# 🧠 Wumpus KB Agent — Logic-Driven Pathfinding

An advanced, interactive web simulation of the classic **Wumpus World** Artificial Intelligence problem[cite: 1]. This project demonstrates how an AI agent uses **Propositional Logic** and a **Knowledge Base (KB)** to navigate a dangerous environment, avoid hazards, and find gold through pure logical deduction[cite: 1].

---

## 🌟 Introduction
The **Wumpus KB Agent** is a specialized pathfinder designed to solve grid-based puzzles where certain cells contain hidden dangers like Pits or the deadly Wumpus[cite: 1]. Unlike traditional algorithms that might rely on luck, this agent uses **Resolution Refutation** to mathematically prove whether a cell is safe before ever stepping into it[cite: 1].

---

## 🛠️ Technical Stack
*   **HTML5:** Used to build the application’s structural framework and interactive interface elements[cite: 1].
*   **CSS3:** Features a futuristic "Cyber" dark-themed UI[cite: 1]. It utilizes the **Syne** and **Space Mono** Google Fonts to provide a professional coding aesthetic[cite: 1]. Custom keyframe animations are used for glowing borders and cell transitions[cite: 1].
*   **Vanilla JavaScript (ES6+):** The core engine of the project[cite: 1]. It handles the Logic Engine, the Resolution Refutation algorithm, and real-time grid state management without the need for external libraries[cite: 1].

---

## ⚙️ Core Features & Functionality

### 1. Knowledge Base (KB) Management
*   **TELL Logic:** As the agent moves, it receives "percepts" (like Breeze or Stench)[cite: 1]. It converts these observations into logical clauses and adds them to the KB[cite: 1].
*   **ASK Logic:** Before moving to an unvisited cell, the agent queries the KB: *"Is it logically certain that this cell is safe?"*[cite: 1]

### 2. Resolution Refutation Engine
The agent solves logic problems using a sophisticated proof method[cite: 1]:
*   It assumes a hazard (Pit or Wumpus) exists in a target cell[cite: 1].
*   If this assumption creates a "Contradiction" with existing facts in the KB, the agent proves the cell is **SAFE**[cite: 1].

### 3. Mission Metrics & Live Logs
*   **Inferences:** Tracks how many logical deductions the AI has performed[cite: 1].
*   **KB Clauses:** Displays the current number of logical formulas (CNF) stored in the memory[cite: 1].
*   **Inference Log:** Provides a real-time feed of the agent’s "thought process"[cite: 1].

### 4. Interactive Simulation
*   **Dynamic Generation:** Every episode randomly places pits and the Wumpus to ensure a unique challenge[cite: 1].
*   **Control Modes:** Users can manually "Step" through the logic or use "Run Auto" to watch the AI navigate the entire cave autonomously[cite: 1].
*   **Speed Control:** Includes a slider to adjust the simulation speed from 100ms to 1500ms[cite: 1].

---

## 🎮 Legend
*   🤖 **Agent:** The logic-driven explorer[cite: 1].
*   🏆 **Gold:** The mission objective[cite: 1].
*   💀 **Pit:** A fatal hazard that terminates the agent[cite: 1].
*   💨 **Breeze:** A percept indicating a Pit is in an adjacent cell[cite: 1].
*   🦨 **Stench:** A percept indicating the Wumpus is nearby[cite: 1].

---

## 🚀 How to Run
1.  **Clone or download** this repository.
2.  Open the `index.html` file in any modern web browser (Chrome, Firefox, or Edge)[cite: 1].
3.  Click **"New Episode"** and watch the AI solve the dungeon![cite: 1]
