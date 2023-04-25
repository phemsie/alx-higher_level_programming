#!/usr/bin/node
//  a script that prints the title of a Star Wars movie by episode number
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (err, response, body) {
  if (err) {
    return console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
