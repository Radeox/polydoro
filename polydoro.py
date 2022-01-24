import time
from subprocess import Popen
from time import sleep

from config import config


class Pomodoro:
    def __init__(self, config) -> None:
        self.timer_duration = int(config["timer_duration"]) * 60
        self.break_duration = int(config["break_duration"]) * 60
        self.long_break_duration = int(config["long_break_duration"]) * 60
        self.break_counter = 0

    def start(self):
        while True:
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

    def __pass_time(self):
        while self.seconds > 0:
            self.seconds -= 1
            self.print_output()
            sleep(1)

    def send_notification(self, title, msg):
        Popen(['notify-send', '--icon=alarm-symbolic', title, msg])

    def play_bell(self):
        Popen(['aplay', '-q', 'bell.wav'])

    def play_double_bell(self):
        Popen(['aplay', '-q', 'double_bell.wav'])

    def print_output(self):
        with open("/tmp/polydoro.output", "w") as f:
            f.write(f"{time.strftime('%M:%S', time.gmtime(self.seconds))}")


if __name__ == '__main__':
    pomodoro = Pomodoro(config)
    pomodoro.start()
