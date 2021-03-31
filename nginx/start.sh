#!/bin/bash
export ALLOWED_HOSTS=mahoushoujobu.com
source ../bin/activate
exec uwsgi --module guyamoe.wsgi --socket ./nginx/socket/guya.sock --chmod-socket=664 --enable-threads
