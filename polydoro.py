import os
import time
from subprocess import Popen
from time import sleep

import pidfile
from playsound import playsound

from config import config


class Pomodoro:
    def __init__(self, config) -> None:
        self.timer_duration = int(config["timer_duration"]) * 60
        self.break_duration = int(config["break_duration"]) * 60
        self.long_break_duration = int(config["long_break_duration"]) * 60
        self.break_counter = 0
        self.running = False
        self.path = os.path.dirname(os.path.abspath(__file__))

    def start(self):
        self.running = True

        while self.running:
            # Working phase
            self.seconds = self.timer_duration
            self.__pass_time()

            # End phase
            self.play_bell()
            self.send_notification("Polydoro", "Time for a break!")

            # Break phase
            if self.break_counter == 3:
                self.seconds = self.long_break_duration
                self.break_counter = 0
            else:
                self.seconds = self.break_duration
                self.break_counter += 1
            self.__pass_time()

            # End phase
            self.play_double_bell()
            self.send_notification("Polydoro", "Get back to work!")

    def stop(self):
        self.running = False
        self.__clean_output()

    def send_notification(self, title, msg):
        Popen(['notify-send', '--icon=alarm-symbolic', title, msg])

    def play_bell(self):
        playsound(f'{self.path}/bell.wav')

    def play_double_bell(self):
        playsound(f'{self.path}/double_bell.wav')

    def __pass_time(self):
        while self.seconds > 0 and self.running:
            self.seconds -= 1
            self.__print_output()
            sleep(1)

    def __print_output(self):
        with open("/tmp/polydoro.output", "w") as f:
            f.write(f"{time.strftime('%M:%S', time.gmtime(self.seconds))}")

    def __clean_output(self):
        with open("/tmp/polydoro.output", "w") as f:
            f.write("")


if __name__ == '__main__':
    with pidfile.PidFile('/tmp/polydoro.pid'):
        pomodoro = Pomodoro(config)
        try:
            pomodoro.start()
        finally:
            pomodoro.stop()
