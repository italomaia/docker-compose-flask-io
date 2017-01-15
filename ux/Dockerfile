FROM node:latest

ENV SRC /usr/src/ux

# disable progress bar (speed up)
RUN npm set progress=false
# silent, global npm install (speed up)
RUN npm install gulp -s -g

RUN mkdir -p ${SRC}
WORKDIR ${SRC}

COPY package.json ./
COPY semantic.json ./
# silent npm install (speed up)
RUN npm install -s
COPY . ./

VOLUME ${SRC}/dist
