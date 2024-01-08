import tkinter as tk
from tkinter import ttk, filedialog
from ttkthemes import ThemedTk

from dev.lib.matrixCalc.matrixGLCM import calc_glcm
from dev.lib.metricCalc.glcmMetrics import calcGLCMMetrics

from dev.lib.matrixCalc.matrixGLDM import calc_gldm
from dev.lib.metricCalc.gldmMetrics import calcGLDMMetrics

from dev.lib.matrixCalc.matrixGLRLM import calc_glrlm
from dev.lib.metricCalc.glrlmMetrics import calcGLRLMMetrics

from dev.lib.matrixCalc.matrixGLSZM import calc_glszm
from dev.lib.metricCalc.glszmMetrics import calcGLSZMMetrics

from dev.lib.matrixCalc.matrixNGTDM import calc_ngtdm
from dev.lib.metricCalc.ngtdmMetrics import calcNGTDMMetrics


case_conditions: dict[ str, tuple ] = {
    "glcm": ( calc_glcm, calcGLCMMetrics ),
    "gldm": ( calc_gldm, calcGLDMMetrics ),
    "glrlm": ( calc_glrlm, calcGLRLMMetrics ),
    "glszm": ( calc_glszm,calcGLSZMMetrics ), 
    "ngltdm ": ( calc_ngtdm, calcNGTDMMetrics )
}

class GUI:

    def __init__(self, master) -> None:

        self.master = master
        self.master.title("Texture Analysis Program\nIMFECT Project")
        self.padx = 15
        self.pady = 15
        
        # Apply a themed style
        self.style = ttk.Style()
        self.style.theme_use(themename="clam")  # You can change the theme name

        self.glcm_var = tk.IntVar()
        self.glcm_checkbox = None
        self.gldm_var = tk.IntVar()
        self.gldm_checkbox = None
        self.glrlm_var = tk.IntVar()
        self.glrlm_checkbox = None
        self.glszm_var = tk.IntVar()
        self.glszm_checkbox = None
        self.ngltdm_var = tk.IntVar()
        self.ngltdm_checkbox = None

        self.image_folder_path = "./images"
        self.results_folder_path = "./results"

        self.create_parameters_section()
        self.create_checkboxes_section()
        self.create_folder_paths_section()
        self.create_buttons_section()
    # ========================================================= Parameter Slider
        
    def create_parameters_section(self) -> None:

        ttk.Label(
            self.master,
            text="Angle:"
        ).grid(
            row=0,
            column=0,
            padx=self.padx,
            pady=self.pady
        )

        self.angle_scale = tk.Scale(
            self.master,
            from_=0,
            to=90,
            resolution=15,
            orient=tk.HORIZONTAL
        )
        
        self.angle_scale.grid(
            row=0,
            column=1,
            padx=10,
            pady=10
        )

        ttk.Label(
            self.master,
            text="Bit Depth:"
        ).grid(
            row=1,
            column=0,
            padx=self.pady,
            pady=self.pady
        )

        self.bit_depth_scale = tk.Scale(
            self.master,
            from_=0,
            to=16,
            resolution=2,
            orient=tk.HORIZONTAL
        )

        self.bit_depth_scale.grid(
            row=1,
            column=1,
            padx=10,
            pady=10
        )

    # =============================================================== Checkboxes

    def create_checkboxes_section(self) -> None:

        self.glcm_checkbox = ttk.Checkbutton(
            self.master, 
            text="GLCM", 
            variable=self.glcm_var
        ).grid(
            row=2,
            column=0,
            padx=self.padx,
            pady=self.pady
        )
        
        self.gldm_checkbox = ttk.Checkbutton(
            self.master, 
            text="GLDM", 
            variable=self.gldm_var
        ).grid(
            row=2,
            column=1,
            padx=self.padx,
            pady=self.pady
        )

        self.glrlm_checkbox = ttk.Checkbutton(
            self.master, 
            text="GLRLM", 
            variable=self.glrlm_var
        ).grid(
            row=2,
            column=2,
            padx=self.padx,
            pady=self.pady
        )

        self.glszm_checkbox = ttk.Checkbutton(
            self.master, 
            text="GLSZM", 
            variable=self.glszm_var
        ).grid(
            row=3,
            column=1,
            padx=self.padx,
            pady=self.pady
        )

        self.ngltdm_checkbox = ttk.Checkbutton(
            self.master, 
            text="NGTDM", 
            variable=self.ngltdm_var
        ).grid(
            row=3,
            column=0,
            padx=self.padx,
            pady=self.pady
        )

    # ================================================================== Folders
        
    def create_folder_paths_section(self) -> None:
        
        ttk.Label(
            self.master,
            text="Image Folder:"
        ).grid(
            row=5,
            column=0,
            padx=self.padx,
            pady=self.pady
        )
        
        self.image_folder_button = ttk.Button(
            self.master,
            text="Browse",
            command=self.browse_image_folder
        )
        
        self.image_folder_button.grid(
            row=5,
            column=1,
            padx=10,
            pady=10
        )

        ttk.Label(
            self.master,
            text="Result Folder:"
        ).grid(
            row=6,
            column=0,
            padx=self.padx,
            pady=self.pady
        )
        
        self.results_button = ttk.Button(
            self.master,
            text="Browse",
            command=self.browse_results_folder
        )
        
        self.results_button.grid(
            row=6,
            column=1,
            padx=self.padx,
            pady=self.pady
        )

    # ============================================================ Browse Folder
        
    def browse_image_folder(self) -> None:

        self.image_folder_path: str = filedialog.askdirectory()

    def browse_results_folder(self) -> None:
        self.results_folder_path: str = filedialog.askdirectory()

    # ================================================================== Buttons
        
    def create_buttons_section(self) -> None:

        self.execute_button = ttk.Button(
            self.master,
            text="Run",
            command=self.submit_params
        )
        
        self.execute_button.grid(
            row=7,
            column=0,
            columnspan=2,
            pady=20
        )

        self.exit_button = ttk.Button(
            self.master,
            text="Exit",
            command=self.exit_program
        )
        
        self.exit_button.grid(
            row=7,
            column=1,
            columnspan=2,
            pady=20
        )

    # ===================================================================== Exit
        
    def exit_program(self) -> None:

        self.master.destroy()

    # ================================================================ Execution
        
    def submit_params(self) -> None:

        angle_value: float = self.angle_scale.get()
        bit_depth_value: float = self.bit_depth_scale.get()

        glcm_selected: int = self.glcm_var.get()
        gldm_selected: int = self.gldm_var.get()
        glrlm_selected: int = self.glrlm_var.get()
        glszm_selected: int = self.glszm_var.get()
        ngltdm_selected: int = self.ngltdm_var.get()

        print("angle-value:", angle_value)
        print("bit-depth value:", bit_depth_value)
        print("glcm method:", glcm_selected)
        print("gldm method:", gldm_selected)
        print("glrlm method:", glrlm_selected)
        print("glszm method:", glszm_selected)
        print("ngltdm method:", ngltdm_selected)
        
        print("Image Folder:", self.image_folder_path)
        print("Results Folder:", self.results_folder_path)

        methods_selected: dict[str, int] = {
            "glcm":glcm_selected, 
            "gldm":gldm_selected, 
            "glrlm":glrlm_selected, 
            "glszm":glszm_selected, 
            "ngltdm":ngltdm_selected 
        }

        # Case condition based on the value of the vars

        for key in list(case_conditions.keys()):
            matrix = case_conditions[key][0] if methods_selected[key] == 1 else None
            features = 