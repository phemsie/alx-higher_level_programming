#!/usr/bin/node
// a script that reads and prints the content of a file.
const fs = require('fs');
fs.readFile(process.argv[2], 'utf-8', function (err, contents) {
  if (err) {
    return console.log(err);
  }
  console.log(contents);
});
