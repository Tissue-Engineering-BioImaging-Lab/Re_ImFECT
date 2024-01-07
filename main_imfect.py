import tkinter as tk
from tkinter import filedialog


class ParameterGUI:

    def __init__(self, master) -> None:
        self.master = master
        self.master.title("Texture Analysis Program\nIMFECT Project")

        # =========================================================== Parameters
        self.angle_parameter = tk.Label(master, text="Angle:")
        self.angle_scale = tk.Scale(
            master, from_=0, to=90, resolution=15, orient=tk.HORIZONTAL)

        self.bit_depth_parameter = tk.Label(master, text="Bit Depth:")
        self.bit_depth_scale = tk.Scale(
            master, from_=0, to=16, resolution=2,  orient=tk.HORIZONTAL)

        # =========================================================== Checkboxes
        self.glcm_var = tk.IntVar()
        self.glcm_checkbox = tk.Checkbutton(
            master, text="GLCM", variable=self.glcm_var)

        self.gldm_var = tk.IntVar()
        self.gldm_checkbox = tk.Checkbutton(
            master, text="GLDM", variable=self.gldm_var)

        self.glrlm_var = tk.IntVar()
        self.glrlm_checkbox = tk.Checkbutton(
            master, text="GLRLM", variable=self.glrlm_var)

        self.glszm_var = tk.IntVar()
        self.glszm_checkbox = tk.Checkbutton(
            master, text="GLSZM", variable=self.glszm_var)

        self.ngltdm_var = tk.IntVar()
        self.ngtdm_checkbox = tk.Checkbutton(
            master, text="NGTDM", variable=self.ngltdm_var)

        # ========================================================= Folder Paths
        self.folder_label = tk.Label(master, text="Image Folder:")
        self.folder_button = tk.Button(
            master, text="Browse", command=self.browse_folder)

        self.results_label = tk.Label(master, text="Result Folder:")
        self.results_button = tk.Button(
            master, text="Browse", command=self.browse_results_folder)

        # ======================================================= Execute Button
        self.execute_button = tk.Button(
            master, text="Run", command=self.submit_params)
        # ======================================================== Submit Button
        self.exit_button = tk.Button(
            master, text="Exit", command=self.exit_program)

        # ========================================================== Grid Layout
        self.angle_parameter.grid(row=0, column=0, padx=10, pady=10)
        self.angle_scale.grid(row=0, column=1, padx=10, pady=10)

        self.bit_depth_parameter.grid(row=1, column=0, padx=10, pady=10)
        self.bit_depth_scale.grid(row=1, column=1, padx=10, pady=10)

        self.glcm_checkbox.grid(row=3, column=0, padx=10, pady=10)
        self.gldm_checkbox.grid(row=3, column=1, padx=10, pady=10)
        self.glrlm_checkbox.grid(row=4, column=0, padx=10, pady=10)
        self.glszm_checkbox.grid(row=4, column=1, padx=10, pady=10)
        self.ngtdm_checkbox.grid(row=5, column=0, padx=10, pady=10)

        self.folder_label.grid(row=7, column=0, padx=10, pady=10)
        self.folder_button.grid(row=7, column=1, padx=10, pady=10)

        self.results_label.grid(row=8, column=0, padx=10, pady=10)
        self.results_button.grid(row=8, column=1, padx=10, pady=10)

        self.execute_button.grid(row=10, column=0, columnspan=2, pady=20)
        self.exit_button.grid(row=10, column=1, columnspan=2, pady=20)

    # ===================================================== Folder Finder Button
    def browse_folder(self) -> None:
        folder_path: str = filedialog.askdirectory()
        print("Image Folder:", folder_path)

    def browse_results_folder(self) -> None:
        results_folder_path: str = filedialog.askdirectory()
        print("Results Folder:", results_folder_path)

    # ============================================================== Exit Button
    def exit_program(self) -> None:
        return exit(code=0)

    # =============================================================== Run Button
    def submit_params(self) -> None:
        angle_value: float = self.angle_scale.get()
        bith_depth_value: float = self.bit_depth_scale.get()
        glcm_selected: int = self.glcm_var.get()
        gldm_selected: int = self.gldm_var.get()
        glrlm__selected: int = self.glrlm_var.get()
        glszm_selected: int = self.glszm_var.get()
        ngltdm_selected: int = self.ngltdm_var.get()

        print("angle-value: ", angle_value)
        print("bith-depth value: ", bith_depth_value)
        print("glcm method: ", glcm_selected)
        print("gldm method: ", gldm_selected)
        print("glrlm method: ", glrlm__selected)
        print("glszm method: ", glszm_selected)
        print("ngltdm method: ", ngltdm_selected)

# ========================================================================= Main


def main():
    root = tk.Tk()
    app = ParameterGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
