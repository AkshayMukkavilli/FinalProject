import os
import sys
from src.crawlers.upper_lower_percentages import percentages_upper_lower
print(f"this is from os.path: {os.getcwd()}")
print(f"this is from sys.path: {sys.path}")


print(__name__)

from matplotlib import pyplot as plt
fig, ax = plt.subplots(3, figsize=(6, 14))
print(ax)
print(type(ax))
print(len(ax))
for a in ax:
    print(a)

print(zip(range(len(ax))))