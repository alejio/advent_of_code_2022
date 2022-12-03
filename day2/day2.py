import pandas as pd


def load_data() -> pd.DataFrame:
    df = pd.read_csv("data/input", sep=" ", names=["player_1_move", "unsure_column_meaning"])
    return df



points = {"X": 1,
          "Y": 2,
          "Z": 3}

def result(player_1_move, player_2_move) -> str:
    if player_1_move == "A":
        if player_2_move == "Y":
            return "W"
        elif player_2_move == "Z":
            return "L"
    elif player_1_move == "B":
        if player_2_move == "X":
            return "L"
        elif player_2_move == "Z":
            return "W"
    elif player_1_move == "C":
        if player_2_move == "X":
            return "W"
        elif player_2_move == "Y":
            return "L"
    return "D"

def score(player_1_move: str, player_2_move: str) -> int:
    score = 0
    match_result = result(player_1_move, player_2_move)
    score += points[player_2_move]
    if match_result == "D":
        score += 3
    elif match_result == "L":
        score += 0
    else:
        score += 6
    return score


def calculate_move(player_1_move, result) -> str:
    result_mapper = {"X": "L",
                     "Y": "D",
                     "Z": "W"}
    if result_mapper[result] == "L":
        if player_1_move == "A":
            return "Z"
        elif player_1_move == "B":
            return "X"
        else:
            return "Y"
    elif result_mapper[result] == "D":
        if player_1_move == "A":
            return "X"
        elif player_1_move == "B":
            return "Y"
        else:
            return "Z"
    else:
        if player_1_move == "A":
            return "Y"
        elif player_1_move == "B":
            return "Z"
        else:
            return "X"


def process_df(df: pd.DataFrame) -> pd.DataFrame:
    df.rename(columns={"unsure_column_meaning": "result"}, inplace=True)
    df["calculated_player_2_move"] = df.apply(lambda x: calculate_move(x["player_1_move"],
                                                                       x["result"]), axis=1)
    return df


def calculate_total_score(df: pd.DataFrame, player_1_move, player_2_move) -> int:
    df["score"] = df.apply(lambda x: score(x[player_1_move], x[player_2_move]), axis=1)
    return df["score"].sum()


if __name__ == "__main__":
    df = load_data()
    total_score_part_1 = calculate_total_score(df, "player_1_move", "unsure_column_meaning")
    print(total_score_part_1)
    df = process_df(df)
    total_score_part_2 = calculate_total_score(df, "player_1_move", "calculated_player_2_move")
    print(total_score_part_2)