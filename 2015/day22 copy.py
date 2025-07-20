from pathlib import Path
from heapq import heappush, heappop


SPELLS = {
    "Magic Missile": {"cost": 53, "damage": 4},
    "Drain": {"cost": 73, "damage": 2, "heal": 2},
    "Shield": {"cost": 113, "timer": 6},
    "Poison": {"cost": 173, "timer": 6},
    "Recharge": {"cost": 229, "timer": 5},
}


def parse_input(file_path):
    lines = Path(file_path).read_text().strip().splitlines()
    boss_hp = int(lines[0].split(":")[1])
    boss_damage = int(lines[1].split(":")[1])
    return boss_hp, boss_damage


def apply_effects(player_hp, player_mana, boss_hp, timers):
    new_timers = timers.copy()
    armor = 0

    if timers["Shield"] > 0:
        armor = 7
        new_timers["Shield"] -= 1
    if timers["Poison"] > 0:
        boss_hp -= 3
        new_timers["Poison"] -= 1
    if timers["Recharge"] > 0:
        player_mana += 101
        new_timers["Recharge"] -= 1

    return player_hp, player_mana, boss_hp, new_timers, armor


def simulate(boss_hp, boss_damage, hard_mode=False):
    initial_state = (
        0,  # total mana spent
        50,  # player_hp
        500,  # player_mana
        boss_hp,  # boss_hp
        {"Shield": 0, "Poison": 0, "Recharge": 0},  # timers
        True,  # is_player_turn
    )

    visited = {}
    heap = [initial_state]

    while heap:
        mana_spent, player_hp, player_mana, boss_hp, timers, is_player_turn = heappop(
            heap
        )

        state_key = (
            player_hp,
            player_mana,
            boss_hp,
            tuple(timers.items()),
            is_player_turn,
        )
        if state_key in visited and visited[state_key] <= mana_spent:
            continue
        visited[state_key] = mana_spent

        # Hard mode: perde 1 HP no início do turno do jogador
        if is_player_turn and hard_mode:
            player_hp -= 1
            if player_hp <= 0:
                continue

        # Aplicar efeitos ativos
        player_hp, player_mana, boss_hp, timers, armor = apply_effects(
            player_hp, player_mana, boss_hp, timers
        )

        # Vitória se boss morrer com efeitos
        if boss_hp <= 0:
            return mana_spent

        if is_player_turn:
            for spell, data in SPELLS.items():
                if data["cost"] > player_mana:
                    continue
                if spell in timers and timers[spell] > 0:
                    continue

                next_player_hp = player_hp
                next_player_mana = player_mana - data["cost"]
                next_boss_hp = boss_hp
                next_timers = timers.copy()
                next_mana_spent = mana_spent + data["cost"]

                # Aplicar efeitos imediatos
                if spell == "Magic Missile":
                    next_boss_hp -= data["damage"]
                elif spell == "Drain":
                    next_boss_hp -= data["damage"]
                    next_player_hp += data["heal"]
                elif spell in ["Shield", "Poison", "Recharge"]:
                    next_timers[spell] = data["timer"]

                if next_boss_hp <= 0:
                    return next_mana_spent

                heappush(
                    heap,
                    (
                        next_mana_spent,
                        next_player_hp,
                        next_player_mana,
                        next_boss_hp,
                        next_timers,
                        False,
                    ),  # type: ignore
                )
        else:
            damage = max(1, boss_damage - armor)
            next_player_hp = player_hp - damage
            if next_player_hp <= 0:
                continue
            heappush(
                heap,
                (mana_spent, next_player_hp, player_mana, boss_hp, timers.copy(), True),  # type: ignore
            )

    return None  # No solution found


def solve_part1(file_path):
    boss_hp, boss_damage = parse_input(file_path)
    return simulate(boss_hp, boss_damage, hard_mode=False)


def solve_part2(file_path):
    boss_hp, boss_damage = parse_input(file_path)
    return simulate(boss_hp, boss_damage, hard_mode=True)


def main():
    day = 22
    # input_path = Path(__file__).parent.parent / "inputs" / f"day_{day}.txt"
    input_path = Path(__file__).parent / "inputday22.txt"

    print("Parte 1:", solve_part1(input_path))
    print("Parte 2:", solve_part2(input_path))


if __name__ == "__main__":
    main()
