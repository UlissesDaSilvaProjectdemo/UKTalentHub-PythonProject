# UKTalentHUB

## python 3.10 

### https://www.python.org/downloads/ 
1. Download Windows embeddable package (64-bit)
2. Download Windows installer (64-bit)
C:\Users\username

===========
pycharm  

https://www.jetbrains.com/pycharm/download/#section=windows 

============  
set up environment variables - system path 

Control Panel-->System and Security--> System - > Advanced system settings --> Enviroment Variable -->System Variables-->path-->Edit-->New-->paste the pyhton c:/path

--------------
Pycharm ---> File -->setting --> plugin --> cucumber 
Pycharm ---> File -->setting --> plugin --> gherkin
Pycharm ---> File --> setting --> projectname -->Pyhton Interpeter--> set non-interpeter in the drop down. 

--------------

1. pip install selenium  :selinium libraries 
2. pip install pytest : Unit Test framework 
3. pip install pytest-html : PytestHtml report  
4.pip install pytest-xdist : run test in parallel 
pip install Openpyxl : MS Excel Support  
pip install Allure-pytest  to generate reports 
pip install webdriver-manager 
pip install behave
pip intall driver
==========

Download git
https://git-scm.com/downloads
============== 
clone Framework: GutHub
git clone
https://github.com/UlissesDaSilvaProjectdemo/UKTalentHub-PythonProject.git

============== 
page object imports:#  
import softest 
import self 
import driver from testCases import TC006_third_solution 
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

============= 
import testCases Imports:#  
import pytest 
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.wait import WebDriverWait 
from webdriver_manager import driver 
from pageObjects.TC006_third_solutionPage import TC006_third_solutionPage 
from utilities.readProperties import ReadConfig 
from utilities.customLogger import LogGen

================ 
execution:

behave testCases/features/TC001_loginNegativePath.feature
behave testCases/selenium/TC004_drag_and_drop.feature
pytest -s -v  --html=.Reports/report.html testCases/TC001_LoginTest.py --browser chrome
pytest -s -v  --html=.Reports/report.html testCases/TC002_LinksSmokeTest.py --browser chrome
pytest -s -v  --html=.Reports/report.html testCases/TC004_RestAPI.py --browser chrome

# UKTalentHub-PythonProject 
Allure- reports 
----------------
1- install allure - report 
pip install allure-pytest

--------------
2 - downloand allure repor 
https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.10.0/

-------------
3 - set enviroment variable --> unzip the dowloand file --> navigate to bin folder --> set the bin path into the system enviroment variable

------------
4 - Open CMD and type -->allure serve and project absolute path ex: C:\Users\UKTalentHub-PythonProject\.Reports\AllureReports
or 
go to pycharm IDE Terminal -->allure serve . Reports/AllureReports

----------------
5 - to create the file --> run example: Pycharm IDE - cucumber Allure-repports <-f allure_behave.formatter:AllureFormatter -o>
behave -f allure_behave.formatter:AllureFormatter -o .Reports/file_name/selenium/features
eg:

To run Allure report
rem C:\User\UKTalentHub-PythonProject\.Reports\AllureReports

rem behave -f allure_behave.formatter:AllureFormatter -o 'Reports\AllureReports' testCases/features/TestFile.feature



----------------
HTML report 
6 - run example: Pycharm IDE - Pytest HTML reports <--html=.Reports/report.html>
pytest -s -v  --html=.Reports/report.html testCases/TC002_LinksSmokeTest.py --browser chrome
 
================
Jenkins installation 
JDK - https://www.oracle.com/java/technologies/downloads/#jdk17-windows
 Jenkins --> https://www.jenkins.io/download/
 
 --------------
 Open AWS Account
 open EC2 instances
 dowload keypair
 navigate to dolowad location -->C:\Users\user.name\Downloads\ keypar.txt 
 Open Gitbash
 Open server location
 copy EC2 instances IP adress into jenkins port 8080
 login into jenkins
 create job and run the pipeline
 
 ----------
 
 
