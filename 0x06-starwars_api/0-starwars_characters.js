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

async function starwarsCharacters(filmId) {
  try {
    const endpoint = 'https://swapi-api.hbtn.io/api/films/' + filmId;
    let response = await request(endpoint);
    const filmData = JSON.parse(response.body);
    const characters = filmData.characters;

    for (const urlCharacter of characters) {
      try {
        const characterResponse = await request(urlCharacter);
        const character = JSON.parse(characterResponse.body);
        console.log(character.name);
      } catch (characterError) {
        console.error("Error fetching character data:", characterError.message);
      }
    }
  } catch (error) {
    console.error("Error fetching film data:", error.message);
  }
}

starwarsCharacters(filmID);
