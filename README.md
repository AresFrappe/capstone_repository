# 1. Clone the repo
git clone https://github.com/AresFrappe/capstone_repository.git
cd repository

# 2. Create virtual environment
# Mac/Linux
python3 -m venv venv
# Windows
python -m venv venv

# 3. Activate virtual environment (run in terminal)
# Mac/Linux
source venv/bin/activate
# Windows (CMD)
venv\Scripts\activate
# Windows (PowerShell)
venv\Scripts\Activate.ps1

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run the app
flask run
or
python run.py

# 6. When done, deactivate environment
deactivate