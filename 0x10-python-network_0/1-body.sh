#!/bin/bash
# Write a script to display the body of a 200 status code response.
# send request and get the response
response=$(curl -s -w "%{http_code}" "$1" | tail -n 1)
if [[ $response -eq 200 ]]; then
curl -s "$1"
fi
