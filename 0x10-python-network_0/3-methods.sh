#!/bin/bash
# Write a script to display all HTTP methods the server will accept.
curl -s -X OPTIONS -I "$1" | grep "allow" | awk -F ': ' "{print \$2}"
