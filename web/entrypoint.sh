#!/bin/bash

set -e

setup_certificate(){
  if [ ! -e "$WEBROOT/.well-known/acme-challenge" ]; then
    local CMD="certbot certonly --webroot -w $WEBROOT --agree-tos -m ${DOMAIN_MAIL}"
    for domain in "${DOMAINS[@]}"
    do
      CMD="$CMD -d ${domain}"
    done
    sh -c "$CMD"
  fi
  # our certificate renew job
  sh -c "systemctl start certbot.timer"
}

# setup correct nginx configuration file
if [ $FLASK_DEBUG == '1' ]; then
  echo "DEBUG MODE"
  envsubst < default.conf.dev > /etc/nginx/conf.d/default.conf
else
  setup_certificate
  envsubst < default.conf > /etc/nginx/conf.d/default.conf
fi

# run web server
exec nginx -g 'daemon off;'
