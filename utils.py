import os


def screenshot(trac, iter):
    os.system("xwd -root -out screenshot.xwd")
    os.system("convert screenshot.xwd test.png")
    os.system(f"cp test.png dataset_ss/{trac}-{iter}.png")
