#!/bin/bash
# Write a script to display the size of the body of a response in bytes.
curl -s -I "$1" | grep "Content-Length" | awk "{print \$2}"
