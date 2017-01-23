FROM nginx:1.11

# where the certificates are
VOLUME /etc/letsencrypt/archive
# where the latest certificates are
VOLUME /etc/letsencrypt/live

ENV SRC /usr/src/web

RUN mkdir -p ${SRC}
WORKDIR ${SRC}

RUN echo "deb http://ftp.debian.org/debian jessie-backports main" > /etc/apt/sources.list.d/backports.list \
  && apt-get -qq update \
  && apt-get install -y -qq cron \
  && apt-get install -y -qq -t jessie-backports certbot \
  && rm -rf /var/lib/apt/lists/*

# auto renew service
COPY certbot.timer /etc/systemd/system/
COPY certbot.service /etc/systemd/system/
COPY entrypoint.sh ./
COPY default.conf ./
COPY default.conf.dev ./

EXPOSE 80
EXPOSE 443

ENTRYPOINT ["./entrypoint.sh"]

