# Learn Python - Lesson 0
### Expected time: 20 min 
### Objectives:
1. Setup Python and Visual Studio Code (VSC)
    1. Download and install Python
        1. Windows
        2. Ubuntu
    2. Download and install VSC
    3. Create Python profile in VSC
    4. Clone **Learn Python** repository
    5. Setup virtual enviroment
    6. Install required packages
2. Be introduced to this course
### About:
This chapter will attempt to get you set up as fast as possible so you can start learning Python programming. We will touch upon many concepts without overly focusing on them such us virtual enviroment, source control, PEP8 coding standard and others, some only mentioned in passing. Most of these tools/ concepts will be elaborated on in subsequent lessons. I have decided to do it this way, because the utility of them is too high to avoid even at the begining, but spending too much time on them would be too tedious and would keep us away from what I consider more fun, the actual coding.

By the end of this chapter. All the tools we will need in upcomming chapters should be setup and we will be able to get to the fun stuff.

## 1.1.1. Download and Install Python (Windows)

**Download Python:**
- Open a web browser and go to the official Python website: [python.org/downloads](https://www.python.org/downloads/).
- You'll see the latest version of Python displayed prominently. Make sure to download the **Python 3.x** version (e.g., Python 3.10, Python 3.11).
![Downloading latest verison of Python](https://github.com/Dvorkam/LearnPython/blob/lesson0/lesson0/assets/python_download.PNG)   

**Install Python:**
- Double-click the installer to run it.
- During the installation process, you'll come across a checkbox that says "Add python.exe to PATH. Red circle in image below" Make sure this checkbox is checked. This will allow you to use Python from the command line without specifying its full path. If you have an earlier version of Python installed, you will instead be offered an upgrade).
![Installing latest verison of Python](https://github.com/Dvorkam/LearnPython/blob/lesson0/lesson0/assets/install_python.png) 
- Complete the installation by following the on-screen instructions. The default settings are usually sufficient.

**Verify the Installation:**
- Opening a command prompt or terminal window for example by
    - press WIN + R
    - type cmd
    - press enter
- or
    - click start button
    - type Command Prompt
    - select Command Prompt

- Type the following command and press Enter:
```
python --version
```
- Confirm the version matches the version of python you downloaded in step 1
```
C:\Users\User>python --version
Python 3.11.5
```
- If not, your python installation has not been added to PATH at which point I suggest to uninstall python and try again from step 2

## 1.1.2 Download and Install Python (Ubuntu WIP)
**Open Terminal:**
- Press `Ctrl` + `Alt` + `T` to open the Terminal.

**Update Package Lists:**

- Before installing any software, it's a good idea to update the package lists to ensure you're getting the latest version. Enter the following commands in the terminal:
```
sudo apt update
sudo apt upgrade
```
**Install Python:**

Ubuntu typically comes with Python pre-installed. However, it's a good practice to install the latest version and pip (Python's package manager). Enter the following command to install Python 3 and pip:

```
sudo apt install python3 python3-pip python3-venv python3-pytest
```

* **Verify the Installation:**

- Once the installation is complete, you can verify that Python was installed successfully by typing:

```
python3 --version
```

- You should see the version of Python you installed printed to the screen (e.g., "Python 3.9.6").
## 1.2 

## 1.5. Setup Virtual Environment

A virtual environment is a self-contained space where you can install Python packages separately from your system's Python installation. This helps prevent conflicts between different projects that might require different package versions. We'll use the built-in `venv` module to create a virtual environment for your project.

I. **Open a Terminal:**

   - On Windows, open the Command Prompt or PowerShell.
   - On macOS or Linux, open the Terminal.

II. **Navigate to Your Project Folder:**

   - Use the `cd` command to navigate to the folder where you want to create your project and virtual environment.
   - alternatively 

3. **Create a Virtual Environment:**

   - To create a virtual environment named `venv`, enter the following command:

     ```
     python -m venv venv
     ```

     This will create a folder named `venv` in your project directory to hold your virtual environment.

   {Image: Create-Virtual-Environment}

4. **Activate the Virtual Environment:**

   - On Windows, activate the virtual environment using this command:

     ```
     venv\Scripts\activate
     ```

   - On macOS and Linux, use this command:

     ```
     source venv/bin/activate
     ```

   When the virtual environment is activated, your command prompt will change to show the name of the virtual environment. This indicates that you're now working within the isolated environment.

   {Image: Activate-Virtual-Environment}

5. **Deactivate the Virtual Environment:**

   - To exit the virtual environment and return to your system's Python, simply enter the command:

     ```
     deactivate
     ```

   The virtual environment will be deactivated, and you'll return to the global Python environment.

   {Image: Deactivate-Virtual-Environment}

Creating and using virtual environments is essential for maintaining a clean and organized development environment. In the next step, we'll install the required packages for your project within this virtual environment.

