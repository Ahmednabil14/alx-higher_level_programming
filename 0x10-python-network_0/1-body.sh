#!/bin/bash
# Write a script to display the body of a 200 status code response.
response=$(curl -s -I "$1" | grep "HTTP/1.1 200 OK")
if [[ $response ]]; then
curl -s "$1"
fi
