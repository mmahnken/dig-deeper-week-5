from flask import g

def calc_welcome_message():
    if g.cool_stuff:
        return "HOWDY YOOOOOOO"
    else:
        return "HOWDY DONT"