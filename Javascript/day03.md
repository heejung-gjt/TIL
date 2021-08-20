#### 👉 타입변환   

```명시적 타입 변환(타입 캐스팅)```    
의도적으로 값의 타입을 변환하는 것이다     

숫자 타입의 x값을 toString을 이용하여 의도적으로 값을 변경하였다. typeof로 데이터 타입을 보면 string 5로 바뀐것을 볼 수 있지만 x값(원시값)의 데이터 타입은 number 5로 x값 자체가 변경된 것은 아니다 즉, 원시값인 x의 값은 부수효과가 발생하지 않는다.
```javascript
var x = 5;
var word = x.toString();
console.log(typeof word, word);  // string 5
```    
<br>

```암묵적 타입 변환(타입 강제 변환)```     
자바스크립트 엔진에 의해 자동으로 타입이 변환되는 것이다 

아래의 코드처럼 (피연산자가 모두가 숫자타입인 경우를 제외하고) x와 문자열''이 + 연산자를 만나면 자바스크립트 엔진이 전부 문자열 처리를 하여 +는 산술연산자가 아닌 "문자열 연결 연산자"가 된다. 하지만 마찬가지로 x값(원시값) 자체가 변경된 것은 아니다.   
```javascript
var x = 10;

var word = x +''; // 연산자 + 가 피연산자의 타입을 체크한다. 문자열이 하나라도 있는 경우 x의 값을 문자열 처리하여 출력한다. 
console.log(typeof str, str); //string 10
```
이때 암묵적 타입 변환은 기존 변수 값을 재할당하여 변경하는 것이 아니다. 자바스크립트 엔진에서 피연산자값을 __암묵적으로 타입을 변환하여 평가한 후 새로운 타입의 값을 생성하여 한번 사용하고 버린다__        
(Q1. 명시적타입변환도 한번 사용되고 버려지는가?       

#### 암묵적 타입 변환 예

```1. 숫자타입으로 (암묵적)변환```   

-, *, /는 피연산자 모두 숫자타입인 경우에 가능한 연산자이므로 자바스크립트 엔진에서 피연산자를 모두 숫자타입으로 변환하여 값을 평가하여 결과를 출력한다                                                                                        
```javascript
1 - '1'
1 * '10'
1 / 'one'
```

<br>

``` 2. 불리언 타입이 아닌 값의 truthy/falsy 구분```   
자바스크립트 엔진에서는 불리언 타입이 아닌 값을 true나 false로 구분하는데 true로 평가되는 truthy값이 있고 false로 평가되는 falsy값이 있다. falsy예시 외의 모든 값은 모두 __true__ 로 평가되는 truthy값이다 

```text
//falsy예시  

falsy 예시로 모두 거짓으로 평가되기 때문에 숫자 0으로 평가가 가능하다.
예를 보면 !은 해당 값을 부정하는 부정 연산자로 false의 값이 true가 되어 콘솔이 출력되어진다.
ex) if(!false) console.log('false') //false 출력

- false
- undefined
- null
- 0, -0
- NaN
- ''(빈문자열)
```
```javascript
if(!false) console.log(false + 'is falsy value') // false는 falsy값이므로 !false는 true가 되어 콘솔문이 출력된다 
```

<br>

#### 명시적 타입 변환 예   

```1. 문자열 타입으로 변환```
- String 생성자 함수를 new연산자 없이 호출하는 방법   
```javascript
String(NaN); //'NaN'
Sting(true); //'true'
```
- Object.prototype.toString메서드를 사용한는 방법   
```javascript
(1).toString(); //'1'
(NaN).toString(); // 'NaN'
```
- 문자열 연결 연산자를 이용하는 방법   
```javascript
1 + '';  // '1'
NaN+'';  // 'NaN'
```

``` 2. 불리언 타입으로 변환```   
불리언 타입이 아닌 값을 불리언 타입으로 변환하는 2가지의 방법이 있다   

1. new 연산자 없이 호출하는 방법
```javascript
Boolean('x'); // true
Boolean(''); // false
Boolean('false') // true
Boolean(null); // false
Boolean(undefined); // false
Boolean({}) // true
```

2. !부정 논리 연산자를 두번 사용하는 방법    

!를 한번 사용하게 되면 해당값을 부정하는 값이 나오므로 한번더 !를 작성하여 원래 값의 불리언 타입이 나올 수 있도록 해준다  
```javascript
!!'x'; // true
!!''; // false
!!'false'; // true
!!0; // false
!!NaN; // false                

```

<br>

#### 👉 단축평가    
단축평가는 표현식을 평가하는 도중에 평가 결과가 확정된 경우 나머지 평가 과정을 생략하는 것을 말한다. 

```논리 연산자를 사용한 단축평가```   

- ```&&연산자```    
__논리곱 연산자__ 는 두개의 피연산자가 모두 true로 평가될 때 true를 반환한다. 

Cat은 truthy값이므로 true로 평가된다. 하지만 &&연산자는 두번째 피연산자의 값까지 평가해야 표현식을 평가할 수 있다. __논리곱 연산자는 두번째의 값이 논리연산의 결과를 결정하기 때문에 Dog를 그대로 반환해준다   
```javascript
'Cat' && 'Dog' //Dog
'Cat' && 'false' //false
```

- ```||연산자```   
__논리합 연산자__ 는 두개의 피연산자 중 하나만 true로 평가되어도 true를 반환해준다. 즉 첫번째 값이 true라면 그대로 첫번째 값이 출력되며 첫번째 값이 false라도 두번째 값이 true라면  두번째 값이 출력된다 

논리합 연산자는 논리 연산의 결과를 결정하는 피연산자의 타입을 반환하는 것이 아니라 값을 그대로 반환해준다. 이러한 과정을 __단축평가__ 라고 한다.   
```javascript
'Cat' || 'Dog' //Cat
'Cat' || false //Cat
false || 'Cat' //Cat
```
<br>

#### 👉 객체
원시값을 제외한 나머지 값들은 모두 객체이다. 예를 들면 함수, 배열, 정규표현식등이 있다. 객체는 0개 이상의 프로퍼티로 구성된 집합이며, 프로퍼티는 키와 값으로 구성된다       
 - 다양한 타입의 값을 하나의 단위로 구성한 복합적인 자료구조(서로 관련있는 값들을 묶어서 사용할 수 있는 자료구조)   

 - 변경 가능한 값으로 원시값과는 다르게 값자체가 변경될 수 있다.    

 ```javascript
 var person = {
     name : 'Lee',  // (name:'Lee' : 프로퍼티), (name : 프로퍼티키) , (20 : 프로퍼티값)  
     age : 20
 }
 ```

- 자바스크립트에 있는 모든 값들은 프로퍼티값이 될 수 있다. 함수도 프로퍼티 값으로 사용할 수 있는데 프로퍼티값이 함수일 경우 일반함수와 구분하기 위해서 메서드라고 부른다 

```javascript
 var counter = {
     increase : function () {  // 메서드 == (프로퍼티)
         this.num++;
     }
 };
 ```   

<br>

 #### 👉 객체 리터럴
 객체 리터럴은 중괄호 내에 0개 이상의 프로퍼티를 정의한다. 변수에 할당이 이루어지는 시점에 자바스크립트 엔진에서 객체 리터럴을 해석해 객체를 생성한다,
 이때 객체 리터럴의 중괄호 뒤에는 세미콜론을 붙여준다.(코드 블록을 의미하지 않기때문에)   

 <br>

 #### 👉 프로퍼티
 객체는 프로퍼티들의 집합이며 프로퍼티는 키와 값으로 구성된다.    
```프로퍼티``` : 객체의 상태를 나타내는 값(data), 키:값의 형식으로 지정되는 값    

```프로퍼티 키``` : 식별자의 의미를 갖는다  


 프로퍼티 키는 식별자 네이밍 규칙을 따르는 것을 권장한다. 만약 일반적인 문자열로 네이밍을 짓는 경우 반드시 따옴표를 사용해야 한다. ```firstName: 'hee-jung'``` -를 자바스크립트 엔진에서 연산자로 보기 때문에 문자열이라는 것을 알려주기 위해 따옴표를 사용한다.   

 ```javascript
 var person = {
     name : 'Son',  
     age : 24
 };
 ```
 프로퍼티키는 동적으로도 생성이 가능하며 변경도 자유롭다
 ```javascript
 var person = {
     name : 'Son',  
     age : 24
 };
 person.name ='jung';
 console.log(person)  //{ name: 'jung', age: 24 }
 ```
 프로퍼티 

 

 <br>

#### 👉 프로퍼티 접근

1. 마침표 표기법 : 접근연산자(.)을 사용한다
2. 대괄호 표기법 : 프로퍼티 접근 연산자([..])를 사용한다
```javascript
var person = {
    name : 'hee'
};

console.log(person.name) //hee 마침표 표기법
console.log(person['name']) //hee 대괄호 표기법
```
객체에 존재하지 않는 프로퍼티에 접근하면 에러발생이 아닌 undefined를 반환하게 된다
```javascript
var person = {
    name : 'son'
};

console.log(person.age)  //undefined
```
__(프로퍼티 키가 식별자 네이밍 규칙을 준수하지 않으면 반드시 대괄호 표기법을 사용해야 한다)__

<br>

#### 👉 프로퍼티 값 갱신
이미 존재하는 프로퍼티에 값을 할당하면 프로퍼티 값이 갱신된다 

값이 할당되어 메모리의 어딘가에 새롭게 생성되는 것이 아닌 son이라는 값이 park로 갱신이 되는 것이다.
```javascript
var person = {
    name: 'son'
};

person.name = 'park';

console.log(person) //{name: 'park'}
```

<br>

#### 👉 프로퍼티 축약 표현
프로퍼티 축약 표현은 자주 쓰이는 표현으로 ES6에서는 프로퍼티 값으로 변수를 사용하는 경우 변수 이름과 프로퍼티 키가 동일한 이름일때 프로퍼티 키를 생략할 수 있다.
```Javascript


var x=1, y=2;

var obj = {  //ES5
    x:x,
    y:y
}

var obj = {x,y} //ES6

```

<br>

  #### 👉 메서드

 ```메서드``` : 일반적인 함수와 구분하기 위해서 메서드라고 부른다, 프로퍼티를 참조하고 조작할 수 있는 동작(함수)       
 ```javascript
 var person ={
     count:5,
     getPersonSum : function(){ //메서드
         console.log(this.count)
     }
 };

 console.log(person.getPersonSum()); //5
 ```
```this```는 객체 자신을 가리키는 참조변수로 count의 값을 참조하기 위해서 this를 사용한다

<br>

#### 👉 메서드 축약 표현
ES6에서부터는 메서드를 정의할때 function 키워드를 생략한 축약 표현을 사용할 수 있다
```javascript

var person = {
    name:'son',
    personInfo: function(){
        console.log(this.name)
    }
}; //ES5 표현


var person = {
    name:'son',
    personInfo(){
        console.log(this.name)
    }
}; //ES6 표현
```

<br>

#### 👉 간단한 정리

- ```;``` : ; 하나만 와도 문이라고 한다 (빈문)
- ```스택오버플로우``` : while문이 무한루프를 돌다가 에러가 발생이 되는 것을 스택 오버플로우라고 한다
<br>

## 예습
###### [모던 자바스크립트 Deep Dive를 읽고 정리한 내용](https://poiemaweb.com/)

#### 👉 함수
함수는 일련의 과정을 문으로 구현하고 코드 블록으로 감싸서 하나의 실행 단위로 정의한것이다.   
함수 내부로 입력을 전달받는 변수를 ```매개변수```, 입력을 ```인수```, 출력을 ```반환값```이라고 한다. 
```javascript
function add(x,y){
    return x+y;
}
add(2,5)
```
```text
//함수정의 
function add(x,y){
    return x+y;
}

//함수이름
add

//매개변수
(x,y)

//반환값
return x+y;

//함수호출
add(2,5);

//인수
(2,5)
```

<br>

#### 👉 함수 리터럴
 함수 리터럴은 function 키워드, 함수 이름, 매개변수 목록, 함수 몸체로 구성된다.
 ```javascript
 var fuc = function add(x, y) {  //fuc에 함수 리터럴을 할당함
  return x + y;
};
 ```

 <br>

 #### 👉 스코프
 모든 식별자는 자신이 선언된 위치에 의해 다른 코드가 식별자 자신을 참조할 수 있는 유효범위가 결정된다. 즉 식별자가 유효한 범위를 스코프라고 한다

 ```javascript
 var x = 'global';

function foo() {
  var x = 'local';
  console.log(x); // local
}

foo();

console.log(x); // global
 ```

 var 키워드로 선언된 변수는 같은 스코프 내에서 중복 선언이 허용되는 단점이 있다. 하지만 let이난 const 키워드로 선언된 변수는 같은 스코프 내에서 중복 선언을 허용하지 않는다