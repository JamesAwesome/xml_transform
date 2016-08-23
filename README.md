# XML Transform Utility

This is a simple webapp which applies an XSLT to some XML via a copy/paste
webform.

## Known Issues

* XML must not contain an encoding in the decleration: (WRONG: `<?xml version="1.0" encoding="UTF-8" ?>` RIGHT: `<?xml version="1.0" ?>`)

## Supports
 * Python3
 * Node 6

## Usage

This app uses webforms, so you need to supply a CSRF token to prevent cross site
scripting attacks. You can do this via openssl with the following command:

`openssl rand -base64 64`

### Manual Installation

```bash
git clone git@github.com:jamesawesome/xml_transform
cd xml_transform/
./build.sh
export XML_TRANSFORM_SECRET_KEY=<YOUR CSRF TOKEN>
gunicorn --pythonpath /srv/xml_transform --bind 0.0.0.0 --log-level info --log-file - --access-logfile - xml_transform:app
```

### Docker

```bash
docker pull jamesawesome/xml_transform
docker run -d -e "XML_TRANSFORM_SECRET_KEY=<YOUR CSRF TOKEN>" -p 8000:8000 jamesawesome/xml_transform
```
