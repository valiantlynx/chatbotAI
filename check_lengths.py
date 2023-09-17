
def find_different_lengths(arr):
    # Initialize a dictionary to store the indices where lengths differ
    differing_lengths = {}

    # Iterate through the outer array
    for i, inner_arr in enumerate(arr):
        # Get the lengths of the inner arrays
        lengths = [len(sub_arr) for sub_arr in inner_arr]

        # Check if all lengths are the same
        if len(set(lengths)) > 1:
            differing_lengths[i] = lengths

    # Print the result
    for i, lengths in differing_lengths.items():
        print(f"At index {i}, lengths are: {lengths}")



