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

# 5. Create .env file
# inside .env file put:
MONGO_URI = mongodb://localhost:27017/database_name

# 6. Run the app
flask run
or
python run.py

# 7. When done, deactivate environment
deactivate