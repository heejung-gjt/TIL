// var line = 5;
// var star = '';

// for(var i=1; i<=line; i++){
//     for(var j=i ; j<=i; j++){
//         star+= '*';
//         console.log(star);
//     }
// }

var line = 5;
var star = '';

for(var i=1; i<=line; i++){
    for(var j=1;j<=i; j++){
        star+= '*';
    }
    star+='\n';
}
console.log(star);
