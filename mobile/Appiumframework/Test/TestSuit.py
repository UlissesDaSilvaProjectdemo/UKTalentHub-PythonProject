# 1. Import the files
import  unittest
from mobile.Appiumframework.Test.LoginPageTest import LoginPageTest
from mobile.Appiumframework.Test.ContatUsFormTest import ContactFormTest


# 2. Create the object of the class using unitTest
cf = unittest.TestLoader().loadTestsFromTestCase(ContactFormTest)
gt = unittest.TestLoader().loadTestsFromTestCase(LoginPageTest)

# 3. Create TestSuite
regressionTest = unittest.TestSuite([cf,gt])

# 4. Call the Test Runner method
unittest.TextTestRunner(verbosity=1).run(regressionTest)

