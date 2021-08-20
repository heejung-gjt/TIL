#### 👉 함수의 호출
ES6 이전까지는 함수는 별다른 구분 없이 다양한 목적으로 사용되었다.   

- ```일반적인 함수로서 호출```    
함수 foo를 호출하는 방법중 하나인 일반적인 함수로서 호출을 하는 방법이다. 이렇게 일반 함수로 호출이 되는 것은 생성자 함수로서 호출 또한 가능했다(ES6이전)
```javascript
var foo = function(){  //함수 표현식
  return 1;
}

foo(); // 1
```

- ```(new연산자와 함깨 호출하여 인스턴스를 생성할 수 있는) 생성자 함수로서 호출```
```javascript
var foo = function(){ 
  return 1;
}

new foo(); // foo{} 생성
```

- ```(객체에 바인딩되어) 메서드로서 호출```

```javascript
var foo = function(){  
  return 1;
}

var obj = {foo:foo};
obj.foo(); // 1
```

- 객체에 바인딩 된 함수 또한 일반함수,생성자 함수, 메서드로서 호출이 가능하다
```javascript
var obj = {
  x : 10,
  y : function(){  // 객체 obj에 바인딩 된 함수
    return this.x;
  }
};
var res = obj.y; //일반 함수로서 호출
console.log(res());  // undefiend


console.log(obj.y()); //메서드로서 호출, 10 

console.log(new obj.y()); //프로퍼티 y에 바인딩된 함수를 생성자 함수로서 호출, y {}
```
<br>

이렇듯 ES6이전의 모든 함수는 사용목적의 구분없이 사용되어 혼란스럽고 실수를 유발시키고 성능에도 좋지 않았다. 때문에 __ES6에서는 함수를 사용 목적에 따라 분류하였다__

__Q) 그렇다면 function Foo{}는 일반함수일까 생성자 함수일까 ?__    

A) 함수의 호출에 따라 결과가 달라진다. ```Foo();```호출시 일반함수가 되며 ```new Foo();```호출시 생성자 함수가 된다. 예측은 해볼 수 있다. 컨벤션 상  네임의 앞부분이 대문자인걸 봐서 Foo함수는 생성자 함수일 가능성이 높다

<br>

#### 👉 메서드
ES6이전에는 메서드를 __객체에 바인딩된 함수__ 라는 의미였지만 ES6부터는 정의가 명확하게 규정되었다. 메서드는 __메서드 축약 표현으로 정의된 함수만을 의미한다__    

ES6이전의 경우 met와 fuc함수를 모두 객체 obj에 바인딩된 함수이기 때문에 메서드로 보았지만 ES6부터는 met는 __메서드__ 이지만 fuc는 __일반함수__ 로 정의된다.  ES6에서 메서드는 인스턴스를 생성할 수 없는 __non-constructor__ 이므로 생성자 함수로서 met를 호출할 수 없다
```Javascript
const obj = {
  x : 10,
  met() {return this.x;},
  fuc : function() {return this.x;}
};

new obj.met();  // error
console.log(new obj.fuc());  // fuc {}

```

__Q) 다음 foo와 bar의 차이점은 무엇인가 ?__    
```javascript
const obj = {
  foo:function(){},
  bar(){}
}
```
A) foo는 메서드 표현이지만 ES6에서는 메서드로 인식하지 않고 일반함수로 인식하여 생성자 함수로서 호출이 가능하다. ```new obj.foo();``` 이 가능하지만 bar함수는 메서드 축약표현으로 메서드로 함수를 인식하여 ```new obj.bar();``` 같은 표현이 불가능하다. 함수를 메서드로서 호출하기 위해 두번째 방법을 지향한다. 

<br>

#### 👉 화살표 함수

```일반함수와 화살표 차이```   

- 화살표 함수는 인스턴스를 생성할 수 없다    
```javascript
const add = () => {};
new add(); // error
```
- 화살표 함수는 인스턴스를 생성할 수 없으므로 프로토타입 프로퍼티가 없다   

- 일반 함수는 중복된 매개변수 이름을 선언해도 에러가 발생하지 않지만(strict mode 제외) 화살표함수는 에러가 발생한다
```javascript
function add (a,a) {return a+a;}
console.log(add(1,3));  // 4

const add = (a,a) => a+a;
console.log(add(1,3));  // error
```   

- 화살표 함수는 ```(=>)``` 화살표를 사용하여 기존 함수 정의 방식보다 간략하게 함수를 정의할 수 있다.    

```javascript
//1
function add(a,b){  // 함수 선언문
  return a+b;
}

//2
const add = function add(a,b){  // 함수 표현식
  return a+b;
}

//3
const add = (a,b) => a+b;  //화살표 함수
```

Q) 2번에 함수 표현식에서 변수명과 함수명이 add로 똑같아도 괜찮은가 ?
A) 변수명과 함수명은 존재하는 스코프가 다르기 때문에 충돌이 나지 않는다
변수명 add는 전역변수에 존재하게 되고 함수명 add는 함수 내부에서 사용되기 때문에 함수내부 즉, 지역변수에 존재하게 된다. 

```함수 정의```    

화살표 함수는 함수 표현식으로 써야한다
```javascript
const adds = (x,y) => x+y;

console.log(adds(100,200));  // 300 
```

```매개변수 선언```     

매개변수가 여러개일 경우 ```()```안에 매개변수를 선언해준다. 하나일 경우 ```()```생략이 가능하다. 매개변수가 없는 경우에는 ```()```를 생략할 수 없다. 이러한 방식은 각자의 컨벤션에 따라 결정된다
```javascript
const mul = (x,y) => {}; //매개변수 여러개일 경우

const num = x => {}; //매개변수 한개인 경우

const add = () => {}; // 매개변수 없는 경우

```

```함수 몸체 정의```   

함수몸체 부분이 하나의 문으로 구성되면 ```{}``` 생갹이 가능하다. 아래의 두개는 같은 표현으로 동일하다.
```javascript
const pow = x => x**2;  // 가능

const pow = x => {return x**2};  //위의 표현 해석, 가능
```

- 함수몸체 부분이 표현식이 아닌 문인 경우 ```{}```를 생략할 수 없다
```javascript
const pow = x => const y = x**2;  //불가능

const pow = x => {return const y = x**2};  //위의 표현 해석, 불가능

const pow = x => {const y = x**2}; // {}써주어야 한다 , 가능
```

- 객체 리터럴을 반환하는 경우 ```{()}```로 감싸주어야 한다. 그렇지 않으면 ```{}```을 함수 몸체를 감싸는 중괄호로 잘못 해석한다
```javascript
const info =(name, age) => ({name, age});
info('hee',20); // {name: 'hee', age: 20};
```

- 화살표 함수는 __즉시실행함수__ 사용이 가능하다
```javascript
const info = ((name,age) => ({
  output(){ return `${name} is ${age}`}
}))('hee',20);

console.log(info.output());  // hee is 20
```

<br>

#### 👉 Rest 파라미터

아래의 코드는 가변인자를 이용하여 함수에 전달된 인수들을 배열로 전달 받는다. 이때 매개변수 args앞에 붙는 ```...``` 점 세개를 붙인것을 나머지 매개변수를 받는다고 해서 Rest 파라미터가 된다. 
```javascript
function add(...args){
  console.log(args); // [1,2,3,4,5]
}

add(1,2,3,4,5)
```

- rest파라미터는 먼저 선언된 매개변수를 제외한 나머지 매개변수들로 구성되는 배열이므로 가장 마지막 파라미터로 와야한다
```javascript
function add(a,b,c,...rest){
  return console.log(a,b,c,rest);
}
add(1,2,3,100,200,300); // 1 2 3 [ 100, 200, 300 ]

```

- 예를 들어보면 인수들의 총 합계를 구할때 for문을 쓴 방법과 reduce를 쓴 방법을 살펴보자. for문을 쓰는 경우 sum은 undefined인 상황에서 숫자를 더하게되므로 NaN이 나오게 된다.
```javascript
const sum = function(...args){
  let sum;
  for(let i = 0 ; i < args.length; i++){
    sum += args[i];
  }
  return sum;
}
console.log(sum(1,2,3,4,5));  //NaN출력 
```
화살표함수와 reduce, args의 배열을 이용해서 훨씬 간단하고 for문의 단점을 해결하여 sum값을 구할수 있는 걸 볼 수 있다. 이때 화살표함수로 가변인자 함수를 구현할땐 Rest파라미터를 사용해야 한다.
```javascript
const sum = (...args) => args.reduce((pre,cur) => pre+cur, 0);

console.log(sum(1,2,3,4,5)); //15
```

<br>

#### 👉 매개변수 기본값

함수를 호출할때 매개변수의 개수만큼 인수를 전달받지 않는 경우에도 에러가 발생하지 않는다. 하지만 인수가 전달되지 않는 매개변수는 undefined가 출력된다. 이를 막기위해 ES6에서부터는 매개변수의 기본값을 사용한다
```javascript
function add(x = 0, y = 0){
  return x + y;
}

console.log(add(1)); // 1
```
- Rest파라미터에는 기본값을 지정할 수 없다.

<br>

#### 👉 배열
배열(객체타입)은 배열 리터럴을 통해 생성된다. 이때 배열이 가지고 있는 값을 ```요소(=엘리먼트)```라고 한다. 배열의 요소는 자신의 위치를 나타내는 ```인덱스```를 가진다.  요소에는 값의 모든것이 올 수 있으며 요소들의 타입이 일치할 필요가 없다. 하지만 배열을 반복하면서 동일한 처리를 해야 할때 타입에 따라 결과가 달라지기 때문에 타입을 일치시키는것을 권장한다. 배열은 인덱스와 lentgth프로퍼티를 갖기 때문에 For문을 통해 순차적으로 요소에 접근할 수 있는 특징이 있다.    

<br>

#### 👉 자료구조 배열과 js배열
(면접 질문)

```자료구조 배열```    
- 자료구조에서의 배열은 동일한 크기의 메모리 공간이 연속적으로 나열된 자료구조를 말한다. 배열 요소는 하나의 데이터 타입으로 통일되어 있다.    

- 자료구조 배열은 인덱스로 요소에 빠르게 접근 가능하지만 배열에 요소를 삽입/삭제하는 경우에 배열의 요소를 연속적으로 유지하기 위해 요소를 이동시켜야 한는 단점이 있다.   



```자바스크립트 배열```   
- 자바스크립트에서의 배열은 동일한 크기의 메모리 공간을 가지고 있지 않아도 되며 데이터 타입이 통일되지 않고 각각 달라도 된다.   

- 배열의 요소가 연속적으로 이어져 있지 않을 수도 있다. 이러한 배열을 ```희소배열```이라고 한다.    

- 자바스크립트 배열은 인덱스로 배열 요소에 접근하는 속도가 상대적으로 느리지만 요소를 삽입/삭제하는 경우에는 상대적으로 빠르다.   

자바스크립트의 배열이 아닌 배열의 흉내를 낸 특수한 객체라고 할수 있다. 해당 배열은 인덱스를 나타내는 문자열을 프로퍼티 키로 가지고 length 프로퍼티를 갖는다.

<br>

#### 👉 희소배열
배열의 length값을 늘리면 length 값은 변경되지만 실제로 배열의 길이가 늘어나지는 않는다. 이처럼 배열의 요소가 일부분 비워있는 배열을 ```희소배열```이라고 한다.  의도적으로 희소 배열을 만들어야 하는 상황은 발생하지 않으므로 희소배열의 사용을 지양한다.
```javascript
const arr = [1];

arr.length = 3;

console.log(arr.length); //3
console.log(arr);  //[ 1, <2 empty items> ]
```

<br>

#### 👉 배열리터럴
배열을 생성하는 방법에는 여러가지가 있지만 현재에는 배열 리터럴만 알아도 문제없다. 배열 리터럴은 0개이상의 요소를 쉼표로 구분해 ```[]```으로 묶는다. 
```javascript
const arr = [1,2,3];
console.log(arr.length); //3
```

<br>

#### 👉 배열요소 추가/갱신/삭제
배열에 요소를 동적으로 변경할 수 있다.

```javascript
const arr = [0];

arr[1]=100; //추가  [0,100]
arr[1] = 1000; // 갱신 [0,1000]
arr['foo'] = 5; //프로퍼티 추가 [0,1000,foo:5]
delete arr[0]; //삭제 [1000,foo:5]
```

<br>

#### 👉 배열 메서드
자바스크립트에는 다양한 빌트인 메서드를 제공한다. Array생성자 함수는 정적 메서드를 제공하고 배열 객체의 프로토타입인 Array.prototype은 프로토타입 메서드를 제공한다. 

배열 메서드에는 2가지의 반환방법이 존재한다   
- #### mutator(뮤테이터) method    
원본 배열을 직접 변경하는 메서드이다    

```push메서드``` 
```javascript
const arr = [0];

arr.push(100);
console.log(arr); //[0,100]
```
```pop메서드``` 
```javascript
const arr = [0,1,2];

arr.pop();
console.log(arr); //[0,1]
``` 
```unshift메서드```    
원본 배열의 선두에 요소를 추가하고 변경된 length값 반환 
```javascript
const arr = [0,1,2];

let res = arr.unshift(100,200);
console.log(res); //5
console.log(arr); //[ 100, 200, 0, 1, 2 ]
```
```shift메서드```    
원본배열에서 첫번째 요소 제거하고 제거한 요소 반환
```javascript
const arr = [0,1,2];

let res = arr.shift();
console.log(res); //0
console.log(arr); //[1,2]
```
```splice메서드```     
splice(start,delete,items)
요소를 제거하기 시작할 인덱스, 제거할 요소 개수 (-1한것과 동일), 제거한 위치에 삽입할 요소목록
```javascript
const arr = [0,2];
const res = arr.splice(0,2,30,40);
console.log(res); //[0,2]
console.log(arr); //[30,40]
```
- #### accessor(액세서) method    
원본 배열을 직접 변경하지 않고 새로운 배열을 생성하여 반환하는 메서드이다. 액세서 사용을 권장한다

```concat```    
원본 배열의 마지막 요소로 추가한 새로운 배열 반환
```javascript
const arr = [0];

const res = arr.concat(1);
console.log(arr); //[0]
console.log(res)  //[0,1]
```
```slice메서드```     
slice(start,end)   
복사를 시작할 인덱스, 복사를 종료할 인덱스(-1한것과 동일)
```javascript
const arr = [0,2];
const res = arr.slice(0,1);
console.log(res); //[0]
console.log(arr); //[0,2]
```

<br>

#### 👉 스프레드 문법
스프레드 문법```...```은 하나로 뭉쳐있는 여러 값들의 집합을 펼쳐서 개별적인 값들의 목록으로 만든다.   

예시를 봐보자. push를 사용하는대신 스프레드 문법으로 요소 객별적인 값으로 넣었다.
```javascript
console arr = [1,2];

const newArr = [...arr,3]; //[1,2,3]
``` 
스프레드 문법을 사용할 수 있는 대상은 array, string, map, set, arguments와 같은 For..of문으로 순회할 수 있는 이터러블, Dom컬렉션이 있다

```javascript
console.log(...[10,20,30]); // 10 20 30
console.log(...'world'); //w o r l d
```
이때 스프레드 문법과 비슷한 Rest파라미터는 풀어져있는 값들을 하나의 배열록 묶는 역할을 한다는 점에서 역할의 차이가 있다

스프레드문법을 이용해 원본에 영향을 주지 않고 프로퍼티를 사용할 수 있다   

push를 예를 들어보자
```javascript
const arr = [1,2,3];

let res = [...arr];

res.push(100);

console.log(res); //[1,2,3,100]
console.log(arr); //[1,2,3]
```
<br>

#### 👉 얕은복사와 깊은복사
slice나 스프레드 문법을 이용해서 배열을 복사할 수 있다. 이때 생성되는 복사본은 얕은 복사를 통해 생성된다. 이때 얕은복사는 참조값이 다른 별개의 객체지만 배열 요소의 참조값은 같다.   
깊은 복사는 Lodash라이브러리의 cloneDeep 메서드를 사용하자
```javascript
const infor = [
  {name : 'hee', age: 20},
  {name : 'jung', age: 30}
]

const copyInfor = infor.slice();
// const copyInfor = [...infor];

console.log(infor === copyInfor); //false

console.log(infor[0]===copyInfor[0]); //true
```

<br>

#### 👉 prototype 체인

생성자 함수로서 Person을 호출하여 런타임중에 me라는 인스턴스를 생성하게 되면 메모리상에 인스턴스가 생성된다. 이때 Person생성자함수는 런타임전에 만들어진다. Person이 만들어질때 Person에 대한 prototype도 함께 생성되어지고 해당 prototype은 인스턴스가 상속받는 상위객체가 된다. 
```javascript
function Person(name){
  this.name = name;
  this.sayHi = function(){
    console.log('hi');
  }
}
const me = new Person('hee');

console.log(me);  //Person { name: 'hee', sayHi: [Function] }
me.sayHi();  //hi
```
![js](https://user-images.githubusercontent.com/64240637/111582163-ca926700-87fd-11eb-8148-fd996a9d4480.png)

이때 sayHi라는 함수는 항상 똑같은 동작을 하는 기능이다. 하지만 인스턴스를 생성할때마다 반복해서 sayHi라는 함수가 생성되어 메모리가 낭비된다. 이때 인스턴스가 상속을 받을 수 있는 상위객체인 prototype에 sayHi라는 함수를 한번 생성하면 필요할때마다 상속 받으면 되므로 메모리의 낭비를 막을 수 있다

```javascript
function Person(name){
    this.name = name;
  }
  Person.prototype.sayHi = function(){
    console.log('hi');
  }
  
  const me = new Person('hee');
  console.log(me); //Person { name: 'hee' }
  me.sayHi(); // hi
```
![js](https://user-images.githubusercontent.com/64240637/111583445-cb2bfd00-87ff-11eb-863d-8d7ecab27f27.png)

<br>

#### 프로토타입 체인의 역할
배열을 생성하면 런타임전에 배열아 생성되고 배열의 프로토타입이 생성된다. 메모리상에 arr에 대한 객체값 [0]이 저장되는데 push는 배열의 프로퍼티이다. 콘솔 평가 결과를 알기위해 스코프 체인상에서 arr을 찾은 후 프로토타입 체인에서 push를 찾아 동작한다. 이때 스코프 체인상에서 먼저 push를 찾은후 프로토타입 체인과정으로 올라간다
```javascript
const arr = [0];
arr.push(1);
console.log(arr);
```
![js](https://user-images.githubusercontent.com/64240637/111584782-a9337a00-8801-11eb-974c-a497c1ddee13.png)


#### 👉 Array.isArray
Array.isArray는 생성자 함수의 정적 메서드이다.   
해당 메서드는 전달된 인수가 배열이면 true, 아니면 false를 반환한다

```javascript
Array.isArray([]); //true
Array.isArray(new Array()); //true

```

<br>

#### 👉 리터럴로 생성

- const arr = [];
배열 객체를 생성해주는 리터럴이다   

- const obj = {};   
객체를 생성주는 리터럴이다   
