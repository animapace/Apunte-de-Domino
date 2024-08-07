class Domino:
    def __init__(self, team_a_name="Equipo A", team_b_name="Equipo B"):
        self.team_a_name = team_a_name
        self.team_b_name = team_b_name
        self.team_a_points = 0
        self.team_b_points = 0
        self.winner = None

    def anadir_puntos(self, team, points):
        if self.winner:
            print(f"El juego ha terminado. {self.winner} ha ganado.")
            return
        if team == self.team_a_name:
            self.team_a_points += points
        elif team == self.team_b_name:
            self.team_b_points += points
        else:
            print(f"Equipo no válido. Use '{self.team_a_name}' o '{self.team_b_name}'.")
            return

        self.check_ganador()

    def check_ganador(self):
        if self.team_a_points >= 200:
            self.winner = self.team_a_name
            print(f"¡{self.team_a_name} ha ganado con {self.team_a_points} puntos!")
        elif self.team_b_points >= 200:
            self.winner = self.team_b_name
            print(f"¡{self.team_b_name} ha ganado con {self.team_b_points} puntos!")
        else:
            print(f"Puntos - {self.team_a_name}: {self.team_a_points}, {self.team_b_name}: {self.team_b_points}")

    def set_team_names(self):
        self.team_a_name = input("Ingrese el nombre del Primer Equipo: ").strip()
        self.team_b_name = input("Ingrese el nombre del Equipo Segundo Equipo: ").strip()

def main():
    game = Domino()
    game.set_team_names()

    while not game.winner:
        team = input(f"Ingrese el equipo que ha ganado puntos ({game.team_a_name}/{game.team_b_name}): ").strip()
        while True:
            try:
                points = int(input("Ingrese los puntos ganados por el equipo: ").strip())
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")
        game.anadir_puntos(team, points)

if __name__ == "__main__":
    main()
