import random


class Tablero:
    def __init__(self):
        self.casillas = ['' for _ in range(40)]
        self.generar_obsta()

    def generar_obsta(self):
        pos_serpiente = random.choice(range(5, 10))
        pos_sacrificio = random.choice(range(11, 20))
        pos_inundacion = random.choice(range(21, 29))
        pos_pozo = random.choice(range(30, 37))

        self.casillas[pos_serpiente] = '🐍'
        self.casillas[pos_sacrificio] = '🪦'
        self.casillas[pos_inundacion] = '🌊'
        self.casillas[pos_pozo] = '🕳️'

    def mostrar(self, posiciones):
        for i in range(40):
            ficha = '[  ]'
            for p in posiciones:
                if p['pos'] == i:
                    ficha = p['ficha']
                    break
            if self.casillas[i]:
                ficha = self.casillas[i]
            print(f"[{ficha}]", end=' ')
            if (i + 1) % 10 == 0:
                print()


class Jugador:
    def __init__(self, nombre, ficha):
        self.nombre = nombre
        self.ficha = ficha
        self.pos = 0
        self.movimientos = 0
        self.estadisticas = {
            'ganadas': 0,
            'perdidas': 0,
            'abandonadas': 0,
            'perdidas_pozo': 0
        }
        self.activo = True

    def mover(self, casillas):
        self.pos += casillas
        self.movimientos += 1


class Juego:
    def __init__(self, jugadores):
        self.tablero = Tablero()
        fichas_dispo = ['🚀', '🚗', '🚢', '✈️', '🚁', '🎲', '🎯', '💎', '🍀', '🎩']
        self.jugadores = []
        fichas_usadas = []

        for nombre in jugadores:
            while True:
                index = random.randint(0, len(fichas_dispo) - 1)
                if index not in fichas_usadas:
                    fichas_usadas.append(index)
                    ficha = fichas_dispo[index]
                    break

            self.jugadores.append(Jugador(nombre, ficha))

        self.actual = 0

    def lanzar_dado(self):
        return random.randint(1, 6)

    def ver_stats(self):
        print("\nEstadísticas de los jugadores:")
        for j in self.jugadores:
            print(f"{j.nombre}:")
            print(f"  - Ganadas: {j.estadisticas['ganadas']} (en {j.movimientos} movimientos)")
            print(f"  - Perdidas: {j.estadisticas['perdidas']}")
            print(f"  - Abandonadas: {j.estadisticas['abandonadas']}")
            print(f"  - Perdidas por pozo: {j.estadisticas['perdidas_pozo']}")
            j.movimientos = 0

    def jugar(self):
        while len([j for j in self.jugadores if j.activo]) > 1:
            print("\nTablero actual:")
            posiciones = [{'pos': j.pos, 'ficha': j.ficha} for j in self.jugadores if j.activo]
            self.tablero.mostrar(posiciones)

            jugador = self.jugadores[self.actual]
            if not jugador.activo:
                self.actual = (self.actual + 1) % len(self.jugadores)
                continue

            print(f"\nTurno de {jugador.nombre} ({jugador.ficha}).")

            accion = ""
            while accion != 'lanzar' and accion != 'abandonar':
                accion = input(f"{jugador.nombre}, ¿quieres 'lanzar' el dado o 'abandonar'? ").lower()

            if accion == 'abandonar':
                print(f"{jugador.nombre} ha abandonado.")
                jugador.estadisticas['abandonadas'] += 1
                jugador.activo = False
                if len([j for j in self.jugadores if j.activo]) == 1:
                    ganador = next(j for j in self.jugadores if j.activo)
                    print(f"{ganador.nombre} ha ganado el juego automáticamente.")
                    ganador.estadisticas['ganadas'] += 0
                    self.finalizar(ganador.nombre)
                    return
                continue

            dado = self.lanzar_dado()
            print(f"Dado: {dado}")
            jugador.mover(dado)

            if jugador.pos > 40:
                jugador.pos = 40 - (jugador.pos - 40)
                print(f"Rebotas a la posición {jugador.pos}.")
            elif jugador.pos == 40:
                print(f"¡{jugador.nombre} ha ganado!")
                jugador.estadisticas['ganadas'] += 0
                self.finalizar(jugador.nombre)
                return

            print(f"{jugador.nombre} está ahora en la posición {jugador.pos}.")
            self.check_obstaculo(jugador)
            self.actual = (self.actual + 1) % len(self.jugadores)

    def check_obstaculo(self, jugador):
        pos = jugador.pos
        if self.tablero.casillas[pos] == '🐍':
            print("Serpiente 🐍: retrocedes 3 casillas.")
            jugador.mover(-3)
            print(f"{jugador.nombre} está ahora en la posición {jugador.pos}.")
        elif self.tablero.casillas[pos] == '🪦':
            dado = self.lanzar_dado()
            print(f"Sacrificio 🪦: retrocedes {dado} casillas.")
            jugador.mover(-dado)
            print(f"{jugador.nombre} está ahora en la posición {jugador.pos}.")
        elif self.tablero.casillas[pos] == '🌊':
            print("Inundación 🌊: vuelves al inicio.")
            jugador.pos = 0
            print(f"{jugador.nombre} está ahora en la posición {jugador.pos}.")
        elif self.tablero.casillas[pos] == '🕳️':
            dado = self.lanzar_dado()
            print(f"Pozo 🕳️: lanzaste {dado}.", end=' ')
            if dado % 2 != 0:
                print("Número impar, pierdes.")
                jugador.estadisticas['perdidas'] += 1
                jugador.estadisticas['perdidas_pozo'] += 1
                jugador.activo = False
            else:
                print("Número par, sigues en juego.")

    def finalizar(self, ganador):
        print(f"\n{ganador} ha ganado el juego en {self.jugadores[self.actual].movimientos} movimientos.")
        for j in self.jugadores:
            if j.nombre != ganador:
                print(f"{j.nombre}, lo siento, perdiste. ¡Gracias por participar!")
                j.estadisticas['perdidas'] += 1
            else:
                j.estadisticas['ganadas'] += 1


def pedir_nombres(canti_jugadores):
    jugadores = []
    for i in range(canti_jugadores):
        while True:
            nombre = input(f"Ingrese el nombre del jugador {i+1}: ")
            if nombre.isalpha():
                jugadores.append(nombre)
                break
            else:
                print("Error: Ingrese un nombre válido solo con letras, por favor.")
    return jugadores


def p_canti_juga():
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de jugadores (2-4): "))
            if cantidad in range(2, 5):
                return cantidad
            else:
                print("Error: Ingrese un número entre 2 y 4.")
        except ValueError:
            print("Error: Ingrese un número válido.")


def menu():
    juego = None
    while True:
        print("\nMenú Principal:")
        print("1. Nuevo Juego")
        print("2. Cómo Jugar")
        print("3. Estadísticas")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            canti_jugadores = p_canti_juga()
            nombres_juga = pedir_nombres(canti_jugadores)
            juego = Juego(nombres_juga)
            juego.jugar()

        elif opcion == '2':
            print("\nCómo Jugar:")
            print("El juego es un clásico juego de mesa.")
            print("- Cada jugador lanza un dado en su turno para avanzar.")
            print("- Si caes en un obstáculo, sufrirás las consecuencias.")
            print("- El primer jugador en llegar exactamente a la casilla 40 gana.")
            print("- Puedes abandonar el juego en tu turno.")
            print("- Si un jugador abandona y queda solo uno, este gana automáticamente.")
            print("- Los obstáculos son: serpiente 🐍 (retrocedes 3 casillas), sacrificio 🪦 (retrocedes el número del dado), inundación 🌊 (vuelves al inicio), y pozo 🕳️ (si sacas impar, pierdes).")

        elif opcion == '3':
            if juego:
                juego.ver_stats()
            else:
                print("No hay estadísticas disponibles aún. Juega una partida primero.")

        elif opcion == '4':
            print("¡Gracias por jugar!")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    menu()