from typing import List

def transport_robots(weight: List[int], limit: int) -> int:
    """
    Calculate the minimum number of transport platforms needed to move robots.
    """
    weight.sort(reverse=True)
    platforms = 0
    while weight:
        actual_weight = weight.pop(0)
        if weight and actual_weight + weight[-1] <= limit:
            weight.pop(0)
        platforms += 1
    return platforms

def main():
    weight = list(map(int, input().split()))
    limit = int(input())
    result = transport_robots(weight, limit)
    print(result)

if __name__ == '__main__':
    main()
