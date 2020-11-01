import pyautogui
import constants as const
from flask import render_template

from app import app


@app.route('/hand')
def hand(name=None):
    return render_template('hand.html', name=name)


@app.route('/selhand1')
def selhand1(name=None):
    return render_template('hand1.html', name=name)


@app.route('/selhand2')
def selhand2(name=None):
    return render_template('hand2.html', name=name)


@app.route('/selhand3')
def selhand3(name=None):
    return render_template('hand3.html', name=name)


@app.route('/selhand4')
def selhand4(name=None):
    return render_template('hand4.html', name=name)


@app.route('/selhand5')
def selhand5(name=None):
    return render_template('hand5.html', name=name)


@app.route('/selhand6')
def selhand6(name=None):
    return render_template('hand6.html', name=name)


@app.route('/selhand7')
def selhand7(name=None):
    return render_template('hand7.html', name=name)


@app.route('/hand1')
def hand1(name=None):
    return render_template('hand.html', name=name)


@app.route('/hand2')
def hand2(name=None):
    return render_template('hand.html', name=name)


@app.route('/hand3')
def hand3(name=None):
    return render_template('hand.html', name=name)


@app.route('/hand4')
def hand4(name=None):
    return render_template('hand.html', name=name)


@app.route('/hand5')
def hand5(name=None):
    return render_template('hand.html', name=name)


@app.route('/hand6')
def hand6(name=None):
    return render_template('hand.html', name=name)


@app.route('/hand7')
def hand7(name=None):
    return render_template('hand.html', name=name)
@app.route('/hand_1_1')
def hand_1_1(name=None):
    pyautogui.click(const.HAND_1_1)
    return render_template('hand.html', name=name)


@app.route('/hand_2_1')
def hand_2_1(name=None):
    pyautogui.click(const.HAND_2_1)
    return render_template('hand.html', name=name)


@app.route('/hand_2_2')
def hand_2_2(name=None):
    pyautogui.click(const.HAND_2_2)
    return render_template('hand.html', name=name)


@app.route('/hand_3_1')
def hand_3_1(name=None):
    pyautogui.click(const.HAND_3_1)
    return render_template('hand.html', name=name)


@app.route('/hand_3_2')
def hand_3_2(name=None):
    pyautogui.click(const.HAND_3_2)
    return render_template('hand.html', name=name)


@app.route('/hand_3_3')
def hand_3_3(name=None):
    pyautogui.click(const.HAND_3_3)
    return render_template('hand.html', name=name)


@app.route('/hand_4_1')
def hand_4_1(name=None):
    pyautogui.click(const.HAND_4_1)
    return render_template('hand.html', name=name)


@app.route('/hand_4_2')
def hand_4_2(name=None):
    pyautogui.click(const.HAND_4_2)
    return render_template('hand.html', name=name)


@app.route('/hand_4_3')
def hand_4_3(name=None):
    pyautogui.click(const.HAND_4_3)
    return render_template('hand.html', name=name)


@app.route('/hand_4_4')
def hand_4_4(name=None):
    pyautogui.click(const.HAND_4_4)
    return render_template('hand.html', name=name)

@app.route('/hand_5_1')
def hand_5_1(name=None):
    pyautogui.click(const.HAND_5_1)
    return render_template('hand.html', name=name)


@app.route('/hand_5_2')
def hand_5_2(name=None):
    pyautogui.click(const.HAND_5_2)
    return render_template('hand.html', name=name)


@app.route('/hand_5_3')
def hand_5_3(name=None):
    pyautogui.click(const.HAND_5_3)
    return render_template('hand.html', name=name)


@app.route('/hand_5_4')
def hand_5_4(name=None):
    pyautogui.click(const.HAND_5_4)
    return render_template('hand.html', name=name)


@app.route('/hand_5_5')
def hand_5_5(name=None):
    pyautogui.click(const.HAND_5_5)
    return render_template('hand.html', name=name)


@app.route('/hand_6_1')
def hand_6_1(name=None):
    pyautogui.click(const.HAND_6_1)
    return render_template('hand.html', name=name)


@app.route('/hand_6_2')
def hand_6_2(name=None):
    pyautogui.click(const.HAND_6_2)
    return render_template('hand.html', name=name)


@app.route('/hand_6_3')
def hand_6_3(name=None):
    pyautogui.click(const.HAND_6_3)
    return render_template('hand.html', name=name)


@app.route('/hand_6_4')
def hand_6_4(name=None):
    pyautogui.click(const.HAND_6_4)
    return render_template('hand.html', name=name)


@app.route('/hand_6_5')
def hand_6_5(name=None):
    pyautogui.click(const.HAND_6_5)
    return render_template('hand.html', name=name)


@app.route('/hand_6_6')
def hand_6_6(name=None):
    pyautogui.click(const.HAND_6_6)
    return render_template('hand.html', name=name)


@app.route('/hand_7_1')
def hand_7_1(name=None):
    pyautogui.click(const.HAND_7_1)
    return render_template('hand.html', name=name)


@app.route('/hand_7_2')
def hand_7_2(name=None):
    pyautogui.click(const.HAND_7_2)
    return render_template('hand.html', name=name)


@app.route('/hand_7_3')
def hand_7_3(name=None):
    pyautogui.click(const.HAND_7_3)
    return render_template('hand.html', name=name)


@app.route('/hand_7_4')
def hand_7_4(name=None):
    pyautogui.click(const.HAND_7_4)
    return render_template('hand.html', name=name)


@app.route('/hand_7_5')
def hand_7_5(name=None):
    pyautogui.click(const.HAND_7_5)
    return render_template('hand.html', name=name)


@app.route('/hand_7_6')
def hand_7_6(name=None):
    pyautogui.click(const.HAND_7_6)
    return render_template('hand.html', name=name)


@app.route('/hand_7_7')
def hand_7_7(name=None):
    pyautogui.click(const.HAND_7_7)
    return render_template('hand.html', name=name)

