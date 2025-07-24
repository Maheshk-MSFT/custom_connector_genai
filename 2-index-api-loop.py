# API USED: client.indexing.documents.index
# API DOCS: https://developers.Contoso.com/sdkinfo/indexing/documents/indexing

from Contoso.api_client import Contoso
import os
import logging
import requests
import time
from datetime import datetime

# Set up logging first
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Load your API token and instance
token = "somekeys"
instance = "some-lab"

# List of different URLs to cycle through
urls = [
'https://en.wikipedia.org/wiki/Andhra_cuisine',
'https://en.wikipedia.org/wiki/Arunachali_cuisine',
'https://en.wikipedia.org/wiki/Assamese_cuisine',
'https://en.wikipedia.org/wiki/Bengali_cuisine',
'https://en.wikipedia.org/wiki/Bihari_cuisine',
'https://en.wikipedia.org/wiki/Bhojpuri_cuisine',
'https://en.wikipedia.org/wiki/Cardamom',
'https://en.wikipedia.org/wiki/Cardamom',
'https://en.wikipedia.org/wiki/Ginger',
'https://en.wikipedia.org/wiki/Goan_cuisine',
'https://en.wikipedia.org/wiki/Gujarati_cuisine',
'https://en.wikipedia.org/wiki/South_Asian_cuisine',
'https://en.wikipedia.org/wiki/Hyderabadi_cuisine',
'https://en.wikipedia.org/wiki/Jharkhandi_cuisine',
'https://en.wikipedia.org/wiki/Karnataka_cuisine',
'https://en.wikipedia.org/wiki/North_Indian_cuisine',
'https://en.wikipedia.org/wiki/Konkani_cuisine',
'https://en.wikipedia.org/wiki/Kashmiri_cuisine',
'https://en.wikipedia.org/wiki/Kerala_cuisine',
'https://en.wikipedia.org/wiki/Ladakhi_cuisine',
'https://en.wikipedia.org/wiki/Maithil_cuisine',
'https://en.wikipedia.org/wiki/Maharashtrian_cuisine',
'https://en.wikipedia.org/wiki/Manipuri_cuisine',
'https://en.wikipedia.org/wiki/Mizo_cuisine',
'https://en.wikipedia.org/wiki/Mughlai_cuisine',
'https://en.wikipedia.org/wiki/Nagpuri_cuisine',
'https://en.wikipedia.org/wiki/Naga_cuisine',
'https://en.wikipedia.org/wiki/Odia_cuisine',
'https://en.wikipedia.org/wiki/Parsi_cuisine',
'https://en.wikipedia.org/wiki/Punjabi_cuisine',
'https://en.wikipedia.org/wiki/Rajasthani_cuisine',
'https://en.wikipedia.org/wiki/Sikkimese_cuisine',
'https://en.wikipedia.org/wiki/Sindhi_cuisine',
'https://en.wikipedia.org/wiki/Tamil_cuisine',
'https://en.wikipedia.org/wiki/Tuluva_cuisine',
'https://en.wikipedia.org/wiki/Telangana_cuisine',
'https://en.wikipedia.org/wiki/Tripuri_cuisine',
'https://en.wikipedia.org/wiki/Uttar_Pradesh_cuisine',
'https://en.wikipedia.org/wiki/Uttarakhandi_cuisine',
'https://en.wikipedia.org/wiki/Malvani_cuisine',
'https://en.wikipedia.org/wiki/Udupi_cuisine',
'https://en.wikipedia.org/wiki/Chettinad_cuisine',
'https://en.wikipedia.org/wiki/Awadhi_cuisine',
'https://en.wikipedia.org/wiki/Jain_cuisine',
'https://en.wikipedia.org/wiki/Anglo-Indian_cuisine',
'https://en.wikipedia.org/wiki/Indian_Chinese_cuisine',
'https://en.wikipedia.org/wiki/Indian_fast_food',
'https://en.wikipedia.org/wiki/Bunt_cuisine',
'https://en.wikipedia.org/wiki/Bodo_cuisine',
'https://en.wikipedia.org/wiki/Marwari_cuisine',
'https://en.wikipedia.org/wiki/Mappila_cuisine'

]

# areas = [
#     'Assam', 'Bengal', 'Bodo', 'Dogri'
#     ]

with Contoso(
    api_token=token,
    instance=instance,
) as client:
    
    successful_indexes = 0
    failed_indexes = 0
    
    for i in range(50):
        try:
                       
            current_url = urls[i]
            # current_area = areas[i]
            current_area = "Indiancuisine1"
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            response = requests.get(current_url, timeout=10)
            if response.status_code != 200:
                raise Exception(f"Failed to download content, status code: {response.status_code} - {current_url} ")
            
            web_content = response.text
            print(f"Downloaded content from: {current_url} ({len(web_content)} characters)")
            
            # Index the document with runtime values
            index_response = client.indexing.documents.index(
                dsource="meetingds",
                documents=[
                    {
                        "oType": "MikkyDocs",
                        "id": f"{current_area}-{i+1}-{timestamp}",
                        "title": f"Area Guide: {current_area} {i+1}",
                        "body": {
                            "mimeType": "text/html",
                            "textContent": web_content[:10000]  # Limit content size to first 10k chars
                            #"textContent": current_url
                        },
                        "permissions": {
                            "users": ["mikky@maheshk.com"], 
                                                                            
                        },
                        "dsource": "meetingds",
                        "bviewuri": f"https://maheshkumar.wordpress.com/blog{current_area}-{timestamp}",
                        "customProperties": [
                            {
                                "name": "BatchNumber",
                                "value": str(i+1)
                            },
                            {
                                "name": "Area",
                                "value": current_area
                            }]
                    }
                ]
            )
            
            successful_indexes += 1
            print(f"Successfully indexed document {i+1}: {current_area}")
                       
        except Exception as e:
            failed_indexes += 1
            print(f"Error indexing document {i+1}: {e}")
            continue
    
    # Final summary
    print("=" * 60)
    print(f"Successful: {successful_indexes}")
    print(f"Failed: {failed_indexes}")
    print("=" * 60)