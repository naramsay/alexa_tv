#!/user/bin/python

import logging
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
import os


app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

Id = "/home/****/.ssh/id_rsa"
user = "****"
host = "****"
ssh = "ssh -i {} {}@{} ".format(Id, user, host)

@ask.intent("TVon")
def tv_on():
    cmd = ssh + """'echo 'on 0' | cec-client -s'"""
    os.system(cmd)
    return statement('Turning TV on')

@ask.intent("TVoff")
def tv_off():
    cmd = ssh + """'echo 'standby 0' | cec-client -s'"""
    os.system(cmd)
    return statement('Turning TV off')


if __name__ == '__main__':

    app.run(debug=True)
