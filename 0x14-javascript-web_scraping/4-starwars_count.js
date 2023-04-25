#!/usr/bin/node
// a script that prints the number of movies where the character “Wedge Antilles” is present
const request = require('request');
let count = 0;
request(process.argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const movies = JSON.parse(body).results;
    for (let i = 0; i < movies.length; i++) {
      for (let j = 0; j < movies[i].characters.length; j++) {
        if (movies[i].characters[j].search('/18/') > 0) {
          count++;
        }
      }
    }
  }
  console.log(count);
});
