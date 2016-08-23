#!/bin/bash
set -eu

echo 'Installing python deps ...'
pip install -r requirements.txt
echo ''

echo 'Installing JavaScript deps ...'
npm install
npm install -g browserify
echo ''

echo 'Copying artifacts into `./static` ...'
cp -v ./node_modules/browser-filesaver/FileSaver.js ./static/FileSaver.js
cp -v ./node_modules/clipboard/dist/clipboard.min.js ./static/clipboard.min.js
echo ''

echo 'Running browserify ...'
echo '  * removing old `./static/bundle.js` ...'
rm -f ./static/bundle.js

echo '  * creating new `./static/bundle.js` ...'
browserify main.js -o static/bundle.js
echo ''

echo '~Fin'
