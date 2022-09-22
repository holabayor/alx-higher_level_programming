#!/bin/bash
# Script that sets key-value variable of a POST request
curl -s --data "email=test@gmail.com&subject=I%20will%20always%20be%20for%20PLD" "$1"
