#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!
curl -s "0.0.0.0:5000/catch_me" -LX PUT -H "Origin: School" -d "user_id=98"
