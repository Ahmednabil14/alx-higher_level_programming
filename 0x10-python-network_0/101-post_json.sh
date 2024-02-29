#!/bin/bash
# Write a script to send a JSON POST request with the contents of a file and display the response body.
curl -X POST -H "Content-Type: application/json" -d @"$2" "$1"
