#!/usr/bin/node
import {argv} from 'node:process';

if (argv[2] !== undefined)
{
	console.log(argv[2]);
}
else
{
	console.log('No argument');
}
