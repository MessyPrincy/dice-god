from core import Die, Problem

dice_pool = [
    Die(4, "gold"),
    Die(4, "material"),
    Die(4, "provisions"),
    Die(4, "manpower"),
    Die(4, "faith")
]

problems = [
    Problem("Gold Rush", "gold", 1),
    Problem("Material Shortage", "material", 7),
]

print("\nDivine Problems this turn:")
for i, problem in enumerate(problems):
    print(f"{i + 1}. {problem}")

print("\nDice Pool:")
for i, die in enumerate(dice_pool):
    print(f"{i + 1}. {die}")

assigned = {
    0: [0, 1],
    1: [2]     
}

print ("\nResolving Problems:")
for prob_index, die_indexes in assigned.items():
    problem = problems[prob_index]
    rolls = []
    for i in die_indexes:
        die = dice_pool[i]
        if die.type != problem.type:
            print(f"Error: {die} is not a {problem.type_required} die.")
            continue
        roll = die.roll()
        rolls.append(roll)
    success = problem.is_solved(rolls)
    print(f"\n{problem.name}: {'Success' if success else 'Failure'}")
    print(f"Rolls: {rolls}")