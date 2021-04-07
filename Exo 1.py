import numpy as np
import matplotlib.pyplot as plt
import math

def main(n: int):

    plt.plot(np.array([ pow(i, 2) for i in range(1, n)])) #n²
    plt.plot(np.array([i* math.log(i) for i in range(1,n)])) #n log(n)
    plt.plot(np.array([ pow(2, i) for i in range(1, n)])) #2n
    plt.plot(np.array([i for i in range(1,n)])) #n
    plt.plot(np.array([math.log(i) for i in range(1,n)])) #log(n)
    plt.legend(['n2', 'n log(n)', '2n', 'n', 'log(n)'])
    plt.show()

if __name__ == '__main__':
    main(5)
