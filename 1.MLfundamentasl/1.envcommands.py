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
