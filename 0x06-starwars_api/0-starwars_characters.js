#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.log('Please provide a movie ID as a command line argument.');
  process.exit(1);
}

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error occurred:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch data. Status code:', response.statusCode);
    process.exit(1);
  }

  const film = JSON.parse(body);
  const charactersUrls = film.characters;

  const fetchCharacters = (urls, index) => {
    if (index >= urls.length) return;
    request(urls[index], (error, response, body) => {
      if (error) {
        console.error('Error occurred:', error);
        return;
      }
  
      if (response.statusCode !== 200) {
        console.error('Failed to fetch character data. Status code:', response.statusCode);
        return;
      }
  
      const character = JSON.parse(body);
      console.log(character.name);
      fetchCharacters(urls, index + 1);
    });
  };

  fetchCharacters(charactersUrls, 0);
});
