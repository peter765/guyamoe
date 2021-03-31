#!/bin/bash
export ALLOWED_HOSTS=mahoushoujobu.com
source ../bin/activate && uwsgi --module guyamoe.wsgi --socket ./nginx/socket/guya.sock --chmod-socket=664 --master --enable-threads
