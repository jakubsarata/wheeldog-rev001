import time
from adafruit_servokit import ServoKit
import motoron
import tkinter as tk
from tkinter import messagebox
import cv2

#inicjalizacja klas serwomechanizmów
kit = ServoKit(channels=16, address=0x40)
kit1 = ServoKit(channels=16, address=0x41)

#inicjalizacja silników
mc1 = motoron.MotoronI2C(address=16)
mc2 = motoron.MotoronI2C(address=17)

def setup_motoron(mc):
  mc.reinitialize()
  mc.disable_crc()
  mc.clear_reset_flag()

setup_motoron(mc1)
setup_motoron(mc2)

mc1.set_max_acceleration(1, 80)
mc1.set_max_deceleration(1, 300)

mc1.set_max_acceleration(2, 80)
mc1.set_max_deceleration(2, 300)


mc2.set_max_acceleration(1, 80)
mc2.set_max_deceleration(1, 300)

mc2.set_max_acceleration(2, 80)
mc2.set_max_deceleration(2, 300)

#Ustawienie początkowych wartości serwomechanizmów
Base_Left_Right = 100 #tułów prawo lewo
Base_Up_Down = 90 #tułów góra dół
Base_Spin = 90 #tułów skręcanie

RF_Abduction = 98 #prawy przód odwodzenie
RF_Front_back = 85 #prawy przód przód-tył
RF_Spin = 20 #prawy przód obrót kołem

LF_Abduction = 100 #lewy przód odwodzenie
LF_Front_back = 130 #lewy przód przód-tył
LF_Spin = 100 #lewy przód obrót kołem

LB_Abduction = 100 #lewy tył odwodzenie
LB_Front_back = 110 #lewy tył przód-tył
LB_Spin = 100 #lewy tył obrót kołem

RB_Abduction = 85 #prawy przód odwodzenie
RB_Front_back = 90 #prawy przód przód-tył
RB_Spin = 20 #prawy przód obrót kołem

# Obsługa tułowia
def Base_Left():
    global Base_Left_Right
    Base_Left_Right = Base_Left_Right - 1
    kit.servo[0].angle = Base_Left_Right 
    return Base_Left_Right

def Base_Right():
    global Base_Left_Right
    Base_Left_Right = Base_Left_Right + 1
    kit.servo[0].angle = Base_Left_Right
    return Base_Left_Right

def Base_Up():
    global Base_Up_Down
    Base_Up_Down = Base_Up_Down - 1
    kit1.servo[0].angle = Base_Up_Down 
    return Base_Up_Down

def Base_Down():
    global Base_Up_Down
    Base_Up_Down = Base_Up_Down + 1
    kit1.servo[0].angle = Base_Up_Down
    return Base_Up_Down

def Base_Spin_Clockwise():
    global Base_Spin
    Base_Spin = Base_Spin - 1
    kit1.servo[1].angle = Base_Spin
    return Base_Spin

def Base_Spin_Counterclockwise():
    global Base_Spin
    Base_Spin = Base_Spin + 1
    kit1.servo[1].angle = Base_Spin
    return Base_Spin        
# Obsługa tułowia

# Obsługa noga prawy przód
def Leg_RF_Abduction():
    global RF_Abduction
    RF_Abduction = RF_Abduction - 1
    kit.servo[6].angle = RF_Abduction
    return RF_Abduction 

def Leg_RF_Adduction():
    global RF_Abduction
    RF_Abduction = RF_Abduction + 1
    kit.servo[6].angle = RF_Abduction
    return RF_Abduction 
 
def Leg_RF_Front():
    global RF_Front_back
    RF_Front_back = RF_Front_back + 1
    kit.servo[5].angle = RF_Front_back
    return RF_Front_back


def Leg_RF_Back():
    global RF_Front_back
    RF_Front_back = RF_Front_back - 1
    kit.servo[5].angle = RF_Front_back
    return RF_Front_back


def Leg_RF_Clockwise():
    global RF_Spin
    RF_Spin = RF_Spin + 1
    kit.servo[4].angle = RF_Spin
    return RF_Spin

def Leg_RF_Counterclockwise():
    global RF_Spin
    RF_Spin = RF_Spin - 1
    kit.servo[4].angle = RF_Spin
    return RF_Spin
# Obsługa noga prawy przód

# Obsługa noga lewy przód
def Leg_LF_Abduction():
    global LF_Abduction
    LF_Abduction = LF_Abduction + 1
    kit.servo[3].angle = LF_Abduction
    return LF_Abduction 

def Leg_LF_Adduction():
    global LF_Abduction
    LF_Abduction = LF_Abduction - 1
    kit.servo[3].angle = LF_Abduction
    return LF_Abduction 
 
def Leg_LF_Front():
    global LF_Front_back
    LF_Front_back = LF_Front_back - 1
    kit.servo[2].angle = LF_Front_back
    return LF_Front_back


def Leg_LF_Back():
    global LF_Front_back
    LF_Front_back = LF_Front_back + 1
    kit.servo[2].angle = LF_Front_back
    return LF_Front_back


def Leg_LF_Clockwise():
    global LF_Spin
    LF_Spin = LF_Spin + 1
    kit.servo[1].angle = LF_Spin
    return LF_Spin

def Leg_LF_Counterclockwise():
    global LF_Spin
    LF_Spin = LF_Spin - 1
    kit.servo[1].angle = LF_Spin
    return LF_Spin
# Obsługa noga lewy przód

# Obsługa noga lewy tył
def Leg_LB_Abduction():
    global LB_Abduction
    LB_Abduction = LB_Abduction + 1
    kit1.servo[4].angle = LB_Abduction
    return LB_Abduction 

def Leg_LB_Adduction():
    global LB_Abduction
    LB_Abduction = LB_Abduction - 1
    kit1.servo[4].angle = LB_Abduction
    return LB_Abduction 
 
def Leg_LB_Front():
    global LB_Front_back
    LB_Front_back = LB_Front_back - 1
    kit1.servo[3].angle = LB_Front_back
    return LB_Front_back


def Leg_LB_Back():
    global LB_Front_back
    LB_Front_back = LB_Front_back + 1
    kit1.servo[3].angle = LB_Front_back
    return LB_Front_back

def Leg_LB_Clockwise():
    global LB_Spin
    LB_Spin = LB_Spin + 1
    kit1.servo[2].angle = LB_Spin
    return LB_Spin

def Leg_LB_Counterclockwise():
    global LB_Spin
    LB_Spin = LB_Spin - 1
    kit1.servo[2].angle = LB_Spin
    return LB_Spin
# Obsługa noga lewy tył

# Obsługa noga prawy tył
def Leg_RB_Abduction():
    global RB_Abduction
    RB_Abduction = RB_Abduction - 1
    kit1.servo[7].angle = RB_Abduction
    return RB_Abduction 

def Leg_RB_Adduction():
    global RB_Abduction
    RB_Abduction = RB_Abduction + 1
    kit1.servo[7].angle = RB_Abduction
    return RB_Abduction 
 
def Leg_RB_Front():
    global RB_Front_back
    RB_Front_back = RB_Front_back + 1
    kit1.servo[6].angle = RB_Front_back
    return RB_Front_back


def Leg_RB_Back():
    global RB_Front_back
    RB_Front_back = RB_Front_back - 1
    kit1.servo[6].angle = RB_Front_back
    return RB_Front_back


def Leg_RB_Clockwise():
    global RB_Spin
    RB_Spin = RB_Spin + 1
    kit1.servo[5].angle = RB_Spin
    return RB_Spin

def Leg_RB_Counterclockwise():
    global RB_Spin
    RB_Spin = RB_Spin - 1
    kit1.servo[5].angle = RB_Spin
    return RB_Spin
# Obsługa noga prawy tył

# Obsługa koła
def Forward():
    mc1.set_speed(1, 800)
    mc1.set_speed(2, -800)
    mc2.set_speed(1, 800)
    mc2.set_speed(2, -800)
    time.sleep(0.5)

def Reverse():
    mc1.set_speed(1, -800)
    mc1.set_speed(2, 800)
    mc2.set_speed(1, -800)
    mc2.set_speed(2, 800)
    time.sleep(0.5)

def Right():
    mc1.set_speed(1, 800)
    mc1.set_speed(2, 800)
    mc2.set_speed(1, 800)
    mc2.set_speed(2, 800)
    time.sleep(0.5)

def Left():
    mc1.set_speed(1, -800)
    mc1.set_speed(2, -800)
    mc2.set_speed(1, -800)
    mc2.set_speed(2, -800)
    time.sleep(0.5)
# Obsługa koła

# Kamera
def Camera():
    cap = cv2.VideoCapture('/dev/video0', cv2.CAP_V4L)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 2560)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1440)
    ret, frame = cap.read()
    cv2.imwrite('image.jpg', frame)
    cap.release()
# Kamera

def main():

    global root
    root = tk.Tk()
    root.title("Wheeldog")

    # Obsługa tułowia przyciski
    labelframe1 = tk.LabelFrame(root, text="Base", padx=10, pady=10) 
    labelframe1.grid(row=0, column=0, padx=20, pady=20)

    frame = tk.Frame(root)
    frame.grid(row=0, column=0, padx=20, pady=20)

    button1 = tk.Button(labelframe1, text="Base Left", command=Base_Left)
    button1.grid(row=0, column=0, padx=10)

    button2 = tk.Button(labelframe1, text="Base Right", command=Base_Right)
    button2.grid(row=0, column=1, padx=10)

    button3 = tk.Button(labelframe1, text="Base Up", command=Base_Up)
    button3.grid(row=1, column=0, pady=10)

    button4 = tk.Button(labelframe1, text="Base Down", command=Base_Down)
    button4.grid(row=1, column=1, pady=10)

    button5 = tk.Button(labelframe1, text="Base Clockwise", command=Base_Spin_Clockwise)
    button5.grid(row=2, column=0, columnspan=2, pady=10)

    button6 = tk.Button(labelframe1, text="Base Counterclockwise", command=Base_Spin_Counterclockwise)
    button6.grid(row=3, column=0, columnspan=2, pady=10)
    # Obsługa tułowia przyciski

    #Obsługa noga prawy przód
    labelframe2 = tk.LabelFrame(root, text="Leg Right Front", padx=10, pady=10) 
    labelframe2.grid(row=0, column=5, padx=20, pady=20)

    button7 = tk.Button(labelframe2, text="RF Abduction", command=Leg_RF_Abduction)
    button7.grid(row=0, column=5, padx=10) 

    button8 = tk.Button(labelframe2, text="RF Adduction", command=Leg_RF_Adduction)
    button8.grid(row=0, column=6, padx=10)

    button9 = tk.Button(labelframe2, text="RF Front", command=Leg_RF_Front)
    button9.grid(row=1, column=5, pady=10) 

    button10 = tk.Button(labelframe2, text="RF Back", command=Leg_RF_Back)
    button10.grid(row=1, column=6, pady=10)  


    button11 = tk.Button(labelframe2, text="RF Clockwise", command=Leg_RF_Clockwise)
    button11.grid(row=2, column=5, pady=10) 

    button12 = tk.Button(labelframe2, text="RF Counterclockwise", command=Leg_RF_Counterclockwise)
    button12.grid(row=2, column=6, pady=10)
    #Obsługa noga prawy przód

    #Obsługa noga lewy przód
    labelframe3 = tk.LabelFrame(root, text="Leg Left Front", padx=10, pady=10) 
    labelframe3.grid(row=0, column=3, padx=20, pady=20)

    button13 = tk.Button(labelframe3, text="LF Abduction", command=Leg_LF_Abduction)
    button13.grid(row=0, column=3, padx=10) 

    button14 = tk.Button(labelframe3, text="LF Adduction", command=Leg_LF_Adduction)
    button14.grid(row=0, column=4, padx=10)

    button14 = tk.Button(labelframe3, text="LF Front", command=Leg_LF_Front)
    button14.grid(row=1, column=3, pady=10) 

    button15 = tk.Button(labelframe3, text="LF Back", command=Leg_LF_Back)
    button15.grid(row=1, column=4, pady=10)  


    button16 = tk.Button(labelframe3, text="LF Clockwise", command=Leg_LF_Clockwise)
    button16.grid(row=2, column=3, pady=10) 

    button17 = tk.Button(labelframe3, text="LF Counterclockwise", command=Leg_LF_Counterclockwise)
    button17.grid(row=2, column=4, pady=10)
    #Obsługa noga lewy przód

    #Obsługa noga lewy tył
    labelframe4 = tk.LabelFrame(root, text="Leg Left Back", padx=10, pady=10) 
    labelframe4.grid(row=4, column=3, padx=20, pady=20)

    button18 = tk.Button(labelframe4, text="LB Abduction", command=Leg_LB_Abduction)
    button18.grid(row=4, column=3, padx=10) 

    button19 = tk.Button(labelframe4, text="LB Adduction", command=Leg_LB_Adduction)
    button19.grid(row=4, column=4, padx=10)

    button20 = tk.Button(labelframe4, text="LB Front", command=Leg_LB_Front)
    button20.grid(row=5, column=3, pady=10) 

    button21 = tk.Button(labelframe4, text="LB Back", command=Leg_LB_Back)
    button21.grid(row=5, column=4, pady=10)  


    button22 = tk.Button(labelframe4, text="LB Clockwise", command=Leg_LB_Clockwise)
    button22.grid(row=6, column=3, pady=10) 

    button23 = tk.Button(labelframe4, text="LB Counterclockwise", command=Leg_LB_Counterclockwise)
    button23.grid(row=6, column=4, pady=10)
    #Obsługa noga lewy tył

    #Obsługa noga prawy tył
    labelframe5 = tk.LabelFrame(root, text="Leg Right Back", padx=10, pady=10) 
    labelframe5.grid(row=4, column=5, padx=20, pady=20)

    button24 = tk.Button(labelframe5, text="RB Abduction", command=Leg_RB_Abduction)
    button24.grid(row=4, column=5, padx=10) 

    button25 = tk.Button(labelframe5, text="RB Adduction", command=Leg_RB_Adduction)
    button25.grid(row=4, column=6, padx=10)

    button26 = tk.Button(labelframe5, text="RB Front", command=Leg_RB_Front)
    button26.grid(row=5, column=5, pady=10) 

    button27 = tk.Button(labelframe5, text="RB Back", command=Leg_RB_Back)
    button27.grid(row=5, column=6, pady=10)  


    button28 = tk.Button(labelframe5, text="RB Clockwise", command=Leg_RB_Clockwise)
    button28.grid(row=6, column=5, pady=10) 

    button29 = tk.Button(labelframe5, text="RB Counterclockwise", command=Leg_RB_Counterclockwise)
    button29.grid(row=6, column=6, pady=10)
    #Obsługa noga prawy tył

    #Obsługa koła
    labelframe6 = tk.LabelFrame(root, text="Driving", padx=10, pady=10) 
    labelframe6.grid(row=4, column=0, padx=20, pady=20)

    button30 = tk.Button(labelframe6, text="Forward", command=Forward)
    button30.grid(row=4, column=0, columnspan=2, padx=10) 

    button31 = tk.Button(labelframe6, text="Right", command=Right)
    button31.grid(row=5, column=1, padx=10)

    button32 = tk.Button(labelframe6, text="Left", command=Left)
    button32.grid(row=5, column=0, pady=10)

    button33 = tk.Button(labelframe6, text="Reverse", command=Reverse)
    button33.grid(row=6, column=0, columnspan=2, pady=10) 
    #Obsługa koła

    #Obsługa kamery
    labelframe7 = tk.LabelFrame(root, text="Camera", padx=10, pady=10) 
    labelframe7.grid(row=7, column=0, padx=20, pady=20)

    button34 = tk.Button(labelframe7, text="Take a photo", command=Camera)
    button34.grid(row=7, column=0, columnspan=2, padx=10) 

    #Obsługa kamery

    root.mainloop()


if __name__ == "__main__":
    main()