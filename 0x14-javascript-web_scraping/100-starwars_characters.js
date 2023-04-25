#!/usr/bin/node
//  a script that prints all characters of a Star Wars movie
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (err, response, body) {
  if (!err) {
    const chars = JSON.parse(body).characters;
    chars.forEach((chars) => {
      request(chars, function (err, response, body) {
        if (!err) {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
