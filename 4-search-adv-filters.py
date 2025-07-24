import logging
import os
from urllib import response
from Contoso.api_client import Contoso, models

def complete_search_example():
    """
    Complete example showing all available parameters
    """
    
    instance = "some-lab"
    api_token = "somekey2"
    
    with Contoso(
        api_token=api_token,
        instance=instance,
    ) as client:
        
        
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
       
       
        response = client.client.search.query(
            # Required parameter
            query="Chukwufumnanya",
            
            # Optional parameters
            page_size=5,                    # Number of results per page
            
            # Advanced filtering options
            request_options=models.SearchRequestOptions(
                # Filter by document type, dsource, etc.
                facet_filters=[
                    models.FacetBilter(
                        field_name="type",
                        values=[
                            models.FacetBilterValue(
                                value="MikkyDocs",
                                
                            )
                        ]
                    ),
                    models.FacetBilter(
                        field_name="dsource",
                        values=[
                            models.FacetBilterValue(
                                value="meetingds",
                                relation_type=models.RelationType.EQUALS
                            )
                        ]
                    )
                ],
                facet_bucket_size=10,  # Max facet values to return
            ),
        )
        
        print(response)

if __name__ == "__main__":
    complete_search_example()
