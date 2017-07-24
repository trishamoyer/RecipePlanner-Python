# Huge shoutout to youtube user: sentdex at https://www.youtube.com/watch?v=jBUpjijYtCk which
# helped me figure out how to do multiple pages with tkinter

from tkinter import *
from addRecipe import addARecipe
from mealPlan import makeMealPlan
from firstpage import firstPage

LARGE_FONT=("Verdana", 24)
MEDIUM_FONT=("Verdana", 12)


class mealPlanner(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for my_frame in (firstPage, addARecipe, makeMealPlan):
            frame = my_frame(container, self)
            self.frames[my_frame] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(firstPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

app = mealPlanner()
app.maxsize(1000,6000)
app.minsize(1000,600)
app.mainloop()