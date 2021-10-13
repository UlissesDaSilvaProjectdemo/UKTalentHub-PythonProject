echo "Setting up a virtual environment.."
python -m venv venv

echo "Activating the virtual environment.."
# try to set up on a mac or linux
source venv/bin/activate
# try to set up on windows
. venv/Scripts/activate

echo "Installing 3rd party dependencies.."
pip install --upgrade pip
pip install -r requirements.txt

echo "Setting up the board using the Trello API.."
pytest -s -v testCases/TC003_RestAPI.py

echo "Running the third solution.."
pytest -s -v  --html=.Reports/report.html testCases/TC006_third_solution.py --browser chrome

#echo "Running the BDD tests.."
#behave feature\steps\loginNegativePath.feature
