# 1.  env steup
python -m venv venv
Set-ExecutionPolicy Unrestricted -Scope CurrentUser  #optional

# Activate the virtual environment: recurring this step only
venv\Scripts\activate  #On Windows (PowerShell):
# venv\Scripts\activate.bat  #On Windows (Command Prompt)

# Check installed packages (optional):
pip list




# 2.Recreate the Environment

# Save dependencies (after installing all required packages):
pip freeze > requirements.txt

# Reinstall dependencies in a new environment (if needed later):
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt





# 2. git initial

git init

# pip install dvc
# dvc --version

dvc init





# 3.
# Freeze your environment:
pip freeze > requirements.txt

# Ignore the venv/ folder so it’s not accidentally pushed to Git: Add this to your .gitignore:
venv/
  
# If needed later on a new system or after deleting the venv/:
python -m venv venv
venv\Scripts\activate  # or source venv/bin/activate (Linux/Mac)
pip install -r requirements.txt
# This will fully restore your environment.


#4. src - data_ingestion.py

