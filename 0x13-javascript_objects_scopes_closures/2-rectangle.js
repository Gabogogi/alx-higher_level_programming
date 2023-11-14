#!/usr/bin/node
// JS Script to define, initialize values if positive integer
class Rectangle {
    constructor (w, h) {
        if (w <= 0 || h <= 0 || w === undefined || h === undefined) {
            return this;
        } else {
            this.width = w;
            this.height = h;
        }
    }
}
module.exports = Rectangle;

rect = new Rectangle(5);
console.log(rect)