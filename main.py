#########################################################################
#Author: Uinter								#	
#Date: xx/xx/xxxx							#	
#version: 0.01								#		
#Flashcard learning							#
#App to make flashcards store them and test them			#
#########################################################################

from tkinter import *


DEFAULT_BUTTON_FONT = ('Ubuntu', 25)


class SampleApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.switch_frame(Acceuil)
        #prevent from stretching
        self.resizable(0, 0)
        self.title("Flashcards learning v:0.01")
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class Acceuil(Frame):
	"""The main window where the user can choose whenever he wants to go"""
	def __init__(self, master):
		Frame.__init__(self, master)

        #Set geometry  
		master.geometry("400x300")
		#Labels      
		Label(self, text="Flashcards", font=('Ubuntu',50)).pack()
		Button(self, text="Create flashcard", font=DEFAULT_BUTTON_FONT, command=lambda: master.switch_frame(CreateFlashcard)).pack()
		Button(self, text="Your library", font=DEFAULT_BUTTON_FONT, command=lambda: master.switch_frame(Library)).pack()
		Button(self, text="Do a test", font=DEFAULT_BUTTON_FONT, command=lambda: master.switch_frame(Test)).pack()
		Button(self, text="Exit", font=DEFAULT_BUTTON_FONT, command=master.destroy).pack()


class CreateFlashcard(Frame):
	def __init__(self, master):
		Frame.__init__(self, master)

		#set geometry
		master.geometry('1000x800')

		#flashcard entry
		flashcard_var = StringVar()
		textBg = 'turquoise1'  # color of flashcard
		textFont = ('Ubuntu', 15)  # font of flashcard no resizable
		T1 = Text(self, bd=1, bg=textBg, font=textFont,width= 50)
		T1.grid(row=0, column=0) # sticky by default on the middle

		#question flashcard
		btn1 = Button(self, text="Question", font=DEFAULT_BUTTON_FONT, command=None) # if answer change question
		btn1.grid(row=1, column=0,sticky=W)
		
		#answer flashcard
		btn2 = Button(self, text="Reponse", font=DEFAULT_BUTTON_FONT, command=None) # if question change answer
		btn2.grid(row=1, column=1,sticky=W)

		#add to repository
		btn3 = Button(self, text='Add', font=DEFAULT_BUTTON_FONT, command=None)
		btn3.grid(row=2, column=0, sticky=W)

		#return to lobby
		btn4 = Button(self, text="Return", font=DEFAULT_BUTTON_FONT, command=lambda: master.switch_frame(Acceuil))
		btn4.grid(row=2, column=1, sticky=W)


class Library(Frame):
	def __init__(self, master):
		Frame.__init__(self, master)

		#set geometry
		master.geometry('400x300')
		Button(self, text="Return", font=DEFAULT_BUTTON_FONT, command=lambda: master.switch_frame(Acceuil)).pack()


class Test(Frame):
	def __init__(self, master):
		Frame.__init__(self, master)

		#set geometry
		master.geometry('400x300')
		Button(self, text="Return", font=DEFAULT_BUTTON_FONT, command=lambda: master.switch_frame(Acceuil)).pack()


if __name__ == '__main__':
	app = SampleApp()
	app.mainloop()

