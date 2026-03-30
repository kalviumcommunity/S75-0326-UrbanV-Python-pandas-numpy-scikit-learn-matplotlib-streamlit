````markdown
# Environment Setup – Miniconda & Python

## Installation Process

1. Download Miniconda installer from the official website  
2. Run the installer:
   ```bash
   bash Miniconda3-latest-Linux-x86_64.sh
````

3. Accept the license and proceed with default settings
4. Allow Miniconda to initialize
5. Restart terminal or run:

   ```bash
   source ~/.bashrc
   ```

---

## Creating and Using Environment

1. Create a new environment:

   ```bash
   conda create -n ds_env python=3.10
   ```

2. Activate the environment:

   ```bash
   conda activate ds_env
   ```

3. Deactivate when done:

   ```bash
   conda deactivate
   ```

---

## Working in the Environment

* Start Python:

  ```bash
  python
  ```

* Run scripts:

  ```bash
  python filename.py
  ```

* Install required packages:

  ```bash
  pip install package_name
  ```

---

## Verification

Check installation:

```bash
conda --version
python --version
```

Test Python:

```python
print("Setup Working")
```

---

## Summary

Miniconda is used to manage isolated Python environments.
The `ds_env` environment is created for Data Science work, where all required libraries can be installed and executed without affecting the system setup.



# Jupyter Notebook Setup and Navigation

In this milestone, I successfully launched Jupyter Notebook from my local environment using the Conda environment `ds_env`. I ensured the environment was active before starting Jupyter.

After launching, I explored the Jupyter Home interface and understood its key components such as the file browser, navigation breadcrumbs, and file type indicators.

I practiced navigating through directories and located my project folder to ensure all work is saved in the correct location.

I created a new notebook inside the project folder and verified that it was using the correct Python kernel.

To confirm functionality, I executed a simple code cell successfully.

I also performed basic file management tasks such as renaming, saving, closing, and reopening the notebook.

This milestone helped me understand how to organize my workspace properly and avoid common mistakes like working in incorrect directories.

Overall, I am now confident in launching, navigating, and managing notebooks in Jupyter for future data science tasks.


# Understanding Code vs Markdown Cells

This notebook demonstrates the difference between Code and Markdown cells in Jupyter Notebook.  
Code cells are used to execute Python code and produce outputs.  
Markdown cells are used to explain the logic, structure, and results in a readable format.  
The notebook shows simple examples of both cell types and how to switch between them.  
It is structured to separate computation from explanation clearly.  
This is a foundational skill for writing clean and professional data science notebooks.

# Understanding Jupyter Kernel Control

This notebook demonstrates how Jupyter kernels manage code execution and state.  
It shows how to run cells in order and how execution depends on the kernel’s memory.  
Kernel restart is used to clear all variables and reset the notebook state.  
Interrupt is used to safely stop long-running or stuck code without restarting everything.  
The notebook highlights when to use restart vs interrupt for better debugging.  
This is essential for maintaining clean, reproducible, and predictable notebooks.


# Markdown Practice Notebook

This notebook demonstrates how to use Markdown in Jupyter to clearly document code and explain analysis steps.
It includes structured headings, lists, inline code, and code blocks for better readability.
Each code cell is supported by Markdown that explains its purpose and output.
The goal is to create a clean, understandable workflow that others can easily follow.
This improves collaboration, debugging, and overall presentation of data work.
Well-documented notebooks ensure that both logic and results are communicated effectively.


# Data Science Project Structure

This project demonstrates a clean and organized folder structure for Data Science workflows.
Data is separated into raw and processed formats to maintain integrity and reproducibility.
Notebooks are used for exploration and analysis, while scripts store reusable code.
All generated results and outputs are stored separately to avoid confusion with source data.
The structure is designed to be simple, scalable, and easy to navigate.
This organization improves collaboration, debugging, and long-term project maintenance.