#!/bin/bash

if [ "$1" == "" ]; then
echo "usage: start_services.sh <fully_qualified_domain_name>"
exit 1
fi

FQDN="$1"
echo "FQDN=$FQDN"

docker network create proxy

docker stack deploy -c proxy-compose.yml proxy

docker service rm codectools
docker service create --name=codectools --mode=replicated --replicas=1 --network=proxy \
                      --label com.df.notify=true --label com.df.port=8080 --label com.df.serviceDomain=$FQDN \
                      chiflux/codectool

