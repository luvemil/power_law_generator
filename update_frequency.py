# I have an array of n equiprobable choices. Users arrive and choose, this alter
# the probability of next user and so on. What's the limit distribution?

import numpy as np
import random
import powerlaw
import matplotlib.pyplot as plt

def increase(arr, index):
    """This is the function that will increase the frequency, given that last
    choice was index."""
    # A simple function for now
    arr[index] += 1
    return arr

def choose(cumul):
    """This algorithm choose an element between 0 and n-1 with the relative
    frequencies given by arr."""
    n = cumul.size
    val = random.randint(1, cumul[n-1])
    return cumul.searchsorted(val)

def do_stuff(data):
    fit = powerlaw.Fit(data)
    fig1 = fit.plot_pdf(color='b', linewidth=2)
    fit.power_law.plot_pdf(color='b', linestyle='--', ax=fig1)
    fit.plot_ccdf(color='r', linewidth=2, ax=fig1)
    fit.power_law.plot_ccdf(color='r', linestyle='--', ax=fig1)
    plt.show()

def main():
    freq = 10 # the starting frequency
    n = 10 # starting number of blogs
    final = 10000 # final number of blogs
    increm = 100 # Time different between increments in the number of blogs
    iter = 1000000 # How many iterations

    arr = np.array([freq for i in range(0,n)])
    for i in range(iter):
        cumul = arr.cumsum()
        index = choose(cumul)
        arr = increase(arr,index)
        if i % increm == 0 and arr.size < final:
            arr = np.resize(arr, (arr.size+1))
            arr[arr.size - 1] = freq
        if i % 100000 == 0:
            print(i)

    do_stuff(arr-freq)

if __name__=="__main__":
    main()
