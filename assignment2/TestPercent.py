def percent_to_graph(pcnt, max_length):
    """
    Converts a percentage value (0.0 to 1.0) into a graph with symbols (#) and spaces.
    :param pcnt: A float value between 0.0 and 1.0 (inclusive).
    :param max_length: The total length of the graph (number of symbols + spaces).
    :return: A string representing the graph.
    """
    # Calculate the number of symbols (#) based on the percentage
    num_symbols = round(pcnt * max_length)
    # Calculate the remaining spaces
    num_spaces = max_length - num_symbols
    # Return the graph as a string
    return '#' * num_symbols + ' ' * num_spaces
