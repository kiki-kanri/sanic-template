#!/bin/bash

. ./env.sh

if [ ! -z $unix ]; then
	args="--unix $unix"
else
	args="--host $host --port $port"
fi

if [ ! -z $1 ] && [ $1 = "--dev" ]; then
	python3.11 -m sanic --dev $args main.asgi:app
else
	python3.11 -m sanic $args --no-access-logs --no-coffee --no-motd --no-noisy-exceptions --workers $workers main.asgi:app
fi
