#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const data = 'https://swapi-api.hbtn.io/api/films/' + movieId;
let people = [];
const names = [];

const checkfilms = async () => {
  await new Promise(resolve => request(data, (err, res, body) => {
    if (err || res.statusCode !== 200) {
      console.log(err | res.statusCode);
    } else {
      const film = JSON.parse(body);
      people = film.characters;
      resolve();
    }
  }));
};

const fetchname = async () => {
  if (people.length > 0) {
    for (const person of people) {
      await new Promise(resolve => request(person, (err, res, body) => {
        if (err || res.statusCode !== 200) {
          console.log(err | res.statusCode);
        } else {
          const character = JSON.parse(body);
          names.push(character.name);
          resolve();
        }
      }));
    }
  }
};

const display = async () => {
  await checkfilms();
  await fetchname();
  if (names.length === people.length) {
    names.forEach(name => console.log(name));
  }
};

display();
