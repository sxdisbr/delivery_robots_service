# delivery_robots_service
Calculate the minimum number of transport platforms needed to move robots.

    Given a list of weights representing individual robots and the weight limit
    for a transport platform, this function determines the minimum number of
    transport platforms required to move all the robots.

    Parameters:
    - weight (List[int]): A list of integers representing the weights of
      individual robots.
    - limit (int): The weight limit of a transport platform.

    Returns:
    - int: The minimum number of transport platforms needed.

    Example:
    >>> transport_robots([1, 2], 3)
    1
    >>> transport_robots([3, 2, 2, 1], 3)
    3
    >>> transport_robots([3, 5, 3, 4], 5)
    4
