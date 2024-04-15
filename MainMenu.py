from GUI import Gui
from Sender import Sender
from mention import Mention


Main_Menu = Gui("WhatsApp Toolkit")

Main_Menu.make_button("Sender",Sender, 0,0)


Main_Menu.make_button("Mention Everyone",Mention, 0,1)



Main_Menu.run()