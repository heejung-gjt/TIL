#### 👉 배열 메서드

```Array.prototype.join```   
join메서드는 원본 배열의 모든 요소값을 문자열로 변환한 다음 인수로 전달받은 구분자로 연결한 문자열을 반환한다. 구분자는 생략가능하며 기본값은 ```,```이다.    
(액세서 메서드)     
```javascript
const arr = [1,2,3,4,5];

console.log(arr.join()); //1,2,3,4,5
console.log(arr.join('-')); //1-2-3-4-5
console.log(arr); //[ 1, 2, 3, 4, 5 ]
```

```Array.prototype.split```
split메서드는 해당 배열을 구분자를 기준으로 배열로 다시 묶어 반환해준다  
```javascript
const arr = [1,2,3,4,5];

joinArr = arr.join('-');
console.log(joinArr);
console.log(joinArr.split('-'));
```

```Array.prototype.reverse```    
reverse메서드는 원본 배열의 순서를 반대로 뒤집는다. 이때 원본 배열이 변경되고 반환값은 변경된 배열이 된다.    
(뮤테이터 메서드)    
```javascript
const arr = [1,2,3,4,5];

const reverArr = arr.reverse();
console.log(arr); //[ 5, 4, 3, 2, 1 ]
console.log(reverArr);  //[ 5, 4, 3, 2, 1 ]
```

__split,reverse,join메서드 예시__   
str은 원시값이므로 원본이 바뀌지 않는다   
```javascript
const str = 'hello';

console.log(str.split('').reverse().join(''));  //olleh
console.log(str);  //hello
```

```Array.prototype.fill```    
ES6에서 도입되었으며 인수로 전달받은 값을 배열의 처음부터 끝까지 요소롤 채운다. 이때 원본 배열이 변경된다    
(뮤테이터 메서드)     

인수로 전달받은 값 0을 배열의 처음부터 끝까지 요소로 채워준다
```javascript
const arr = [1,2,3];
arr.fill(0);
console.log(arr); //[0,0,0]
```    

인수로 전달받은 값 0을 배열의 인덱스 2부터 4이전까지 요소로 채워준다
```javascript
const arr = [1,2,3,4,5];
arr.fill(0,2,4);
console.log(arr); //[1,2,0,0,5]
```    

```Array.prototype.includes```    
ES7에서 도입된 메서드이고 배열 내에 특정한 요소가 포함되어 있는지 확인하여 불린형 타입으로 반환한다
```javascript
const arr = [1,2,3];
arr.includes(2); //true
```  

```Array.prototype.flat```    
ES10에서 도입된 메서드이고 인수로 전달한 깊이만큼 배열을 평탄화한다(배열을 풀어준다)  
```javascript
[1, [2, [3, [4]]]].flat();  // -> [1, 2, [3, [4]]]
[1, [2, [3, [4]]]].flat(1); // -> [1, 2, [3, [4]]]
[1, [2, [3, [4]]]].flat().flat(); // -> [1, 2, 3, [4]]
```    

<br>

#### 👉 고차함수
함수를 인수로 전달받거나 반환할 수도 있는 함수이다.     

func를 인수로 전달 받거나 리턴하는 add를 ```고차함수```라고 한다. 인수로 들어가는 함수 callback은 add의 ```콜백함수```라고 한다.     

add는 인수로 정수 2개와 익명함수를 전달받는다. add함수가 호출되면 sum에 a+b의 값이 들어가고 sum을 인수로 받는 callback함수가 리턴된다. callback함수는 익명의 함수이므로 익명의 함수가 실행되어 결과를 출력해준다
```javascript
function add(a,b, callback){
    let sum = a + b;
    return callback(sum);
}

add(1,2,function(num){
    console.log(`합계는 ${num}`);  //합계는 3
});
```

### Array.prototype.sort    
sort메서드는 배열의 요소를 정렬한다. 원본 배열을 직접 변경하며 정렬된 배열을 반환해준다. 
```javascript
const word = ['people','apple','car'];
word.sort();

console.log(word);  //[ 'apple', 'car', 'people' ]
``` 

sort()후 reverse()을 이용해 내림차순으로 요소를 정렬할 수 있다
```javascript
const word = ['people','apple','car'];
word.sort();
word.reverse();

console.log(word);  //[ 'people', 'car', 'apple' ]
```

__! 문자열 요소로 이루어진 배열의 정렬은 문제가 없지만 숫자 요소로 이루어진 배열을 정렬하기 위해서는 비교함수를 사용해야 한다.__   

sort메서드의 기본 정렬 순서가 유니코드 코드포인트의 순서를 따르기 때문이다. 10의 유니코드 포인트는  U+0031U+0030이며 2의 유니코드 포인트는 U+0032이다. 10의 유니코드 코드 포인트가 2보다 앞서므로 10이 2보다 먼저 정렬된다. 이렇기 때문에 비교함수를 이용해야 한다
```javascript
['2','10'].sort(); //[ '10', '2' ]
[2,10].sort(); //[ 10, 2 ]
```

##### 비교함수 이용
```javascript
const arr = [40, 100, 1, 5, 2, 25, 10];

arr.sort((a,b) => a-b);
console.log(arr); //[ 1, 2, 5, 10, 25, 40, 100 ]
```

### Array.prototype.forEach    
forEach메서드는 자신의 내부에서 반복문을 실행한다. 즉 반복문을 통해 자신을 호출한 배열을 순회하면서 수행해야 할 처리를 콜백함수로 전달받아 반복 호출한다.
(사용을 많이 하지는 않는 메서드)
```javascript
const numbers = [1,2,3];
let arr = [];

numbers.forEach(item => arr.push(item*2));
console.log(arr); //[ 2, 4, 6 ]
```

### Array.prototype.map    
map 메서드는 (입력으로 들어온) 배열을 인자로 받는 콜백함수를 호출함으로써 새로운 배열을 만들어낸다. 따라서 원본 배열은 변경되지 않는다. map메서드로 전해진 콜백함수는 item, index, array의 3가지 인수를 받는다.   

1. ```함수를 정의하여 map메서드 호출```   

*2를 해주는 기능을 갖는 함수를 따로 정의하여 map의 콜백함수로 써주는 방법이 있다. 라인수도 길어지고 가독성도 좋지 않은 것을 볼 수 있다
```javascript
const arr = [1,2,3,4];

function mul(num){
    return num*2;
}
let mulArr = arr.map(mul);
console.log(mulArr); // [1,4,6,8]
```

2. ```함수를 map메서드의 인수로 직접 정의하여 호출```        
함수를 따로 정의하지 않고 map메서드 인수안에 함수를 직접 호출하여 콜백함수로 써주는 방법이 있다. 1보다는 가독성도 좋고 라인수도 덜 차지하는것을 볼 수 있다
```javascript
const arr = [1,2,3,4];

let mulArr = arr.map(function(num){
    return num*2;
});
console.log(mulArr); // [1,4,6,8]
```

3. ```map메서드 인수안에 화살표함수로 콜백함수를 써주는 방법이 있다. 2가지의 방법보다 라인수도, 가독성도 좋아진것을 볼 수 있다```    
arr이라는 배열객체를 map을 이용하여 콜백함수를 호출해 새로운 배열을 만드는데 이때 콜백함수에서 각 배열의 요소에 제곱을 한 값이 리턴되므로 arr의 배열 요소 각각에 제곱된 새로운 배열이 mulArr에 저장된다 (고차함수:map, 콜백함수 item=>item**2)
```javascript
const arr = [1,2,3,4];
const mulArr = arr.map(item=>item*2);

console.log(mulArr); //[ 1,4,6,8]
```

map메서드의 콜백함수는 map메서드를 호출한 배열의 요소값,인덱스값, 배열자체, 즉 this를 순차적으로 전달받을 수 있다. 

map메서드는 콜백함수를 호출할때 3개의 인수를 순차적으로 전달해준다. 아래의 코드를 보면 콜백함수에 3개의 인수를 써주면 차례대로 num 배열의 요소값, 인덱스값, 배열자체가 호출되어지는 것을 볼 수 있다. 
```javascript
const num = [1,2,3];
num.map((item,index,arr)=>{
    console.log(`item ${item} index ${index} arr ${arr}`);
});

// 결과값
// item 1 index 0 arr 1,2,3
// item 2 index 1 arr 1,2,3
// item 3 index 2 arr 1,2,3
```

```map에 대한 예시```    

__1. map과 화살표 함수를 사용하여 배열의 제곱값을 구한다__   
```javascript
const numbers = [1,2,3];
console.log(numbers.map(v=>v**2)); //[1,4,9]
```

__2. polyfill을 이용하여 map기능 구현하기__      

Q. polyfill(폴리필)이란 ?   
A. polyfill은 브라우저에서 지원하지 않는 코드를 사용가능한 코드로 바꾸어 작성한 기능을 의미한다.    


numbers라는 배열 객체를 메서드인 myMap 함수를 이용하여 인수값으로 콜백함수를 호출해 새로운 배열을 만드는데 이때 콜백함수를 인자로 받는 callback 타입이 function이 아니면 에러를 출력해준다. 만약 타입이 function인 경우 새로 만든 배열 res에 callback함수는 인수로 받을수 있는 3가지를 받아 push해준다.(기본으로 3가지를 받을 수 있지만 필수는 아니다) 이때 callback함수는 결국 첫번째 요소값 만을 사용하여 제곱 해주므로 리턴은 제곱된 첫번째 요소값이 리턴되고 해당 값들이 배열로 출력된다.    

map은 콜백함수의 리턴함수로 이루어진 배열을 리턴한다. 즉 새로운 배열을 리턴해준다
```javascript
const numbers = [1,2,3,4,5];

Array.prototype.myMap = function(callback){
    if(typeof callback != 'function'){
        throw new TypeError(`${callback} is not a function`);
    }
    const res = [];
    
    for(let i =0; i<this.length; i++){
        res.push(callback(this[i],i,this));
    }
    return res;
};
console.log(numbers.myMap(v => v**2)); //[ 1, 4, 9, 16, 25 ]



// console.log(arr.myMap(function(item){  일반익명 함수로 작성했을때 
//     return item**2;  // [ 1, 4, 9, 16, 25 ]

// }));
```

<br>

### Array.prototype.filter
filter메서드는 자신을 호출한 배열의 모든 요소를 돌면서 조건을 확인한 후 조건을 만족하는 요소로 구성된 새로운 배열을 반환한다.        
```(item%2)는 item이 홀수를 만족한다는 이야기이다```
```javascript
const arr = [1,2,3,4,5]; 

// arr의 각 요소값중 짝수인 값만을 필터링하여 새로운 배열에 넣어준다
const even = arr.filter(item => item%2==0);
console.log(even);  // [2,4]
```
filter메서드는 콜백 함수를 호출할때 3개의 인수 즉, 요소값 인덱스값 배열자체(this)를 순차적으로 전달한다   

```filter에 대한 예시```    

__1. filter와 화살표 함수를 사용하여 길이가 3이하인 요소를 구한다__       
```javascript
const words = ['abc','abcde','a','aa','sdfs'];
newWords = words.filter(word => word.length <= 3));  
console.log(newWords);// [ 'abc', 'a', 'aa' ]
```

__2. polyfill을 이용하여 filter기능 구현하기__     

Q1. 왜 callback함수가 인수로 3가지를 받는지 확인해야 하는가? true인지 false인지는 return v<=3에서 결정하는 것 아닌가 ?     

Q2. 왜 3가지를 전부 써주어야 하는가 그냥 filter메서드의 규칙인가 ?       

```javascript
const arr = [1,2,3,4,5];

Array.prototype.myFilter=function(callback){
    if(typeof callback !='function'){
        throw new TypeError(`${callback} is not a function`);
    }
    let newArr = [];
    for(let i = 0; i< this.length; i++){
        if(callback(this[i],i,this)){
            newArr.push(this[i]);
        }
    }
    return newArr
};

console.log(arr.myFilter(v => v <= 3)); //[1,2,3]

// console.log(arr.myFilter(function(v){
//     return v<=3;
// }));

```
왜 이렇게 작성하면 안되는가 ? 답은 [1,2,3]으로 동일하다
```javascript
.
.
 let newArr = [];
    for(let i = 0; i< this.length; i++){
        if(callback(this[i])){
            newArr.push(this[i]);
        }
    }
    return newArr
};
console.log(arr.myFilter(function(v){
    return v<=3;
}));
```


<br>

#### map과 filter의 공통점/차이점   
- 기존 배열이 변경되지 않고 새로운 배열을 리턴한다   

- map은 콜백함수가 적용된 새로운 요소값으로 이루어진 배열을 반환한다    
- filter는 조건문을 만족하는 요소값을 반환한다   

<br>

### Array.prototype.reduce
(reduce는 많이 사용되지 않는다. 어떻게 쓰이는 것인지만 알고 넘어가자)    

reduce 메서드는 자신을 호출한 배열을 모든 요소를 돌면서 전달받은 콜백함수를 반복으로 호출한다. 콜백함수의 반환값을 다음 순회시 콜백 함수의 첫번째 인수로 전달후 콜백함수를 호출하여 하나의 결과값을 만들어 반환한다.    

reduce메서드는 첫번째 인수로 콜백 함수, 두번째 인수로 초기값을 전달받는다. reduce 메서드의 콜백 함수에는 4개의 인수, ```초기값```, ```콜백 함수 이전반환값```, ```reduce 메서드를 호출한 배열의 요소값과 인덱스```, ```배열자체(this)```가 전달된다   

```javascript
const arr = [1,2,3,4,5];
const sum = arr.reduce((accumulator, currentValue, index, array)=> accumulator + currentValue, 0);

console.log(sum);  // 15
```

```reduce에 대한 예시```    
최댓값 구하기
```javascript
const values = [1,2,3];

const max = values.reduce((acc,cur) => (acc >cur > acc:cur),0);
console.log(max);  //3
```
이땐 reduce를 이용하는 것보단 Math.max 메서드를 사용하는 것이 더욱 직관적이다
```javascript
const values = [1,2,3];

const max = Math.max(...values);
console.log(max); //3
```

<br>

### Array.prototype.some
some메서드는 자신을 호출한 배열의 요소를 순회하면서 인수로 전달된 콜백 함수를 호출한다. 이때 콜백 함수의 반환값이 단 한번이라도 참이면 true, 모두 거짓이면 false를 반환한다
some 메서드를 호출한 배열이 빈 배열인 경우 언제나 false를 반환한다.   
```javascript
[5,10,15].some(item => item >10); // true
```

### Array.prototype.every
some메서드와 반대로 반환값이 단 한번이라도 거짓이면 false를 반환한다. every메서드를 호출한 배열이 빈 배열인 경우 언제나 true를 반환한다
```javascript
[5,10,15].every(item => item > 10); // false
```

### Array.prototype.find
ES6에서 도입된 find메서드는 자신을 호출한 배열의 요소를 순회하면서 인수로 전달된 콜백함수를 호출하여 반환값이 true인 첫번째 요소를 반환한다. 콜백 함수의 반환값이 true인 요소가 존재하지 않는다면 undefined를 반환한다
```javascript
const users = [
  { id: 1, name: 'Lee' },
  { id: 2, name: 'Kim' },
  { id: 2, name: 'Choi' },
  { id: 3, name: 'Park' }
];

// id가 2인 첫번째 요소의 값을 반환한다
users.find(user => user.id === 2); // {id: 2, name: 'Kim'}
```

### Array.prototype.findindex
ES6에서 도입된 해당 메서드는 콜백 함수를 호출하여 반환값이 true인 첫번째 요소의 인덱스를 반환한다. 콜백 함수의 반환값이 true인 요소가 존재하지 않으면 -1을 반환한다.
```javascript
const users = [
    { id: 1, name: 'Lee' },
    { id: 2, name: 'Kim' },
    { id: 2, name: 'Choi' },
    { id: 3, name: 'Park' }
  ];
  
  // id가 2인 첫번째 요소의 인덱스값을 반환한다
console.log(users.findIndex(user => user.id === 2)); // 1
```

<br>

#### 👉 복사방법

- slice호출   

```javascript
const arr = [1,2,3,4,5];
const res = arr.slice(0,5);
console.log(res); //console.log(arr); //[0,2]   
```

- ...호출    

```javascript
const arr = [1,2,3,4,5];
const res = [...arr];
console.log(res);  //[ 1, 2, 3, 4, 5 ]

```

<br>


#### 👉 this 출력

일반함수로서  this를 출력하면 window라는 전역 객체가 출력된다
```javascript
function add(a,b){
    console.log(this);  // window라는 전역객체가 출력
    return a+b;
}
add(1,2);

//결과값
// Object [global] {
// global: [Circular],
// process:
// process {
// title: 'node',
// version: 'v10.19.0',
// versions:
// { http_parser: '2.9.3',
// node: '10.19.0',
// v8: '6.8.275.32-node.55',
// uv: '1.34.2',
.
.
```

생성자 함수로서 this를 호출하면 생성자 인스턴스를 출력한다
```javascript
function add(a,b){
    console.log(this);  // 생성자 객체를 가리킨다
    return a+b;
}

new add(1,2);

//결과값
// add {}
```

메서드 함수로서 this를 호출하면 메서드 객체를 가리킨다
```javascript
function add(){
    return this;  //메서드 객체 가리킨다 
}

let obj = {
    add:add
}
console.log(obj.add());

//결과값
//{ add: [Function: add] }
```