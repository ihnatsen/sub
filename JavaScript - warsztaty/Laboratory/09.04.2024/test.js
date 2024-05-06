person_one = {name:'Ivan', age: 22, email:"node@jsmail.com"};
person_two = {name:'Anna', age: 32, email:"node@jsmail.com"};
person_three = {name:'Kate', age: 23, email:"python@py.com"};

list = [person_one, person_two];
empty_list = [];

function checking(object, lst){
    if(lst.length===0){
        return false;
    }
    for(let i= 0; i< list.length; i++) {
        if(object.name === lst[i].name){
            return true;
        }
    }
    return false
}
console.log(checking(person_three,mpty_list));