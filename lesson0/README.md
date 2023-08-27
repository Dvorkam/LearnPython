# Learn Python - Lesson 0
### Expected time: 20 min 
### Objectives:
1. Setup Python
    1. Download and install Python
    2. Setup virtual enviroment
    3. Install required packages
2. Setup Visual Studio Code
    1. Download and install VSC
    2. Create Python profile
    3. Clone **Learn Python** repository
3. Be introduced to this course
### About:
This chapter will attempt to get you set up as fast as possible so you can start learning Python programming. We will touch upon many concepts without overly focusing on them such us virtual enviroment, source control, PEP8 coding standard and others, some only mentioned in passing. Most of these tools/ concepts will be elaborated on in subsequent lessons. I have decided to do it this way, because the utility of them is too high to avoid even at the begining, but spending too much time on them would be too tedious and would keep us away from what I consider more fun, the actual coding.

By the end of this chapter. All the tools we will need in upcomming chapters should be setup and we will be able to get to the fun stuff.

## I. Download and Install Python

1. **Download Python:**
   - Open a web browser and go to the official Python website: [python.org/downloads](https://www.python.org/downloads/).
   - You'll see the latest version of Python displayed prominently. Make sure to download the **Python 3.x** version (e.g., Python 3.10, Python 3.11).
   ![Downloading latest verison of Python](https://github.com/Dvorkam/LearnPython/blob/lesson0/lesson0/assets/python_download.PNG)   

2. **Install Python:**
   - Double-click the installer to run it.
   - During the installation process, you'll come across a checkbox that says "Add python.exe to PATH. Red circle in image below" Make sure this checkbox is checked. This will allow you to use Python from the command line without specifying its full path. If you have an earlier version of Python installed, you will instead be offered an upgrade).
   ![Installing latest verison of Python](https://github.com/Dvorkam/LearnPython/blob/lesson0/lesson0/assets/install_python.png) 
   - Complete the installation by following the on-screen instructions. The default settings are usually sufficient.

3. **Verify the Installation:**
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
     C:\Users\Michal>python --version
     Python 3.11.5
     ```
   - If not, your python installation has not been added to PATH at which point I suggest to uninstall python and try again from step 2

