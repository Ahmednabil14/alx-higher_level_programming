#!/bin/bash
# Write a script to send a GET request with a custom header and display the response body.
curl -s -X PUT -H "X-School-User-Id: 98" "$1"
