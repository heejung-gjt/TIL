## 제어문 연습 문제

#### 1. 변수 x가 10보다 크고 20보다 작을때 변수 x를 출력하는 조건식을 완성해라     

```Javascript
var x = 15;

if (x > 10 && x < 20) {
  console.log(x);
}
```

<br>

#### 2. for문을 사용하여 0부터 10미만의 정수 중에서 짝수만을 작은 수부터 출력하시오.    


```Javascript
for(var i = 0; i < 10; i++){
  if (i%2 == 0){
    console.log(i);
  }
}
```

<br>

#### 3.  for문을 사용하여 0부터 10미만의 정수 중에서 짝수만을 작은 수부터 문자열로 출력하시오. 


```Javascript
var words= '';

for(var i = 0; i < 10; i++){
  if(i % 2 == 0){
     words += i;
   }
}
console.log(words);
```

<br>

#### 4. for문을 사용하여 0부터 10미만의 정수 중에서 홀수만을 큰수부터 출력하시오 


```Javascript
for(var i = 9; i > 0; i--){
  if(i % 2 == 1){
    console.log(i);
  }
}
```

<br>

#### 5. while문을 사용하여 0 부터 10 미만의 정수 중에서 짝수만을 작은 수부터 출력하시오.


```Javascript
var i = 0;

while (i < 10){
    console.log(i);
    i += 2;
} 
```

<br>

#### 6. while문을 사용하여 0 부터 10 미만의 정수 중에서 홀수만을 큰수부터 출력하시오.


```Javascript
var i = 9;

while(i > 0){
    console.log(i);
    i -= 2;

}
```

<br>

#### 7. for 문을 사용하여 0부터 10미만의 정수의 합을 출력하시오.

```Javascript
var sum = 0;

for(var i = 0; i < 10; i++){
    sum += i;
}
console.log(sum);
```

<br>

#### 8. 1부터 20 미만의 정수 중에서 2 또는 3의 배수가 아닌 수의 총합을 구하시오.

```Javascript
var sum = 0;

for(var i = 1; i < 20; i++){
    if(i % 2 != 0 && i % 3 != 0){
        sum += i;
    }
}
console.log(sum);
```

<br>

#### 9. 1부터 20 미만의 정수 중에서 2 또는 3의 배수인 수의 총합을 구하시오.

```Javascript
var sum = 0;

for(var i = 1; i < 20; i++){
    if(i % 2 == 0 || i % 3 == 0){
        sum += i;
    }
}
console.log(sum);
```

<br>

#### 10. 두 개의 주사위를 던졌을 때, 눈의 합이 6이 되는 모든 경우의 수를 출력하시오.

```Javascript
for(var i = 1; i < 6; i++){
    for(var j = 1; j < 6; j++){
        if(i + j == 6){
            console.log(`[ ${i}, ${j} ]`);
        }
    }
}
```

<br>

#### 11. *(별)로 높이가 5인(var line = 5) 삼각형을 문자열로 완성하라. 개행문자(‘\n’)를 사용하여 개행한다. 완성된 문자열의 마지막은 개행문자(‘\n’)로 끝나도 관계없다.

```내풀이```
```Javascript
var line = 5;
var star = '';

for(var i=1; i<=line; i++){
    for(var j=i;j<=i; j++){
        star+= '*';
        console.log(star);
    }
}
```
```참고한 풀이```
```Javascript
var line = 5;
var star = '';

for(var i = 1; i <= line; i++){
    for(var j = 1;j <= i; j++){
        star += '*';
    }
    star += '\n';
}
console.log(star);

```

<br>

#### 12. *(별)로 트리를 문자열로 완성하라. 개행문자(‘\n’)를 사용하여 개행한다. 완성된 문자열의 마지막은 개행문자(‘\n’)로 끝나도 관계없다.

```내풀이```    
```Javascript
var line = 5;

for(var i=0 ; i<=line ; i++){
    var star = '';
    var empty = '';
    for(var j=5-i ; j>0 ; j--){
        star+= '*';
    }
    empty+=' '.repeat(i);
    console.log(empty+star);
}
```
```11번 참고한 내풀이```
```Javascript
var line = 5;
var star = '';

for(var i = line ; i >= 1; i--){
    for(var j = 1 ; j <= i ; j++){
        star += '*';
    }
    star += '\n';
    for(var k = line-i; k >= 0; k--){
        star += ' ';
    }
}
console.log(star);
```

<br>

#### 13. *(별)로 트리를 문자열로 완성하라. 개행문자(‘\n’)를 사용하여 개행한다. 완성된 문자열의 마지막은 개행문자(‘\n’)로 끝나도 관계없다.

```내풀이```
```Javascript
var line = 5;

for(var i=0 ; i<=line ; i++){
    var star = '';
    var empty = '';
    for(var j=5-i ; j>0 ; j--){
        star+= '*';
    }
    empty+=' '.repeat(i);
    console.log(star+empty);
}
```
```11번 참고한 내풀이```
```Javascript
var line = 5;
var star = '';

for(var i = line ; i >= 1; i--){
    for(var j = 1 ; j <= i ; j++){
        star += '*';
    }
    star += '\n';
}
console.log(star);
```

<br>

#### 14. *(별)로 트리를 문자열로 완성하라. 개행문자(‘\n’)를 사용하여 개행한다. 완성된 문자열의 마지막은 개행문자(‘\n’)로 끝나도 관계없다.

```내풀이```
```Javascript
var line = 5;

for(var i=1 ; i<=line ; i++){
    var star = '';
    var empty = '';
    for(var j=0 ; j<i ; j++){
        star += '*';
    }
    empty += ' '.repeat(line-i)
    console.log(empty+star);
}
```
```11번 참고한 내풀이```
```Javascript
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
```

<br>

#### 15. 정삼각형 출력하기

```내풀이```
```Javascript
for(var i=0 ; i<5 ; i++){
    var empty='';
    for(var j=(i*2)+1 ; j<=i*2+1 ; j++){
        var star = '';
        star += '*'.repeat(j)
    }
    empty = ' '.repeat(5-(i+1))
    console.log(empty+star);
}
```
```11번 참고한 내풀이```
```Javascript
var line = 5;
var star='';

for(var i = 1; i <= line ; i++){
    for(var j = line-i; j > 0; j--){
        star+=' ';
    }
    for(var k = (i*2)-1; k > 0; k--){
        star += '*';
    }
    for(var z = line-i; z > 0; z--){
    star += ' ';
    }
    star += '\n';
}
console.log(star);
```

<br>

#### 16. 역정삼각형 출력하기

```내풀이```
```Javascript
for(var i=5 ; i>0 ; i--){
    var empty='';
    for(var j=(i*2)-1 ; j>=i*2-1 ; j--){
        var star = '';
        star += '*'.repeat(j)
    }
    empty=' '.repeat(5-i)
    console.log(empty+star);
}
```
```11번 참고한 내풀이```
```Javascript
var line = 5;
var star = '';

for(var i = line; i >= 0; i--){
    for(var j = line-i; j > 0; j--){
        star += ' ';
    }
    for(var k = (i*2)-1; k > 0; k--){
        star += '*';
    }
    for(var z = line-i; z > 0; z--){
    star += ' ';
    }
    star += '\n';
}
console.log(star)
```

<br>