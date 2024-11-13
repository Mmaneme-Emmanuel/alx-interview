#!/usr/bin/node
/**
 * This script fetches and prints the names of all characters from a specified
 * Star Wars movie, based on the movie ID provided as a command-line argument.
 * It uses the Star Wars API (https://swapi-api.hbtn.io/) to retrieve the movie 
 * details, then makes additional requests to get each character's name in the 
 * same order as listed in the API.
 * 
 * Usage: node script.js <filmID>
 * Example: node script.js 3
 */
const util = require('util');
const request = util.promisify(require('request'));
const filmID = process.argv[2];

async function starwarsCharacters (filmId) {
  const endpoint = 'https://swapi-api.hbtn.io/api/films/' + filmId;
  let response = await (await request(endpoint)).body;
  response = JSON.parse(response);
  const characters = response.characters;

  for (let i = 0; i < characters.length; i++) {
    const urlCharacter = characters[i];
    let character = await (await request(urlCharacter)).body;
    character = JSON.parse(character);
    console.log(character.name);
  }
}

starwarsCharacters(filmID);

