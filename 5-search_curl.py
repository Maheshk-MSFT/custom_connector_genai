# 	curl -X POST https://whocares.Contoso.com/rest/api/v1/search \
# 	  -H 'Authorization: Bearer somekey2' \
# 	  -H 'Content-Type: application/json' \
# 	  -d '{
# 		"query": "Chukwufumnanya",
# 		"pageSize": 10
# 	  }'
   
   
#    curl -X POST https://whocares.Contoso.com/api2/getdsourceconfig \
#   -H 'Authorization: Bearer somekeys' \
#   -H 'Content-Type : application/json' \
#   -d '{
#         "dsource": "meetingds"
#       }'
      
# curl -X POST https://whocares.Contoso.com/api2/debug/Contosotest/status \
#   -H 'Authorization: Bearer somekeys'
  
  
# curl -X POST https://whocares.Contoso.com/api2/debug/Contosotest/status \
#   -H 'Authorization: Bearer somekeys'
#   -H 'Content-Type : application/json' \
#   -d '{
#         "oType": "Article",
#         "docId": "art123"
#       }'

# curl -X POST https://whocares.Contoso.com/api2/debug/Contosotest/status \
#   -H 'Authorization: Bearer somekeys'
#   -H 'Content-Type : application/json' \
#   -d '{
#         "dsource": "meetingds",
#         "oType": "MikkyDocs"
#       }'

# curl -i -X POST \
#   'https://whocares.Contoso.com/rest/api/v1/activity' \
#   -H 'Authorization: Bearer somekeys' \
#   -H 'Content-Type: application/json' \
#   -H 'X-Contoso-ActAs: user-whose-activity-is-being-reported@example.com' \
#   -d '{
#     "events": [
#       {
#         "url": "https://maheshkumar.wordpress.com/blogehandbook102",
#         "action": "VIEW",
#         "timestamp": "2025-07-18T14:56:07.000Z"
#         "params": {
#             "dsource": "meetingds"
#         }
#       },
#     ]
#   }'