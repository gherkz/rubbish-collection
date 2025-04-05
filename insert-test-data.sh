#!/usr/bin/env sh

curl -X POST \
  -H 'Content-Type: application/json' \
  "http://localhost:8000/api/v1alpha1/rubbish-types/" \
  -d '{"name": "Refuse"}'

curl -X POST \
  -H 'Content-Type: application/json' \
  "http://localhost:8000/api/v1alpha1/rubbish-types/" \
  -d '{"name": "Recycling"}'

ADDRESS_ID=$(curl -X POST \
  -H 'Content-Type: application/json' \
  "http://localhost:8000/api/v1alpha1/addresses/" \
  -d '{"street":"1 Station Rd", "city":"Cambridge", "postcode":"CB1 2JW", "council":"Cambridge City Council"}' \
  | jq -r '.id')

curl -X POST \
  -H 'Content-Type: application/json' \
  "http://localhost:8000/api/v1alpha1/addresses/${ADDRESS_ID}/collection-schedules/" \
  -d '{"rubbishType": {"name": "Refuse"}, "frequency": "B", "startDate": "2025-01-01"}'

curl -X POST \
  -H 'Content-Type: application/json' \
  "http://localhost:8000/api/v1alpha1/addresses/${ADDRESS_ID}/collection-schedules/" \
  -d '{"rubbishType": {"name": "Recycling"}, "frequency": "B", "startDate": "2025-01-08"}'