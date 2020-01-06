#!/usr/bin/env bash

`docker exec -it phabricator_phabricator_1 bash

/opt/bitnami/phabricator/bin/config set phabricator.base-uri 'http://matrix.phabricator.com:7098'`
`docker-compose restart`
