#!/bin/bash
# Write a script to display only the status code of the response.
curl -s -o /dev/null -w "%{http_code}" "$1"
