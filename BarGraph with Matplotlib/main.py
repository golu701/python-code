# pip install matplotlib
from matplotlib import pyplot as plt

players = ["first", "second", "third", "fourth"]
score = [55, 90, 42, 36]
plt.bar(players, score, color="red")
plt.title("Score card")
plt.xlabel("Players ")
plt.ylabel("scores")
plt.show()
