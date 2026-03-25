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





    

    



