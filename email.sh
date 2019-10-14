#!/bin/sh

echo "$1" | mail -s "$2" "$3"
