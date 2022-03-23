import requests
from bs4 import BeautifulSoup
import pandas as pd

sdata = []
allsupplierIds = []
nletter = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z", "other"]

for test in nletter:
    for pg in range(1, 11):
        p = {"prefix": test, "page": pg, "framework": "g-cloud"}
        spIdRequest = requests.get("https://www.digitalmarketplace.service.gov.uk/g-cloud/suppliers", params=p)
        if spIdRequest.status_code == 400:
            break
        soup = BeautifulSoup(spIdRequest.text, 'html.parser')
        supplierIds = soup.find_all("h2", attrs={"class": "govuk-heading-s govuk-!-margin-bottom-1"})
        for item in supplierIds:
            supplierData = []
            re = requests.get("https://www.digitalmarketplace.service.gov.uk" + str(item.a["href"]).strip())
            sets = BeautifulSoup(re.text, 'html.parser')
            contact = sets.find_all("p", attrs={"class": "govuk-body"})
            try:
                print("Supplier Name: " + str(contact[3].find_all('span')[0].text))
                supplierData.append(str(contact[3].find_all('span')[0].text))
                print("Supplier Details: " + str(contact[2].text.strip()))
                supplierData.append(str(contact[2].text.strip()))
                print("Supplier contact Email Address: " + str(contact[3].a['href']).strip().replace("mailto:", ""))
                supplierData.append(str(contact[3].a['href']).strip().replace("mailto:", ""))
                print("Supplier contact Telephone: " + str(contact[3].getText(separator="|").split('|')[5].strip()))
                supplierData.append(str(contact[3].getText(separator="|").split('|')[5].strip()))
                print("Supplier contact Address: " + str(contact[3].getText(separator="|").split('|')[2].strip()))
                supplierData.append(str(contact[3].getText(separator="|").split('|')[2].strip()))
            except IndexError:
                print("Supplier Name: " + str(contact[2].find_all('span')[0].text))
                supplierData.append(str(contact[2].find_all('span')[0].text))
                print("Supplier Details: " + "")
                supplierData.append("")
                print("Supplier contact Email Address: " + str(contact[2].a['href']).strip().replace("mailto:", ""))
                supplierData.append(str(contact[2].a['href']).strip().replace("mailto:", ""))
                print("Supplier contact Telephone: " + str(contact[2].getText(separator="|").split('|')[5].strip()))
                supplierData.append(str(contact[2].getText(separator="|").split('|')[5].strip()))
                print("Supplier contact Address: " + str(contact[2].getText(separator="|").split('|')[2].strip()))
                supplierData.append(str(contact[2].getText(separator="|").split('|')[2].strip()))
            print("=================================================================================================")
            sdata.append(supplierData)
supplier = pd.DataFrame(sdata,
                        columns=['Supplier Name', 'Supplier Details', 'Supplier Email', 'Supplier Telephone',
                                 'Supplier Contact Name'])
supplier.to_csv('C:\\Users\\anshujit.mishra\\Documents\\Test\\ukgov.csv', index=False)