FROM node:latest

ENV USR node
ENV SRC /usr/src/ux

VOLUME ${SRC}/dist

# disable progress bar (speed up)
RUN npm set progress=false
# silent, global npm install (speed up)
RUN npm install gulp@3.9.1 -s -g

RUN mkdir -p ${SRC}
WORKDIR ${SRC}

# silent npm install (speed up)
COPY package.json ./
RUN npm install -s

COPY semantic.json ./
COPY semantic-ui ./
RUN npm install semantic-ui@2.2.7 \
  && gulp --cwd=semantic-ui build \
  && npm cache clean

COPY . ./
RUN chown -R ${USR}:${USR} ./
USER ${USR}
