#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on November 27, 2022, at 11:30
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from prac_ssst_iti_draw
msg = "do!"
# Run 'Before Experiment' code from prac_tom_code
msg = 'do!'
# Run 'Before Experiment' code from prac_ssst_iti_draw
msg = "do!"
# Run 'Before Experiment' code from prac_ssst_iti_draw
msg = "do!"
# Run 'Before Experiment' code from prac_ssst_iti_draw
msg = "do!"
# Run 'Before Experiment' code from code
msg= "do!"


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'Dual-task'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'Phone number last five*': '',
    'Email*': '',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\psychopy_full_dual-task\\full_dual-task_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "welcome" ---
text = visual.TextStim(win=win, name='text',
    text='Welcome!\n\nHere you will play two games. But first, we will practice these games.\n\nDuring the practice you will recieve feedback on your responses but you will not during the actual game. \n\nAfter you complete the practices and tasks you will be given a link to complete the final part of the study.\n\nTo continue press SPACEBAR.\n',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
welcome_adv = keyboard.Keyboard()

# --- Initialize components for Routine "ssst_prac_inst" ---
ssst_inst1 = visual.TextStim(win=win, name='ssst_inst1',
    text='Shapes game practice\n\nIn this game, you will respond as fast as you can to a downward arrow by pressing the SPACEBAR with your RIGHT THUMB.\n',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
ssst_inst2 = visual.TextStim(win=win, name='ssst_inst2',
    text='But wait, if a red diamond appears after the arrow –  PRESS ‘K’ with your RIGHT INDEX FINGER.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
ssst_inst3 = visual.TextStim(win=win, name='ssst_inst3',
    text='If a green square appears after the downward arrow – do not press anything. ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
ssst_inst5 = visual.ImageStim(
    win=win,
    name='ssst_inst5', 
    image='practice_stimuli/inst_ssst.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
ssst_inst6 = visual.TextStim(win=win, name='ssst_inst6',
    text='Remember to respond as fast as you can!\n\nShapes game practice will start in 10 seconds or press SPACEBAR to start. ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "prac_ssst_trial" ---
# Run 'Begin Experiment' code from prac_ssst_staircase
# setting parameters for staircase
ssd_prac = 0.15 # starts at 150ms
stepsize = 0.05 # steps of 50ms
minval = 0.05 # minimum value of 50ms for SSD
maxval = 1.05 # maxSSD is 1050ms



prac_ssst_go = visual.ImageStim(
    win=win,
    name='prac_ssst_go', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
prac_ssst_stop = visual.ImageStim(
    win=win,
    name='prac_ssst_stop', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
prac_ssst_resp = keyboard.Keyboard()

# --- Initialize components for Routine "prac_ssst_iti" ---
prac_ssst_iti_cross = visual.TextStim(win=win, name='prac_ssst_iti_cross',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "prac_tom_inst" ---
tom_inst1 = visual.TextStim(win=win, name='tom_inst1',
    text='Cartoon game practice\n\nHere you will see three cartoon story scenes and it is up to you to decide the ending of these stories. ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
tom_inst1_2 = visual.TextStim(win=win, name='tom_inst1_2',
    text='To solve these stories, you will have to try to take the perspective of the characters to decide the most possible ending. ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
tom_inst1_3 = visual.TextStim(win=win, name='tom_inst1_3',
    text='There are no wrong or right solutions. We are interested in your thoughts on how the story might end, considering the characters’ feelings and thoughts.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
tom_inst2 = visual.TextStim(win=win, name='tom_inst2',
    text='Your choices will be labeled 1, 2, and 3 and you will select your option by pressing 1, 2, or 3 at the top of your keyboard with your left hand. ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
tom_inst3 = visual.TextStim(win=win, name='tom_inst3',
    text='DO NOT use numbers on the right of your keyboard ONLY USE the numbers at the top of your keyboard. ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
tom_inst4 = visual.ImageStim(
    win=win,
    name='tom_inst4', 
    image='practice_stimuli/inst_tom.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
tom_inst5 = visual.TextStim(win=win, name='tom_inst5',
    text='Cartoon game practice will start in 10 seconds or press SPACEBAR',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
tom_inst_resp = keyboard.Keyboard()

# --- Initialize components for Routine "prac_tom_trial" ---
prac_tom1 = visual.ImageStim(
    win=win,
    name='prac_tom1', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
prac_tom2 = visual.ImageStim(
    win=win,
    name='prac_tom2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
prac_tom3 = visual.ImageStim(
    win=win,
    name='prac_tom3', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
prac_tom_dec = visual.ImageStim(
    win=win,
    name='prac_tom_dec', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
prac_tom_resp = keyboard.Keyboard()

# --- Initialize components for Routine "prac_tom_iti" ---
prac_tom_fb = visual.TextStim(win=win, name='prac_tom_fb',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "prac_dual_inst" ---
dual_inst1 = visual.TextStim(win=win, name='dual_inst1',
    text='Combined Game Practice\n\nHere you will be asked to play both games at the same time',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
dual_inst2 = visual.TextStim(win=win, name='dual_inst2',
    text='You will use the same buttons as the prior games, but you will use all of them in this combined game.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
dual_inst3 = visual.TextStim(win=win, name='dual_inst3',
    text='Please place your both of your hands on the left and right sides of the keyboard to play the combined game.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
dual_inst4 = visual.ImageStim(
    win=win,
    name='dual_inst4', 
    image='practice_stimuli/inst_dual-task.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
dial_inst5 = visual.TextStim(win=win, name='dial_inst5',
    text='Combined game practice will start in 10 seconds or press SPACEBAR. ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
dual_inst_resp = keyboard.Keyboard()

# --- Initialize components for Routine "prac_ssst_trial" ---
# Run 'Begin Experiment' code from prac_ssst_staircase
# setting parameters for staircase
ssd_prac = 0.15 # starts at 150ms
stepsize = 0.05 # steps of 50ms
minval = 0.05 # minimum value of 50ms for SSD
maxval = 1.05 # maxSSD is 1050ms



prac_ssst_go = visual.ImageStim(
    win=win,
    name='prac_ssst_go', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
prac_ssst_stop = visual.ImageStim(
    win=win,
    name='prac_ssst_stop', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
prac_ssst_resp = keyboard.Keyboard()

# --- Initialize components for Routine "prac_ssst_iti" ---
prac_ssst_iti_cross = visual.TextStim(win=win, name='prac_ssst_iti_cross',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "prac_dual_tom1" ---
prac_d_tom1 = visual.ImageStim(
    win=win,
    name='prac_d_tom1', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "prac_ssst_trial" ---
# Run 'Begin Experiment' code from prac_ssst_staircase
# setting parameters for staircase
ssd_prac = 0.15 # starts at 150ms
stepsize = 0.05 # steps of 50ms
minval = 0.05 # minimum value of 50ms for SSD
maxval = 1.05 # maxSSD is 1050ms



prac_ssst_go = visual.ImageStim(
    win=win,
    name='prac_ssst_go', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
prac_ssst_stop = visual.ImageStim(
    win=win,
    name='prac_ssst_stop', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
prac_ssst_resp = keyboard.Keyboard()

# --- Initialize components for Routine "prac_ssst_iti" ---
prac_ssst_iti_cross = visual.TextStim(win=win, name='prac_ssst_iti_cross',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "prac_dual_tom2" ---
prac_d_tom2 = visual.ImageStim(
    win=win,
    name='prac_d_tom2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "prac_ssst_trial" ---
# Run 'Begin Experiment' code from prac_ssst_staircase
# setting parameters for staircase
ssd_prac = 0.15 # starts at 150ms
stepsize = 0.05 # steps of 50ms
minval = 0.05 # minimum value of 50ms for SSD
maxval = 1.05 # maxSSD is 1050ms



prac_ssst_go = visual.ImageStim(
    win=win,
    name='prac_ssst_go', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
prac_ssst_stop = visual.ImageStim(
    win=win,
    name='prac_ssst_stop', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
prac_ssst_resp = keyboard.Keyboard()

# --- Initialize components for Routine "prac_ssst_iti" ---
prac_ssst_iti_cross = visual.TextStim(win=win, name='prac_ssst_iti_cross',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "prac_dual_tom3" ---
prac_d_tom3 = visual.ImageStim(
    win=win,
    name='prac_d_tom3', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "prac_dual_tom_dec" ---
prac_d_tom_choice = visual.ImageStim(
    win=win,
    name='prac_d_tom_choice', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
prac_d_tom_resp = keyboard.Keyboard()

# --- Initialize components for Routine "prac_d_tom_iti" ---
prac_d_tom_fb = visual.TextStim(win=win, name='prac_d_tom_fb',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "real_task_inst" ---
trial_inst = visual.TextStim(win=win, name='trial_inst',
    text='Rest for 15 seconds - we will start the study next. \n\nPlease place you left and right hands on the keyboard as instructred. \n\nRemember, if you respond to > 90% of the trials you will recieve an additional 10 dollars, so respond as quickly and as accurately as you can.\n\nYou will no longer recieve feedback about your response.\n\n\n\n',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
trial_inst2 = visual.TextStim(win=win, name='trial_inst2',
    text='Press SPACEBAR to start to start the task',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
trial_start = keyboard.Keyboard()

# --- Initialize components for Routine "tom_intro" ---
tom_task = visual.TextStim(win=win, name='tom_task',
    text='Now you will play the cartoon game.\n\npress SPACEBAR',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
tom_int_resp = keyboard.Keyboard()

# --- Initialize components for Routine "tom_single_trial" ---
tom_s_1 = visual.ImageStim(
    win=win,
    name='tom_s_1', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
tom_s_2 = visual.ImageStim(
    win=win,
    name='tom_s_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
tom_s_3 = visual.ImageStim(
    win=win,
    name='tom_s_3', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
tom_s_dec = visual.ImageStim(
    win=win,
    name='tom_s_dec', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
tom_s_resp = keyboard.Keyboard()

# --- Initialize components for Routine "ITI_2000" ---
tom_iti = visual.TextStim(win=win, name='tom_iti',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "rest" ---
rest_15 = visual.TextStim(win=win, name='rest_15',
    text='Take a 15 second break before the next task.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
rest_15_2 = visual.TextStim(win=win, name='rest_15_2',
    text='Press SPACEBAR to continue. ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
rest_resp = keyboard.Keyboard()

# --- Initialize components for Routine "dual_intro" ---
dual_task_intro = visual.TextStim(win=win, name='dual_task_intro',
    text='Now you will play the combination game.\n\nRemember to respond as fast as you can!\n\npress SPACEBAR',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
dual_task_intro_resp = keyboard.Keyboard()

# --- Initialize components for Routine "dual_iti" ---
dual_iti_cross = visual.TextStim(win=win, name='dual_iti_cross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "ssst_iti" ---
ssst_iti_cross = visual.TextStim(win=win, name='ssst_iti_cross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "stop_sig" ---
# Run 'Begin Experiment' code from ssst_staircase
# setting parameters for staircase
ssd = 0.15 # starts at 150ms
stepsize = 0.05 # steps of 50ms
minval = 0.05 # minimum value of 50ms for SSD
maxval = 1.05 # maxSSD is 1050ms



ssst_go = visual.ImageStim(
    win=win,
    name='ssst_go', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
ssst_stop = visual.ImageStim(
    win=win,
    name='ssst_stop', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
ssst_resp = keyboard.Keyboard()

# --- Initialize components for Routine "tom_dual_1" ---
tom_d_1 = visual.ImageStim(
    win=win,
    name='tom_d_1', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "ssst_iti" ---
ssst_iti_cross = visual.TextStim(win=win, name='ssst_iti_cross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "stop_sig" ---
# Run 'Begin Experiment' code from ssst_staircase
# setting parameters for staircase
ssd = 0.15 # starts at 150ms
stepsize = 0.05 # steps of 50ms
minval = 0.05 # minimum value of 50ms for SSD
maxval = 1.05 # maxSSD is 1050ms



ssst_go = visual.ImageStim(
    win=win,
    name='ssst_go', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
ssst_stop = visual.ImageStim(
    win=win,
    name='ssst_stop', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
ssst_resp = keyboard.Keyboard()

# --- Initialize components for Routine "tom_dual_2" ---
tom_d_2 = visual.ImageStim(
    win=win,
    name='tom_d_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "ssst_iti" ---
ssst_iti_cross = visual.TextStim(win=win, name='ssst_iti_cross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "stop_sig" ---
# Run 'Begin Experiment' code from ssst_staircase
# setting parameters for staircase
ssd = 0.15 # starts at 150ms
stepsize = 0.05 # steps of 50ms
minval = 0.05 # minimum value of 50ms for SSD
maxval = 1.05 # maxSSD is 1050ms



ssst_go = visual.ImageStim(
    win=win,
    name='ssst_go', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
ssst_stop = visual.ImageStim(
    win=win,
    name='ssst_stop', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
ssst_resp = keyboard.Keyboard()

# --- Initialize components for Routine "tom_dual_3" ---
tom_d_3 = visual.ImageStim(
    win=win,
    name='tom_d_3', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "tom_dual_dec" ---
tom_choice = visual.ImageStim(
    win=win,
    name='tom_choice', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
tom_d_resp = keyboard.Keyboard()

# --- Initialize components for Routine "outro" ---
outro_text = visual.TextStim(win=win, name='outro_text',
    text='Contrats on completing the first portion of the study! \n\nAfter leaving the next page you will be asked to press ok with your mouse which will immediately take you to the next portion of the study.\n\nRemember the last 5 digits of your phone number and the email you registered with so that you can enter the next part of the study. ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
outro_text2 = visual.TextStim(win=win, name='outro_text2',
    text='Again you will need the last 5 digits of your phone number and the email you registered with so to enter the next part of the study. \n\nPress SPACEBAR to go to end this part the study and wait until a box appears that asks you to click ok with your mouse. ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
outro_resp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "welcome" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
welcome_adv.keys = []
welcome_adv.rt = []
_welcome_adv_allKeys = []
# keep track of which components have finished
welcomeComponents = [text, welcome_adv]
for thisComponent in welcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "welcome" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text.started')
        text.setAutoDraw(True)
    
    # *welcome_adv* updates
    waitOnFlip = False
    if welcome_adv.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        welcome_adv.frameNStart = frameN  # exact frame index
        welcome_adv.tStart = t  # local t and not account for scr refresh
        welcome_adv.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_adv, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'welcome_adv.started')
        welcome_adv.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(welcome_adv.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(welcome_adv.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if welcome_adv.status == STARTED and not waitOnFlip:
        theseKeys = welcome_adv.getKeys(keyList=['space'], waitRelease=False)
        _welcome_adv_allKeys.extend(theseKeys)
        if len(_welcome_adv_allKeys):
            welcome_adv.keys = _welcome_adv_allKeys[-1].name  # just the last key pressed
            welcome_adv.rt = _welcome_adv_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "welcome" ---
for thisComponent in welcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if welcome_adv.keys in ['', [], None]:  # No response was made
    welcome_adv.keys = None
thisExp.addData('welcome_adv.keys',welcome_adv.keys)
if welcome_adv.keys != None:  # we had a response
    thisExp.addData('welcome_adv.rt', welcome_adv.rt)
thisExp.nextEntry()
# the Routine "welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "ssst_prac_inst" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
ssst_prac_instComponents = [ssst_inst1, ssst_inst2, ssst_inst3, ssst_inst5, ssst_inst6, key_resp]
for thisComponent in ssst_prac_instComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "ssst_prac_inst" ---
while continueRoutine and routineTimer.getTime() < 47.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ssst_inst1* updates
    if ssst_inst1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ssst_inst1.frameNStart = frameN  # exact frame index
        ssst_inst1.tStart = t  # local t and not account for scr refresh
        ssst_inst1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ssst_inst1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ssst_inst1.started')
        ssst_inst1.setAutoDraw(True)
    if ssst_inst1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > ssst_inst1.tStartRefresh + 9-frameTolerance:
            # keep track of stop time/frame for later
            ssst_inst1.tStop = t  # not accounting for scr refresh
            ssst_inst1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ssst_inst1.stopped')
            ssst_inst1.setAutoDraw(False)
    
    # *ssst_inst2* updates
    if ssst_inst2.status == NOT_STARTED and tThisFlip >= 9-frameTolerance:
        # keep track of start time/frame for later
        ssst_inst2.frameNStart = frameN  # exact frame index
        ssst_inst2.tStart = t  # local t and not account for scr refresh
        ssst_inst2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ssst_inst2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ssst_inst2.started')
        ssst_inst2.setAutoDraw(True)
    if ssst_inst2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > ssst_inst2.tStartRefresh + 7-frameTolerance:
            # keep track of stop time/frame for later
            ssst_inst2.tStop = t  # not accounting for scr refresh
            ssst_inst2.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ssst_inst2.stopped')
            ssst_inst2.setAutoDraw(False)
    
    # *ssst_inst3* updates
    if ssst_inst3.status == NOT_STARTED and tThisFlip >= 16-frameTolerance:
        # keep track of start time/frame for later
        ssst_inst3.frameNStart = frameN  # exact frame index
        ssst_inst3.tStart = t  # local t and not account for scr refresh
        ssst_inst3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ssst_inst3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ssst_inst3.started')
        ssst_inst3.setAutoDraw(True)
    if ssst_inst3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > ssst_inst3.tStartRefresh + 7-frameTolerance:
            # keep track of stop time/frame for later
            ssst_inst3.tStop = t  # not accounting for scr refresh
            ssst_inst3.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ssst_inst3.stopped')
            ssst_inst3.setAutoDraw(False)
    
    # *ssst_inst5* updates
    if ssst_inst5.status == NOT_STARTED and tThisFlip >= 23-frameTolerance:
        # keep track of start time/frame for later
        ssst_inst5.frameNStart = frameN  # exact frame index
        ssst_inst5.tStart = t  # local t and not account for scr refresh
        ssst_inst5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ssst_inst5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ssst_inst5.started')
        ssst_inst5.setAutoDraw(True)
    if ssst_inst5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > ssst_inst5.tStartRefresh + 14-frameTolerance:
            # keep track of stop time/frame for later
            ssst_inst5.tStop = t  # not accounting for scr refresh
            ssst_inst5.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ssst_inst5.stopped')
            ssst_inst5.setAutoDraw(False)
    
    # *ssst_inst6* updates
    if ssst_inst6.status == NOT_STARTED and tThisFlip >= 37-frameTolerance:
        # keep track of start time/frame for later
        ssst_inst6.frameNStart = frameN  # exact frame index
        ssst_inst6.tStart = t  # local t and not account for scr refresh
        ssst_inst6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ssst_inst6, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ssst_inst6.started')
        ssst_inst6.setAutoDraw(True)
    if ssst_inst6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > ssst_inst6.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            ssst_inst6.tStop = t  # not accounting for scr refresh
            ssst_inst6.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ssst_inst6.stopped')
            ssst_inst6.setAutoDraw(False)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 37-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp.started')
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            key_resp.tStop = t  # not accounting for scr refresh
            key_resp.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp.stopped')
            key_resp.status = FINISHED
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ssst_prac_instComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "ssst_prac_inst" ---
for thisComponent in ssst_prac_instComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.nextEntry()
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-47.000000)

# set up handler to look after randomisation of conditions etc
prac_ssst = data.TrialHandler(nReps=3.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions/ssst_go_stop.xlsx'),
    seed=None, name='prac_ssst')
thisExp.addLoop(prac_ssst)  # add the loop to the experiment
thisPrac_ssst = prac_ssst.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPrac_ssst.rgb)
if thisPrac_ssst != None:
    for paramName in thisPrac_ssst:
        exec('{} = thisPrac_ssst[paramName]'.format(paramName))

for thisPrac_ssst in prac_ssst:
    currentLoop = prac_ssst
    # abbreviate parameter names if possible (e.g. rgb = thisPrac_ssst.rgb)
    if thisPrac_ssst != None:
        for paramName in thisPrac_ssst:
            exec('{} = thisPrac_ssst[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "prac_ssst_trial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    prac_ssst_go.setImage(go_img)
    prac_ssst_stop.setImage(st_img)
    prac_ssst_resp.keys = []
    prac_ssst_resp.rt = []
    _prac_ssst_resp_allKeys = []
    # keep track of which components have finished
    prac_ssst_trialComponents = [prac_ssst_go, prac_ssst_stop, prac_ssst_resp]
    for thisComponent in prac_ssst_trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "prac_ssst_trial" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *prac_ssst_go* updates
        if prac_ssst_go.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            prac_ssst_go.frameNStart = frameN  # exact frame index
            prac_ssst_go.tStart = t  # local t and not account for scr refresh
            prac_ssst_go.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_ssst_go, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'prac_ssst_go.started')
            prac_ssst_go.setAutoDraw(True)
        if prac_ssst_go.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > prac_ssst_go.tStartRefresh + ssd-frameTolerance:
                # keep track of stop time/frame for later
                prac_ssst_go.tStop = t  # not accounting for scr refresh
                prac_ssst_go.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'prac_ssst_go.stopped')
                prac_ssst_go.setAutoDraw(False)
        
        # *prac_ssst_stop* updates
        if prac_ssst_stop.status == NOT_STARTED and tThisFlip >= ssd - 0.00001-frameTolerance:
            # keep track of start time/frame for later
            prac_ssst_stop.frameNStart = frameN  # exact frame index
            prac_ssst_stop.tStart = t  # local t and not account for scr refresh
            prac_ssst_stop.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_ssst_stop, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'prac_ssst_stop.started')
            prac_ssst_stop.setAutoDraw(True)
        if prac_ssst_stop.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > prac_ssst_stop.tStartRefresh + 1.25 - ssd-frameTolerance:
                # keep track of stop time/frame for later
                prac_ssst_stop.tStop = t  # not accounting for scr refresh
                prac_ssst_stop.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'prac_ssst_stop.stopped')
                prac_ssst_stop.setAutoDraw(False)
        
        # *prac_ssst_resp* updates
        waitOnFlip = False
        if prac_ssst_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prac_ssst_resp.frameNStart = frameN  # exact frame index
            prac_ssst_resp.tStart = t  # local t and not account for scr refresh
            prac_ssst_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_ssst_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'prac_ssst_resp.started')
            prac_ssst_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(prac_ssst_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(prac_ssst_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if prac_ssst_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > prac_ssst_resp.tStartRefresh + 1.25-frameTolerance:
                # keep track of stop time/frame for later
                prac_ssst_resp.tStop = t  # not accounting for scr refresh
                prac_ssst_resp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'prac_ssst_resp.stopped')
                prac_ssst_resp.status = FINISHED
        if prac_ssst_resp.status == STARTED and not waitOnFlip:
            theseKeys = prac_ssst_resp.getKeys(keyList=['k','space','None'], waitRelease=False)
            _prac_ssst_resp_allKeys.extend(theseKeys)
            if len(_prac_ssst_resp_allKeys):
                prac_ssst_resp.keys = _prac_ssst_resp_allKeys[-1].name  # just the last key pressed
                prac_ssst_resp.rt = _prac_ssst_resp_allKeys[-1].rt
                # was this correct?
                if (prac_ssst_resp.keys == str(corr_resp)) or (prac_ssst_resp.keys == corr_resp):
                    prac_ssst_resp.corr = 1
                else:
                    prac_ssst_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prac_ssst_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "prac_ssst_trial" ---
    for thisComponent in prac_ssst_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from prac_ssst_staircase
    thisExp.addData('trial_type', trial_type)
    thisExp.addData('ssd_prac', ssd_prac)
    thisExp.addData('prac_ssst_resp', prac_ssst_resp.keys)
    
    if trial_type == 'stop': # only adjust on stop trials
        #adjust the stepsize
        if prac_ssst_resp.corr == 1:
            ssd_prac += stepsize
        else:
            ssd_prac -= stepsize
    
        # cap the stop time
        if ssd_prac < minval:
            ssd_prac = minval
        if ssd_prac > maxval:
            ssd_prac = maxval
    
    # check responses
    if prac_ssst_resp.keys in ['', [], None]:  # No response was made
        prac_ssst_resp.keys = None
        # was no response the correct answer?!
        if str(corr_resp).lower() == 'none':
           prac_ssst_resp.corr = 1;  # correct non-response
        else:
           prac_ssst_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for prac_ssst (TrialHandler)
    prac_ssst.addData('prac_ssst_resp.keys',prac_ssst_resp.keys)
    prac_ssst.addData('prac_ssst_resp.corr', prac_ssst_resp.corr)
    if prac_ssst_resp.keys != None:  # we had a response
        prac_ssst.addData('prac_ssst_resp.rt', prac_ssst_resp.rt)
    # the Routine "prac_ssst_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "prac_ssst_iti" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from prac_ssst_iti_draw
    
    if prac_ssst_resp.corr :#stored on last run routine
        msg="Correct!"
        color = "green"
    else:
        msg="Oops! That was wrong - space for arrow, K for red square"
        color = "red"
    
    
    prac_ssst_iti_cross.setColor(color, colorSpace='rgb')
    prac_ssst_iti_cross.setText(msg)
    # keep track of which components have finished
    prac_ssst_itiComponents = [prac_ssst_iti_cross]
    for thisComponent in prac_ssst_itiComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "prac_ssst_iti" ---
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *prac_ssst_iti_cross* updates
        if prac_ssst_iti_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prac_ssst_iti_cross.frameNStart = frameN  # exact frame index
            prac_ssst_iti_cross.tStart = t  # local t and not account for scr refresh
            prac_ssst_iti_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_ssst_iti_cross, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'prac_ssst_iti_cross.started')
            prac_ssst_iti_cross.setAutoDraw(True)
        if prac_ssst_iti_cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > prac_ssst_iti_cross.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                prac_ssst_iti_cross.tStop = t  # not accounting for scr refresh
                prac_ssst_iti_cross.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'prac_ssst_iti_cross.stopped')
                prac_ssst_iti_cross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prac_ssst_itiComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "prac_ssst_iti" ---
    for thisComponent in prac_ssst_itiComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    thisExp.nextEntry()
    
# completed 3.0 repeats of 'prac_ssst'


# --- Prepare to start Routine "prac_tom_inst" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
tom_inst_resp.keys = []
tom_inst_resp.rt = []
_tom_inst_resp_allKeys = []
# keep track of which components have finished
prac_tom_instComponents = [tom_inst1, tom_inst1_2, tom_inst1_3, tom_inst2, tom_inst3, tom_inst4, tom_inst5, tom_inst_resp]
for thisComponent in prac_tom_instComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "prac_tom_inst" ---
while continueRoutine and routineTimer.getTime() < 55.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *tom_inst1* updates
    if tom_inst1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        tom_inst1.frameNStart = frameN  # exact frame index
        tom_inst1.tStart = t  # local t and not account for scr refresh
        tom_inst1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(tom_inst1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'tom_inst1.started')
        tom_inst1.setAutoDraw(True)
    if tom_inst1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > tom_inst1.tStartRefresh + 7-frameTolerance:
            # keep track of stop time/frame for later
            tom_inst1.tStop = t  # not accounting for scr refresh
            tom_inst1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'tom_inst1.stopped')
            tom_inst1.setAutoDraw(False)
    
    # *tom_inst1_2* updates
    if tom_inst1_2.status == NOT_STARTED and tThisFlip >= 7-frameTolerance:
        # keep track of start time/frame for later
        tom_inst1_2.frameNStart = frameN  # exact frame index
        tom_inst1_2.tStart = t  # local t and not account for scr refresh
        tom_inst1_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(tom_inst1_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'tom_inst1_2.started')
        tom_inst1_2.setAutoDraw(True)
    if tom_inst1_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > tom_inst1_2.tStartRefresh + 7-frameTolerance:
            # keep track of stop time/frame for later
            tom_inst1_2.tStop = t  # not accounting for scr refresh
            tom_inst1_2.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'tom_inst1_2.stopped')
            tom_inst1_2.setAutoDraw(False)
    
    # *tom_inst1_3* updates
    if tom_inst1_3.status == NOT_STARTED and tThisFlip >= 14-frameTolerance:
        # keep track of start time/frame for later
        tom_inst1_3.frameNStart = frameN  # exact frame index
        tom_inst1_3.tStart = t  # local t and not account for scr refresh
        tom_inst1_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(tom_inst1_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'tom_inst1_3.started')
        tom_inst1_3.setAutoDraw(True)
    if tom_inst1_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > tom_inst1_3.tStartRefresh + 7-frameTolerance:
            # keep track of stop time/frame for later
            tom_inst1_3.tStop = t  # not accounting for scr refresh
            tom_inst1_3.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'tom_inst1_3.stopped')
            tom_inst1_3.setAutoDraw(False)
    
    # *tom_inst2* updates
    if tom_inst2.status == NOT_STARTED and tThisFlip >= 21-frameTolerance:
        # keep track of start time/frame for later
        tom_inst2.frameNStart = frameN  # exact frame index
        tom_inst2.tStart = t  # local t and not account for scr refresh
        tom_inst2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(tom_inst2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'tom_inst2.started')
        tom_inst2.setAutoDraw(True)
    if tom_inst2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > tom_inst2.tStartRefresh + 7-frameTolerance:
            # keep track of stop time/frame for later
            tom_inst2.tStop = t  # not accounting for scr refresh
            tom_inst2.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'tom_inst2.stopped')
            tom_inst2.setAutoDraw(False)
    
    # *tom_inst3* updates
    if tom_inst3.status == NOT_STARTED and tThisFlip >= 28-frameTolerance:
        # keep track of start time/frame for later
        tom_inst3.frameNStart = frameN  # exact frame index
        tom_inst3.tStart = t  # local t and not account for scr refresh
        tom_inst3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(tom_inst3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'tom_inst3.started')
        tom_inst3.setAutoDraw(True)
    if tom_inst3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > tom_inst3.tStartRefresh + 7-frameTolerance:
            # keep track of stop time/frame for later
            tom_inst3.tStop = t  # not accounting for scr refresh
            tom_inst3.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'tom_inst3.stopped')
            tom_inst3.setAutoDraw(False)
    
    # *tom_inst4* updates
    if tom_inst4.status == NOT_STARTED and tThisFlip >= 35-frameTolerance:
        # keep track of start time/frame for later
        tom_inst4.frameNStart = frameN  # exact frame index
        tom_inst4.tStart = t  # local t and not account for scr refresh
        tom_inst4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(tom_inst4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'tom_inst4.started')
        tom_inst4.setAutoDraw(True)
    if tom_inst4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > tom_inst4.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            tom_inst4.tStop = t  # not accounting for scr refresh
            tom_inst4.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'tom_inst4.stopped')
            tom_inst4.setAutoDraw(False)
    
    # *tom_inst5* updates
    if tom_inst5.status == NOT_STARTED and tThisFlip >= 45-frameTolerance:
        # keep track of start time/frame for later
        tom_inst5.frameNStart = frameN  # exact frame index
        tom_inst5.tStart = t  # local t and not account for scr refresh
        tom_inst5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(tom_inst5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'tom_inst5.started')
        tom_inst5.setAutoDraw(True)
    if tom_inst5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > tom_inst5.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            tom_inst5.tStop = t  # not accounting for scr refresh
            tom_inst5.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'tom_inst5.stopped')
            tom_inst5.setAutoDraw(False)
    
    # *tom_inst_resp* updates
    waitOnFlip = False
    if tom_inst_resp.status == NOT_STARTED and tThisFlip >= 45-frameTolerance:
        # keep track of start time/frame for later
        tom_inst_resp.frameNStart = frameN  # exact frame index
        tom_inst_resp.tStart = t  # local t and not account for scr refresh
        tom_inst_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(tom_inst_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'tom_inst_resp.started')
        tom_inst_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(tom_inst_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(tom_inst_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if tom_inst_resp.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > tom_inst_resp.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            tom_inst_resp.tStop = t  # not accounting for scr refresh
            tom_inst_resp.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'tom_inst_resp.stopped')
            tom_inst_resp.status = FINISHED
    if tom_inst_resp.status == STARTED and not waitOnFlip:
        theseKeys = tom_inst_resp.getKeys(keyList=['space'], waitRelease=False)
        _tom_inst_resp_allKeys.extend(theseKeys)
        if len(_tom_inst_resp_allKeys):
            tom_inst_resp.keys = _tom_inst_resp_allKeys[-1].name  # just the last key pressed
            tom_inst_resp.rt = _tom_inst_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in prac_tom_instComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "prac_tom_inst" ---
for thisComponent in prac_tom_instComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if tom_inst_resp.keys in ['', [], None]:  # No response was made
    tom_inst_resp.keys = None
thisExp.addData('tom_inst_resp.keys',tom_inst_resp.keys)
if tom_inst_resp.keys != None:  # we had a response
    thisExp.addData('tom_inst_resp.rt', tom_inst_resp.rt)
thisExp.nextEntry()
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-55.000000)

# set up handler to look after randomisation of conditions etc
prac_tom = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions/prac_tom_cond.xlsx'),
    seed=None, name='prac_tom')
thisExp.addLoop(prac_tom)  # add the loop to the experiment
thisPrac_tom = prac_tom.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPrac_tom.rgb)
if thisPrac_tom != None:
    for paramName in thisPrac_tom:
        exec('{} = thisPrac_tom[paramName]'.format(paramName))

for thisPrac_tom in prac_tom:
    currentLoop = prac_tom
    # abbreviate parameter names if possible (e.g. rgb = thisPrac_tom.rgb)
    if thisPrac_tom != None:
        for paramName in thisPrac_tom:
            exec('{} = thisPrac_tom[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "prac_tom_trial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    prac_tom1.setImage(prac_img1)
    prac_tom2.setImage(prac_img2)
    prac_tom3.setImage(prac_img3)
    prac_tom_dec.setImage(prac_dec_img)
    prac_tom_resp.keys = []
    prac_tom_resp.rt = []
    _prac_tom_resp_allKeys = []
    # keep track of which components have finished
    prac_tom_trialComponents = [prac_tom1, prac_tom2, prac_tom3, prac_tom_dec, prac_tom_resp]
    for thisComponent in prac_tom_trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "prac_tom_trial" ---
    while continueRoutine and routineTimer.getTime() < 11.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *prac_tom1* updates
        if prac_tom1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            prac_tom1.frameNStart = frameN  # exact frame index
            prac_tom1.tStart = t  # local t and not account for scr refresh
            prac_tom1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_tom1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'prac_tom1.started')
            prac_tom1.setAutoDraw(True)
        if prac_tom1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > prac_tom1.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                prac_tom1.tStop = t  # not accounting for scr refresh
                prac_tom1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'prac_tom1.stopped')
                prac_tom1.setAutoDraw(False)
        
        # *prac_tom2* updates
        if prac_tom2.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            prac_tom2.frameNStart = frameN  # exact frame index
            prac_tom2.tStart = t  # local t and not account for scr refresh
            prac_tom2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_tom2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'prac_tom2.started')
            prac_tom2.setAutoDraw(True)
        if prac_tom2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > prac_tom2.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                prac_tom2.tStop = t  # not accounting for scr refresh
                prac_tom2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'prac_tom2.stopped')
                prac_tom2.setAutoDraw(False)
        
        # *prac_tom3* updates
        if prac_tom3.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            prac_tom3.frameNStart = frameN  # exact frame index
            prac_tom3.tStart = t  # local t and not account for scr refresh
            prac_tom3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_tom3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'prac_tom3.started')
            prac_tom3.setAutoDraw(True)
        if prac_tom3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > prac_tom3.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                prac_tom3.tStop = t  # not accounting for scr refresh
                prac_tom3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'prac_tom3.stopped')
                prac_tom3.setAutoDraw(False)
        
        # *prac_tom_dec* updates
        if prac_tom_dec.status == NOT_STARTED and tThisFlip >= 4.5-frameTolerance:
            # keep track of start time/frame for later
            prac_tom_dec.frameNStart = frameN  # exact frame index
            prac_tom_dec.tStart = t  # local t and not account for scr refresh
            prac_tom_dec.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_tom_dec, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'prac_tom_dec.started')
            prac_tom_dec.setAutoDraw(True)
        if prac_tom_dec.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > prac_tom_dec.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                prac_tom_dec.tStop = t  # not accounting for scr refresh
                prac_tom_dec.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'prac_tom_dec.stopped')
                prac_tom_dec.setAutoDraw(False)
        
        # *prac_tom_resp* updates
        waitOnFlip = False
        if prac_tom_resp.status == NOT_STARTED and tThisFlip >= 4.5-frameTolerance:
            # keep track of start time/frame for later
            prac_tom_resp.frameNStart = frameN  # exact frame index
            prac_tom_resp.tStart = t  # local t and not account for scr refresh
            prac_tom_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_tom_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'prac_tom_resp.started')
            prac_tom_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(prac_tom_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(prac_tom_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if prac_tom_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > prac_tom_resp.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                prac_tom_resp.tStop = t  # not accounting for scr refresh
                prac_tom_resp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'prac_tom_resp.stopped')
                prac_tom_resp.status = FINISHED
        if prac_tom_resp.status == STARTED and not waitOnFlip:
            theseKeys = prac_tom_resp.getKeys(keyList=['1','2','3'], waitRelease=False)
            _prac_tom_resp_allKeys.extend(theseKeys)
            if len(_prac_tom_resp_allKeys):
                prac_tom_resp.keys = _prac_tom_resp_allKeys[-1].name  # just the last key pressed
                prac_tom_resp.rt = _prac_tom_resp_allKeys[-1].rt
                # was this correct?
                if (prac_tom_resp.keys == str(corr_resp_tom_prac)) or (prac_tom_resp.keys == corr_resp_tom_prac):
                    prac_tom_resp.corr = 1
                else:
                    prac_tom_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prac_tom_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "prac_tom_trial" ---
    for thisComponent in prac_tom_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if prac_tom_resp.keys in ['', [], None]:  # No response was made
        prac_tom_resp.keys = None
        # was no response the correct answer?!
        if str(corr_resp_tom_prac).lower() == 'none':
           prac_tom_resp.corr = 1;  # correct non-response
        else:
           prac_tom_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for prac_tom (TrialHandler)
    prac_tom.addData('prac_tom_resp.keys',prac_tom_resp.keys)
    prac_tom.addData('prac_tom_resp.corr', prac_tom_resp.corr)
    if prac_tom_resp.keys != None:  # we had a response
        prac_tom.addData('prac_tom_resp.rt', prac_tom_resp.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-11.500000)
    
    # --- Prepare to start Routine "prac_tom_iti" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from prac_tom_code
    
    if not prac_tom_resp.keys :
        msg="Failed to respond"
        color = "red"
    else:
        msg="Your reaction time was %.3f" %(round(prac_tom_resp.rt,3))
        color = "white"
    
    prac_tom_fb.setColor(color, colorSpace='rgb')
    prac_tom_fb.setText(msg)
    # keep track of which components have finished
    prac_tom_itiComponents = [prac_tom_fb]
    for thisComponent in prac_tom_itiComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "prac_tom_iti" ---
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *prac_tom_fb* updates
        if prac_tom_fb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prac_tom_fb.frameNStart = frameN  # exact frame index
            prac_tom_fb.tStart = t  # local t and not account for scr refresh
            prac_tom_fb.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_tom_fb, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'prac_tom_fb.started')
            prac_tom_fb.setAutoDraw(True)
        if prac_tom_fb.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > prac_tom_fb.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                prac_tom_fb.tStop = t  # not accounting for scr refresh
                prac_tom_fb.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'prac_tom_fb.stopped')
                prac_tom_fb.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prac_tom_itiComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "prac_tom_iti" ---
    for thisComponent in prac_tom_itiComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'prac_tom'


# --- Prepare to start Routine "prac_dual_inst" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
dual_inst_resp.keys = []
dual_inst_resp.rt = []
_dual_inst_resp_allKeys = []
# keep track of which components have finished
prac_dual_instComponents = [dual_inst1, dual_inst2, dual_inst3, dual_inst4, dial_inst5, dual_inst_resp]
for thisComponent in prac_dual_instComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "prac_dual_inst" ---
while continueRoutine and routineTimer.getTime() < 39.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *dual_inst1* updates
    if dual_inst1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        dual_inst1.frameNStart = frameN  # exact frame index
        dual_inst1.tStart = t  # local t and not account for scr refresh
        dual_inst1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(dual_inst1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'dual_inst1.started')
        dual_inst1.setAutoDraw(True)
    if dual_inst1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > dual_inst1.tStartRefresh + 7-frameTolerance:
            # keep track of stop time/frame for later
            dual_inst1.tStop = t  # not accounting for scr refresh
            dual_inst1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'dual_inst1.stopped')
            dual_inst1.setAutoDraw(False)
    
    # *dual_inst2* updates
    if dual_inst2.status == NOT_STARTED and tThisFlip >= 7-frameTolerance:
        # keep track of start time/frame for later
        dual_inst2.frameNStart = frameN  # exact frame index
        dual_inst2.tStart = t  # local t and not account for scr refresh
        dual_inst2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(dual_inst2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'dual_inst2.started')
        dual_inst2.setAutoDraw(True)
    if dual_inst2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > dual_inst2.tStartRefresh + 7-frameTolerance:
            # keep track of stop time/frame for later
            dual_inst2.tStop = t  # not accounting for scr refresh
            dual_inst2.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'dual_inst2.stopped')
            dual_inst2.setAutoDraw(False)
    
    # *dual_inst3* updates
    if dual_inst3.status == NOT_STARTED and tThisFlip >= 14-frameTolerance:
        # keep track of start time/frame for later
        dual_inst3.frameNStart = frameN  # exact frame index
        dual_inst3.tStart = t  # local t and not account for scr refresh
        dual_inst3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(dual_inst3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'dual_inst3.started')
        dual_inst3.setAutoDraw(True)
    if dual_inst3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > dual_inst3.tStartRefresh + 7-frameTolerance:
            # keep track of stop time/frame for later
            dual_inst3.tStop = t  # not accounting for scr refresh
            dual_inst3.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'dual_inst3.stopped')
            dual_inst3.setAutoDraw(False)
    
    # *dual_inst4* updates
    if dual_inst4.status == NOT_STARTED and tThisFlip >= 21-frameTolerance:
        # keep track of start time/frame for later
        dual_inst4.frameNStart = frameN  # exact frame index
        dual_inst4.tStart = t  # local t and not account for scr refresh
        dual_inst4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(dual_inst4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'dual_inst4.started')
        dual_inst4.setAutoDraw(True)
    if dual_inst4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > dual_inst4.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            dual_inst4.tStop = t  # not accounting for scr refresh
            dual_inst4.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'dual_inst4.stopped')
            dual_inst4.setAutoDraw(False)
    
    # *dial_inst5* updates
    if dial_inst5.status == NOT_STARTED and tThisFlip >= 31-frameTolerance:
        # keep track of start time/frame for later
        dial_inst5.frameNStart = frameN  # exact frame index
        dial_inst5.tStart = t  # local t and not account for scr refresh
        dial_inst5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(dial_inst5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'dial_inst5.started')
        dial_inst5.setAutoDraw(True)
    if dial_inst5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > dial_inst5.tStartRefresh + 8-frameTolerance:
            # keep track of stop time/frame for later
            dial_inst5.tStop = t  # not accounting for scr refresh
            dial_inst5.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'dial_inst5.stopped')
            dial_inst5.setAutoDraw(False)
    
    # *dual_inst_resp* updates
    waitOnFlip = False
    if dual_inst_resp.status == NOT_STARTED and tThisFlip >= 31-frameTolerance:
        # keep track of start time/frame for later
        dual_inst_resp.frameNStart = frameN  # exact frame index
        dual_inst_resp.tStart = t  # local t and not account for scr refresh
        dual_inst_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(dual_inst_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'dual_inst_resp.started')
        dual_inst_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(dual_inst_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(dual_inst_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if dual_inst_resp.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > dual_inst_resp.tStartRefresh + 8-frameTolerance:
            # keep track of stop time/frame for later
            dual_inst_resp.tStop = t  # not accounting for scr refresh
            dual_inst_resp.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'dual_inst_resp.stopped')
            dual_inst_resp.status = FINISHED
    if dual_inst_resp.status == STARTED and not waitOnFlip:
        theseKeys = dual_inst_resp.getKeys(keyList=['space'], waitRelease=False)
        _dual_inst_resp_allKeys.extend(theseKeys)
        if len(_dual_inst_resp_allKeys):
            dual_inst_resp.keys = _dual_inst_resp_allKeys[-1].name  # just the last key pressed
            dual_inst_resp.rt = _dual_inst_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in prac_dual_instComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "prac_dual_inst" ---
for thisComponent in prac_dual_instComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if dual_inst_resp.keys in ['', [], None]:  # No response was made
    dual_inst_resp.keys = None
thisExp.addData('dual_inst_resp.keys',dual_inst_resp.keys)
if dual_inst_resp.keys != None:  # we had a response
    thisExp.addData('dual_inst_resp.rt', dual_inst_resp.rt)
thisExp.nextEntry()
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-39.000000)

# set up handler to look after randomisation of conditions etc
prac_dual = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions/prac_dual_tom_cond.xlsx'),
    seed=None, name='prac_dual')
thisExp.addLoop(prac_dual)  # add the loop to the experiment
thisPrac_dual = prac_dual.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPrac_dual.rgb)
if thisPrac_dual != None:
    for paramName in thisPrac_dual:
        exec('{} = thisPrac_dual[paramName]'.format(paramName))

for thisPrac_dual in prac_dual:
    currentLoop = prac_dual
    # abbreviate parameter names if possible (e.g. rgb = thisPrac_dual.rgb)
    if thisPrac_dual != None:
        for paramName in thisPrac_dual:
            exec('{} = thisPrac_dual[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    prac_dual_ssst1 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('conditions/ssst_go_stop.xlsx'),
        seed=None, name='prac_dual_ssst1')
    thisExp.addLoop(prac_dual_ssst1)  # add the loop to the experiment
    thisPrac_dual_ssst1 = prac_dual_ssst1.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPrac_dual_ssst1.rgb)
    if thisPrac_dual_ssst1 != None:
        for paramName in thisPrac_dual_ssst1:
            exec('{} = thisPrac_dual_ssst1[paramName]'.format(paramName))
    
    for thisPrac_dual_ssst1 in prac_dual_ssst1:
        currentLoop = prac_dual_ssst1
        # abbreviate parameter names if possible (e.g. rgb = thisPrac_dual_ssst1.rgb)
        if thisPrac_dual_ssst1 != None:
            for paramName in thisPrac_dual_ssst1:
                exec('{} = thisPrac_dual_ssst1[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "prac_ssst_trial" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        prac_ssst_go.setImage(go_img)
        prac_ssst_stop.setImage(st_img)
        prac_ssst_resp.keys = []
        prac_ssst_resp.rt = []
        _prac_ssst_resp_allKeys = []
        # keep track of which components have finished
        prac_ssst_trialComponents = [prac_ssst_go, prac_ssst_stop, prac_ssst_resp]
        for thisComponent in prac_ssst_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "prac_ssst_trial" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *prac_ssst_go* updates
            if prac_ssst_go.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                prac_ssst_go.frameNStart = frameN  # exact frame index
                prac_ssst_go.tStart = t  # local t and not account for scr refresh
                prac_ssst_go.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(prac_ssst_go, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'prac_ssst_go.started')
                prac_ssst_go.setAutoDraw(True)
            if prac_ssst_go.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > prac_ssst_go.tStartRefresh + ssd-frameTolerance:
                    # keep track of stop time/frame for later
                    prac_ssst_go.tStop = t  # not accounting for scr refresh
                    prac_ssst_go.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'prac_ssst_go.stopped')
                    prac_ssst_go.setAutoDraw(False)
            
            # *prac_ssst_stop* updates
            if prac_ssst_stop.status == NOT_STARTED and tThisFlip >= ssd - 0.00001-frameTolerance:
                # keep track of start time/frame for later
                prac_ssst_stop.frameNStart = frameN  # exact frame index
                prac_ssst_stop.tStart = t  # local t and not account for scr refresh
                prac_ssst_stop.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(prac_ssst_stop, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'prac_ssst_stop.started')
                prac_ssst_stop.setAutoDraw(True)
            if prac_ssst_stop.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > prac_ssst_stop.tStartRefresh + 1.25 - ssd-frameTolerance:
                    # keep track of stop time/frame for later
                    prac_ssst_stop.tStop = t  # not accounting for scr refresh
                    prac_ssst_stop.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'prac_ssst_stop.stopped')
                    prac_ssst_stop.setAutoDraw(False)
            
            # *prac_ssst_resp* updates
            waitOnFlip = False
            if prac_ssst_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                prac_ssst_resp.frameNStart = frameN  # exact frame index
                prac_ssst_resp.tStart = t  # local t and not account for scr refresh
                prac_ssst_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(prac_ssst_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'prac_ssst_resp.started')
                prac_ssst_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(prac_ssst_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(prac_ssst_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if prac_ssst_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > prac_ssst_resp.tStartRefresh + 1.25-frameTolerance:
                    # keep track of stop time/frame for later
                    prac_ssst_resp.tStop = t  # not accounting for scr refresh
                    prac_ssst_resp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'prac_ssst_resp.stopped')
                    prac_ssst_resp.status = FINISHED
            if prac_ssst_resp.status == STARTED and not waitOnFlip:
                theseKeys = prac_ssst_resp.getKeys(keyList=['k','space','None'], waitRelease=False)
                _prac_ssst_resp_allKeys.extend(theseKeys)
                if len(_prac_ssst_resp_allKeys):
                    prac_ssst_resp.keys = _prac_ssst_resp_allKeys[-1].name  # just the last key pressed
                    prac_ssst_resp.rt = _prac_ssst_resp_allKeys[-1].rt
                    # was this correct?
                    if (prac_ssst_resp.keys == str(corr_resp)) or (prac_ssst_resp.keys == corr_resp):
                        prac_ssst_resp.corr = 1
                    else:
                        prac_ssst_resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in prac_ssst_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "prac_ssst_trial" ---
        for thisComponent in prac_ssst_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from prac_ssst_staircase
        thisExp.addData('trial_type', trial_type)
        thisExp.addData('ssd_prac', ssd_prac)
        thisExp.addData('prac_ssst_resp', prac_ssst_resp.keys)
        
        if trial_type == 'stop': # only adjust on stop trials
            #adjust the stepsize
            if prac_ssst_resp.corr == 1:
                ssd_prac += stepsize
            else:
                ssd_prac -= stepsize
        
            # cap the stop time
            if ssd_prac < minval:
                ssd_prac = minval
            if ssd_prac > maxval:
                ssd_prac = maxval
        
        # check responses
        if prac_ssst_resp.keys in ['', [], None]:  # No response was made
            prac_ssst_resp.keys = None
            # was no response the correct answer?!
            if str(corr_resp).lower() == 'none':
               prac_ssst_resp.corr = 1;  # correct non-response
            else:
               prac_ssst_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for prac_dual_ssst1 (TrialHandler)
        prac_dual_ssst1.addData('prac_ssst_resp.keys',prac_ssst_resp.keys)
        prac_dual_ssst1.addData('prac_ssst_resp.corr', prac_ssst_resp.corr)
        if prac_ssst_resp.keys != None:  # we had a response
            prac_dual_ssst1.addData('prac_ssst_resp.rt', prac_ssst_resp.rt)
        # the Routine "prac_ssst_trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "prac_ssst_iti" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from prac_ssst_iti_draw
        
        if prac_ssst_resp.corr :#stored on last run routine
            msg="Correct!"
            color = "green"
        else:
            msg="Oops! That was wrong - space for arrow, K for red square"
            color = "red"
        
        
        prac_ssst_iti_cross.setColor(color, colorSpace='rgb')
        prac_ssst_iti_cross.setText(msg)
        # keep track of which components have finished
        prac_ssst_itiComponents = [prac_ssst_iti_cross]
        for thisComponent in prac_ssst_itiComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "prac_ssst_iti" ---
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *prac_ssst_iti_cross* updates
            if prac_ssst_iti_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                prac_ssst_iti_cross.frameNStart = frameN  # exact frame index
                prac_ssst_iti_cross.tStart = t  # local t and not account for scr refresh
                prac_ssst_iti_cross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(prac_ssst_iti_cross, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'prac_ssst_iti_cross.started')
                prac_ssst_iti_cross.setAutoDraw(True)
            if prac_ssst_iti_cross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > prac_ssst_iti_cross.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    prac_ssst_iti_cross.tStop = t  # not accounting for scr refresh
                    prac_ssst_iti_cross.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'prac_ssst_iti_cross.stopped')
                    prac_ssst_iti_cross.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in prac_ssst_itiComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "prac_ssst_iti" ---
        for thisComponent in prac_ssst_itiComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'prac_dual_ssst1'
    
    
    # --- Prepare to start Routine "prac_dual_tom1" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    prac_d_tom1.setImage(prac_img1)
    # keep track of which components have finished
    prac_dual_tom1Components = [prac_d_tom1]
    for thisComponent in prac_dual_tom1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "prac_dual_tom1" ---
    while continueRoutine and routineTimer.getTime() < 1.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *prac_d_tom1* updates
        if prac_d_tom1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            prac_d_tom1.frameNStart = frameN  # exact frame index
            prac_d_tom1.tStart = t  # local t and not account for scr refresh
            prac_d_tom1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_d_tom1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'prac_d_tom1.started')
            prac_d_tom1.setAutoDraw(True)
        if prac_d_tom1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > prac_d_tom1.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                prac_d_tom1.tStop = t  # not accounting for scr refresh
                prac_d_tom1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'prac_d_tom1.stopped')
                prac_d_tom1.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prac_dual_tom1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "prac_dual_tom1" ---
    for thisComponent in prac_dual_tom1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.500000)
    
    # set up handler to look after randomisation of conditions etc
    prac_dual_ssst2 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('conditions/ssst_go_stop.xlsx'),
        seed=None, name='prac_dual_ssst2')
    thisExp.addLoop(prac_dual_ssst2)  # add the loop to the experiment
    thisPrac_dual_ssst2 = prac_dual_ssst2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPrac_dual_ssst2.rgb)
    if thisPrac_dual_ssst2 != None:
        for paramName in thisPrac_dual_ssst2:
            exec('{} = thisPrac_dual_ssst2[paramName]'.format(paramName))
    
    for thisPrac_dual_ssst2 in prac_dual_ssst2:
        currentLoop = prac_dual_ssst2
        # abbreviate parameter names if possible (e.g. rgb = thisPrac_dual_ssst2.rgb)
        if thisPrac_dual_ssst2 != None:
            for paramName in thisPrac_dual_ssst2:
                exec('{} = thisPrac_dual_ssst2[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "prac_ssst_trial" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        prac_ssst_go.setImage(go_img)
        prac_ssst_stop.setImage(st_img)
        prac_ssst_resp.keys = []
        prac_ssst_resp.rt = []
        _prac_ssst_resp_allKeys = []
        # keep track of which components have finished
        prac_ssst_trialComponents = [prac_ssst_go, prac_ssst_stop, prac_ssst_resp]
        for thisComponent in prac_ssst_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "prac_ssst_trial" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *prac_ssst_go* updates
            if prac_ssst_go.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                prac_ssst_go.frameNStart = frameN  # exact frame index
                prac_ssst_go.tStart = t  # local t and not account for scr refresh
                prac_ssst_go.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(prac_ssst_go, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'prac_ssst_go.started')
                prac_ssst_go.setAutoDraw(True)
            if prac_ssst_go.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > prac_ssst_go.tStartRefresh + ssd-frameTolerance:
                    # keep track of stop time/frame for later
                    prac_ssst_go.tStop = t  # not accounting for scr refresh
                    prac_ssst_go.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'prac_ssst_go.stopped')
                    prac_ssst_go.setAutoDraw(False)
            
            # *prac_ssst_stop* updates
            if prac_ssst_stop.status == NOT_STARTED and tThisFlip >= ssd - 0.00001-frameTolerance:
                # keep track of start time/frame for later
                prac_ssst_stop.frameNStart = frameN  # exact frame index
                prac_ssst_stop.tStart = t  # local t and not account for scr refresh
                prac_ssst_stop.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(prac_ssst_stop, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'prac_ssst_stop.started')
                prac_ssst_stop.setAutoDraw(True)
            if prac_ssst_stop.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > prac_ssst_stop.tStartRefresh + 1.25 - ssd-frameTolerance:
                    # keep track of stop time/frame for later
                    prac_ssst_stop.tStop = t  # not accounting for scr refresh
                    prac_ssst_stop.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'prac_ssst_stop.stopped')
                    prac_ssst_stop.setAutoDraw(False)
            
            # *prac_ssst_resp* updates
            waitOnFlip = False
            if prac_ssst_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                prac_ssst_resp.frameNStart = frameN  # exact frame index
                prac_ssst_resp.tStart = t  # local t and not account for scr refresh
                prac_ssst_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(prac_ssst_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'prac_ssst_resp.started')
                prac_ssst_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(prac_ssst_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(prac_ssst_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if prac_ssst_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > prac_ssst_resp.tStartRefresh + 1.25-frameTolerance:
                    # keep track of stop time/frame for later
                    prac_ssst_resp.tStop = t  # not accounting for scr refresh
                    prac_ssst_resp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'prac_ssst_resp.stopped')
                    prac_ssst_resp.status = FINISHED
            if prac_ssst_resp.status == STARTED and not waitOnFlip:
                theseKeys = prac_ssst_resp.getKeys(keyList=['k','space','None'], waitRelease=False)
                _prac_ssst_resp_allKeys.extend(theseKeys)
                if len(_prac_ssst_resp_allKeys):
                    prac_ssst_resp.keys = _prac_ssst_resp_allKeys[-1].name  # just the last key pressed
                    prac_ssst_resp.rt = _prac_ssst_resp_allKeys[-1].rt
                    # was this correct?
                    if (prac_ssst_resp.keys == str(corr_resp)) or (prac_ssst_resp.keys == corr_resp):
                        prac_ssst_resp.corr = 1
                    else:
                        prac_ssst_resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in prac_ssst_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "prac_ssst_trial" ---
        for thisComponent in prac_ssst_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from prac_ssst_staircase
        thisExp.addData('trial_type', trial_type)
        thisExp.addData('ssd_prac', ssd_prac)
        thisExp.addData('prac_ssst_resp', prac_ssst_resp.keys)
        
        if trial_type == 'stop': # only adjust on stop trials
            #adjust the stepsize
            if prac_ssst_resp.corr == 1:
                ssd_prac += stepsize
            else:
                ssd_prac -= stepsize
        
            # cap the stop time
            if ssd_prac < minval:
                ssd_prac = minval
            if ssd_prac > maxval:
                ssd_prac = maxval
        
        # check responses
        if prac_ssst_resp.keys in ['', [], None]:  # No response was made
            prac_ssst_resp.keys = None
            # was no response the correct answer?!
            if str(corr_resp).lower() == 'none':
               prac_ssst_resp.corr = 1;  # correct non-response
            else:
               prac_ssst_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for prac_dual_ssst2 (TrialHandler)
        prac_dual_ssst2.addData('prac_ssst_resp.keys',prac_ssst_resp.keys)
        prac_dual_ssst2.addData('prac_ssst_resp.corr', prac_ssst_resp.corr)
        if prac_ssst_resp.keys != None:  # we had a response
            prac_dual_ssst2.addData('prac_ssst_resp.rt', prac_ssst_resp.rt)
        # the Routine "prac_ssst_trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "prac_ssst_iti" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from prac_ssst_iti_draw
        
        if prac_ssst_resp.corr :#stored on last run routine
            msg="Correct!"
            color = "green"
        else:
            msg="Oops! That was wrong - space for arrow, K for red square"
            color = "red"
        
        
        prac_ssst_iti_cross.setColor(color, colorSpace='rgb')
        prac_ssst_iti_cross.setText(msg)
        # keep track of which components have finished
        prac_ssst_itiComponents = [prac_ssst_iti_cross]
        for thisComponent in prac_ssst_itiComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "prac_ssst_iti" ---
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *prac_ssst_iti_cross* updates
            if prac_ssst_iti_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                prac_ssst_iti_cross.frameNStart = frameN  # exact frame index
                prac_ssst_iti_cross.tStart = t  # local t and not account for scr refresh
                prac_ssst_iti_cross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(prac_ssst_iti_cross, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'prac_ssst_iti_cross.started')
                prac_ssst_iti_cross.setAutoDraw(True)
            if prac_ssst_iti_cross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > prac_ssst_iti_cross.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    prac_ssst_iti_cross.tStop = t  # not accounting for scr refresh
                    prac_ssst_iti_cross.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'prac_ssst_iti_cross.stopped')
                    prac_ssst_iti_cross.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in prac_ssst_itiComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "prac_ssst_iti" ---
        for thisComponent in prac_ssst_itiComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'prac_dual_ssst2'
    
    
    # --- Prepare to start Routine "prac_dual_tom2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    prac_d_tom2.setImage(prac_img2)
    # keep track of which components have finished
    prac_dual_tom2Components = [prac_d_tom2]
    for thisComponent in prac_dual_tom2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "prac_dual_tom2" ---
    while continueRoutine and routineTimer.getTime() < 1.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *prac_d_tom2* updates
        if prac_d_tom2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            prac_d_tom2.frameNStart = frameN  # exact frame index
            prac_d_tom2.tStart = t  # local t and not account for scr refresh
            prac_d_tom2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_d_tom2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'prac_d_tom2.started')
            prac_d_tom2.setAutoDraw(True)
        if prac_d_tom2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > prac_d_tom2.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                prac_d_tom2.tStop = t  # not accounting for scr refresh
                prac_d_tom2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'prac_d_tom2.stopped')
                prac_d_tom2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prac_dual_tom2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "prac_dual_tom2" ---
    for thisComponent in prac_dual_tom2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.500000)
    
    # set up handler to look after randomisation of conditions etc
    prac_dual_ssst3 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('conditions/ssst_go_stop.xlsx'),
        seed=None, name='prac_dual_ssst3')
    thisExp.addLoop(prac_dual_ssst3)  # add the loop to the experiment
    thisPrac_dual_ssst3 = prac_dual_ssst3.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPrac_dual_ssst3.rgb)
    if thisPrac_dual_ssst3 != None:
        for paramName in thisPrac_dual_ssst3:
            exec('{} = thisPrac_dual_ssst3[paramName]'.format(paramName))
    
    for thisPrac_dual_ssst3 in prac_dual_ssst3:
        currentLoop = prac_dual_ssst3
        # abbreviate parameter names if possible (e.g. rgb = thisPrac_dual_ssst3.rgb)
        if thisPrac_dual_ssst3 != None:
            for paramName in thisPrac_dual_ssst3:
                exec('{} = thisPrac_dual_ssst3[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "prac_ssst_trial" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        prac_ssst_go.setImage(go_img)
        prac_ssst_stop.setImage(st_img)
        prac_ssst_resp.keys = []
        prac_ssst_resp.rt = []
        _prac_ssst_resp_allKeys = []
        # keep track of which components have finished
        prac_ssst_trialComponents = [prac_ssst_go, prac_ssst_stop, prac_ssst_resp]
        for thisComponent in prac_ssst_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "prac_ssst_trial" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *prac_ssst_go* updates
            if prac_ssst_go.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                prac_ssst_go.frameNStart = frameN  # exact frame index
                prac_ssst_go.tStart = t  # local t and not account for scr refresh
                prac_ssst_go.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(prac_ssst_go, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'prac_ssst_go.started')
                prac_ssst_go.setAutoDraw(True)
            if prac_ssst_go.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > prac_ssst_go.tStartRefresh + ssd-frameTolerance:
                    # keep track of stop time/frame for later
                    prac_ssst_go.tStop = t  # not accounting for scr refresh
                    prac_ssst_go.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'prac_ssst_go.stopped')
                    prac_ssst_go.setAutoDraw(False)
            
            # *prac_ssst_stop* updates
            if prac_ssst_stop.status == NOT_STARTED and tThisFlip >= ssd - 0.00001-frameTolerance:
                # keep track of start time/frame for later
                prac_ssst_stop.frameNStart = frameN  # exact frame index
                prac_ssst_stop.tStart = t  # local t and not account for scr refresh
                prac_ssst_stop.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(prac_ssst_stop, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'prac_ssst_stop.started')
                prac_ssst_stop.setAutoDraw(True)
            if prac_ssst_stop.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > prac_ssst_stop.tStartRefresh + 1.25 - ssd-frameTolerance:
                    # keep track of stop time/frame for later
                    prac_ssst_stop.tStop = t  # not accounting for scr refresh
                    prac_ssst_stop.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'prac_ssst_stop.stopped')
                    prac_ssst_stop.setAutoDraw(False)
            
            # *prac_ssst_resp* updates
            waitOnFlip = False
            if prac_ssst_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                prac_ssst_resp.frameNStart = frameN  # exact frame index
                prac_ssst_resp.tStart = t  # local t and not account for scr refresh
                prac_ssst_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(prac_ssst_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'prac_ssst_resp.started')
                prac_ssst_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(prac_ssst_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(prac_ssst_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if prac_ssst_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > prac_ssst_resp.tStartRefresh + 1.25-frameTolerance:
                    # keep track of stop time/frame for later
                    prac_ssst_resp.tStop = t  # not accounting for scr refresh
                    prac_ssst_resp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'prac_ssst_resp.stopped')
                    prac_ssst_resp.status = FINISHED
            if prac_ssst_resp.status == STARTED and not waitOnFlip:
                theseKeys = prac_ssst_resp.getKeys(keyList=['k','space','None'], waitRelease=False)
                _prac_ssst_resp_allKeys.extend(theseKeys)
                if len(_prac_ssst_resp_allKeys):
                    prac_ssst_resp.keys = _prac_ssst_resp_allKeys[-1].name  # just the last key pressed
                    prac_ssst_resp.rt = _prac_ssst_resp_allKeys[-1].rt
                    # was this correct?
                    if (prac_ssst_resp.keys == str(corr_resp)) or (prac_ssst_resp.keys == corr_resp):
                        prac_ssst_resp.corr = 1
                    else:
                        prac_ssst_resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in prac_ssst_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "prac_ssst_trial" ---
        for thisComponent in prac_ssst_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from prac_ssst_staircase
        thisExp.addData('trial_type', trial_type)
        thisExp.addData('ssd_prac', ssd_prac)
        thisExp.addData('prac_ssst_resp', prac_ssst_resp.keys)
        
        if trial_type == 'stop': # only adjust on stop trials
            #adjust the stepsize
            if prac_ssst_resp.corr == 1:
                ssd_prac += stepsize
            else:
                ssd_prac -= stepsize
        
            # cap the stop time
            if ssd_prac < minval:
                ssd_prac = minval
            if ssd_prac > maxval:
                ssd_prac = maxval
        
        # check responses
        if prac_ssst_resp.keys in ['', [], None]:  # No response was made
            prac_ssst_resp.keys = None
            # was no response the correct answer?!
            if str(corr_resp).lower() == 'none':
               prac_ssst_resp.corr = 1;  # correct non-response
            else:
               prac_ssst_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for prac_dual_ssst3 (TrialHandler)
        prac_dual_ssst3.addData('prac_ssst_resp.keys',prac_ssst_resp.keys)
        prac_dual_ssst3.addData('prac_ssst_resp.corr', prac_ssst_resp.corr)
        if prac_ssst_resp.keys != None:  # we had a response
            prac_dual_ssst3.addData('prac_ssst_resp.rt', prac_ssst_resp.rt)
        # the Routine "prac_ssst_trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "prac_ssst_iti" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from prac_ssst_iti_draw
        
        if prac_ssst_resp.corr :#stored on last run routine
            msg="Correct!"
            color = "green"
        else:
            msg="Oops! That was wrong - space for arrow, K for red square"
            color = "red"
        
        
        prac_ssst_iti_cross.setColor(color, colorSpace='rgb')
        prac_ssst_iti_cross.setText(msg)
        # keep track of which components have finished
        prac_ssst_itiComponents = [prac_ssst_iti_cross]
        for thisComponent in prac_ssst_itiComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "prac_ssst_iti" ---
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *prac_ssst_iti_cross* updates
            if prac_ssst_iti_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                prac_ssst_iti_cross.frameNStart = frameN  # exact frame index
                prac_ssst_iti_cross.tStart = t  # local t and not account for scr refresh
                prac_ssst_iti_cross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(prac_ssst_iti_cross, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'prac_ssst_iti_cross.started')
                prac_ssst_iti_cross.setAutoDraw(True)
            if prac_ssst_iti_cross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > prac_ssst_iti_cross.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    prac_ssst_iti_cross.tStop = t  # not accounting for scr refresh
                    prac_ssst_iti_cross.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'prac_ssst_iti_cross.stopped')
                    prac_ssst_iti_cross.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in prac_ssst_itiComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "prac_ssst_iti" ---
        for thisComponent in prac_ssst_itiComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'prac_dual_ssst3'
    
    
    # --- Prepare to start Routine "prac_dual_tom3" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    prac_d_tom3.setImage(prac_img3)
    # keep track of which components have finished
    prac_dual_tom3Components = [prac_d_tom3]
    for thisComponent in prac_dual_tom3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "prac_dual_tom3" ---
    while continueRoutine and routineTimer.getTime() < 1.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *prac_d_tom3* updates
        if prac_d_tom3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            prac_d_tom3.frameNStart = frameN  # exact frame index
            prac_d_tom3.tStart = t  # local t and not account for scr refresh
            prac_d_tom3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_d_tom3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'prac_d_tom3.started')
            prac_d_tom3.setAutoDraw(True)
        if prac_d_tom3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > prac_d_tom3.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                prac_d_tom3.tStop = t  # not accounting for scr refresh
                prac_d_tom3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'prac_d_tom3.stopped')
                prac_d_tom3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prac_dual_tom3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "prac_dual_tom3" ---
    for thisComponent in prac_dual_tom3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.500000)
    
    # --- Prepare to start Routine "prac_dual_tom_dec" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    prac_d_tom_choice.setImage(prac_dec_img)
    prac_d_tom_resp.keys = []
    prac_d_tom_resp.rt = []
    _prac_d_tom_resp_allKeys = []
    # keep track of which components have finished
    prac_dual_tom_decComponents = [prac_d_tom_choice, prac_d_tom_resp]
    for thisComponent in prac_dual_tom_decComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "prac_dual_tom_dec" ---
    while continueRoutine and routineTimer.getTime() < 7.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *prac_d_tom_choice* updates
        if prac_d_tom_choice.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            prac_d_tom_choice.frameNStart = frameN  # exact frame index
            prac_d_tom_choice.tStart = t  # local t and not account for scr refresh
            prac_d_tom_choice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_d_tom_choice, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'prac_d_tom_choice.started')
            prac_d_tom_choice.setAutoDraw(True)
        if prac_d_tom_choice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > prac_d_tom_choice.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                prac_d_tom_choice.tStop = t  # not accounting for scr refresh
                prac_d_tom_choice.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'prac_d_tom_choice.stopped')
                prac_d_tom_choice.setAutoDraw(False)
        
        # *prac_d_tom_resp* updates
        waitOnFlip = False
        if prac_d_tom_resp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            prac_d_tom_resp.frameNStart = frameN  # exact frame index
            prac_d_tom_resp.tStart = t  # local t and not account for scr refresh
            prac_d_tom_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_d_tom_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'prac_d_tom_resp.started')
            prac_d_tom_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(prac_d_tom_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(prac_d_tom_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if prac_d_tom_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > prac_d_tom_resp.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                prac_d_tom_resp.tStop = t  # not accounting for scr refresh
                prac_d_tom_resp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'prac_d_tom_resp.stopped')
                prac_d_tom_resp.status = FINISHED
        if prac_d_tom_resp.status == STARTED and not waitOnFlip:
            theseKeys = prac_d_tom_resp.getKeys(keyList=['1','2','3'], waitRelease=False)
            _prac_d_tom_resp_allKeys.extend(theseKeys)
            if len(_prac_d_tom_resp_allKeys):
                prac_d_tom_resp.keys = _prac_d_tom_resp_allKeys[-1].name  # just the last key pressed
                prac_d_tom_resp.rt = _prac_d_tom_resp_allKeys[-1].rt
                # was this correct?
                if (prac_d_tom_resp.keys == str(corr_resp_dual_prac)) or (prac_d_tom_resp.keys == corr_resp_dual_prac):
                    prac_d_tom_resp.corr = 1
                else:
                    prac_d_tom_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prac_dual_tom_decComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "prac_dual_tom_dec" ---
    for thisComponent in prac_dual_tom_decComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if prac_d_tom_resp.keys in ['', [], None]:  # No response was made
        prac_d_tom_resp.keys = None
        # was no response the correct answer?!
        if str(corr_resp_dual_prac).lower() == 'none':
           prac_d_tom_resp.corr = 1;  # correct non-response
        else:
           prac_d_tom_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for prac_dual (TrialHandler)
    prac_dual.addData('prac_d_tom_resp.keys',prac_d_tom_resp.keys)
    prac_dual.addData('prac_d_tom_resp.corr', prac_d_tom_resp.corr)
    if prac_d_tom_resp.keys != None:  # we had a response
        prac_dual.addData('prac_d_tom_resp.rt', prac_d_tom_resp.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-7.000000)
    
    # --- Prepare to start Routine "prac_d_tom_iti" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code
    
    if not prac_d_tom_resp.keys :
        msg="Failed to respond"
    else:
        msg= "Reaction Time =%.3f" %(round(prac_d_tom_resp.rt,3))
    
    prac_d_tom_fb.setText(msg)
    # keep track of which components have finished
    prac_d_tom_itiComponents = [prac_d_tom_fb]
    for thisComponent in prac_d_tom_itiComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "prac_d_tom_iti" ---
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *prac_d_tom_fb* updates
        if prac_d_tom_fb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prac_d_tom_fb.frameNStart = frameN  # exact frame index
            prac_d_tom_fb.tStart = t  # local t and not account for scr refresh
            prac_d_tom_fb.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_d_tom_fb, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'prac_d_tom_fb.started')
            prac_d_tom_fb.setAutoDraw(True)
        if prac_d_tom_fb.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > prac_d_tom_fb.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                prac_d_tom_fb.tStop = t  # not accounting for scr refresh
                prac_d_tom_fb.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'prac_d_tom_fb.stopped')
                prac_d_tom_fb.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prac_d_tom_itiComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "prac_d_tom_iti" ---
    for thisComponent in prac_d_tom_itiComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'prac_dual'


# --- Prepare to start Routine "real_task_inst" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
trial_start.keys = []
trial_start.rt = []
_trial_start_allKeys = []
# keep track of which components have finished
real_task_instComponents = [trial_inst, trial_inst2, trial_start]
for thisComponent in real_task_instComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "real_task_inst" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *trial_inst* updates
    if trial_inst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        trial_inst.frameNStart = frameN  # exact frame index
        trial_inst.tStart = t  # local t and not account for scr refresh
        trial_inst.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trial_inst, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'trial_inst.started')
        trial_inst.setAutoDraw(True)
    if trial_inst.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > trial_inst.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            trial_inst.tStop = t  # not accounting for scr refresh
            trial_inst.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'trial_inst.stopped')
            trial_inst.setAutoDraw(False)
    
    # *trial_inst2* updates
    if trial_inst2.status == NOT_STARTED and tThisFlip >= 15-frameTolerance:
        # keep track of start time/frame for later
        trial_inst2.frameNStart = frameN  # exact frame index
        trial_inst2.tStart = t  # local t and not account for scr refresh
        trial_inst2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trial_inst2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'trial_inst2.started')
        trial_inst2.setAutoDraw(True)
    
    # *trial_start* updates
    waitOnFlip = False
    if trial_start.status == NOT_STARTED and tThisFlip >= 15-frameTolerance:
        # keep track of start time/frame for later
        trial_start.frameNStart = frameN  # exact frame index
        trial_start.tStart = t  # local t and not account for scr refresh
        trial_start.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trial_start, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'trial_start.started')
        trial_start.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(trial_start.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(trial_start.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if trial_start.status == STARTED and not waitOnFlip:
        theseKeys = trial_start.getKeys(keyList=['space'], waitRelease=False)
        _trial_start_allKeys.extend(theseKeys)
        if len(_trial_start_allKeys):
            trial_start.keys = _trial_start_allKeys[-1].name  # just the last key pressed
            trial_start.rt = _trial_start_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in real_task_instComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "real_task_inst" ---
for thisComponent in real_task_instComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if trial_start.keys in ['', [], None]:  # No response was made
    trial_start.keys = None
thisExp.addData('trial_start.keys',trial_start.keys)
if trial_start.keys != None:  # we had a response
    thisExp.addData('trial_start.rt', trial_start.rt)
thisExp.nextEntry()
# the Routine "real_task_inst" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
tom_block = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='tom_block')
thisExp.addLoop(tom_block)  # add the loop to the experiment
thisTom_block = tom_block.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTom_block.rgb)
if thisTom_block != None:
    for paramName in thisTom_block:
        exec('{} = thisTom_block[paramName]'.format(paramName))

for thisTom_block in tom_block:
    currentLoop = tom_block
    # abbreviate parameter names if possible (e.g. rgb = thisTom_block.rgb)
    if thisTom_block != None:
        for paramName in thisTom_block:
            exec('{} = thisTom_block[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "tom_intro" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    tom_int_resp.keys = []
    tom_int_resp.rt = []
    _tom_int_resp_allKeys = []
    # keep track of which components have finished
    tom_introComponents = [tom_task, tom_int_resp]
    for thisComponent in tom_introComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "tom_intro" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *tom_task* updates
        if tom_task.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            tom_task.frameNStart = frameN  # exact frame index
            tom_task.tStart = t  # local t and not account for scr refresh
            tom_task.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tom_task, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'tom_task.started')
            tom_task.setAutoDraw(True)
        
        # *tom_int_resp* updates
        waitOnFlip = False
        if tom_int_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            tom_int_resp.frameNStart = frameN  # exact frame index
            tom_int_resp.tStart = t  # local t and not account for scr refresh
            tom_int_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tom_int_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'tom_int_resp.started')
            tom_int_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(tom_int_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(tom_int_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if tom_int_resp.status == STARTED and not waitOnFlip:
            theseKeys = tom_int_resp.getKeys(keyList=['space'], waitRelease=False)
            _tom_int_resp_allKeys.extend(theseKeys)
            if len(_tom_int_resp_allKeys):
                tom_int_resp.keys = _tom_int_resp_allKeys[-1].name  # just the last key pressed
                tom_int_resp.rt = _tom_int_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in tom_introComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "tom_intro" ---
    for thisComponent in tom_introComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if tom_int_resp.keys in ['', [], None]:  # No response was made
        tom_int_resp.keys = None
    tom_block.addData('tom_int_resp.keys',tom_int_resp.keys)
    if tom_int_resp.keys != None:  # we had a response
        tom_block.addData('tom_int_resp.rt', tom_int_resp.rt)
    # the Routine "tom_intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    tom_single = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('conditions/tom_cond.xlsx'),
        seed=None, name='tom_single')
    thisExp.addLoop(tom_single)  # add the loop to the experiment
    thisTom_single = tom_single.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTom_single.rgb)
    if thisTom_single != None:
        for paramName in thisTom_single:
            exec('{} = thisTom_single[paramName]'.format(paramName))
    
    for thisTom_single in tom_single:
        currentLoop = tom_single
        # abbreviate parameter names if possible (e.g. rgb = thisTom_single.rgb)
        if thisTom_single != None:
            for paramName in thisTom_single:
                exec('{} = thisTom_single[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "tom_single_trial" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        tom_s_1.setImage(tom_img1)
        tom_s_2.setImage(tom_img2)
        tom_s_3.setImage(tom_img3)
        tom_s_dec.setImage(tom_dec_img)
        tom_s_resp.keys = []
        tom_s_resp.rt = []
        _tom_s_resp_allKeys = []
        # keep track of which components have finished
        tom_single_trialComponents = [tom_s_1, tom_s_2, tom_s_3, tom_s_dec, tom_s_resp]
        for thisComponent in tom_single_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "tom_single_trial" ---
        while continueRoutine and routineTimer.getTime() < 16.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *tom_s_1* updates
            if tom_s_1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tom_s_1.frameNStart = frameN  # exact frame index
                tom_s_1.tStart = t  # local t and not account for scr refresh
                tom_s_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tom_s_1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'tom_s_1.started')
                tom_s_1.setAutoDraw(True)
            if tom_s_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tom_s_1.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    tom_s_1.tStop = t  # not accounting for scr refresh
                    tom_s_1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'tom_s_1.stopped')
                    tom_s_1.setAutoDraw(False)
            
            # *tom_s_2* updates
            if tom_s_2.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                tom_s_2.frameNStart = frameN  # exact frame index
                tom_s_2.tStart = t  # local t and not account for scr refresh
                tom_s_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tom_s_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'tom_s_2.started')
                tom_s_2.setAutoDraw(True)
            if tom_s_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tom_s_2.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    tom_s_2.tStop = t  # not accounting for scr refresh
                    tom_s_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'tom_s_2.stopped')
                    tom_s_2.setAutoDraw(False)
            
            # *tom_s_3* updates
            if tom_s_3.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
                # keep track of start time/frame for later
                tom_s_3.frameNStart = frameN  # exact frame index
                tom_s_3.tStart = t  # local t and not account for scr refresh
                tom_s_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tom_s_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'tom_s_3.started')
                tom_s_3.setAutoDraw(True)
            if tom_s_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tom_s_3.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    tom_s_3.tStop = t  # not accounting for scr refresh
                    tom_s_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'tom_s_3.stopped')
                    tom_s_3.setAutoDraw(False)
            
            # *tom_s_dec* updates
            if tom_s_dec.status == NOT_STARTED and tThisFlip >= 4.5-frameTolerance:
                # keep track of start time/frame for later
                tom_s_dec.frameNStart = frameN  # exact frame index
                tom_s_dec.tStart = t  # local t and not account for scr refresh
                tom_s_dec.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tom_s_dec, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'tom_s_dec.started')
                tom_s_dec.setAutoDraw(True)
            if tom_s_dec.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tom_s_dec.tStartRefresh + 11.5-frameTolerance:
                    # keep track of stop time/frame for later
                    tom_s_dec.tStop = t  # not accounting for scr refresh
                    tom_s_dec.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'tom_s_dec.stopped')
                    tom_s_dec.setAutoDraw(False)
            
            # *tom_s_resp* updates
            waitOnFlip = False
            if tom_s_resp.status == NOT_STARTED and tThisFlip >= 4.5-frameTolerance:
                # keep track of start time/frame for later
                tom_s_resp.frameNStart = frameN  # exact frame index
                tom_s_resp.tStart = t  # local t and not account for scr refresh
                tom_s_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tom_s_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'tom_s_resp.started')
                tom_s_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(tom_s_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(tom_s_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if tom_s_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tom_s_resp.tStartRefresh + 11.5-frameTolerance:
                    # keep track of stop time/frame for later
                    tom_s_resp.tStop = t  # not accounting for scr refresh
                    tom_s_resp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'tom_s_resp.stopped')
                    tom_s_resp.status = FINISHED
            if tom_s_resp.status == STARTED and not waitOnFlip:
                theseKeys = tom_s_resp.getKeys(keyList=['1','2','3'], waitRelease=False)
                _tom_s_resp_allKeys.extend(theseKeys)
                if len(_tom_s_resp_allKeys):
                    tom_s_resp.keys = _tom_s_resp_allKeys[-1].name  # just the last key pressed
                    tom_s_resp.rt = _tom_s_resp_allKeys[-1].rt
                    # was this correct?
                    if (tom_s_resp.keys == str(corr_resp)) or (tom_s_resp.keys == corr_resp):
                        tom_s_resp.corr = 1
                    else:
                        tom_s_resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in tom_single_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "tom_single_trial" ---
        for thisComponent in tom_single_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if tom_s_resp.keys in ['', [], None]:  # No response was made
            tom_s_resp.keys = None
            # was no response the correct answer?!
            if str(corr_resp).lower() == 'none':
               tom_s_resp.corr = 1;  # correct non-response
            else:
               tom_s_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for tom_single (TrialHandler)
        tom_single.addData('tom_s_resp.keys',tom_s_resp.keys)
        tom_single.addData('tom_s_resp.corr', tom_s_resp.corr)
        if tom_s_resp.keys != None:  # we had a response
            tom_single.addData('tom_s_resp.rt', tom_s_resp.rt)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-16.000000)
        
        # --- Prepare to start Routine "ITI_2000" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        ITI_2000Components = [tom_iti]
        for thisComponent in ITI_2000Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "ITI_2000" ---
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *tom_iti* updates
            if tom_iti.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                tom_iti.frameNStart = frameN  # exact frame index
                tom_iti.tStart = t  # local t and not account for scr refresh
                tom_iti.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tom_iti, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'tom_iti.started')
                tom_iti.setAutoDraw(True)
            if tom_iti.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tom_iti.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    tom_iti.tStop = t  # not accounting for scr refresh
                    tom_iti.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'tom_iti.stopped')
                    tom_iti.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ITI_2000Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ITI_2000" ---
        for thisComponent in ITI_2000Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'tom_single'
    
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'tom_block'


# --- Prepare to start Routine "rest" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
rest_resp.keys = []
rest_resp.rt = []
_rest_resp_allKeys = []
# keep track of which components have finished
restComponents = [rest_15, rest_15_2, rest_resp]
for thisComponent in restComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "rest" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *rest_15* updates
    if rest_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        rest_15.frameNStart = frameN  # exact frame index
        rest_15.tStart = t  # local t and not account for scr refresh
        rest_15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rest_15, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'rest_15.started')
        rest_15.setAutoDraw(True)
    if rest_15.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > rest_15.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            rest_15.tStop = t  # not accounting for scr refresh
            rest_15.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'rest_15.stopped')
            rest_15.setAutoDraw(False)
    
    # *rest_15_2* updates
    if rest_15_2.status == NOT_STARTED and tThisFlip >= 15-frameTolerance:
        # keep track of start time/frame for later
        rest_15_2.frameNStart = frameN  # exact frame index
        rest_15_2.tStart = t  # local t and not account for scr refresh
        rest_15_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rest_15_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'rest_15_2.started')
        rest_15_2.setAutoDraw(True)
    
    # *rest_resp* updates
    waitOnFlip = False
    if rest_resp.status == NOT_STARTED and tThisFlip >= 15-frameTolerance:
        # keep track of start time/frame for later
        rest_resp.frameNStart = frameN  # exact frame index
        rest_resp.tStart = t  # local t and not account for scr refresh
        rest_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rest_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'rest_resp.started')
        rest_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(rest_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(rest_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if rest_resp.status == STARTED and not waitOnFlip:
        theseKeys = rest_resp.getKeys(keyList=['space'], waitRelease=False)
        _rest_resp_allKeys.extend(theseKeys)
        if len(_rest_resp_allKeys):
            rest_resp.keys = _rest_resp_allKeys[-1].name  # just the last key pressed
            rest_resp.rt = _rest_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in restComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "rest" ---
for thisComponent in restComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if rest_resp.keys in ['', [], None]:  # No response was made
    rest_resp.keys = None
thisExp.addData('rest_resp.keys',rest_resp.keys)
if rest_resp.keys != None:  # we had a response
    thisExp.addData('rest_resp.rt', rest_resp.rt)
thisExp.nextEntry()
# the Routine "rest" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
dual_block = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='dual_block')
thisExp.addLoop(dual_block)  # add the loop to the experiment
thisDual_block = dual_block.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisDual_block.rgb)
if thisDual_block != None:
    for paramName in thisDual_block:
        exec('{} = thisDual_block[paramName]'.format(paramName))

for thisDual_block in dual_block:
    currentLoop = dual_block
    # abbreviate parameter names if possible (e.g. rgb = thisDual_block.rgb)
    if thisDual_block != None:
        for paramName in thisDual_block:
            exec('{} = thisDual_block[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "dual_intro" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    dual_task_intro_resp.keys = []
    dual_task_intro_resp.rt = []
    _dual_task_intro_resp_allKeys = []
    # keep track of which components have finished
    dual_introComponents = [dual_task_intro, dual_task_intro_resp]
    for thisComponent in dual_introComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "dual_intro" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *dual_task_intro* updates
        if dual_task_intro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            dual_task_intro.frameNStart = frameN  # exact frame index
            dual_task_intro.tStart = t  # local t and not account for scr refresh
            dual_task_intro.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dual_task_intro, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'dual_task_intro.started')
            dual_task_intro.setAutoDraw(True)
        
        # *dual_task_intro_resp* updates
        waitOnFlip = False
        if dual_task_intro_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            dual_task_intro_resp.frameNStart = frameN  # exact frame index
            dual_task_intro_resp.tStart = t  # local t and not account for scr refresh
            dual_task_intro_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dual_task_intro_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'dual_task_intro_resp.started')
            dual_task_intro_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(dual_task_intro_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(dual_task_intro_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if dual_task_intro_resp.status == STARTED and not waitOnFlip:
            theseKeys = dual_task_intro_resp.getKeys(keyList=['space'], waitRelease=False)
            _dual_task_intro_resp_allKeys.extend(theseKeys)
            if len(_dual_task_intro_resp_allKeys):
                dual_task_intro_resp.keys = _dual_task_intro_resp_allKeys[-1].name  # just the last key pressed
                dual_task_intro_resp.rt = _dual_task_intro_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in dual_introComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "dual_intro" ---
    for thisComponent in dual_introComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if dual_task_intro_resp.keys in ['', [], None]:  # No response was made
        dual_task_intro_resp.keys = None
    dual_block.addData('dual_task_intro_resp.keys',dual_task_intro_resp.keys)
    if dual_task_intro_resp.keys != None:  # we had a response
        dual_block.addData('dual_task_intro_resp.rt', dual_task_intro_resp.rt)
    # the Routine "dual_intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    dual_task = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('conditions/tom_cond.xlsx'),
        seed=None, name='dual_task')
    thisExp.addLoop(dual_task)  # add the loop to the experiment
    thisDual_task = dual_task.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisDual_task.rgb)
    if thisDual_task != None:
        for paramName in thisDual_task:
            exec('{} = thisDual_task[paramName]'.format(paramName))
    
    for thisDual_task in dual_task:
        currentLoop = dual_task
        # abbreviate parameter names if possible (e.g. rgb = thisDual_task.rgb)
        if thisDual_task != None:
            for paramName in thisDual_task:
                exec('{} = thisDual_task[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "dual_iti" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from dual_iti_code
        dual_iti = 2.5-(random())
        # keep track of which components have finished
        dual_itiComponents = [dual_iti_cross]
        for thisComponent in dual_itiComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "dual_iti" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *dual_iti_cross* updates
            if dual_iti_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                dual_iti_cross.frameNStart = frameN  # exact frame index
                dual_iti_cross.tStart = t  # local t and not account for scr refresh
                dual_iti_cross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(dual_iti_cross, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'dual_iti_cross.started')
                dual_iti_cross.setAutoDraw(True)
            if dual_iti_cross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > dual_iti_cross.tStartRefresh + dual_iti-frameTolerance:
                    # keep track of stop time/frame for later
                    dual_iti_cross.tStop = t  # not accounting for scr refresh
                    dual_iti_cross.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'dual_iti_cross.stopped')
                    dual_iti_cross.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in dual_itiComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "dual_iti" ---
        for thisComponent in dual_itiComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "dual_iti" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        ssst_loop1 = data.TrialHandler(nReps=1.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('conditions/ssst_go_stop.xlsx'),
            seed=None, name='ssst_loop1')
        thisExp.addLoop(ssst_loop1)  # add the loop to the experiment
        thisSsst_loop1 = ssst_loop1.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisSsst_loop1.rgb)
        if thisSsst_loop1 != None:
            for paramName in thisSsst_loop1:
                exec('{} = thisSsst_loop1[paramName]'.format(paramName))
        
        for thisSsst_loop1 in ssst_loop1:
            currentLoop = ssst_loop1
            # abbreviate parameter names if possible (e.g. rgb = thisSsst_loop1.rgb)
            if thisSsst_loop1 != None:
                for paramName in thisSsst_loop1:
                    exec('{} = thisSsst_loop1[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "ssst_iti" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # Run 'Begin Routine' code from ssst_iti_draw
            ITI_value = 1.5-(random())
            # keep track of which components have finished
            ssst_itiComponents = [ssst_iti_cross]
            for thisComponent in ssst_itiComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "ssst_iti" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *ssst_iti_cross* updates
                if ssst_iti_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    ssst_iti_cross.frameNStart = frameN  # exact frame index
                    ssst_iti_cross.tStart = t  # local t and not account for scr refresh
                    ssst_iti_cross.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ssst_iti_cross, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'ssst_iti_cross.started')
                    ssst_iti_cross.setAutoDraw(True)
                if ssst_iti_cross.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ssst_iti_cross.tStartRefresh + ITI_value-frameTolerance:
                        # keep track of stop time/frame for later
                        ssst_iti_cross.tStop = t  # not accounting for scr refresh
                        ssst_iti_cross.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'ssst_iti_cross.stopped')
                        ssst_iti_cross.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ssst_itiComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "ssst_iti" ---
            for thisComponent in ssst_itiComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # the Routine "ssst_iti" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "stop_sig" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            ssst_go.setImage(go_img)
            ssst_stop.setImage(st_img)
            ssst_resp.keys = []
            ssst_resp.rt = []
            _ssst_resp_allKeys = []
            # keep track of which components have finished
            stop_sigComponents = [ssst_go, ssst_stop, ssst_resp]
            for thisComponent in stop_sigComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "stop_sig" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *ssst_go* updates
                if ssst_go.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    ssst_go.frameNStart = frameN  # exact frame index
                    ssst_go.tStart = t  # local t and not account for scr refresh
                    ssst_go.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ssst_go, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'ssst_go.started')
                    ssst_go.setAutoDraw(True)
                if ssst_go.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ssst_go.tStartRefresh + ssd-frameTolerance:
                        # keep track of stop time/frame for later
                        ssst_go.tStop = t  # not accounting for scr refresh
                        ssst_go.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'ssst_go.stopped')
                        ssst_go.setAutoDraw(False)
                
                # *ssst_stop* updates
                if ssst_stop.status == NOT_STARTED and tThisFlip >= ssd - 0.00001-frameTolerance:
                    # keep track of start time/frame for later
                    ssst_stop.frameNStart = frameN  # exact frame index
                    ssst_stop.tStart = t  # local t and not account for scr refresh
                    ssst_stop.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ssst_stop, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'ssst_stop.started')
                    ssst_stop.setAutoDraw(True)
                if ssst_stop.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ssst_stop.tStartRefresh + 1.25 - ssd-frameTolerance:
                        # keep track of stop time/frame for later
                        ssst_stop.tStop = t  # not accounting for scr refresh
                        ssst_stop.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'ssst_stop.stopped')
                        ssst_stop.setAutoDraw(False)
                
                # *ssst_resp* updates
                waitOnFlip = False
                if ssst_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    ssst_resp.frameNStart = frameN  # exact frame index
                    ssst_resp.tStart = t  # local t and not account for scr refresh
                    ssst_resp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ssst_resp, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'ssst_resp.started')
                    ssst_resp.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(ssst_resp.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(ssst_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if ssst_resp.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ssst_resp.tStartRefresh + 1.25-frameTolerance:
                        # keep track of stop time/frame for later
                        ssst_resp.tStop = t  # not accounting for scr refresh
                        ssst_resp.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'ssst_resp.stopped')
                        ssst_resp.status = FINISHED
                if ssst_resp.status == STARTED and not waitOnFlip:
                    theseKeys = ssst_resp.getKeys(keyList=['k','space', 'None'], waitRelease=False)
                    _ssst_resp_allKeys.extend(theseKeys)
                    if len(_ssst_resp_allKeys):
                        ssst_resp.keys = _ssst_resp_allKeys[-1].name  # just the last key pressed
                        ssst_resp.rt = _ssst_resp_allKeys[-1].rt
                        # was this correct?
                        if (ssst_resp.keys == str(corr_resp)) or (ssst_resp.keys == corr_resp):
                            ssst_resp.corr = 1
                        else:
                            ssst_resp.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in stop_sigComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "stop_sig" ---
            for thisComponent in stop_sigComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # Run 'End Routine' code from ssst_staircase
            thisExp.addData('trial_type', trial_type)
            thisExp.addData('ssd', ssd)
            thisExp.addData('ssst_resp', ssst_resp.keys)
            
            if trial_type == 'stop': # only adjust on stop trials
                #adjust the stepsize
                if ssst_resp.corr == 1:
                    ssd += stepsize
                else:
                    ssd -= stepsize
            
                # cap the stop time
                if ssd < minval:
                    ssd = minval
                if ssd > maxval:
                    ssd = maxval
            
            #print(ssd)
            # check responses
            if ssst_resp.keys in ['', [], None]:  # No response was made
                ssst_resp.keys = None
                # was no response the correct answer?!
                if str(corr_resp).lower() == 'none':
                   ssst_resp.corr = 1;  # correct non-response
                else:
                   ssst_resp.corr = 0;  # failed to respond (incorrectly)
            # store data for ssst_loop1 (TrialHandler)
            ssst_loop1.addData('ssst_resp.keys',ssst_resp.keys)
            ssst_loop1.addData('ssst_resp.corr', ssst_resp.corr)
            if ssst_resp.keys != None:  # we had a response
                ssst_loop1.addData('ssst_resp.rt', ssst_resp.rt)
            # the Routine "stop_sig" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'ssst_loop1'
        
        
        # --- Prepare to start Routine "tom_dual_1" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        tom_d_1.setImage(tom_img1)
        # keep track of which components have finished
        tom_dual_1Components = [tom_d_1]
        for thisComponent in tom_dual_1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "tom_dual_1" ---
        while continueRoutine and routineTimer.getTime() < 1.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *tom_d_1* updates
            if tom_d_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                tom_d_1.frameNStart = frameN  # exact frame index
                tom_d_1.tStart = t  # local t and not account for scr refresh
                tom_d_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tom_d_1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'tom_d_1.started')
                tom_d_1.setAutoDraw(True)
            if tom_d_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tom_d_1.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    tom_d_1.tStop = t  # not accounting for scr refresh
                    tom_d_1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'tom_d_1.stopped')
                    tom_d_1.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in tom_dual_1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "tom_dual_1" ---
        for thisComponent in tom_dual_1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.500000)
        
        # set up handler to look after randomisation of conditions etc
        ssst_loop2 = data.TrialHandler(nReps=1.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('conditions/ssst_go_stop.xlsx'),
            seed=None, name='ssst_loop2')
        thisExp.addLoop(ssst_loop2)  # add the loop to the experiment
        thisSsst_loop2 = ssst_loop2.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisSsst_loop2.rgb)
        if thisSsst_loop2 != None:
            for paramName in thisSsst_loop2:
                exec('{} = thisSsst_loop2[paramName]'.format(paramName))
        
        for thisSsst_loop2 in ssst_loop2:
            currentLoop = ssst_loop2
            # abbreviate parameter names if possible (e.g. rgb = thisSsst_loop2.rgb)
            if thisSsst_loop2 != None:
                for paramName in thisSsst_loop2:
                    exec('{} = thisSsst_loop2[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "ssst_iti" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # Run 'Begin Routine' code from ssst_iti_draw
            ITI_value = 1.5-(random())
            # keep track of which components have finished
            ssst_itiComponents = [ssst_iti_cross]
            for thisComponent in ssst_itiComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "ssst_iti" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *ssst_iti_cross* updates
                if ssst_iti_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    ssst_iti_cross.frameNStart = frameN  # exact frame index
                    ssst_iti_cross.tStart = t  # local t and not account for scr refresh
                    ssst_iti_cross.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ssst_iti_cross, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'ssst_iti_cross.started')
                    ssst_iti_cross.setAutoDraw(True)
                if ssst_iti_cross.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ssst_iti_cross.tStartRefresh + ITI_value-frameTolerance:
                        # keep track of stop time/frame for later
                        ssst_iti_cross.tStop = t  # not accounting for scr refresh
                        ssst_iti_cross.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'ssst_iti_cross.stopped')
                        ssst_iti_cross.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ssst_itiComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "ssst_iti" ---
            for thisComponent in ssst_itiComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # the Routine "ssst_iti" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "stop_sig" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            ssst_go.setImage(go_img)
            ssst_stop.setImage(st_img)
            ssst_resp.keys = []
            ssst_resp.rt = []
            _ssst_resp_allKeys = []
            # keep track of which components have finished
            stop_sigComponents = [ssst_go, ssst_stop, ssst_resp]
            for thisComponent in stop_sigComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "stop_sig" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *ssst_go* updates
                if ssst_go.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    ssst_go.frameNStart = frameN  # exact frame index
                    ssst_go.tStart = t  # local t and not account for scr refresh
                    ssst_go.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ssst_go, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'ssst_go.started')
                    ssst_go.setAutoDraw(True)
                if ssst_go.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ssst_go.tStartRefresh + ssd-frameTolerance:
                        # keep track of stop time/frame for later
                        ssst_go.tStop = t  # not accounting for scr refresh
                        ssst_go.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'ssst_go.stopped')
                        ssst_go.setAutoDraw(False)
                
                # *ssst_stop* updates
                if ssst_stop.status == NOT_STARTED and tThisFlip >= ssd - 0.00001-frameTolerance:
                    # keep track of start time/frame for later
                    ssst_stop.frameNStart = frameN  # exact frame index
                    ssst_stop.tStart = t  # local t and not account for scr refresh
                    ssst_stop.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ssst_stop, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'ssst_stop.started')
                    ssst_stop.setAutoDraw(True)
                if ssst_stop.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ssst_stop.tStartRefresh + 1.25 - ssd-frameTolerance:
                        # keep track of stop time/frame for later
                        ssst_stop.tStop = t  # not accounting for scr refresh
                        ssst_stop.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'ssst_stop.stopped')
                        ssst_stop.setAutoDraw(False)
                
                # *ssst_resp* updates
                waitOnFlip = False
                if ssst_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    ssst_resp.frameNStart = frameN  # exact frame index
                    ssst_resp.tStart = t  # local t and not account for scr refresh
                    ssst_resp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ssst_resp, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'ssst_resp.started')
                    ssst_resp.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(ssst_resp.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(ssst_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if ssst_resp.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ssst_resp.tStartRefresh + 1.25-frameTolerance:
                        # keep track of stop time/frame for later
                        ssst_resp.tStop = t  # not accounting for scr refresh
                        ssst_resp.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'ssst_resp.stopped')
                        ssst_resp.status = FINISHED
                if ssst_resp.status == STARTED and not waitOnFlip:
                    theseKeys = ssst_resp.getKeys(keyList=['k','space', 'None'], waitRelease=False)
                    _ssst_resp_allKeys.extend(theseKeys)
                    if len(_ssst_resp_allKeys):
                        ssst_resp.keys = _ssst_resp_allKeys[-1].name  # just the last key pressed
                        ssst_resp.rt = _ssst_resp_allKeys[-1].rt
                        # was this correct?
                        if (ssst_resp.keys == str(corr_resp)) or (ssst_resp.keys == corr_resp):
                            ssst_resp.corr = 1
                        else:
                            ssst_resp.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in stop_sigComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "stop_sig" ---
            for thisComponent in stop_sigComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # Run 'End Routine' code from ssst_staircase
            thisExp.addData('trial_type', trial_type)
            thisExp.addData('ssd', ssd)
            thisExp.addData('ssst_resp', ssst_resp.keys)
            
            if trial_type == 'stop': # only adjust on stop trials
                #adjust the stepsize
                if ssst_resp.corr == 1:
                    ssd += stepsize
                else:
                    ssd -= stepsize
            
                # cap the stop time
                if ssd < minval:
                    ssd = minval
                if ssd > maxval:
                    ssd = maxval
            
            #print(ssd)
            # check responses
            if ssst_resp.keys in ['', [], None]:  # No response was made
                ssst_resp.keys = None
                # was no response the correct answer?!
                if str(corr_resp).lower() == 'none':
                   ssst_resp.corr = 1;  # correct non-response
                else:
                   ssst_resp.corr = 0;  # failed to respond (incorrectly)
            # store data for ssst_loop2 (TrialHandler)
            ssst_loop2.addData('ssst_resp.keys',ssst_resp.keys)
            ssst_loop2.addData('ssst_resp.corr', ssst_resp.corr)
            if ssst_resp.keys != None:  # we had a response
                ssst_loop2.addData('ssst_resp.rt', ssst_resp.rt)
            # the Routine "stop_sig" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'ssst_loop2'
        
        
        # --- Prepare to start Routine "tom_dual_2" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        tom_d_2.setImage(tom_img2)
        # keep track of which components have finished
        tom_dual_2Components = [tom_d_2]
        for thisComponent in tom_dual_2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "tom_dual_2" ---
        while continueRoutine and routineTimer.getTime() < 1.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *tom_d_2* updates
            if tom_d_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tom_d_2.frameNStart = frameN  # exact frame index
                tom_d_2.tStart = t  # local t and not account for scr refresh
                tom_d_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tom_d_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'tom_d_2.started')
                tom_d_2.setAutoDraw(True)
            if tom_d_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tom_d_2.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    tom_d_2.tStop = t  # not accounting for scr refresh
                    tom_d_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'tom_d_2.stopped')
                    tom_d_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in tom_dual_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "tom_dual_2" ---
        for thisComponent in tom_dual_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.500000)
        
        # set up handler to look after randomisation of conditions etc
        ssst_loop3 = data.TrialHandler(nReps=1.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('conditions/ssst_go_stop.xlsx'),
            seed=None, name='ssst_loop3')
        thisExp.addLoop(ssst_loop3)  # add the loop to the experiment
        thisSsst_loop3 = ssst_loop3.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisSsst_loop3.rgb)
        if thisSsst_loop3 != None:
            for paramName in thisSsst_loop3:
                exec('{} = thisSsst_loop3[paramName]'.format(paramName))
        
        for thisSsst_loop3 in ssst_loop3:
            currentLoop = ssst_loop3
            # abbreviate parameter names if possible (e.g. rgb = thisSsst_loop3.rgb)
            if thisSsst_loop3 != None:
                for paramName in thisSsst_loop3:
                    exec('{} = thisSsst_loop3[paramName]'.format(paramName))
            
            # --- Prepare to start Routine "ssst_iti" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            # Run 'Begin Routine' code from ssst_iti_draw
            ITI_value = 1.5-(random())
            # keep track of which components have finished
            ssst_itiComponents = [ssst_iti_cross]
            for thisComponent in ssst_itiComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "ssst_iti" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *ssst_iti_cross* updates
                if ssst_iti_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    ssst_iti_cross.frameNStart = frameN  # exact frame index
                    ssst_iti_cross.tStart = t  # local t and not account for scr refresh
                    ssst_iti_cross.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ssst_iti_cross, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'ssst_iti_cross.started')
                    ssst_iti_cross.setAutoDraw(True)
                if ssst_iti_cross.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ssst_iti_cross.tStartRefresh + ITI_value-frameTolerance:
                        # keep track of stop time/frame for later
                        ssst_iti_cross.tStop = t  # not accounting for scr refresh
                        ssst_iti_cross.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'ssst_iti_cross.stopped')
                        ssst_iti_cross.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ssst_itiComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "ssst_iti" ---
            for thisComponent in ssst_itiComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # the Routine "ssst_iti" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "stop_sig" ---
            continueRoutine = True
            routineForceEnded = False
            # update component parameters for each repeat
            ssst_go.setImage(go_img)
            ssst_stop.setImage(st_img)
            ssst_resp.keys = []
            ssst_resp.rt = []
            _ssst_resp_allKeys = []
            # keep track of which components have finished
            stop_sigComponents = [ssst_go, ssst_stop, ssst_resp]
            for thisComponent in stop_sigComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "stop_sig" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *ssst_go* updates
                if ssst_go.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    ssst_go.frameNStart = frameN  # exact frame index
                    ssst_go.tStart = t  # local t and not account for scr refresh
                    ssst_go.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ssst_go, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'ssst_go.started')
                    ssst_go.setAutoDraw(True)
                if ssst_go.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ssst_go.tStartRefresh + ssd-frameTolerance:
                        # keep track of stop time/frame for later
                        ssst_go.tStop = t  # not accounting for scr refresh
                        ssst_go.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'ssst_go.stopped')
                        ssst_go.setAutoDraw(False)
                
                # *ssst_stop* updates
                if ssst_stop.status == NOT_STARTED and tThisFlip >= ssd - 0.00001-frameTolerance:
                    # keep track of start time/frame for later
                    ssst_stop.frameNStart = frameN  # exact frame index
                    ssst_stop.tStart = t  # local t and not account for scr refresh
                    ssst_stop.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ssst_stop, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'ssst_stop.started')
                    ssst_stop.setAutoDraw(True)
                if ssst_stop.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ssst_stop.tStartRefresh + 1.25 - ssd-frameTolerance:
                        # keep track of stop time/frame for later
                        ssst_stop.tStop = t  # not accounting for scr refresh
                        ssst_stop.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'ssst_stop.stopped')
                        ssst_stop.setAutoDraw(False)
                
                # *ssst_resp* updates
                waitOnFlip = False
                if ssst_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    ssst_resp.frameNStart = frameN  # exact frame index
                    ssst_resp.tStart = t  # local t and not account for scr refresh
                    ssst_resp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ssst_resp, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'ssst_resp.started')
                    ssst_resp.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(ssst_resp.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(ssst_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if ssst_resp.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ssst_resp.tStartRefresh + 1.25-frameTolerance:
                        # keep track of stop time/frame for later
                        ssst_resp.tStop = t  # not accounting for scr refresh
                        ssst_resp.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'ssst_resp.stopped')
                        ssst_resp.status = FINISHED
                if ssst_resp.status == STARTED and not waitOnFlip:
                    theseKeys = ssst_resp.getKeys(keyList=['k','space', 'None'], waitRelease=False)
                    _ssst_resp_allKeys.extend(theseKeys)
                    if len(_ssst_resp_allKeys):
                        ssst_resp.keys = _ssst_resp_allKeys[-1].name  # just the last key pressed
                        ssst_resp.rt = _ssst_resp_allKeys[-1].rt
                        # was this correct?
                        if (ssst_resp.keys == str(corr_resp)) or (ssst_resp.keys == corr_resp):
                            ssst_resp.corr = 1
                        else:
                            ssst_resp.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in stop_sigComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "stop_sig" ---
            for thisComponent in stop_sigComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # Run 'End Routine' code from ssst_staircase
            thisExp.addData('trial_type', trial_type)
            thisExp.addData('ssd', ssd)
            thisExp.addData('ssst_resp', ssst_resp.keys)
            
            if trial_type == 'stop': # only adjust on stop trials
                #adjust the stepsize
                if ssst_resp.corr == 1:
                    ssd += stepsize
                else:
                    ssd -= stepsize
            
                # cap the stop time
                if ssd < minval:
                    ssd = minval
                if ssd > maxval:
                    ssd = maxval
            
            #print(ssd)
            # check responses
            if ssst_resp.keys in ['', [], None]:  # No response was made
                ssst_resp.keys = None
                # was no response the correct answer?!
                if str(corr_resp).lower() == 'none':
                   ssst_resp.corr = 1;  # correct non-response
                else:
                   ssst_resp.corr = 0;  # failed to respond (incorrectly)
            # store data for ssst_loop3 (TrialHandler)
            ssst_loop3.addData('ssst_resp.keys',ssst_resp.keys)
            ssst_loop3.addData('ssst_resp.corr', ssst_resp.corr)
            if ssst_resp.keys != None:  # we had a response
                ssst_loop3.addData('ssst_resp.rt', ssst_resp.rt)
            # the Routine "stop_sig" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'ssst_loop3'
        
        
        # --- Prepare to start Routine "tom_dual_3" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        tom_d_3.setImage(tom_img3)
        # keep track of which components have finished
        tom_dual_3Components = [tom_d_3]
        for thisComponent in tom_dual_3Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "tom_dual_3" ---
        while continueRoutine and routineTimer.getTime() < 1.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *tom_d_3* updates
            if tom_d_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                tom_d_3.frameNStart = frameN  # exact frame index
                tom_d_3.tStart = t  # local t and not account for scr refresh
                tom_d_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tom_d_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'tom_d_3.started')
                tom_d_3.setAutoDraw(True)
            if tom_d_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tom_d_3.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    tom_d_3.tStop = t  # not accounting for scr refresh
                    tom_d_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'tom_d_3.stopped')
                    tom_d_3.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in tom_dual_3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "tom_dual_3" ---
        for thisComponent in tom_dual_3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.500000)
        
        # --- Prepare to start Routine "tom_dual_dec" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        tom_choice.setImage(tom_dec_img)
        tom_d_resp.keys = []
        tom_d_resp.rt = []
        _tom_d_resp_allKeys = []
        # keep track of which components have finished
        tom_dual_decComponents = [tom_choice, tom_d_resp]
        for thisComponent in tom_dual_decComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "tom_dual_dec" ---
        while continueRoutine and routineTimer.getTime() < 7.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *tom_choice* updates
            if tom_choice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                tom_choice.frameNStart = frameN  # exact frame index
                tom_choice.tStart = t  # local t and not account for scr refresh
                tom_choice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tom_choice, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'tom_choice.started')
                tom_choice.setAutoDraw(True)
            if tom_choice.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tom_choice.tStartRefresh + 7-frameTolerance:
                    # keep track of stop time/frame for later
                    tom_choice.tStop = t  # not accounting for scr refresh
                    tom_choice.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'tom_choice.stopped')
                    tom_choice.setAutoDraw(False)
            
            # *tom_d_resp* updates
            waitOnFlip = False
            if tom_d_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                tom_d_resp.frameNStart = frameN  # exact frame index
                tom_d_resp.tStart = t  # local t and not account for scr refresh
                tom_d_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tom_d_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'tom_d_resp.started')
                tom_d_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(tom_d_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(tom_d_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if tom_d_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tom_d_resp.tStartRefresh + 7-frameTolerance:
                    # keep track of stop time/frame for later
                    tom_d_resp.tStop = t  # not accounting for scr refresh
                    tom_d_resp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'tom_d_resp.stopped')
                    tom_d_resp.status = FINISHED
            if tom_d_resp.status == STARTED and not waitOnFlip:
                theseKeys = tom_d_resp.getKeys(keyList=['1','2','3'], waitRelease=False)
                _tom_d_resp_allKeys.extend(theseKeys)
                if len(_tom_d_resp_allKeys):
                    tom_d_resp.keys = _tom_d_resp_allKeys[-1].name  # just the last key pressed
                    tom_d_resp.rt = _tom_d_resp_allKeys[-1].rt
                    # was this correct?
                    if (tom_d_resp.keys == str(corr_resp_tom)) or (tom_d_resp.keys == corr_resp_tom):
                        tom_d_resp.corr = 1
                    else:
                        tom_d_resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in tom_dual_decComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "tom_dual_dec" ---
        for thisComponent in tom_dual_decComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if tom_d_resp.keys in ['', [], None]:  # No response was made
            tom_d_resp.keys = None
            # was no response the correct answer?!
            if str(corr_resp_tom).lower() == 'none':
               tom_d_resp.corr = 1;  # correct non-response
            else:
               tom_d_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for dual_task (TrialHandler)
        dual_task.addData('tom_d_resp.keys',tom_d_resp.keys)
        dual_task.addData('tom_d_resp.corr', tom_d_resp.corr)
        if tom_d_resp.keys != None:  # we had a response
            dual_task.addData('tom_d_resp.rt', tom_d_resp.rt)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-7.000000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'dual_task'
    
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'dual_block'


# --- Prepare to start Routine "outro" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
outro_resp.keys = []
outro_resp.rt = []
_outro_resp_allKeys = []
# keep track of which components have finished
outroComponents = [outro_text, outro_text2, outro_resp]
for thisComponent in outroComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "outro" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *outro_text* updates
    if outro_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        outro_text.frameNStart = frameN  # exact frame index
        outro_text.tStart = t  # local t and not account for scr refresh
        outro_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(outro_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'outro_text.started')
        outro_text.setAutoDraw(True)
    if outro_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > outro_text.tStartRefresh + 7-frameTolerance:
            # keep track of stop time/frame for later
            outro_text.tStop = t  # not accounting for scr refresh
            outro_text.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'outro_text.stopped')
            outro_text.setAutoDraw(False)
    
    # *outro_text2* updates
    if outro_text2.status == NOT_STARTED and tThisFlip >= 7-frameTolerance:
        # keep track of start time/frame for later
        outro_text2.frameNStart = frameN  # exact frame index
        outro_text2.tStart = t  # local t and not account for scr refresh
        outro_text2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(outro_text2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'outro_text2.started')
        outro_text2.setAutoDraw(True)
    
    # *outro_resp* updates
    waitOnFlip = False
    if outro_resp.status == NOT_STARTED and tThisFlip >= 7-frameTolerance:
        # keep track of start time/frame for later
        outro_resp.frameNStart = frameN  # exact frame index
        outro_resp.tStart = t  # local t and not account for scr refresh
        outro_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(outro_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'outro_resp.started')
        outro_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(outro_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(outro_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if outro_resp.status == STARTED and not waitOnFlip:
        theseKeys = outro_resp.getKeys(keyList=['space'], waitRelease=False)
        _outro_resp_allKeys.extend(theseKeys)
        if len(_outro_resp_allKeys):
            outro_resp.keys = _outro_resp_allKeys[-1].name  # just the last key pressed
            outro_resp.rt = _outro_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in outroComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "outro" ---
for thisComponent in outroComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if outro_resp.keys in ['', [], None]:  # No response was made
    outro_resp.keys = None
thisExp.addData('outro_resp.keys',outro_resp.keys)
if outro_resp.keys != None:  # we had a response
    thisExp.addData('outro_resp.rt', outro_resp.rt)
thisExp.nextEntry()
# the Routine "outro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
