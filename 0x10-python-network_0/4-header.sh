#!/bin/bash
# This script takes in a URL as an argument, sends a GET request to the URL using curl, and displays the body of the response
# It also sends a header variable X-School-User-Id with the value 98

url=$1
curl -sH "X-School-User-Id: 98" "$url"
