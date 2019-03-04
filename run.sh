#!/bin/bash

docker rm -f codectool
docker build -t chiflux/codectool . && docker run --name=codectool -p 8080:8080 -it chiflux/codectool
