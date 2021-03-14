// var line = 5;
// for(var i=0; i<=line; i++){
//     var star = '';
//     var empty = '';
//     for(var j=5-i;j>0; j--){
//         star+= '*';
//     }
//     empty+=' '.repeat(i);
//     console.log(star+empty);
// }

var line = 5;
var star = '';

for(var i = line ; i >= 1; i--){
    for(var j= 1 ; j <= i ; j++){
        star+= '*';
    }
    star += '\n';
}
console.log(star);