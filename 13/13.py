def binary_sequences(n):
    sequences = []
    count = 0

    def recursive_generator(idx=0, current=''):
        if idx == n:
            sequences.append(current)
            nonlocal count
            count += 1
            return

        recursive_generator(idx+1, current + '0')
        recursive_generator(idx+1, current + '1')

    return sequences, count


class Coins:

    def __init__(self, coins, _sum) -> None:
        self._sum = _sum
        self.no_of_coins = len(coins)
        self.coins = [None] + coins

    def solve_recursive(self):
        coins = self.coins

        def recursive_helper(i, j):
            if i == 0:
                return True
            if i < 0 or j == 0:
                return False

            return recursive_helper(i, j-1) or recursive_helper(i-coins[j], j-1)

        return recursive_helper(self._sum, self.no_of_coins)

    def solve(self):
        _sum = self._sum
        no_of_coins = self.no_of_coins
        coins = self.coins

        possible = [[False]*(no_of_coins+1) for _ in range(_sum+1)]
        possible[0][0] = True

        for i in range(1, _sum+1):
            for j in range(1, no_of_coins+1):
                possible[i][j] = possible[i][j-1]
                if i >= coins[j] and possible[i-coins[j]][j-1]:
                    possible[i][j] = True

        return possible[_sum][no_of_coins]