#!/usr/bin/node
import { argv } from 'node:process';

if (!isNaN(parseInt(argv[2], 10))) {
  console.log('My number: ' + parseInt(argv[2]));
} else {
  console.log('Not a number');
}
