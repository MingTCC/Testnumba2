import random
import tkinter as tk
from tkinter import messagebox

# ฟังก์ชันสำหรับการทอยลูกเต๋า
def roll():
    return random.randint(1, 6)

# ฟังก์ชันสำหรับเริ่มเกมใหม่
def start_game():
    global player_scores, current_player, max_score, game_active
    player_scores = [0 for _ in range(players)]
    current_player = 0
    max_score = 50
    game_active = True
    update_score()
    result_label.config(text="Game started! Player 1's turn.")
    
def update_score():
    score_text = "\n".join([f"Player {i+1}: {score}" for i, score in enumerate(player_scores)])
    score_label.config(text=score_text)

def play_turn():
    global current_player, game_active
    if not game_active:
        return
    
    current_score = 0
    while True:
        value = roll()
        if value == 1:
            current_score = 0
            break
        else:
            current_score += value
            break
    
    player_scores[current_player] += current_score
    update_score()
    
    if player_scores[current_player] >= max_score:
        game_active = False
        messagebox.showinfo("Game Over", f"Player {current_player + 1} wins!")
        return
    
    current_player = (current_player + 1) % players
    result_label.config(text=f"Player {current_player + 1}'s turn.")

# เริ่มต้นโปรแกรม
root = tk.Tk()
root.title("Dice Rolling Game")

# ตั้งค่าจำนวนผู้เล่น
players = 4
player_scores = [0 for _ in range(players)]
current_player = 0
max_score = 50
game_active = True

# ปุ่มและป้ายกำกับสำหรับ UI
start_button = tk.Button(root, text="Start Game", command=start_game)
start_button.pack()

roll_button = tk.Button(root, text="Roll Dice", command=play_turn)
roll_button.pack()

score_label = tk.Label(root, text="Scores will be shown here")
score_label.pack()

result_label = tk.Label(root, text="Game has not started yet.")
result_label.pack()

# แสดงหน้าต่าง
root.mainloop()
