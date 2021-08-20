// var line = 5;

// for(var i=1; i<=line; i++){
//     var star = '';
//     var empty ='';
//     for(var j=0;j<i; j++){
//         star+= '*';
//     }
//     empty +=' '.repeat(line-i)
//     console.log(empty+star);
// }

var line = 5;
var star = '';

for(var i = 1; i <= line; i++){
    for(var j = line-i; j > 0; j--){
        star += ' ';
    }
    for(var k = 1; k <= i; k++){
        star += '*';
    }
    star += '\n';
}
console.log(star);