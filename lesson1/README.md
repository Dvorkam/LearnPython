## 1.5 Setup Virtual Environment

I. **Open a Terminal in VSC:**

- In VSC in menu click on View
- Here click on Terminal

III. **Create a Virtual Environment:**

- To create a virtual environment named `venv`, enter the following command:

     ```sh
     python -m venv venv
     ```

     or on Ubuntu

     ```sh
     python3 -m venv venv
     ```

     This will create a folder named `venv` in your project directory to hold your virtual environment.

IV. **Activate the Virtual Environment:**

- On Windows, activate the virtual environment using this command:

     ```sh
     venv\Scripts\activate
     ```

- On macOS and Linux, use this command:

     ```sh
     source venv/bin/activate
     ```

   When the virtual environment is activated, your command prompt will change to show the name of the virtual environment.

   Something like this:

     ```terminal
     (venv) PS D:\repos\LearnPython>
     ```

V. **(Don't do) Deactivate the Virtual Environment:**

- To exit the virtual environment and return to your system's Python, simply enter into terminal the command:

     ```sh
     deactivate
     ```

   The virtual environment will be deactivated, and you'll return to the global Python environment.

Virtual environments are a fairly broad topic, we will not get into in this chapter. But since its usefulness is too high even without fully understanding it, we will use it, without further elaboration, until later.