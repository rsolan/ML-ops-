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
import numpy as np
import pandas as pd
import os
from sklearn.model_selection import train_test_split

# Load data
df = pd.read_csv('https://raw.githubusercontent.com/campusx-official/jupyter-masterclass/main/tweet_emotions.csv')
df.drop(columns=['tweet_id'], inplace=True)

# Filter for happiness and sadness
final_df = df[df['sentiment'].isin(['happiness', 'sadness'])]
final_df['sentiment'].replace({'happiness': 1, 'sadness': 0}, inplace=True)

# Split into train and test
train_data, test_data = train_test_split(final_df, test_size=0.2, random_state=42)

# Save to local folders
data_path = os.path.join("data", "raw")
os.makedirs(data_path, exist_ok=True)

train_data.to_csv(os.path.join(data_path, "train.csv"), index=False)
test_data.to_csv(os.path.join(data_path, "test.csv"), index=False)

# data - raw test/train file created

# 5. cmd - 
dvc stage add -n data_ingestion -d src/data_ingestion.py -o data/raw python src/data_ingestion.py
# - update or create new folder depending upon changes

# dvc.yaml file created
'''
stages:
  data_ingestion:
    cmd: python src/data_ingestion.py
    deps:
    - src/data_ingestion.py
    outs:
    - data/raw
'''

# 6. run cmd
dvc repro   #dv run outdated

