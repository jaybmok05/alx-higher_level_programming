** 0x13-javascript_objects_scopes_closures **
---
This directory will contain a series of tasks on javascript_objects_scopes_closures
---

- Task 0 - Write an empty class Rectangle that defines a rectangle:
        - You must use the class notation for defining your class

- Task 1 : Continuation
        - The constructor must take 2 arguments w and h
        - Initialize the instance attribute width with the value of w
        - Initialize the instance attribute height with the value of h

- Task 2 : continuation
        - If w or h is equal to 0 or not a positive integer, create an empty object.

- Task 3 : continuation
        - Create an instance method called print() that prints the rectangle using the character X
 
- Task 4 : conntinuation
        - Create an instance method called rotate() that exchanges the width and the height of the rectangle
        - Create an instance method called double() that multiples the width and the height of the rectangle by 2.

- Task 5 : Write a class Square that defines a square and inherits from Rectangle of 4-rectangle.js:
        - You must use the class notation for defining your class and extends
        - The constructor must take 1 argument: size
        - The constructor of Rectangle must be called (by using super())

- Task 6 : continuation of class square
        - Create an instance method called charPrint(c) that prints the rectangle using the character c
                - If c is undefined, use the character X

- Task 7 : Write a function that returns the number of occurrences in a list:
	- Prototype: exports.nbOccurences = function (list, searchElement)

- Task 8 - Write a function that returns the reversed version of a list:
	- Prototype: exports.esrever = function (list)
	- You are not allow to use the built-in method reverse

- Task 9 - Write a function that prints the number of arguments already printed and the new argument value. 
	- Prototype: exports.logMe = function (item)
	- Output format: <number arguments already printed>: <current argument value>

- Task 10 - Write a function that converts a number from base 10 to another base passed as argument:
	- Prototype: exports.converter = function (base)
	- You are not allowed to import any file
	- You are not allowed to declare any new variable (var, let, etc..)
