FROM python:3.6

ENV USER nonroot
ENV SRC /usr/src/code
ENV FLASK_RUN ${SRC}/autoapp.py

# shared volumes may give some headaches if id is not 1000
RUN groupadd -g 1000 ${USER} \
  && useradd --create-home --home-dir=${SRC} -u 1000 -g ${USER} ${USER}

WORKDIR ${SRC}

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . ./
RUN chown -R ${USER}:${USER} ${SRC}
USER ${USER}
