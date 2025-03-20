# 1.  env steup
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

# 2. git initial
git init



# 3. DVC

pip install dvc
dvc --version

dvc init

dvc stage add


# dvc run  - outdated
dvc repro
