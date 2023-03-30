#!/bin/bash
# sends a JSON POST request to a URL and displays the body of the response.
curl -s "$1" -X POST -H "Content-Type: application/json" -d "@$2"
