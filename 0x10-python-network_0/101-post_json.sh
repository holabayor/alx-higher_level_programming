#!/bin/bash
# Script that sends a JSON POST request
curl -sX "$1" -H "Content-Type: application/json" --data-raw "$2"
