# Day 23: virtual environments, one per project
mkdir my_project && cd my_project
python3 -m venv venv                  # create      (Windows: python -m venv venv)
source venv/bin/activate              # activate    (Windows: venv\Scripts\activate)
pip install requests                  # installs into THIS project only
pip freeze > requirements.txt         # save exact versions
cat requirements.txt
deactivate                            # leave the venv
echo "venv/" > .gitignore             # never commit the venv folder
# New computer or fresh clone:  python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt
