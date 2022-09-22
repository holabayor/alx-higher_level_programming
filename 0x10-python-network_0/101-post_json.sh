#!/bin/bash
# Script that sends a JSON POST request
curl -s --json "$2" "$1"
