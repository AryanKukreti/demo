import matplotlib.pyplot as plt
from tkinter import Tk, filedialog

def get_image_path():
    """Open a file dialog and return the selected image path."""
    root = Tk()
    root.withdraw()  # Hide the main tkinter window
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff")]
    )
    return file_path

def onclick(event, image_array, starting_point):
    """Callback function for user to select starting point."""
    if event.xdata is not None and event.ydata is not None:
        x, y = int(event.xdata), int(event.ydata)
        if image_array[y, x] < 60:
            print("Sorry, but you can't make the irrigation over the ditch.")
        else:
            starting_point[0] = x
            starting_point[1] = y
            print(f"Selected Starting Point: {starting_point}")
            plt.close()  # Close plot once the point is selected
