#!/usr/bin/node
// a script that computes the number of tasks completed by user id.
const request = require('request');
const completed = {};
request(process.argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    for (const task of JSON.parse(body)) {
      if (task.completed === true) {
        if (!(task.userId in completed)) {
          completed[task.userId] = 1;
        } else {
          completed[task.userId] += 1;
        }
      }
    }
  }
  console.log(completed);
});
