import numpy as np


def load_and_prep_data():
    with open("data/input") as f:
        data = [line.strip() for line in f]
    return data


def transform_data(data: list) -> np.array:
    out = [[int(d) for d in l] for l in data]
    out = np.array(out)
    return out


def element_visibility(trees: np.array,
                       idx_x: int, idx_y: int) -> bool:
    # left_visibility
    if idx_y == 0:
        left_visibility = True
    else:
        max_previous_tree = trees[idx_x, :idx_y].max()
        left_visibility = trees[idx_x, idx_y] > max_previous_tree
    # right_visibility
    if idx_y == trees.shape[1] - 1:
        right_visibility = True
    else:
        max_next_tree = trees[idx_x, idx_y + 1:].max()
        right_visibility = trees[idx_x, idx_y] > max_next_tree
    # up visibility
    if idx_x == 0:
        up_visibility = True
    else:
        max_up_tree = trees[:idx_x, idx_y].max()
        up_visibility = trees[idx_x, idx_y] > max_up_tree
    # down visibility
    if idx_x == trees.shape[0] - 1:
        down_visibility = True
    else:
        max_down_tree = trees[idx_x + 1:, idx_y].max()
        down_visibility = trees[idx_x, idx_y] > max_down_tree
    return left_visibility or right_visibility or up_visibility or down_visibility


def calculate_total_visible(data: np.array) -> int:
    dimensions = data.shape
    counter = 0
    for i in range(0, dimensions[0]):
        for j in range(0, dimensions[1]):
            if element_visibility(data, i, j):
                counter += 1
    return counter


def calculate_left_visible_trees(trees: np.array,
                            idx_x: int,
                            idx_y: int) -> int:
    tree = trees[idx_x, idx_y]
    # number of left visible
    if idx_y == 0:
        n_left = 0
    else:
        n_left = 0
        for idx in reversed(range(0, idx_y)):
            if trees[idx_x, idx] < tree:
                n_left += 1
            else:
                n_left += 1
                break
    return n_left


def calculate_right_visible_trees(trees: np.array,
                                 idx_x: int,
                                 idx_y: int) -> int:
    tree = trees[idx_x, idx_y]
    # number of right visible
    if idx_y == trees.shape[1] - 1:
        n_right = 0
    else:
        n_right = 0
        for idx in range(idx_y + 1, trees.shape[1]):
            if trees[idx_x, idx] < tree:
                n_right += 1
            else:
                n_right += 1
                break
    return n_right


def calculate_up_visible_trees(trees: np.array,
                                  idx_x: int,
                                  idx_y: int) -> int:
    tree = trees[idx_x, idx_y]
    # number of up visible
    if idx_x == 0:
        n_up = 0
    else:
        n_up = 0
        for idx in reversed(range(0, idx_x - 1)):
            if trees[idx, idx_y] < tree:
                n_up += 1
            else:
                n_up += 1
                break
    return n_up


def calculate_down_visible_trees(trees: np.array,
                                  idx_x: int,
                                  idx_y: int) -> int:
    tree = trees[idx_x, idx_y]
    # number of down visible
    if idx_x == trees.shape[1] - 1:
        n_down = 0
    else:
        n_down = 0
        for idx in range(idx_x + 1, trees.shape[1]):
            if trees[idx, idx_y] < tree:
                n_down += 1
            else:
                n_down += 1
                break
    return n_down


def calculate_visibility_score(left: int, right: int, down: int, up: int) -> int:
    return left * right * down * up


def calculate_vis_score_for_each_tree(trees: np.array):
    dimensions = trees.shape
    scores = []
    for i in range(0, dimensions[0]):
        temp_list = []
        for j in range(0, dimensions[1]):
            left_v_trees = calculate_left_visible_trees(trees, i, j)
            right_v_trees = calculate_right_visible_trees(trees, i, j)
            up_v_trees = calculate_up_visible_trees(trees, i, j)
            down_v_trees = calculate_down_visible_trees(trees, i, j)
            temp_list.append(calculate_visibility_score(left_v_trees, right_v_trees, down_v_trees, up_v_trees))
        scores.append(temp_list)
    return max(max(l) for l in scores)


if __name__ == "__main__":
    data = load_and_prep_data()
    data = transform_data(data)
    print(calculate_total_visible(data))
    print(calculate_vis_score_for_each_tree(data))
