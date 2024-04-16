object_one = {name: 'Ivan', age: 22 }
object_two = {name: 'Ivan', age: 22 }
object_three = {name: 'Ivan', age: 22 }
object_four = {name: 'Ooo', age: 22 }
list = [object_one, object_two, object_three]

function checking(object, listObject){
    let parseObject = JSON.stringify(object)
    for(let index= 0; index<listObject.length; index++){
        if(parseObject === JSON.stringify(listObject[index])){
            return false
        }
    return true
    }
}
console.log(checking(object_four,list))