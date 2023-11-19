class Person {
    constructor(name, age, sex) {
        this.name = name;
        this.age = age;
        this.sex = sex;
    }
}

var person = new Person("罗盛林", 10, "男");
console.log(person);
var b = Number.isInteger("90");
console.log(!b)
export {person,Person as PersonObj};

