import requests
import json
import pandas as pd

url = "https://tenant.saasit.com/api/odata/businessobject/externalcontacts"

df = pd.read_csv('C:/Users/Desktop/Scripts/tenant/tenant.csv')

ID_List = df.ID.tolist()
Last_List = df.Last.tolist()
First_List = df.First.tolist()
Email_List =  df.Email.tolist()


for ID, LAST, FIRST, EMAIL in zip(ID_List, Last_List, First_List, Email_List):
    
    body = {"FirstName": FIRST, "LastName": LAST, "PrimaryEmail": EMAIL, "Emp_LoginId": ID}

    headers = {'Authorization': 'tenant.saasit.com/#O8H24T05IV53TAVQT7K8FT41CG42F9J9#2'}

    response = requests.post(url, data=json.dumps(body), headers=headers)

    print(response.text)








