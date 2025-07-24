######################################################################
## client.indexing.documents.index
## One call, One document/content - Works
######################################################################

from contoso.api_client import contoso
import os
import logging
import requests

# Load your API token and instance
token = ""
instance = ""

with contoso(
    api_token=token,
    instance=instance,
) as client:
    # Index a document
    try:
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
        
        url = 'https://raw.githubusercontent.com/datasciencedojo/dss/refs/heads/master/titanic.csv'   
        #url = 'https://en.wikipedia.org/wiki/Brookefield'
        #url = 'https://github.com/laxmimerit/All-CSV-ML-Data-Files-Download/blob/master/Customer_Churn_Modelling.csv'
       
        response = requests.get(url)
        csv_content = response.text

        print(f"Downloading CSV from: {url}")
        if response.status_code != 200:
            raise Exception(f"Failed to download CSV file, status code: {response.status_code}")
        
        print("Indexing document with CSV content...", csv_content[:500] + "...")  
        
        response = client.indexing.documents.index(
            dsource="meetingds",
            documents=[
                {
                    "oType": "MikkyDocs",
                    "id": "jburkardt-datacsv",
                    "title": "This doc will help you get jburkardt/data/csv/cities.",
                                      
                    "body": {
                        #"mimeType": "text/plain",
                        #"mimeType": "text/html",
                        "mimeType": "text/csv",
                        "textContent": csv_content, 
                    },
                    "permissions": {
                        "users": ["mikky@maheshk.com"],                         
                                                                       
                    },
                    "dsource": "meetingds",
                    "bviewuri": "https://maheshkumar.wordpress.com/blogjburkardt-data-csv-cities",
                }
            ]
        )
        
        print("Document indexed successfully:", response)
        
    except Exception as e:
        print(f"Exception when indexing document: {e}")
