from gui import Application
from linkedin_search import search
import tkinter as tk

root = tk.Tk()
app = Application(master=root)
app.mainloop()

f = open("lastStored.txt", "r")
firstName = f.readline().strip('\n')
lastName = f.readline().strip('\n')
email = f.readline().strip('\n')
linkedIn = f.readline().strip('\n')
area1 = f.readline().strip('\n')
area2 = f.readline().strip('\n')
area3 = f.readline().strip('\n')
anything = f.readline().strip('\n')
f.close()

print("INFORMATION OBTAINED FROM LINKEDIN")
university, grad_yr, yrs_experience = search(linkedIn)

print()
print("=========================== SUMMARY ===========================")
print("First Name:\t\t\t\t\t", firstName)
print("Last Name:\t\t\t\t\t", lastName)
print("Email:\t\t\t\t\t\t", email)
print("LinkedIn:\t\t\t\t\t", linkedIn)
print("Area 1:\t\t\t\t\t\t", area1)
print("Area 2:\t\t\t\t\t\t", area2)
print("Area 3:\t\t\t\t\t\t", area3)
print("Anything Else:\t\t\t\t", anything)
print("University:\t\t\t\t\t", university)
print("Undergrad Graduation Year:\t", grad_yr)
print("Years of Experience:\t\t", yrs_experience)