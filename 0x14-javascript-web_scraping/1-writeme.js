#!/usr/bin/node
// a script that Reads and writes content to a file.
const fs = require('fs');
fs.writeFile(process.argv[2], process.argv[3], function (err) {
  if (err) {
    return console.log(err);
  }
});
