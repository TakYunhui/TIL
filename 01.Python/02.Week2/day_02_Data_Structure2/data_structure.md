# 코드 예시 많이 보기
### 비시퀀스형 구조
- set: 고유한 항목들의 정렬되지 않은 컬렉션(중복x, 순서x)

> 세트 메서드
1. s.add(x): 세트 s에 항목 x를 추가, 이미 x가 있다면 변화 없음 (중복x)
- 
2. s.clear(): 세트 s의 모든 항목 제거
3. s.remove(x): 항목 x 제거, 존재하지 않는 요소를 x로 사용하면 Key error
4. s.pop(): '임의'의 요소를 제거하고 '반환' -> set는 순서가 없어서
5. s.discard(x): x 제거, 존재하지 않는 요소로 실행해도 에러 x, None 인듯?
6. s.update(iterable): s에 다른 iterable 요소 추가
> 세트의 집합 메서드
1. set1.difference(set2): set1에는 있지만 2에는 없는 항목으로 세트를 생성 후 반환 차집합
- set - set2
2. set1.intersection(set2): 합집합
- set1 & set2
3. set1.issubset(set2): set1 항목이 모두 2 에 있으면 True
- set1 <= set2
4. set1.issuperset(set2): set1 항목이 set2 항목을 모두 가지면 True
- set1 >= set2
5. set1.union(set2): set1 또는 set2, 혹은 둘 다에 들어있는 항목 
- set1 | set2

> 딕셔너리 메서드
1. D.clear():모든 요소 제거
2. D.get(key[,default]): 키 연결된 값을 반환하거나 키가 없음 None 혹은 기본 값 반환
3. D.keys(): 딕셔너리 키를 모은 객체를 반환 
4. D.pop(key[,default]): 키를 제거하고 연결됐던 값을 반환 (없으면 에러나 default 반환)
5. D.setdefault(key[,default]): 키와 연결된 값을 반환 -> get과 같음
- 키가 없다면 default와 연결한 키를 딕셔너리에 추가하고 default를 반환
6. .update([other]): other가 제공하는 키/값 쌍으로 딕셔너리 갱신, 기존 키는 덮어씀

> 데이터 타입과 복사
### 가변형 데이터 타입의 복사
- 같은 주소를 보고 있었기에 같이 수정

### 불변형 데이터 타입의 복사
- 같은 주소 공유 x, 값을 공유하였기에 참조 방향을 바꾼 걸로 같이 수정되지 않는다!

> 복사 유형

1. 할당
- 같은 주소를 보게 된다....
- 할당 연산자 = 를 통한 복사는 해당 객체에 대한 객체 참조를 복사

2. 얕은 복사 
- 슬라이싱으로 자르기 
- 참조 주소가 바뀐다 
- 슬라이싱을 통해 생성된 객체는 원본 객체와 독립적으로 존재

+ copy(교재 코드 참고)