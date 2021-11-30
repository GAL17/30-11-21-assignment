import numpy as np
import itertools

def make_inputs(num_columns): # Input - number of columns, Output - array with all the possibilities
    arr = np.array(list(itertools.product([0,1], repeat=num_columns)))
    return arr

def check_valid(arr): # Checks if the array from "make_inputs" is valid
    if (not np.array_equal(arr, make_inputs(5))):
        return make_inputs(5)

def train_test_split(arr, split=0.7): # Input - The possibilities array and a split, Output - A tuple with two arrays for training and testing
    if type(arr) != np.ndarray:
        arr = np.array(arr)

    np.random.seed(3)
    np.random.shuffle(arr)

    return (arr[: int(len(arr) * split)], arr[int(len(arr) * split) :])


inps = make_inputs(5)
print(train_test_split(list(inps)))