# Python Virtual Environment (virtualenv)

- [Python Virtual Environment (virtualenv)](#python-virtual-environment-virtualenv)
	- [1. Introduction:](#1-introduction)
	- [2. Overview:](#2-overview)
	- [3. Installation:](#3-installation)
	- [4. Creating Virtual Environments:](#4-creating-virtual-environments)
	- [5. Activating the Virtual Environment:](#5-activating-the-virtual-environment)
	- [6. Installing python requirements:](#6-installing-python-requirements)
	- [7. Deactivating the Virtual Environment:](#7-deactivating-the-virtual-environment)
	- [Additional Resources:\*\*](#additional-resources)



## 1. Introduction:

This documentation serves as a guide to using Python Virtual Environment (virtualenv). Python Virtual Environment simplifies managing project dependencies by creating isolated environments.

## 2. Overview:
   
Python Virtual Environment is a tool that helps manage multiple Python projects by creating isolated environments for each, preventing conflicts between project dependencies.

     - Isolation of project dependencies.
     - Easy installation and management of project-specific packages.
     - Facilitates version control of Python and its libraries.

## 3. Installation:

Make sure that your are using Python (preferably Python 3.3 or newer) and have Pip (Python package installer) installed in your system.

   - **Installation Steps:**
     ```bash
     pip install virtualenv
     ```

## 4. Creating Virtual Environments:

We strongly recommend creating a virtualenv to execute and maintain the `imfect`` project.

   - **Command:**
     ```bash
     virtualenv re_imfect
     ```

## 5. Activating the Virtual Environment:

When you activate your virtual environment, your local environment changes the python binaries that from of your system to the local virtual environment. This step is necessary to garantee that you are using the correct modules and version required to run this project.

   - **On Unix or MacOS:**
     ```bash
     source re_imfect/bin/activate
     ```


   - **On Windows:**
     ```bash
     .\env\Scripts\activate
     ```

   - **Activated Environment:**
     - The command prompt should change, indicating the active virtual environment.

## 6. Installing python requirements:

This step is responsible for installing all the required dependencies, packages, and modules that the project uses.
First make sure that you are using the virtualenv python

   - **Which Python?**
   	 ```bash
	 which python3
	 ```

   - The results should be something in the lines of `/home/.../re_imfect/bin/python3`

   - **Usage:**
     - Install: 
     ```bash 
     pip install -r requirements.txt
     ```


## 7. Deactivating the Virtual Environment:

Deactivating the virtualend allows you to use the system default python3 binaries.

   - **on Linux:**
     ```bash
     deactivate
     ```
   - **Notes:**
     - Returns to the global Python environment.
     - The command prompt should revert to its original state.

   - **Which Python?**
   	 ```bash
	 which python3
	 ```

   - The result now should be `/usr/bin/python3`

## Additional Resources:**
Additional documentation can be foudn in the [Official Documentation](https://virtualenv.pypa.io/en/latest/).
