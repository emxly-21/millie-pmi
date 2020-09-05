from tkinter import *

variables = ["First Name", "Last Name", "Email", "LinkedIn"]

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Millie PMI")

        self.storedInfo = []
        self.create_widgets()

    def save(self):
        firstName = self.storedInfo[0].get()
        lastName = self.storedInfo[1].get()
        email = self.storedInfo[2].get()
        linkedIn = self.storedInfo[3].get()
        area1 = self.storedInfo[4].get()
        area2 = self.storedInfo[5].get()
        area3 = self.storedInfo[6].get()
        anything = self.storedInfo[7].get()
        list = [firstName, lastName, email, linkedIn, area1, area2, area3, anything]

        f = open("lastStored.txt", "w")
        for l in list:
            f.write(l)
            f.write('\n')
        f.close()

        self.master.destroy()

    def create_widgets(self):
        r = 0

        for var in variables:
            Label(text=var).grid(row=r, column=0, sticky=E)
            enteredText = StringVar()
            Entry(textvariable=enteredText).grid(row=r, column=1)
            self.storedInfo.append(enteredText)
            r += 1

        Label(text="3 areas you feel comfortable sharing your expertise in", justify=RIGHT, wraplength=120).grid(rowspan=3, column=0)
        for x in range(3):
            enteredText = StringVar()
            Entry(textvariable=enteredText).grid(row=r, column=1)
            self.storedInfo.append(enteredText)
            r += 1

        Label(text="Anything else").grid(row=r, column=0, sticky=E)
        enteredText = StringVar()
        Entry(textvariable=enteredText).grid(row=r, column=1)
        self.storedInfo.append(enteredText)
        r += 1

        submit = Button(text="Submit", command=self.save).grid(row=r, columnspan=2)