FROM python:3-slim

RUN mkdir -p /srv/xml_transform
COPY ./ /srv/xml_transform/
RUN apt-get update -y && apt-get install build-essential lib32z1-dev libxml2-dev libxslt1-dev python3-dev -y && apt-get clean -y
RUN pip install -r /srv/xml_transform/requirements.txt

CMD gunicorn --pythonpath /srv/xml_transform --bind 0.0.0.0 --log-level info --log-file - --access-logfile - xml_transform:app
