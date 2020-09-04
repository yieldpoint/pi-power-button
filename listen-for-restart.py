#!/usr/bin/env python


import RPi.GPIO as GPIO
import subprocess


GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.wait_for_edge(2, GPIO.FALLING)

subprocess.call(['reboot'], shell=False)
