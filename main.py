from abc import ABC, abstractmethod
import random


# Шаг 1: Создаем абстрактный класс Weapon
class Weapon(ABC):
    @abstractmethod
    def attack(self, attack_type: str):
        pass


# Шаг 2: Реализуем конкретные типы оружия

class Sword(Weapon):
    def attack(self, attack_type: str):
        print(f"Боец наносит удар мечом {attack_type}.")


class Bow(Weapon):
    def attack(self, attack_type: str):
        print(f"Боец наносит удар из лука {attack_type}.")


# Шаг 3: Модифицируем класс Fighter

class Fighter:
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def changeWeapon(self, weapon: Weapon):
        self.weapon = weapon

    def attack(self, attack_type: str):
        self.weapon.attack(attack_type)


# Шаг 4: Реализация боя

class Monster:
    def __init__(self, health: int):
        self.health = health

    def block(self):
        # Монстр случайным образом выбирает направление блока
        return random.choice(["слева", "справа", "прямым ударом"])

    def take_damage(self, damage: int):
        self.health -= damage
        if self.health <= 0:
            print("Монстр побежден!")
        else:
            print(f"У монстра осталось {self.health} здоровья.")


# Пример использования
if __name__ == "__main__":
    sword = Sword()
    bow = Bow()

    fighter = Fighter(sword)
    monster = Monster(health=100)

    while monster.health > 0:
        print("\nВыберите оружие: 1 - Меч, 2 - Лук")
        weapon_choice = input("Ваш выбор: ")
        if weapon_choice == "1":
            fighter.changeWeapon(sword)
        elif weapon_choice == "2":
            fighter.changeWeapon(bow)
        else:
            print("Неверный выбор, попробуйте снова.")
            continue

        print("\nВыберите тип удара: 1 - Слева, 2 - Справа, 3 - Прямым ударом")
        attack_choice = input("Ваш выбор: ")
        if attack_choice == "1":
            attack_type = "слева"
        elif attack_choice == "2":
            attack_type = "справа"
        elif attack_choice == "3":
            attack_type = "прямым ударом"
        else:
            print("Неверный выбор, попробуйте снова.")
            continue

        monster_block = monster.block()
        print(f"Монстр ставит блок {monster_block}.")

        if attack_type == monster_block:
            print("Монстр заблокировал атаку!")
        else:
            fighter.attack(attack_type)
            monster.take_damage(50)

        if monster.health <= 0:
            print("Вы победили монстра!")
            break