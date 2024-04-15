import os
from time import sleep
import pyautogui as auto
from GUI import Gui

def main(msg, *args):
    for i in args:
        print(i)
        PhoneNumber = 966000000000 + int(i)
        url = f'https://web.whatsapp.com/send?phone={str(PhoneNumber)}&text={msg}'
        os.startfile(url)
        sleep(15)
        auto.press("Enter")

    print("Done")


def Sender():
    def buttonFunc():
        Numbers = str(phone.get()).split()
        main(msg.get(), *Numbers)

    SendToEveyOne_Menu = Gui("Sender")
    msg_Label = SendToEveyOne_Menu.make_label("Enter your message here:-",0,0)
    msg = SendToEveyOne_Menu.make_input_Field(1,0)
    msg_Label = SendToEveyOne_Menu.make_label("Enter your the list of your phone numbers at this form '05xxxxxxxx 05xxxxxxxx ...':-",2,0)
    phone = SendToEveyOne_Menu.make_input_Field(3,0)
    Button = SendToEveyOne_Menu.make_button("Send",buttonFunc,4,0)

    SendToEveyOne_Menu.run()