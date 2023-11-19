// 传统函数表达式
const add = function (x, y) {
    return x + y;
};

// 箭头函数
const addArrow = (x, y) => x + y;

//const 是在JavaScript中声明常量的关键字。使用 const 关键字声明的变量在整个生命周期中保持不变，即它的值一旦被赋予就不能被修改。
console.log(add(1, 2))
console.log(addArrow(1, 2))

// 块级声明
/**
 * 在ES6中新增了使用let关键字声明变量的方式。let的用法和var类似，
 * 所不同的是，使用let声明的变量只在let所在的代码块内有效。
 * 这个警告意味着你在代码中使用了 `var` 关键字，而不是推荐使用的 `let` 或 `const` 关键字。
 * 在现代JavaScript中，`let` 和 `const` 更常用，而 `var` 有一些不足之处。
 *
 * 主要的区别如下：
 * 1. **作用域：**
 *    - `var` 声明的变量具有函数作用域，而不是块级作用域。这意味着在函数内部声明的 `var` 变量在整个函数内都是可见的。
 *    - `let` 和 `const` 声明的变量具有块级作用域，它们在包含它们的块（例如，`if` 语句、`for` 循环等）内可见，而在块之外不可见。
 *
 * 2. **变量提升：**
 *    - 在函数作用域中，`var` 声明的变量会被提升到函数的顶部，而在块级作用域中（`if` 语句、`for` 循环等），`var` 也会被提升到包含块的顶部。
 *    - `let` 和 `const` 声明的变量不会发生变量提升，而且在声明之前访问它们会引发一个暂时性死区错误（Temporal Dead Zone，TDZ）。
 *
 * 3. **重复声明：**
 *    - 使用 `var` 可以多次声明相同的变量名而不引发错误。
 *    - 使用 `let` 或 `const` 尝试重复声明相同的变量名会引发错误。
 *
 * 推荐在现代JavaScript中使用 `let` 或 `const`，并根据变量是否需要重新赋值来选择使用哪一个。如果变量的值不会被重新赋值，
 * 最好使用 `const`，以提高代码的可读性和可维护性。
 */

{
    var a = 10;
    a = a + 1;
    let b = 20;
}
console.log(a);   //10
//console.log(b);   //报错：b没有定义

for (let i = 0; i < 10; i++) {
    console.log(i)
}
//document.write(i);              //报错：i没有定义

let str = "月落乌啼霜满天，\
     江枫渔火对愁眠。\
     姑苏城外寒山寺，\
     夜半钟声到客船。"
console.log(str)

str = "月落乌啼霜满天，"
    + "江枫渔火对愁眠。"
    + "姑苏城外寒山寺，"
    + "夜半钟声到客船。"
//定义的属性 不能多次定义
console.log(str);

{
    let name = "Tony";
    let sex = "男";
    let age = 25;
    let str = `姓名：${name} 性别：${sex} 年龄：${age}`;
    console.log(str);
}

{
    let unitPrice = 566;                            //商品单价
    let number = 6;                                 //商品数量
    let str = `商品总价：${unitPrice * number}元`;
    console.log(str);
}

function table(width, height, rows, cols) {
    width = width || 300;   // 如果 width 未定义或者为假，结果为 300
    height = height || 200;
    rows = rows || 6;
    cols = cols || 3;

    console.log(cols)
    console.log(rows)
    console.log(height)
    console.log(width)
}

function table2(width = 200, height = 100, rows = 4, cols = 5) {
    table(width, height, rows, cols)
}

table2(null, 100, null, 100)

function compare(...args) {
    let maxValue = 0;
    for (let i = 0; i < args.length; i++) {
        if (args[i] > maxValue) {
            maxValue = args[i];
        }
    }
    return maxValue;
}

console.log("最大值", compare(1, 2, 3, 4, 5, 6, 100))

function person(name, sex, age, ...interest) {
    let info = "";
    info = `姓名:${name} \n年龄:${age} \n性别:${sex} `;
    for (let i = 0; i < interest.length; i++) {
        info += `\n兴趣:${interest[i]}`
    }
    return info;
}

console.log(person("罗盛林", "男", "22", "放屁", "购物"))

{
    let person = {
        name: "罗盛林",
        sex: "男",
        age: 12
    }

    let{name,age,sex}=person
    console.log(name)
    console.log(age)
    console.log(sex)
}

{
    let person = {
        name: "罗盛林",
        sex: "男",
        age: 12
    }

    let name;
    let age;
    let sex;
    ({name,age,sex}=person)
    console.log(name)
    console.log(age)
    console.log(sex)
}

{
    let person = ["Tony", "Kelly", "Jerry"];
    let [a, b, c] = person;
    console.log(a);                           //Tony
    console.log(b);                           //Kelly
    console.log(c);                           //Jerry
    let [, , d] = person;
    console.log(d);                           //Jerry

    let a1, b1, c1;
    [a1, b1, c1] = person;
    console.log(a1);                           //Tony
    console.log(b1);                           //Kelly
    console.log(c1);                           //Jerry
}

{
    function product(a, b, c){
        return a * b * c;
    }
    let arr = [3, 5, 6];
    console.log(product(...arr));  //90

    let arr1 = ["Tony", "Kelly"];
    let arr2 = ["Tom", "Jerry"];
    console.log([...arr1, ...arr2]);  //['Tony', 'Kelly', 'Tom', 'Jerry']

    let arr3 = ["Tony", "Kelly", "Tom", "Jerry"];
    let [name1, name2, ...name3] = arr3;
    console.log(name1);                           //Tony
    console.log(name2);                           //Kelly
    console.log(name3);                           //['Tom', 'Jerry']
}



