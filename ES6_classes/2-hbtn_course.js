export default class HolbertonCourse {
    constructor(name, length, students){
      this._name = this._verifyString(name, 'Name');
      this._length = this._verifyNumber(length, 'Length');
      this._students = this._verifyArray(students, 'Students');
    }

    get name() {
      return this._name;
    }

    get length() {
      return this._length;
    }

    get students() {
      return this._students;
    }

    set name(newName) {
      this._name = this._verifyString(newName, 'Name');
    }

    set length(newLength) {
      this._length = this._verifyNumber(newLength, 'Length');
    }

    set students(newStudents) {
      this._students = this._verifyArray(newStudents, 'Students');
    }

    _verifyString(value, attribute) {
      if(typeof value !== 'string') {
        throw new TypeError(`${attribute} must be a string`);
      }
      return value;
    }

    _verifyNumber(value, attribute) {
      if (typeof value !== 'number' || isNaN(value)) {
        throw new TypeError(`${attribute} must be a number`);
      }
      return value;
    }

    _verifyArray(value, attribute) {
      if (!Array.isArray(value) || value.some((student) => typeof student !== 'string')) {
        throw new TypeError(`${attribute} must be an array of strings`);
      }
      return value;
    }
  }
