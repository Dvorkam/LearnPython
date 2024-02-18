# Learn Python - Lesson 0

## Expected time: 20 min

## Objectives


1. Download and install Python
    1. [Windows](#111-on-windows)
    2. [Ubuntu](#112-on-ubuntu-wip)
2. Download and install VSC
    1. [Windows](#121-for-windows)
    2. [Ubuntu](#112-on-ubuntu-wip) 
3. [Create Python profile in VSC](#13-create-python-profile-in-vsc)
4. [Clone Learn Python repository](#14-clone-learn-python-repository)


## About

This chapter will attempt to get you set up as fast as possible so you can start learning Python programming. We will touch upon many concepts without overly focusing on them such us virtual enviroment, source control, PEP8 coding standard and others, some only mentioned in passing. Most of these tools/ concepts will be elaborated on in subsequent lessons. I have decided to do it this way, because the utility of them is too high to avoid even at the begining, but spending too much time on them would be too tedious and would keep us away from what I consider more fun, the actual coding.

By the end of this chapter. All the tools we will need in upcomming chapters should be setup and we will be able to get to the fun stuff.

## 1.1 Download and Install Python

### 1.1.1 On Windows

#### **Download Python:**

- Open a web browser and go to the official Python website: [python.org/downloads](https://www.python.org/downloads/).
- You'll see the latest version of Python displayed prominently. Make sure to download the **Python 3.x** version (e.g., Python 3.10, Python 3.11).
![Downloading latest version of Python](https://github.com/Dvorkam/LearnPython/blob/lesson0/lesson0/assets/python_download.PNG)

**Install Python:**

- Double-click the installer to run it.
- During the installation process, you'll come across a checkbox that says "Add python.exe to PATH. Red circle in image below" Make sure this checkbox is checked. This will allow you to use Python from the command line without specifying its full path. If you have an earlier version of Python installed, you will instead be offered an upgrade.
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

```console
python --version
```

- Confirm the version matches the version of python you downloaded in step 1

```console
C:\Users\User>python --version
Python 3.11.5
```

- If not, your python installation has not been added to PATH and you will have to add it manually.

### 1.1.2 On Ubuntu (WIP)

**Open Terminal:**

- Press `Ctrl` + `Alt` + `T` to open the Terminal.

**Update Package Lists:**

- Before installing any software, it's a good idea to update the package lists to ensure you're getting the latest version. Enter the following commands in the terminal:

```console
sudo apt update
sudo apt upgrade
```

**Install Python:**

Ubuntu typically comes with Python pre-installed. However, it's a good practice to install the latest version, pip (Python's package manager), venv (virtual enviroments package) and pytest (Python testing framework). Enter the following command to install:

```console
sudo apt install python3 python3-pip python3-venv python3-pytest
```

**Verify the Installation:**

- Once the installation is complete, you can verify that Python was installed successfully by typing:

```console
python3 --version
```

- You should see the version of Python you installed printed to the screen e.g.:

```shell
user@PCNAME:~$ python3 --version
Python 3.10.12
```

## 1.2 Download and Install Visual Studio Code

Visual Studio Code (VSC) is a popular code editor that provides a range of features for writing and debugging code. Here's how you can download and install it on both Windows and Ubuntu:

### 1.2.1 For Windows

I. **Open a Web Browser:**

- Launch your web browser and navigate to the Visual Studio Code download page: [https://code.visualstudio.com/download](https://code.visualstudio.com/download).

II. **Download Visual Studio Code:**

- On the download page, you'll see a section with download buttons for different operating systems. Click on the "Windows" button to download the installer for Windows.

III. **Run the Installer:**

- Locate the downloaded installer file in your "Downloads" folder (usually named `VSCodeSetup.exe`).
- Double-click the installer to run it.
- Follow the on-screen instructions to complete the installation. You can choose the default settings for most options.

IV. **Open Visual Studio Code:**

- Once the installation is complete, you can open Visual Studio Code by searching for "Visual Studio Code" in the Start menu or by clicking its icon on your desktop (if you chose to create one during installation), or by typing `code` in Command Prompt.

### 1.2.2 For Ubuntu

I. **Open Terminal:**

- Press `Ctrl` + `Alt` + `T` to open a Terminal window.

II. **Add Repository Key:**

- To install Visual Studio Code on Ubuntu, you'll need to add the Microsoft GPG key to your system. Enter the following command:

     ```sh
     curl -fsSL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
     sudo mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg
     ```

III. **Add Repository:**

- Add the Visual Studio Code repository to your list of software sources:

     ```sh
     sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list'
     ```

IV. **Update Package List:**

- Update the package list to include the newly added repository:

     ```sh
     sudo apt update
     ```

V. **Install Visual Studio Code:**

- Finally, install Visual Studio Code:

     ```sh
     sudo apt install code
     ```

VI. **Open Visual Studio Code:**

- After installation, you can open Visual Studio Code by typing `code` in the Terminal or by searching for "Visual Studio Code" in the Applications menu.

   {Image: Open-VSC-Ubuntu}


## 1.3 Create Python profile in VSC

Setting up the profile is by no means mandatory, but is an easy way to quickly collect useful extensions and apply settings that are generally suitable for python programming. Following image should be fairly self explanatory but ltes add the steps as well

I. Click on the Manage (cog-wheel) at bottom of the page

II. Here click on Profile(Default)

III. Finally click on Create Profile...

IV. From the selection at the top of the window Python

V. Selection on the left shows you what setting and extensions will be downloaded/applied, for now, you can leave as is, or if you want to save some disk space, you can unselect Dev Containers, Docker, WSL, and all Remote * extensions, at the time of writing of this document I wasn't sure if we will use them at all, but can always get them later.

{Profile setup}

## 1.4 Clone Learn Python Repository

1. **Open Visual Studio Code:**

   - If Visual Studio Code is not already open, launch it from the Start menu (Windows) or Applications menu (Ubuntu).

2. **Open Source Control View:**

   - Click on the Source Control icon in the sidebar on the left (or press `Ctrl` + `Shift` + `G`) and click Clone Repository. Or if Welcome screen is opened you can click `Clone Git Repository...`
       ![Clone Repository](https://github.com/Dvorkam/LearnPython/blob/lesson0/lesson0/assets/clone_repository.png)
       - WARNING: If you don't have git installed on your PC, you will instead see following:
   
       ![Donwnload Git](https://github.com/Dvorkam/LearnPython/blob/lesson0/lesson0/assets/download_git.PNG)
       - In which case please just click Download Git for Windows, which will take you yo git.com and download and install the Git.

       - All the default settings are ok, but since we already have the VSC installed, you may just as well use VSC as your default Git editor.
       ![Set VSC as default Git editor during installation](https://github.com/Dvorkam/LearnPython/blob/lesson0/lesson0/assets/git_setup.PNG)

3. **Enter Repository URL:**
   - In the input field, enter the URL of the **Learn Python** repository: [https://github.com/Dvorkam/LearnPython.git](https://github.com/Dvorkam/LearnPython.git).
   - Choose a local path where you want to clone the repository and confirm.
4. **Sign up at GitHub.com**
    - RECOMMENDED: This step is not really necessary at this point, and in general will not be necessary, until you decide you want to start your own GitHub portfolio (on that later). BUT these is not really reason not to do it so ...
    - Register and account at [https://github.com/signup](https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home)

5. **(SKIP FOR NOW) Fork the Repository:**
     - If you want to push changes in your git repository, you either need to have access, or fork it. Since this is not really an introductory or necessary step, we will skip it for now.

6. **Open Cloned Repository:**

   - Once the repository is cloned, you can open it in Visual Studio Code by clicking the "Open Repository" button in the notification that appears after the cloning is complete.
