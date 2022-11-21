#!/bin/bash

. ./env.sh

if [ ! -z $1 ] && [ $1 = "--dev" ]; then
	python3.11 -m sanic --dev --host $host --port $port main.asgi:app
else
	python3.11 -m sanic --host $host --no-access-logs --no-coffee --no-motd --port $port --workers $workers main.asgi:app
fi
