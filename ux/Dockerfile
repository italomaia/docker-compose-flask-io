FROM node:latest

ENV USR node
ENV SRC /usr/src/ux

VOLUME ${SRC}/dist

# disable progress bar (speed up)
RUN npm set progress=false
# silent, global npm install (speed up)
RUN npm install gulp -s -g

RUN mkdir -p ${SRC}
WORKDIR ${SRC}

# silent npm install (speed up)
RUN npm install -s

COPY . ./
RUN chown -R ${USR}:${USR} ./
USER ${USR}

