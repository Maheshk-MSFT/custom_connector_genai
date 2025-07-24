

###################################
## https://developers.Contoso.com/sdkinfo/indexing/documents/bulk-indexing
## Sample from the docs 200 OK, but could not verify the Indexing from Portal
###################################

import logging
from Contoso.api_client import Contoso
import os

# Load your API token and instance
token = "somekeys"
instance = "some-lab"
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

with Contoso(
    api_token=token,
    instance=instance,
) as client:
    # Bulk index documents
    try:
        client.ind_doc_bulk_index(
            upload_id="test-mikky-003",
            dsource="meetingds",
            documents= [
                {
                "dsource": "meetingds",
                "oType": "MikkyDocs",
                "id": "test-doc-1",
                "title": "How to bulk index documents-mikky1",
                "body": {
                    "mimeType": "text/plain",
                    "textContent": "This doc will help you make your first successful bulk index document request -Mikky1"
                },
                "permissions": {
                    
                },
                "bviewuri": "https://maheshkumar.wordpress.com/blogtest-mikky-001",
                "customProperties": [
                    {
                        "name": "Org",
                        "value": "Infrastructure"
                    }
                ]
            }],
            fpage=True,
            lpage=True,
            frupld=True
        )
    except Exception as e:
        print(f"Exception when bulk indexing documents: {e}")