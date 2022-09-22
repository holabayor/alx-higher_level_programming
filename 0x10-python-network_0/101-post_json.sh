#!/bin/bash
# Script that sends a JSON POST request
curl -sX POST --data @"$2" -H "Content-Type: application/json" "$1"
