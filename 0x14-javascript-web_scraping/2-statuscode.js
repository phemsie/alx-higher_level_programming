#!/usr/bin/node
// a script that display the status code of a GET request.
const request = require('request');
request(process.argv[2], function (err, response, body) {
  if (err) {
    return console.log(err);
  }
  console.log('code:', response && response.statusCode);
});
