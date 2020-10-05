import RPi.GPIO as G
import time
class motor():
    def __init__():

        self.stp_2 = 11
        self.dir_2 = 12
        self.stp_1 = 13
        self.dir_1 = 15
        self.fre = 100
        
        G.setmode(G.BOARD)
        G.setup(self.dir_2, G.OUT)
        G.setup(self.dir_1, G.OUT)
        pwm_2 = GPIO.PWM(self.stp_2, self.fre)
        pwm_1 = GPIO.PWM(self.stp_1, self.fre)

        pwm_2.start(0)
        pwm_1.start(0)
        pwm_2.stop()
        pwm_1.stop()


    def run(self):
        pwm_2.start(50)
        pwm_1.start(50)
        timw.sleep(3)


if __name__ == '__main__':
    _motor = motor()
    _motor.run()
