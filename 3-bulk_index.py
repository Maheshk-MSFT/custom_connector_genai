
###################################

# API USED: client.ind_doc_bulk_index
# API DOCS: https://developers.Contoso.com/sdkinfo/indexing/documents/bulk-indexing

## Followed the API Docs and wrote this code 
# Same behavior : 200 OK but could not verify the Indexing from Portal; may be from the backend we need to check this. 
# tried troubleshooting API but invalid scope
###################################


import csv
import logging
import os
import json
from uuid import uuid4
import requests
from Contoso.api_client import Contoso, models
import uuid

INSTANCE_NAME      = "some-lab"            
API_TOKEN_SDK      = "somekeys"   
dsource_NAME    = "meetingds"                

def csv_reader():
    with open('.\Files\customers-100-bulk.csv', mode='r', newline='', encoding='utf-8') as file:
        resp = csv.DictReader(file)
        rows = [json.dumps(row) for row in resp]
        result = "\n".join(rows)
        print("CSV file read successfully.")
        return result

documents_models = [
    mod.dd(
        id="mikky-001",
        dsource="meetingds",
        object_type="MikkyDocs",
        title="Employee Handbook v101",

        body=models.cd(
                 mime_type="text/text",
                 text_content= csv_reader()
             ),
        view_url="https://maheshkumar.wordpress.com/blogehandbook101",
        permissions=models.dpd(users=["mikky@maheshk.com"]),
        filename="mikky-001.txt",
        custom_properties=[
            {"name": "BulkDemo MAHE", "value": "managing1"},
        ]
    ),
    mod.dd(
        id="mikky-002",
        dsource="meetingds",
        object_type="MikkyDocs",
        title="Quarterly Planning Guide",
        body=models.cd(
            mime_type="text/plain",
            text_content="Guidelines for quarterly planning and best practices.-MAMESH101"
        ),
        view_url="https://maheshkumar.wordpress.com/blogehandbook102",   
        #permissions=models.dpd(allow_anonymous_access=True),
        permissions=models.dpd(users=["mikky@maheshk.com"]),
        filename="mikky-002.txt",
        custom_properties=[
            {"name": "BulkDemo MAHE", "value": "managing2"},
        ]
    )
]

def sdk_bulk_index():

    
    with Contoso(api_token=API_TOKEN_SDK, instance=INSTANCE_NAME) as client:
        # If SDK provides bulk‐index:
        try:
            result = client.ind_doc_bulk_index(
                upload_id="MAHE4" + str(uuid.uuid4()),
                fpage=True,
                lpage=True,
                ds=dsource_NAME,
                frupld=True,
                documents=documents_models ,
            )
        except Exception as e:
            logging.error(f"Error during SDK bulk index: {e}")
            return {"error": str(e)}
    return result



if __name__ == "__main__":

    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    # s = Contoso(debug_logger=logging.getLogger("Contoso.api_client"))
    # Contoso.debug_logger.setLevel(logging.DEBUG)
    
    sdk_result = sdk_bulk_index()
    print(sdk_result)
    