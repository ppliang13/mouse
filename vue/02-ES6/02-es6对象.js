{
    let name="罗盛林";
    let sex="男";
    let age=10;

    let key="name";

    let person={
        [key]:name,
        sex:sex,
        age:age,

        age2: (age) => age, // 修正箭头函数的位置

        show(){
            console.log(`名字:${name}`)
        },
        age(){
            return age;
        }
    }
    console.log(person)
    person.show()
    console.log(person.age)


    //动态属性名
    person.happy="放屁";
    console.log(person);
}


{
    var type = "手机";
    var obj = {
        type: "电脑",
        show: function(){
            setTimeout(() => console.log(this.type), 3000);
        }
    }
    obj.show();  //电脑
}