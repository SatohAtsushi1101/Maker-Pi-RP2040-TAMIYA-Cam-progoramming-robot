import machine
import utime
from machine import Pin,Timer
# Setup DC Motor pins
M1A = machine.PWM(machine.Pin(8))
M1B = machine.PWM(machine.Pin(9))
M2A = machine.PWM(machine.Pin(10))
M2B = machine.PWM(machine.Pin(11))
M1A.freq(50)
M1B.freq(50)
M2A.freq(50)
M2B.freq(50)
# Setup LED
timer = Timer()
right_led = Pin(2, Pin.OUT)
left_led = Pin(3, Pin.OUT)
def right_turn_signal(timer):
    global right_led
    right_led.toggle()
def left_turn_signal(timer):
    global left_led
    left_led.toggle()
def back_light(timer):
    left_led.toggle()
    right_led.toggle()
def forwards(speed,time):
    print("Forward")
    right_led.value(0)
    left_led.value(0)
    utime.sleep(1)
    right_led.value(1)
    left_led.value(1)
    utime.sleep(0.1)
    right_led.value(0)
    left_led.value(0)
    utime.sleep(0.3)
    right_led.value(1)
    left_led.value(1)
    utime.sleep(0.2)
    right_led.value(0)
    left_led.value(0)
    M1A.duty_u16(speed)   
    M1B.duty_u16(0)
    M2A.duty_u16(speed)
    M2B.duty_u16(0)
    utime.sleep(time)

def backwards(speed,time):
    timer.init(freq=6,mode=Timer.PERIODIC, callback=back_light)
    print("backwards")
    M1A.duty_u16(0)   
    M1B.duty_u16(speed)
    M2A.duty_u16(0)
    M2B.duty_u16(speed)
    utime.sleep(time)
    timer.deinit()

def stop(time):
    print("Stop")
    M1A.duty_u16(0)   
    M1B.duty_u16(0)
    M2A.duty_u16(0)
    M2B.duty_u16(0)
    utime.sleep(time)

def leftturn(time):
    timer.init(freq=2,mode=Timer.PERIODIC, callback=left_turn_signal)
    print("leftturn")
    M1A.duty_u16(0) 
    M1B.duty_u16(30000)
    M2A.duty_u16(30000)
    M2B.duty_u16(0)
    utime.sleep(time) #180 degree 6 seconds,90 degree 3seconds
    timer.deinit()

def rightturn(time):
    timer.init(freq=2,mode=Timer.PERIODIC, callback=right_turn_signal)
    print("rightturn")
    M1A.duty_u16(30000) 
    M1B.duty_u16(0)
    M2A.duty_u16(0)
    M2B.duty_u16(30000)
    utime.sleep(time) #180 degree 6 seconds,90 degree 3seconds
    timer.deinit()

def serching(time):
    print('serching')
    for j in range(time):
        for i in range(4):
            right_led.toggle()
            left_led.toggle()
            utime.sleep(0.18)

        M1A.duty_u16(30000) 
        M1B.duty_u16(0)
        M2A.duty_u16(0)
        M2B.duty_u16(30000)
        utime.sleep(1.5)
        stop(1)
        
while True:
    stop(5)
    serching(4)
    leftturn(3)
    forwards(30000,5)
    leftturn(10)
    stop(10)
