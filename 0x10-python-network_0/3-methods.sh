#!/bin/bash
# Script that displays all methods a server will accept
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
