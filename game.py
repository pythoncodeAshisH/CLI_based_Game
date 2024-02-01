import random


# Base classes
class Gun:
    def shoot(self):
        pass


class Animal:
    def __init__(self, points):
        self.points = points


# Specific guns
class Rifle(Gun):
    def shoot(self):
        return random.choice([True, False])


class Shotgun(Gun):
    def shoot(self):
        return random.choice([True, False, False])  # Higher chance of missing


# Specific animals
class Deer(Animal):
    def __init__(self):
        super().__init__(10)


class Bear(Animal):
    def __init__(self):
        super().__init__(20)


# Player class
class Player:
    def __init__(self, gun):
        self.gun = gun
        self.points = 0

    def shoot(self, animal):
        if self.gun.shoot():
            self.points += animal.points
            return True
        return False


# Game class
class Game:
    def __init__(self):
        self.player = None
        self.animals = [Deer(), Bear()]

    def select_gun(self):
        choice = input("Select a gun (1: Rifle, 2: Shotgun): ")
        if choice == '1':
            self.player = Player(Rifle())
        else:
            self.player = Player(Shotgun())

    def start(self):
        self.select_gun()
        for _ in range(5):  # Let's say 5 turns
            animal = random.choice(self.animals)
            print(f"An animal appears: {animal.__class__.__name__}")
            shoot = input("Do you want to shoot? (yes/no): ")
            if shoot.lower() == 'yes':
                if self.player.shoot(animal):
                    print(f"You hit a {animal.__class__.__name__}! Points: {self.player.points}")
                else:
                    print("You missed!")
        print(f"Game over. Total points: {self.player.points}")


# Running the game
if __name__ == "__main__":
    game = Game()
    game.start()
