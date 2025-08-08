#!/bin/sh

# Change ownership of the app directory
# This is necessary to handle the case where a volume is mounted from the host
chown -R appuser:appuser /app

# Execute the command passed to this script as the appuser
exec gosu appuser "$@"
