import automate
import logic
import utils
import random
init = automate.roboflow_init()
iter = 1
trac = random.randint(1, 2000)

while (1):
    utils.screenshot(trac, iter)
    data = automate.roboflow_exec(init)
    t_cat = logic.num_cal(data)
    print("total cats :", t_cat)
    matrix_data = logic.array(t_cat, data)
    # print(matrix_data)
    logic.pair_move(t_cat, matrix_data)
    iter += 1
