#!/usr/bin/env bash
set -e

FRONTEND_COLOR='\033[01;35;47m'
BACKEND_COLOR='\033[01;34;47m'
NC='\033[0m' # No Color

# Helpers functions
frontend() {
    echo -e "${FRONTEND_COLOR} Building the frontend ${NC}"
    cd frontend;
    npm run build &&\
    cd ..;
}
backend() {
    echo -e "${BACKEND_COLOR} Building the backend ${NC}"
    cd backend;
    FLASK_APP=run.py FLASK_DEBUG=1 flask run &&\
    cd ..;
}

# Testing what to build in regards to the options passed
case "$1" in
    -f) frontend ;; # Building only the frontend
    -b) backend ;; # Building only the backend
    *) frontend && backend ;; # Building both if any other options is passed
esac