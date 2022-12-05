import pandas as pd


def load_data_part_1() -> dict:
    df = pd.read_fwf("data/input_part_1")
    result = {}
    for col in df.columns:
        result[col] = list(df[col].dropna().values)
    return result


def load_data_part_2() -> list:
    with open("data/input_part_2") as f:
        moves = []
        for line in f:
            moves.append([int(i) for i in line.strip().split() if i.isdigit()])
    return moves

def make_move(crates: dict, move: list, part_1: bool) -> list:
    crate_from = crates[str(move[1])]
    crate_to = crates[str(move[2])]
    n_crates_to_move = move[0]
    if part_1 is True:
        for _ in range(n_crates_to_move):
            crate_to.insert(0, crate_from.pop(0))
    else:
        crates_in_transit = crate_from[0:n_crates_to_move]
        crate_from = crate_from[n_crates_to_move:]
        crate_to = crates_in_transit + crate_to
    crates[str(move[1])] = crate_from
    crates[str(move[2])] = crate_to
    return crates


if __name__ == "__main__":
    crates_part_1 = load_data_part_1()
    crates_part_2 = load_data_part_1()
    moves = load_data_part_2()
    for move in moves:
        crates_part_1 = make_move(crates_part_1, move, True)
        crates_part_2 = make_move(crates_part_2, move, False)
    print("".join([i[0].replace("[", "").replace("]", "") for i in crates_part_1.values()]))
    print("".join([i[0].replace("[", "").replace("]", "") for i in crates_part_2.values()]))