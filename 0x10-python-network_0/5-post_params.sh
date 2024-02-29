#!/bin/bash
# Write a script to send a POST request with parameters and display the response body.
curl -s -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
