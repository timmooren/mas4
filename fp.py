import numpy as np
import nashpy as nash

A = np.array([[1, 2, 3, 3], [3, 4, 2, 4], [1, 2, 5, 2]])
B = np.array([[5, 2, 4, 1], [0, 1, 5, 2], [3, 6, 2, 3]])

game = nash.Game(A, B)

fp_generator = game.fictitious_play(iterations=10000)

final_strategy_A, final_strategy_B = None, None
for strategy_A, strategy_B in fp_generator:
    final_strategy_A, final_strategy_B = strategy_A, strategy_B

# show probabilities of each strategy
final_strategy_A = final_strategy_A / final_strategy_A.sum()
final_strategy_B = final_strategy_B / final_strategy_B.sum()

print("Player A's Final Mixed Strategy:", final_strategy_A)
print("Player B's Final Mixed Strategy:", final_strategy_B)
