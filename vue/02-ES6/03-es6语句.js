//数组循环
{
    const numbers = [1, 2, 3, 4, 5];

    for (const num of numbers) {
        console.log(num);
    }
}
//对象键值对循环
{
    const person = {
        name: "John",
        age: 30,
        gender: "male"
    };

    for (const key in person) {
        console.log(key, person[key]);
    }
}

//foreach
{
    const colors = ["red", "green", "blue"];

    colors.forEach(color => {
        console.log(color);
    });

}

//map set
{
    const myMap = new Map([[1, "one"], [2, "two"], [3, "three"]]);

    for (const [key, value] of myMap) {
        console.log(key, value);
    }

    const mySet = new Set([1, 2, 3]);

    for (const num of mySet) {
        console.log(num);
    }

}

//条件语句
{
    const age = 18;

// 使用三元运算符
    const message = age >= 18 ? "You are an adult" : "You are a minor";

    console.log(message);

// 使用模板字符串
    if (age >= 18) {
        console.log(`You are ${age} years old. You are an adult.`);
    } else {
        console.log(`You are ${age} years old. You are a minor.`);
    }

}

//while
{
    let count = 0;

    while (count < 5) {
        console.log(count);
        count++;
    }
}

//do while
{
    let count = 0;

    do {
        console.log(count);
        count++;
    } while (count < 5);
}

//switch
{
    let day = 3;
    let dayName;

    switch (day) {
        case 1:
            dayName = "Monday";
            break;
        case 2:
            dayName = "Tuesday";
            break;
        case 3:
            dayName = "Wednesday";
            break;
        case 4:
            dayName = "Thursday";
            break;
        case 5:
            dayName = "Friday";
            break;
        default:
            dayName = "Unknown";
    }

    console.log(dayName);
}