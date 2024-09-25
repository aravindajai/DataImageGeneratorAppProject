import tkinter as tk
from PIL import Image, ImageDraw, ImageFont

class DataImageGeneratorApp:
    def __init__(self, master):
        self.master = master
        master.title("Data Image Generator")

        self.label = tk.Label(master, text="Enter the Input:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.generate_button = tk.Button(master, text="Generate Image", command=self.generate_image)
        self.generate_button.pack()

    def generate_image(self):
        try:
            text_entered = str(self.entry.get())
            image_size = (400, 400)
            font_size = 80
        
            generate_number_image(text_entered, image_size,font_size)
        except ValueError:
            tk.messagebox.showerror("Error", "Please enter a valid input.")

def generate_number_image(text_entered, image_size=(400, 400), font_size=400):
    # Create a blank image with a white background
    image = Image.new("RGB", image_size, "white")

    # Initialize the drawing context
    draw = ImageDraw.Draw(image)

    # Use the default font
    font = ImageFont.load_default(font_size)

    # Convert the number to a string
    text = str(text_entered)

    # Calculate the position to center the text
    text_bbox = draw.textbbox((0, 0, image_size[0], image_size[1]), text, font)
    position = ((image_size[0] - text_bbox[2]) // 2, (image_size[1] - text_bbox[3]) // 2)

    # Draw the text on the image
    draw.text(position, text, font=font, fill='black')

    # Save or display the image
    image.save(f"Generated_Image_{text_entered}.png")
    image.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = DataImageGeneratorApp(root)
    root.mainloop()
