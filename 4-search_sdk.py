from Contoso.api_client import Contoso, models
from Contoso.api_client.utils import parse_datetime


import os

# Load your API token and instance
token = "somekey2"
instance = "some-lab"

# Instantiate Contoso client with your instance and API token
with Contoso(
    api_token=token,
    instance=instance,
) as Contoso:
    # Minimal search: only the query parameter is required
    response = Contoso.client.search.query(query="Achille", 
                                         page_size=5,
                                        )
    print(response)