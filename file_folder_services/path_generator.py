from tkinter import Tk
from tkinter import filedialog


def get_folder_path(
        title_message: str):
    root = \
        Tk()

    root.withdraw()

    folder_path = \
        filedialog.askdirectory(
            parent=root,
            initialdir="/",
            title=title_message)

    return \
        folder_path
