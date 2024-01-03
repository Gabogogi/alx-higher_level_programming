#!/usr/bin/node
const request = require('request');

const filmNo = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';
const peopleUrl = 'https://swapi-api.alx-tools.com/api/people/';
const completeUrl = url + filmNo;
// get the details of te film
request.get(completeUrl, (error, response) => {
  if (error) {
    console.error('error');
  } else {
    const myResponse = JSON.parse(response.body);
    // console.log(myResponse);
    const myUrls = myResponse.characters;
    // console.log(myResponse.title);
    const numericIds = myUrls.map(url => parseInt(url.match(/\/(\d+)\/$/)[1], 10));
    // console.log(numericIds);
    // get people's names from aboe iDS
    for (let i = 0; i < numericIds.length; i++) {
      const finalUrl = peopleUrl + numericIds[i];
      request.get(finalUrl, (error, resp) => {
        if (error) {
          console.log(error);
        } else {
          const peopleResponse = JSON.parse(resp.body);
          console.log(peopleResponse.name);
        }
      });
    }
  }
});
