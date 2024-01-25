from typing import List


def transport_robots(weight: List[int], limit: int) -> int:
    """
    Calculate the minimum number of transport platforms needed to move robots.
    """
    weight.sort(reverse=True)
    platforms: int = 0
    left_pointer, right_pointer = 0, len(weight) - 1

    while left_pointer <= right_pointer:
        # If two robots can fit on the platform, we move both pointers.
        if weight[left_pointer] + weight[right_pointer] <= limit:
            left_pointer += 1
        # In any case, move the right pointer.
        right_pointer -= 1

    return platforms


def main():
    weight = list(map(int, input().split()))
    limit = int(input())
    result = transport_robots(weight, limit)
    print(result)


if __name__ == '__main__':
    main()

