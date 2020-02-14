2 점근적 표기법
========

## 2.1 Big-Θ(빅 세타) 표기법 [최적값]

최악의 경우 선형검색의 실행 시간은 배열 크기인 n에 따라 커집니다. 
여기서 실행시간을 표시하기 위해 사용하는 표기법은 Θ(n)입니다.
이는 그리스어인 '세타'로 'n의 빅세타' 또는 그냥 'n의 세타'라고 읽습니다.

* 특정 실행 시간이 Θ(n)이라고 하는 것은 n이 충분히 크다면 실행시간은 어떤 상수 l과 m에 대하여 최소 lxf(n)이며 최대 mxf(n)가 된다는 뜻입니다. 
* n의 작은 값에 대해서는 lxn나 mxn와 실행시간을 어떻게 비교하는지 고려하지 않습니다.

*이점 : 우리가 사용하는 시간 단위를 고려할 필요가 없다.
* 실행시간에 대해 점근적으로 근접한 한계값이 있다고 표현하는 것
* '점근적'이라는 말을 쓰는 이유는 큰 값의 n에 대해서만 적용되기 때문이다.
* 근접한 한계값이라는 말은 위, 아래로 상수값 내에서 실행 시간을 좁힐 수 있다.

*목적 : 실행시간이 커지는 것을 일정 하한선과 상한선 내에서 점근적으로 제한하기 위해 Big-Θ 표기법을 사용합니다. 상한선만 정할 때도 있습니다.
- 이진검색의 실행시간은 결코 Θ(lg n)보다 느리지 않으며 때때로 더 나은 결과가 나오기도 한다.


## 2.2 점근적 표기법
* 미리 알고 가요
1. 알고리즘이 입력 크기와 상관 없이 일정한 시간이 소요될 때, n의 0승은 1이므로, Θ(n의 0승이 아니라), Θ(1)라고 쓴다.

2. a > 1일 때, 지수함수 a의 n승이 b가 상수인 모든 다항식 함수 n의 b승보다 빨리 커집니다.


## 2.3 Big-O(빅 오) 표기법 [최댓값]

*의미 : 실행시간은 최대한 이만큼 커지지만 더 천천히 커질 수도 있다.
실행시간이 O(f(n))이라면 충분히 큰 값인 n와 상수 k에 대해 실행시간은 최대 kxf(n)가 됩니다. 실행시간이 O(f(n))인 경우에 대해 이렇게 생각할 수 있다.

*목적 : 점근적 상한선에 사용합니다. 이는 충분히 큰 입력 크기에 대하여 실행 시간에 상한값을 두고 제한하기 때문입니다.


## 2.4 Big-Ω(빅 오메가) 표기법 [최솟값]

*목적 : 알고리즘이 상한선 없이 최소한 어느 정도 걸린다고 해야할 때 사용한다.
*점근적 하한선 : Big-Ω 를 사용하는 이유는 점근적 하한선은 충분히 큰 입력 크기에서 실행 시간을 밑에서 제한하기 때문이다.


## 2.5 관계

1. 이진검색의 실행 시간은 항상 O(lgn)라고 할 수 있습니다. 왜냐하면, 실행 시간은 일정한 시간 n 내의 속도로 커지기 때문입니다. 최악의 경우 실행 시간에 대해서 더욱 강력한 식을 만들 수도 있습니다. 바로 Θ(lg n)이죠. 그렇지만 모든 경우를 포괄하는 일반적 표현으로는 이진검색이 O(lg n) 시간 내에 실행된다고 하는 것이 가장 강력하게 표현하는 것입니다.

2. Big-Θ의 정의를 다시 보면 실행 시간에서 상한과 하한 둘 다 존재한다는 것을 제외하면 Big-O 표기법과 상당히 비슷합니다.
-특정 상황에서 실행시간이 Θ(f(n))라면, 이는 또한 O(f(n))이기도 합니다. 예를 들어 이진검색의 최대 실행 시간은 Θ(lg n)이기 때문에 O(lg n)이라고 할 수도 있습니다. 역이 항상 참이 되지는 않습니다. 앞에서도 봤듯이 이진검색이 O(lg n) 시간 안에 실행된다고 해서 항상 Θ(lg n) 시간에 실행되는 것은 아닙니다.

3. 

<pre><code>
/* Returns either the index of the location in the array,
  or -1 if the array did not contain the targetValue */
var doSearch = function(array, targetValue) {
  var min = 0;
  var max = array.length - 1; // 첫 번째 인덱스는 1이 아니라 0에서 시작합니다. 
  var guess;
  var targetValue;
  while(max >= min){ //max 값이 min보다 커야 반복문이 실행됩니다.
      guess = Math.floor(( max + min )/2); // 받은 인자에 Math.floor 함수를 써서 가운데 인덱스 값의 소수점을 버릴거에요.
      println(guess); // 각 단계의 guess를 출력하게 할래요.
      if(array[guess] < targetValue){ // 우리가 추론한 guess 값이 targetValue보다 작을 경우,  
          min = guess+1;  //범위를 하나씩 더 늘립니다.
      }
      else if(array[guess]> targetValue){ //우리가 추론한 guess 값이 targetValue보다 클 경우,
          max = guess-1; // 범위를 하나씩 더늘립니다.
      }
      else { //추론한 guess 값이 targetValue와 일치하다면
          return guess; // guess를 반환합니다.
      }
    }    
  return -1; // 배열에 targetValue가 없을 경우, -1을 반환합니다. 즉 max < min이면 더이상 반복문을 돌리지 않습니다.
};

var primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 
    41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97];

var result = doSearch(primes, 73);
println("Found prime at index " + result);

Program.assertEqual(doSearch(primes, 73), 20);
</code></pre>



본 문서는 칸 아카데미의 알고리즘 강좌를 참조하였습니다.
출처: [칸아카데미](https://ko.khanacademy.org/computing/computer-science/algorithms/binary-search)

