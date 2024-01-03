#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a Movie ID as the first argument.');
  process.exit(1);
}

const filmUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Fetch film details
request.get(filmUrl, (error, response) => {
  if (error) {
    console.error('Error:', error);
  } else {
    const filmData = JSON.parse(response.body);

    // Display characters in the order of appearance in the film
    filmData.characters.forEach(characterUrl => {
      request.get(characterUrl, (error, characterResponse) => {
        if (error) {
          console.error('Error:', error);
        } else {
          const characterData = JSON.parse(characterResponse.body);
          console.log(characterData.name);
        }
      });
    });
  }
});
