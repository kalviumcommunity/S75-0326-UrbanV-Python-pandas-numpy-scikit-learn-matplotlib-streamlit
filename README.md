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