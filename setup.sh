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

#echo "Setting up the board using the Trello API.."
#pytest -s -v testCases/TC004_RestAPI.py

echo "Running the  pytest solution.."
pytest -s -v  --html=.Reports/report.html testCases/TC001_LoginTest.py --browser chrome
pytest -s -v  --html=.Reports/report.html testCases/TC002_LinksSmokeTest.py --browser chrome
pytest -s -v  --html=.Reports/report.html testCases/TC003_ImgsSmokeTest.py --browser chrome


echo "Running the BDD tests.."
behave testCases/selenium/TC001_selecct_dropdown.feature
behave testCases/selenium/TC002_clickSendKeys.feature
behave testCases/selenium/TC003_RadioButtonsAndCheckboxes.feature
behave testCases/selenium/TC005_mouse_hovering.feature
behave testCases/selenium/TC006_switch_to_alert.feature
behave testCases/selenium/TC007_switch_to_frame.feature
behave testCases/selenium/TC008_switch_to_window.feature
behave testCases/selenium/TC009_sliders.feature
behave testCases/selenium/TC010_scrolling_element.feature

