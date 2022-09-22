#!/bin/bash
# Script that makes a request and return the body
curl -sLv -X PUT -d "user_id=98" 0.0.0.0:5000/catch_me
