// for(var i=5; i>0; i--){
//     var empty='';
//     for(var j=(i*2)-1;j>=i*2-1; j--){
//         var star = '';
//         star+= '*'.repeat(j)
//     }
//     empty=' '.repeat(5-i)
//     console.log(empty+star);
// }

var line = 5;
var star='';

for(var i=line; i>=0; i--){
    for(var j=line-i ; j>0 ; j--){
        star+=' ';
    }
    for(var k=(i*2)-1 ; k>0 ; k--){
        star+='*';
    }
    for(var z=line-i ; z>0;z--){
    star+=' ';
    }
    star+='\n';
}
console.log(star)