FROM python:3-slim

RUN mkdir -p /srv/xml_transform

COPY ./ /srv/xml_transform/

RUN apt-get update -y && \
    apt-get install -y \
      curl \
      build-essential \
      lib32z1-dev \
      libxml2-dev \
      libxslt1-dev \
      nodejs \
      python3-dev && \
    (curl -sL https://deb.nodesource.com/setup_6.x | bash -) && \
    apt-get install -y nodejs && \
    apt-get clean -y

RUN cd /srv/xml_transform && ./build.sh

CMD gunicorn --pythonpath /srv/xml_transform --bind 0.0.0.0 --log-level info --log-file - --access-logfile - xml_transform:app
