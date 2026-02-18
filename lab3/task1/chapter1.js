alert ('I am Javascript')

alert(3 +
1
+ 2);

(function() {
  'use strict';

  // ...ваш код...
})()

let admin, name1;
name = "Jhon";
admin = name;
alert(admin);


let planet_name = "Earth";
let current_usname = "jhon"


const birthday = '18.04.1982';

const age = someCode(birthday);

// 2.5
let name2 = "Ilya";

alert( `hello ${1}` ); // hello 1

alert( `hello ${"name"}` ); // hello name

alert( `hello ${name2}` ); // hello Ilya

// 2.6
let name = prompt("What is your name?", "");
alert(name);

let a = 1, b = 1;

alert( ++a ); // 2
alert( b++ ); // 1

alert( a ); // 2
alert( b ); // 2 

// Basic operators, maths
let apples = "2";
let oranges = "3";

// both values converted to numbers before the binary plus
alert( +apples + +oranges ); // 5

// the longer variant
// alert( Number(apples) + Number(oranges) ); // 5

// task
let aa = 1, bb = 1;

let c = ++aa; // 2
let d = bb++; // 2


5 > 4
"apple" > "pineapple"
"2" > "12"
undefined == null
undefined === null
null == "\n0\n"
null === +"\n0\n"


'use strict';

    let value = prompt('What is the "official" name of JavaScript?', '');

    if (value == 'ECMAScript') {
      alert('Right!');
    } else {
      alert("You don't know? ECMAScript!");
    }
