import tkinter as tk
from tkinter import messagebox

class Domino:
    def __init__(self):
        self.team_a_name = "Equipo A"
        self.team_b_name = "Equipo B"
        self.team_a_points = 0
        self.team_b_points = 0
        self.winner = None

    def anadir_puntos(self, team, points):
        if self.winner:
            return
        if team == self.team_a_name:
            self.team_a_points += points
        elif team == self.team_b_name:
            self.team_b_points += points
        else:
            messagebox.showerror("Error", f"Equipo no válido. Use '{self.team_a_name}' o '{self.team_b_name}'.")
            return

        self.check_ganador()

    def check_ganador(self):
        if self.team_a_points >= 200:
            self.winner = self.team_a_name
            messagebox.showinfo("Ganador", f"¡{self.team_a_name} ha ganado con {self.team_a_points} puntos!")
            root.destroy()
        elif self.team_b_points >= 200:
            self.winner = self.team_b_name
            messagebox.showinfo("Ganador", f"¡{self.team_b_name} ha ganado con {self.team_b_points} puntos!")
            root.destroy()
        else:
            self.update_points_display()

    def update_points_display(self):
        points_label.config(text=f"Puntos - {self.team_a_name}: {self.team_a_points}, {self.team_b_name}: {self.team_b_points}")

def add_points():
    team = team_var.get()
    try:
        points = int(points_entry.get().strip())
        game.anadir_puntos(team, points)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un número válido para los puntos.")

# Crear la ventana principal
root = tk.Tk()
root.title("Juego de Domino")

game = Domino()

# Selección de equipo y entrada de puntos
team_var = tk.StringVar(value=game.team_a_name)
team_a_radio = tk.Radiobutton(root, text=game.team_a_name, variable=team_var, value=game.team_a_name)
team_a_radio.grid(row=0, column=0, padx=10, pady=10)

team_b_radio = tk.Radiobutton(root, text=game.team_b_name, variable=team_var, value=game.team_b_name)
team_b_radio.grid(row=0, column=1, padx=10, pady=10)

points_label = tk.Label(root, text="Ingrese los puntos ganados:")
points_label.grid(row=1, column=0, padx=10, pady=10)

points_entry = tk.Entry(root)
points_entry.grid(row=1, column=1, padx=10, pady=10)

add_points_button = tk.Button(root, text="Añadir Puntos", command=add_points)
add_points_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Display de puntos actuales
points_label = tk.Label(root, text="Puntos - Equipo A: 0, Equipo B: 0")
points_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Ejecutar la interfaz
root.mainloop()
