{
    var promise=new Promise(function (resolve, reject) {
        setTimeout(function (){
            try {
                let a=5+7;
                resolve(a);
            }catch (ex){
                reject(ex)
            }
        },1000);
    })

    promise.then(function (value){
        console.log(value);
    },function (error){
        console.log(error.message)
    })
}

import {PersonObj} from './05-类对象.js';
{
    console.log(PersonObj);
}

// Cannot use import statement outside a module