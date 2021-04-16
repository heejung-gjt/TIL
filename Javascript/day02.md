#### 👉 할당과 재할당

```할당```    
할당은 다른말로 대입,저장,assignment라고도 불린다. 말그대로 변수에 값을 저장하는것을 할당이라고 한다.   
``재할당```   
값이 있는 변수에 다른 값을 넣어 사용하는것을 재할당이라고 말한다. 이때 기존에 있던 값이 변경되는 것이 아닌 메모리의 어딘가에 새로운 값이 들어가고 그 메모리의 주소를 변수가 읽게 되는 것이다.   
```초기화```   
변수를 처음 선언하면 선언된 값 안에는 undefined로 값이 처음 할당되어지고 이를 초기화라고 한다. (Q.다른값을 넣는것은 초기화라고 하지 않는가??)    

<br>

#### 👉 메모리 관리

```바인딩```    
변수에 값을 할당하면 메모리의 어딘가에 값이 들어가게 된다. 이때 변수에 새로운 값을 재할당하게 되면 또다시 공간이 할당되어 메모리에 값이 들어가게 되고 처음 값을 가리키고 있었던 변수가 새로운 값이 가지고 있는 주소를 가리키게 된다. 이를 값과 식별자의 바인딩이라고 한다.   

```할당(allocate)```   
변수에 값을 할당하면 메모리 어딘가에 공간을 할당하여 값을 넣어주게 된다. 이를 allocate , 할당이라고 한다   

```해제(release)```   
값을 가지고 있었던 변수에 값을 재할당하게 되면 기존에 가리키고 있었던 값은 해제되고 새로운 값이 들어가 있는 메모리의 주소를 변수가 가리키게 된다.   

```var myNumaber = 23``` 값을 할당하면 메모리에 값이 ```할당```되어진다. 이때 새로운 값으로 재할당하게 되면 변수가 가리키고 있던 메모리가 ```해제```되고 새로운 메모리의 주소를 가리키게 된다. 이 과정을 값과 식별자의 ```바인딩```이라고 한다       
<img src="https://user-images.githubusercontent.com/64240637/110337172-f75db600-8068-11eb-91e5-ad1d1240faa1.png" width="500">

<br>

#### 👉 원시타입과 참조타입

자바스크립트의 변수 타입에는 원시타입(Primitive type)과 참조타입(Reference)으로 나누어져 있다.  

```원시타입```    
- 변수가 할당될때 메모리에 부여되는 크기가 고정되는 타입   

- 변수가 직접 메모리를 가리키고 있다   

- 처음 할당되어진 값은 절대 변하지 않기때문에 변수에 값을 재할당하게 되면 새로운 메모리 공간에 값이 저장되어진다.   

변수b에 원시값을 갖는 변수a를 할당하면 할당받는 변수b에는 원시값이 복사되어 전달된다. 이를 __값에 의한 전달(pass by value)__ 라고 한다.
```javascript
var a = 100;
var b = a;
var a = 50;

console.log(b); // 100
```

<img src ="https://user-images.githubusercontent.com/64240637/110760251-db892880-8291-11eb-8898-1ef2ad53975c.png" width=300>

변수 a에 100을 할당하면 메모리에 100의 값이 들어가게되고 해당 값 주소를 변수 a가 가리키고 있다. b에 a를 할당하면 a에는 100이라는 값이 저장되어 있기때문에 메모리에 b에도 100이 할당되어지고 메모리상에서도 b가 가리키고 있는 100의 주소가 생성되어진다. 이때 원시타입은 할당되어진 값은 변하지 않기때문에 a에 값을 재할당하게 되면 메모리에 새로운 곳에 50이 저장되고 변수 a가 50을 가리키게 된다. 따라서 a의 값이 바뀌어도 서로 가리키고 있는 위치가 다르기 때문에 b의 값은 변함이 없다. 

```원시타입 종류```   

```text
- 숫자
- 문자열
- boolean
- undefined
- null
- 심벌
```   
<br>

```참조타입```    
- 참조타입의 데이터는 크기가 정해져 있지 않고 동적으로 변한다   

- 변수는 데이터에 대한 주소가 저장된다. 자바스크립트 엔진이 변수가 가지고 있는 메모리 주소를 이용해 변수값에 접근한다      

객체를 가리키는 변수를 다른 변수 b에 할당하면 원본의 참조값이 복사되어 전달된다. 이를 __참조에 의한 전달(pass by reference)__ 라고 한다.
```javascript
var a = [];
var b = a;
var a = 'hi';

console.log(b) //hi
```

<img src ="https://user-images.githubusercontent.com/64240637/111060913-b0961300-84e3-11eb-8d46-e418bb915b43.png
" width=300>

객체의 데이터 자체는 별도의 메모리 공간(heap)에 저장되어진다. 변수에 값이 할당되면 데이터에 대한 주소(heap주소)가 저장되고 자바스크립트 엔진이 해당 주소를 가지고 변수값에 접근하기 때문에 a와 b가 가리키는 메모리 공간은 똑같다. 따라서 a의 값이 변하면 b의 값도 똑같이 변하게 된다.

```참조타입 종류```   

```text
- 배열   
- 함수    
- 객체    
```

<br>

#### 👉 네이밍 컨벤션
식별자를 만들때 가독성 좋게 한눈에 구분하기 위해 규정한 규칙이다   

```카멜케이스(camelCase)``` : 주로 변수나 함수명을 지을때 사용   

```스네이크케이스(snake_case)```   

```파스칼케이스(PascalCase)``` : 주로 생성자 함수나 클래스를 지을때 사용  

<br>

#### 👉 표현식

```값``` : 식이 평가되어 생성된 결과   
10+20은 평가되어 30이라는 결과를 생성하기 때문에 값이라고 할 수 있다.    
var num은 생성되는 결과가 없기 때문에 값이라고 할 수 없다
```javascript
10+20;  // 0

var num; // x
```

```리터럴``` : 사람이 이해할수 있는 문자나 약속된 기호로 표기한 코드    
값은 리터럴로 구성이 되어진다

```표현식``` : 값으로 평가될 수 있는 문으로 표현식이 평가되면 새로운 값을 생성하거나 기존값을 참조한다. 10+20에서 리터럴10과 20은 사람이 이해할 수 있는 문자로 자바스크립트 엔진에서 숫자 10,20으로 평가하여 결과를 생성하기 때문에 10,20은 값이라고 할 수 있으며 값으로 평가되어지기 때문에 표현식이라고도 할 수 있다        

```문``` : 문은 프로그램을 구성하는 기본 단위이자 최소 실행단위이며 여러가지 토큰으로 구성되어 있다    

```토큰``` : 문법적인 의미를 가지며 더이상 나눌 수 없는 코드의 기본 요소를 의미한다   

```javascript
var sum = 1 + 2; // 각각 토큰이라고 말 할 수 있다
```

``` 표현식인 문과 아닌문```    
표현식인지 아닌지 구분하는 것은 어렵다. 이럴땐 변수에 할당하여 계산해보면 쉽다    
```var pre = var x;``` 가능하지 않다   
```var y = x = 1+2;``` 가능하다

```javascript
var x = 1+ 2; // 값으로 평가되는 문으로 표현식이다

x = 1+2; // 식이 평가될 수 없기 때문에 값이 아니다. 따라서 표현식이라고 할 수 없다
```

<br>

#### 👉 템플릿 리터럴

ES6에 도입된 새로운 문자열 표기법이며 ``(백틱)을 사용해 표현한다     

```멀티라인 문자열``` : 원래는 문자라인을 바꾸는 것이 불가능하지만 멀티라인 문자열을 이용해 문자라인을 바꾸어 출력하는것이 가능해졌다
```javascript
var str = `hello
        nice to meet you`;
``` 

```표현식 삽입``` : ES5에서는 +연산자를 이용해 문자열을 연결했지만 표현식 삽입에서는 ```${}``` 기호를 이용해 나타낼 수 있다
```javascript
var name = 'hee';
var age = '24';

console.log(`my name ${name} age ${age}`)
```

<br>

#### 👉 연산자
연산자는 익숙하니 간단히 개념만 작성했다.    
(연산자는 하나 이상의 표현식을 대상으로) 여러 연산자를 이용해 하나의 값을 만든다. 산술,할당,비교 연산자들을 사용해 계산한다

<br>

#### 👉 제어문
제어문도 익숙하기 때문에 간단히 개념만 작성했다.    
제어문은 주어진 조건에 따라 코드블록을 실행(조건문 if)하거나 반복실행(for,while)할때 사용한다. 일반적인 플로우는 위에서 아래로 실행이 되지만 제어문에 의해 순서가 뒤죽박죽이 될 수 있다.    


## 예습
###### [모던 자바스크립트 Deep Dive를 읽고 정리한 내용](https://poiemaweb.com/)

#### 👉 객체란
객체는 0개 이상의 프로퍼티로 구성된 집합이며 프로퍼티는 키와 값으로 구성된다
```javascript
var person = {
        name : 'Lee';  // 프로퍼티
        age : 20  // age(프로퍼티 키), 20(프로퍼티 값)
}
```
- 프로퍼티 : 객체의 상태를 나타내는 값   
- 메서드 : 프로퍼티를 참조하고 조작할 수 있는 동작   
- 인스턴스 : 클래스에 의해 생성되어 메모리에 저장된 실체를 말한다.  
- 객체 : 클래스와 인스턴스를 포함한 개념, 프로퍼티들의 집합이며 프로퍼티는 키와 값으로 구성된다    
- 프로토타입 기반 객체지향 언어 : 자바스크립트는 프로토타입을 기반으로 한 언어이다   
- 객체 리터럴의 닫는 중괄호 뒤에는 세미콜론을 붙인다   