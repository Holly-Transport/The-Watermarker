from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont

# ---------------------------- CONSTANTS ------------------------------- #
WHITE = "white"
BLUE = "#5eaaa8"
FONT_NAME = "Courier"

# ---------------------------- FUNCTIONS ----------------------- #

def upload():
    filename = filedialog.askopenfilename()
    IMG = Image.open(filename)
    width, height = IMG.size

    draw = ImageDraw.Draw(IMG)
    text = text_input.get()
    font = ImageFont.truetype("Raleway-Black.ttf",100)
    textwidth, textheight = draw.textsize(text, font)

    margin = 10
    x = width - textwidth - margin
    y = height - textheight - margin
    draw.text((x, y), text, font=font)
    IMG.show()
    IMG.save('watermark.jpg')


# ---------------------------- UI SETUP ------------------------------- #

# Set up Window
window = Tk()
window.title ("The Watermarker")
window.minsize(width = 200, height = 250)
window.config(background = BLUE, padx=100, pady=10, bg = BLUE)

# Labels
label_status = Label(text = "The Watermarker", font = ("Courier", 56), foreground = WHITE, background = BLUE, pady=30)
label_status.grid(column=2, row = 1)

label_guide = Label(text = "Please enter watermark text, below.\nAfter selecting file, watermarked image will be saved as\n'watermark.jpg' in this directory.\n", font = ("Courier", 20), foreground = WHITE, background = BLUE)
label_guide.grid(column=2, row = 2)

# Buttons and Inputs
text_input = Entry(width = 35)
text_input.grid(column= 2, row = 4, columnspan = 2)
text_input.focus()

button_upload = Button(text="Let's Watermark!", font = ("Courier", 20), command=upload)
button_upload.grid(column=2, row = 5, pady=(50,50))

# ---------------------------- APP ------------------------------- #

window.mainloop()

