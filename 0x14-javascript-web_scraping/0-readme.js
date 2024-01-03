#!/usr/bin/node
const fs = require('fs');

const filePath = process.argv[2];

// read file in utf-8 encoding
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
