// var line = 5;
// var empty = '';
// for(var i=5; i>0; i--){
//     var star = '';
//     for(var j=i;j>0; j--){
//         star+= '*';
//     }
//     console.log(star);
// }


var line = 5;
var star = '';

for(var i = line ; i >= 1; i--){
    for(var j= 1 ; j <= i ; j++){
        star+= '*';
    }
    star += '\n';
    for(var k = line-i; k>=0; k--){
        star+=' ';
    }
}
console.log(star);