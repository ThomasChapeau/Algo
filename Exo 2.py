import numpy as np
import math


def main():

    sec = 1
    print("Pour", sec, "secondes : ")

    instruc = (float(sec)) / 10**-7

    print("Nombre d'instruction :", instruc)
    print("log(n) :"  , np.log10(instruc))
    print("n :"       , instruc)
    print("n log(n) :", instruc * math.log10(instruc))
    print("n² :"      , pow(instruc, 2))
    print("2^n :"     , pow(2, instruc))


if __name__ == '__main__':
    main()