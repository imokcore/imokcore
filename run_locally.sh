#!/usr/bin/env bash

docker build . -t im-ok-core
docker run -e STARBUG_CLUSTER='' \
--rm -p 8080:8080 im-ok-core:latest
