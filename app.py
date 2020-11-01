import pyautogui
import time
import constants as const

from flask import Flask
from flask import render_template

app = Flask(__name__)
import handcards
# flask run --host=0.0.0.0


@app.route('/')
def default(name=None):
    return render_template('main.html', name=name)


@app.route('/main')
def main(name=None):
    return render_template('main.html', name=name)


@app.route('/summon')
def summon(name=None):
    pyautogui.click(const.SUMMON_ACTIVATE_EFF)
    return render_template('hand.html')

@app.route('/special_summon')
def special_summon(name=None):
    return render_template('special_summon.html')

@app.route('/ssm1')
def ssm1(name=None):
    pyautogui.click(const.MONSTER_SEL_1)
    return render_template('special_summon.html')

@app.route('/ssm2')
def ssm2(name=None):
    pyautogui.click(const.MONSTER_SEL_2)
    return render_template('special_summon.html')

@app.route('/ssm3')
def ssm3(name=None):
    pyautogui.click(const.MONSTER_SEL_3)
    return render_template('special_summon.html')


@app.route('/draw_card')
def draw_card(name=None):
    pyautogui.click(const.DRAW_CARD_1)
    time.sleep(0.8)
    pyautogui.click(const.DRAW_CARD_2)
    return render_template('hand.html')


@app.route('/set')
def set_card(name=None):
    pyautogui.click(const.SET_CARD)
    return render_template('hand.html')


@app.route('/next_phase')
def next_phase(name=None):
    pyautogui.click(const.CHANGE_PHASE)
    return render_template('hand.html')


@app.route('/battle_phase')
def battle_phase(name=None):
    pyautogui.click(const.CHANGE_PHASE)
    return render_template('battle_phase.html')


@app.route('/goto_battle')
def goto_battle_phase(name=None):
    return render_template('battle_phase.html')


@app.route('/end_phase')
def end_phase(name=None):
    pyautogui.click(const.END_PHASE)
    return render_template('main.html')


@app.route('/attack')
def attack(name=None):
    pyautogui.click(const.ATTACK)
    return render_template('battle_phase.html')


@app.route('/mz1')
def mz1(name=None):
    pyautogui.click(const.MONSTER_ZONE_1)
    return render_template('battle_phase.html')


@app.route('/mz2')
def mz2(name=None):
    pyautogui.click(const.MONSTER_ZONE_2)
    return render_template('battle_phase.html')


@app.route('/mz3')
def mz3(name=None):
    pyautogui.click(const.MONSTER_ZONE_3)
    return render_template('battle_phase.html')



@app.route('/st1')
def st1(name=None):
    pyautogui.click(const.SPELL_TRAP_ZONE_1)
    return render_template('main.html')


@app.route('/st2')
def st2(name=None):
    pyautogui.click(const.SPELL_TRAP_ZONE_2)
    return render_template('main.html')


@app.route('/st3')
def st3(name=None):
    pyautogui.click(const.SPELL_TRAP_ZONE_3)
    return render_template('main.html')


@app.route('/confirm')
def confirm(name=None):
    pyautogui.click(const.CONFIRM)
    return render_template('hand.html')


@app.route('/back')
def back(name=None):
    pyautogui.click(const.BACK)
    return render_template('special_summon.html')


@app.route('/no')
def no(name=None):
    pyautogui.click(const.NO)
    return render_template('special_summon.html')


@app.route('/yes')
def yes(name=None):
    pyautogui.click(const.YES)
    return render_template('hand.html')


@app.route('/capture')
def mouse_capture():
    current_mouse_x, current_mouse_y = pyautogui.position()
    return 'x: '+str(current_mouse_x)+' y: '+str(current_mouse_y)




if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
