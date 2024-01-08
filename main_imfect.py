
import tkinter as tk
from dev.gui import gui as gui 

# ========================================================================== GUI
def initialize_gui():
    root = tk.Tk()
    app = gui.GUI( root )
    return root

# ========================================================================= Main
def main() -> None:
    root = initialize_gui()
    root.mainloop()

if __name__ == "__main__":
    main()
