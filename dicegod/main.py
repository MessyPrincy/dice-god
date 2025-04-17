import random
from core import Die, Problem
from collections import Counter

DICE_SETUP = {
    "gold": [(4,2), (6,1)],
    "material": [(4,1)],
    "provisions": [(4,1)],
    "manpower": [(4,1)],
    "faith": [(4,1)]
}


def create_dice_pool(setup):
    pool = []
    for die_type, specs in setup.items():
        for sides, count in specs:
            for _ in range(count):
                pool.append(Die(sides, die_type))
    return pool

dice_pool = create_dice_pool(DICE_SETUP)

problems = [
    Problem("Gold Rush", "gold", 6)
]

# Game functions

def introduction():
    print("Welcome to the Divine Dice Game!")
    print("You will be rolling dice to solve divine problems.")
    print("Each problem requires specific types of dice and a minimum total to be solved.")
    print("Let's get started!")
    input()

def display_infromation(turn, health):
    print(f"\nTurn: {turn}")
    print(f"Health: {health}")
    display_dice_pool(dice_pool)
    input()

def display_dice_pool(dice_list):
    print("\nYou have the following dice in your pool:")
    dice_count = Counter((die.type, die.sides) for die in dice_list)
    for (die_type, sides), count in dice_count.items():
        print(f"- {count}× {die_type.title()} d{sides}")


def problems_this_turn(problems_list):
    print("\nDivine Problems this turn:")
    for i, problem in enumerate(problems_list, 1):
        print(f"{i}. {problem}")


def select_dice_for_problem(problem, dice_list):
    available = [die for die in dice_list if die.type == problem.type]
    print(f"\nSelect dice for: {problem.name} (need ≥{problem.min_total})")
    
    for i, die in enumerate(available, 1):
        print(f"{i}. d{die.sides}")

    raw = input("Enter the dice numbers you want, separated by spaces: ").strip()
    picks = sorted({int(x)-1 for x in raw.split() if x.isdigit()}, reverse=True)

    selected = []
    for index in picks:
        if 0 <= index < len(available):
            selected.append(available.pop(index))
            print(f"Selected d{selected[-1].sides}.")
        else:
            print(f"Ignored invalid choice: {index+1}")

    return selected


def update_dice_pool(dice_list, adjustments):
    for sides, die_type, count, add in adjustments:
        if add:
            for _ in range(count):
                dice_list.append(Die(sides, die_type))
            print(f"Added {count}× {die_type} d{sides}")
        else:
            removed = 0
            for _ in range(count):
                for die in dice_list:
                    if die.sides == sides and die.type == die_type:
                        dice_list.remove(die)
                        removed += 1
                        break
                else:
                    print(f"Couldn’t remove {die_type} d{sides}: none left")
                    break
            print(f"Removed {removed}× {die_type} d{sides}")


# Main game loop

def main():
    introduction()
    health = 1
    turn = 0
    while health > 0:
        turn += 1
        display_infromation(turn, health)
        problems_this_turn(problems)
        for problem in problems:
            selected = select_dice_for_problem(problem, dice_pool)
            adjustments = [
                (die.sides, die.type, 1, False)
                for die in selected
            ]
            update_dice_pool(dice_pool, adjustments)
        display_dice_pool(dice_pool)
        health -= 1

if __name__ == '__main__':
    main()
