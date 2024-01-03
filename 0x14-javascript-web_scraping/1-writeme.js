#!/usr/bin/node
const fs = require('fs');

const filePath = process.argv[2];
const data = process.argv[3];

// write to file in utf-8 encoding
fs.writeFile(filePath, data, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
