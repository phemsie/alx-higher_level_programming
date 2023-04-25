#!/usr/bin/node
// a script that gets the contents of a webpage and stores it in a file.

const request = require('request');
const fs = require('fs');
request(process.argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    fs.appendFile(process.argv[3], body, function (err) {
      if (err) {
        return console.log(err);
      }
    });
  }
});
