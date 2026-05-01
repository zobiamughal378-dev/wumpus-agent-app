import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Wumpus World Game")
SIZE = 4

world = {
    (3, 1): ["W"],
    (3, 3): ["PIT"],
    (4, 4): ["PIT"],
    (1, 3): ["PIT"],
    (2, 3): ["GOLD"]
}

agent_pos  = [1, 1]
score      = [0]
arrows     = [7]
rem_golds  = [sum(1 for v in world.values() if "GOLD" in v)]

def get_adjacent(x, y):
    moves = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
    return [(i,j) for i,j in moves if 1 <= i <= SIZE and 1 <= j <= SIZE]

def build_world():
    for pos in list(world.keys()):
        world[pos] = [i for i in world[pos] if i not in ["Breeze","Stench"]]
    for (x,y), items in list(world.items()):
        if "PIT" in items:
            for nx, ny in get_adjacent(x, y):
                if "Breeze" not in world.get((nx,ny), []):
                    world.setdefault((nx,ny), []).append("Breeze")
        if "W" in items:
            for nx, ny in get_adjacent(x, y):
                if "Stench" not in world.get((nx,ny), []):
                    world.setdefault((nx,ny), []).append("Stench")

build_world()

cells = {}

def update_status():
    status_label.config(
        text=f"  Score {score[0]}     "
             f"🏹 Arrow: {arrows[0]}     "
             f"💰 Remaining Golds: {rem_golds[0]}  "
    )

def format_cell(x, y):
    items = world.get((x,y), [])
    text = ""
    if [x,y] == agent_pos: text += "AGENT\n"
    if "GOLD"   in items:  text += "GOLD\n"
    if "PIT"    in items:  text += "PIT\n"
    if "W"      in items:  text += "WUMPUS\n"
    if "Breeze" in items:  text += "~ Breeze\n"
    if "Stench" in items:  text += "~ Stench\n"
    return text.strip()

def get_color(x, y):
    items = world.get((x,y), [])
    if [x,y] == agent_pos: return "#90EE90"
    if "PIT"  in items:    return "#FF6B6B"
    if "W"    in items:    return "#FFB347"
    if "GOLD" in items:    return "#FFD700"
    return "#f2f2f2"

def draw_grid():
    for row in range(1, SIZE+1):
        for col in range(1, SIZE+1):
            text  = format_cell(col, row)
            color = get_color(col, row)
            cells[(col,row)].config(text=f"({col},{row})\n{text}", bg=color)

def check_status():
    pos   = tuple(agent_pos)
    items = world.get(pos, [])
    if "PIT" in items:
        score[0] -= 1000
        update_status()
        messagebox.showerror("Game Over", f"You fell into a PIT!\nFinal Score: {score[0]}")
        root.quit()
    elif "W" in items:
        score[0] -= 1000
        update_status()
        messagebox.showerror("Game Over", f"Wumpus ate you!\nFinal Score: {score[0]}")
        root.quit()
    elif "GOLD" in items:
        score[0]     += 1000
        rem_golds[0] -= 1
        world[pos].remove("GOLD")
        draw_grid()
        update_status()
        messagebox.showinfo("Gold!", f"You collected GOLD! +1000\nScore: {score[0]}")
        if rem_golds[0] == 0:
            messagebox.showinfo("You Win!", f"All gold collected!\nFinal Score: {score[0]}")
            root.quit()

def move(dx, dy):
    new_x = agent_pos[0] + dx
    new_y = agent_pos[1] + dy
    if 1 <= new_x <= SIZE and 1 <= new_y <= SIZE:
        agent_pos[0]  = new_x
        agent_pos[1]  = new_y
        score[0]     -= 1
        draw_grid()
        update_status()
        check_status()
    else:
        messagebox.showwarning("Invalid", "Cannot move outside the grid!")

# ── Grid UI ──
for row in range(SIZE, 0, -1):
    for col in range(1, SIZE+1):
        cell = tk.Label(root, borderwidth=2, relief="solid",
                        width=15, height=6, bg="#f2f2f2",
                        font=("Arial", 9, "bold"), justify="center")
        cell.grid(row=SIZE-row, column=col-1, padx=2, pady=2)
        cells[(col,row)] = cell

# ── Buttons ──
btn_frame = tk.Frame(root)
btn_frame.grid(row=SIZE+1, column=0, columnspan=SIZE, pady=8)

tk.Button(btn_frame, text="  UP  ", width=7, bg="lightblue",
          command=lambda: move(0, 1)).grid(row=0, column=1, padx=3)
tk.Button(btn_frame, text=" LEFT ", width=7, bg="lightblue",
          command=lambda: move(-1, 0)).grid(row=1, column=0, padx=3)
tk.Button(btn_frame, text=" RIGHT", width=7, bg="lightblue",
          command=lambda: move(1, 0)).grid(row=1, column=2, padx=3)
tk.Button(btn_frame, text=" DOWN ", width=7, bg="lightblue",
          command=lambda: move(0, -1)).grid(row=2, column=1, padx=3)

# ── Status Bar ──
status_label = tk.Label(root, text="", font=("Arial", 11),
                        bg="#222", fg="white", anchor="w", pady=4)
status_label.grid(row=SIZE+2, column=0, columnspan=SIZE, sticky="ew")

draw_grid()
update_status()
root.mainloop()