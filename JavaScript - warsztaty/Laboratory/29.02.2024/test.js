lst =['Ivan Ihnatsenkau', 'Anna Pop']
function test(name) {
    for(let i =0; i<lst.length; ++i){
        if(lst[i] == name){
            return true
        }
    }
    return false
}
console.log(test('Anna Pop'))
console.log('Anna Pop' in lst)