# 0x10-python-network_0

## Project Overview

This project is part of the SE Foundations curriculum, focusing on Python and Networking. It aims to deepen understanding of HTTP, cURL, and Bash scripting, with a particular emphasis on making HTTP requests and handling responses. The project includes a variety of tasks that require the use of cURL for HTTP requests and Bash scripting for automating these requests.

## Learning Objectives

By the end of this project, you should be able to:

- Understand and explain the concepts of URLs, HTTP, domain names, sub-domains, port numbers, query strings, HTTP requests, HTTP responses, HTTP headers, HTTP message bodies, HTTP request methods, HTTP response status codes, and HTTP Cookies.
- Make HTTP requests using cURL.
- Write Bash scripts for automating HTTP requests and handling responses.
- Understand the structure and components of a URL.
- Explain the process of making a request when typing a URL into a browser.

## Requirements

- All scripts must be written in Bash or Python, as specified by the task.
- Bash scripts must be exactly 3 lines long.
- Python files must adhere to pycodestyle version 2.8.*.
- All files must be executable and end with a new line.
- The first line of all Bash files should be `#!/bin/bash`, and the first line of all Python files should be `#!/usr/bin/python3`.
- All curl commands must use the `-s` option for silent mode.
- Documentation is required for all modules, classes, and functions.

## Tasks

### Bash Scripts

1. **cURL body size**: Write a script to display the size of the body of a response in bytes.
2. **cURL to the end**: Write a script to display the body of a 200 status code response.
3. **cURL Method**: Write a script to send a DELETE request and display the response body.
4. **cURL only methods**: Write a script to display all HTTP methods the server will accept.
5. **cURL headers**: Write a script to send a GET request with a custom header and display the response body.
6. **cURL POST parameters**: Write a script to send a POST request with parameters and display the response body.
7. **Only status code**: Write a script to display only the status code of the response.
8. **cURL a JSON file**: Write a script to send a JSON POST request with the contents of a file and display the response body.
9. **Catch me if you can!**: Write a script that makes a specific request to receive a specific response.

### Python Function

- **Find a peak**: Write a function to find a peak in a list of unsorted integers without using any modules.

## Getting Started

1. Clone the repository: `git clone https://github.com/alx-higher_level_programming/0x10-python-network_0.git`
2. Navigate to the project directory: `cd 0x10-python-network_0`
3. Make sure all scripts are executable: `chmod +x *.sh`
4. Run the Bash scripts as per the instructions provided in the tasks.
5. For the Python function, run the test script: `./6-main.py`
