#!/usr/bin/node

const req = require('request');

const url = process.argv[2];
req.get(url, (error, resp, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  const tasks = JSON.parse(body);
  const taskCompleted = {};

  tasks.forEach(task => {
    if (task.completed) {
      if (taskCompleted[task.userId]) {
        taskCompleted[task.userId]++;
      } else {
        taskCompleted[task.userId] = 1;
      }
    }
  });
  console.log(taskCompleted);
});
