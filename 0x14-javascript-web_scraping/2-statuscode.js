#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

// display status code of a GET request
request.get(url, (error, response) => {
  if (error) {
    console.error('error');
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
