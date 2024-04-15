from os import startfile
from GUI import Gui

def writeOneFile(numberOfMembers):
    data = str(numberOfMembers)

    file_name = open("../arg.txt",'w+')

    file_name.write(data)
    file_name.close()
    print(f"Number 5 has been written to '{file_name}' file.")


def Mention():
    def Mentioning():
        Group_Members = InputField.get()
        writeOneFile(Group_Members)
        startfile("Process.exe")


    Mentionor = Gui("Mention @Everyone")
    Mentionor.make_label("Number of group Members",0,0)
    InputField = Mentionor.make_input_Field(1,0)
    Mentionor.make_button("Send !",Mentioning,2,0)
    Mentionor.run()






# writeOneFile(50)

# startfile("Process.exe")