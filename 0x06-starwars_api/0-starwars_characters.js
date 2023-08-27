#!/usr/bin/node

const request = require('request');
const argv = require('process').argv;

const requestPromise = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      }
      resolve(JSON.parse(body));
    });
  });
};

const printCharacters = async (filmId) => {
 try {
    const film = await requestPromise(`https://swapi-api.alx-tools.com/api/films/${filmId}`);
    const charactersUrl = await film.characters;
    for (const url of charactersUrl) {
      const character = await requestPromise(url);
      const name = await character.name;
      console.log(name);
    }
  } catch (err) {

  }
};

printCharacters(argv[2]);
