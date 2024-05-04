import numpy as np


def num_cal(data):
    x = 0
    for dx in data['predictions']:
        x += 1
    return x


def array(t_cat, data):
    parameters = 4
    temp = np.arange(t_cat * parameters,
                     dtype=object).reshape(t_cat, parameters)
    iter = 0
    for dx in data['predictions']:
        # x-axis
        temp[iter][0] = dx['x']
        # y-axis
        temp[iter][1] = dx['y']
        # confidence
        temp[iter][2] = round(dx['confidence']*100)
        # class
        temp[iter][3] = dx['class']
        # iter
        iter += 1

    temp = sorted(temp, key=lambda x: x[3])

    return temp


def pair_move(t_cat, data):
    import move
    import time
    for i in range(t_cat-1):
        if data[i][3] == data[i+1][3]:
            print("\nmatched")
            print("moving")
            print(data[i])
            print("to")
            print(data[i+1])
            move.add(data[i][0], data[i][1],
                     data[i+1][0], data[i+1][1])
            time.sleep(1)
