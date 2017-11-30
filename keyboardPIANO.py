"""I'm trying to build a keyboard that plays beep tones."""
"""Frequencies obtained from https://gist.github.com/tagliati/1804108"""
from winsound import Beep
from Tkinter import *

d={"c":"Q","d": "W","e":"E","f":"R","g": "T", "gS": "Y", "a": "U",
   "aS": "I", "b": "O", "cH": "P",
   "cSH": "A", "dH": "S", "dSH": "D", "eH": "F", "fH": "G", "fSH": "H",
   "gH": "J", "gSH": "K", "aH": "L"}

duration=300

def c(event):
    freq=261
    Beep(freq, duration)
def d(event):
    freq=294
    Beep(freq, duration)
def e(event):
    freq=329
    Beep(freq, duration)
def f(event):
    freq=349
    Beep(freq, duration)
def g(event):
    freq=391
    Beep(freq, duration)
def gS(event):
    freq=415
    Beep(freq, duration)
def a(event):
    freq=440
    Beep(freq, duration)
def aS(event):
    freq=455
    Beep(freq, duration)
def b(event):
    freq=466
    Beep(freq, duration)
def cH(event):
    freq=523
    Beep(freq, duration)
def cSH(event):
    freq=554
    Beep(freq, duration)
def dH(event):
    freq=587
    Beep(freq, duration)
def dSH(event):
    freq=622
    Beep(freq, duration)
def eH(event):
    freq=659
    Beep(freq, duration)
def fH(event):
    freq=698
    Beep(freq, duration)
def fSH(event):
    freq=740
    Beep(freq, duration)
def gH(event):
    freq=784
    Beep(freq, duration)
def gSH(event):
    freq=830
    Beep(freq, duration)
def aH(event):
    freq=880
    Beep(freq, duration)
def hold(event):
    while True:
        duration+=1
def release(event):
    pass
root = Tk()
frame = Frame(root, width=100, height=100)
#frame.bind("<KeyPress>", hold)
#frame.bind("<KeyRelease>", release)
freq=0
frame.bind("<KeyPress-Q>",c)
frame.bind("<KeyPress-W>",d)
frame.bind("<KeyPress-E>",e)
frame.bind("<KeyPress-R>",f)
frame.bind("<KeyPress-T>",g)
frame.bind("<KeyPress-Y>",gS)
frame.bind("<KeyPress-U>",a)
frame.bind("<KeyPress-I>",aS)
frame.bind("<KeyPress-O>",b)
frame.bind("<KeyPress-P>",cH)
frame.bind("<KeyPress-A>",cSH)
frame.bind("<KeyPress-S>",dH)
frame.bind("<KeyPress-D>",dSH)
frame.bind("<KeyPress-F>",eH)
frame.bind("<KeyPress-G>",fH)
frame.bind("<KeyPress-H>",fSH)
frame.bind("<KeyPress-J>",gH)
frame.bind("<KeyPress-K>",gSH)
frame.bind("<KeyPress-L>",aH)
frame.pack()
frame.focus_set()
root.mainloop()
