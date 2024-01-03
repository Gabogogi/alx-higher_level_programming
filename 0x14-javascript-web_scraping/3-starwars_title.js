#!/usr/bin/node
const request = require('request');

const filmNo = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';
const completeUrl = url + filmNo;
// get the details of te film
request.get(completeUrl, (error, response) => {
  if (error) {
    console.error('error');
  } else {
    const myResponse = JSON.parse(response.body);
    console.log(myResponse.title);
  }
});
