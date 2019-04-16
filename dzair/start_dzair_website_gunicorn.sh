#!/bin/bash

gunicorn --workers=2 --bind=0.0.0.0:5001 --log-level=debug qarta:app --access-logfile=logs/access.log --error-logfile=logs/error.log
