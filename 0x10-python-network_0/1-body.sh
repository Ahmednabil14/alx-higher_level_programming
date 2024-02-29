#!/bin/bash
# Write a script to display the body of a 200 status code response.
# send request and get the response
[ "$(curl -sI -w '%{http_code}' "$1" | tail -n 1)" == 200 ] && curl -s "$1"
