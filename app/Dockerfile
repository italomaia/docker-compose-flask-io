FROM python:3.6

ENV USER nonroot
ENV SRC /usr/src/code

# shared volumes may give some headaches if id is not 1000
RUN groupadd -g 1000 ${USER} \
  && useradd -m -d ${SRC} -u 1000 -g ${USER} ${USER}

WORKDIR ${SRC}
COPY . ./
RUN pip install -r requirements.txt
RUN chown -R ${USER}:${USER} ${SRC}
USER ${USER}
