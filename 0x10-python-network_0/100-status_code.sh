#!/bin/bash
# Script that displays the status code of a response
curl -sI -o /dev/null -w "%{http_code}" "$1"
