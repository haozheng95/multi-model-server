#!/usr/bin/env bash

`docker exec -it phabricator_phabricator_1 bash

/opt/bitnami/phabricator/bin/config set phabricator.base-uri 'http://www.multi-git.com'`
`docker-compose restart`
