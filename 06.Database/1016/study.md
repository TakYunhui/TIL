# N : M
## M : N 관계의 역할과 필요성
### N : 1 의 한계
- (ex) 진료 예약 시스템
1. 환자 carol(1번)이 두 의사 모두에게 진료를 받고자 한다면 환자 테이블에 1번 환자 데이터가 중복으로 입력됨 
2. 문법 구조 상 동시에 예약을 남길 수 없다
3. 동일한 환자지만 다른 의사에게도 진료받으려면 객체를 하나 더 만들어 진행해야 함
- ex_1.py

📑 예약 테이블을 따로 만들자 
- 새로운 중개 모델로 의사와 환자에 대해서 각각 n : 1 관계를 가진다 
- ex_2.py
```
In [8]: doctor1.reservation_set.all()
   ...: 
Out[8]: <QuerySet [<Reservation: 1번 의사의 1번 환
자>, <Reservation: 1번 의사의 2번 환자>]>
```

### ManyToManyField 
- 서로에게 종속된 관계 x 
- MTMField 사고하기 좋은 위치에 작성 (참조, 역참조 관계만 바뀜)


### through argument
- 중개 테이블에 '추가 데이터'를 사용해 M:N 관계를 형성하려는 경우에 사용
- 예약정보에 '증상'과 '예약일' 추가

### M:N 관계 주요 사항
1. M:N 관계로 맺어진 두 테이블에는 물리적 변화가 없음
2. MTMfield는 중개 테이블을 자동으로 생성
3. MTMfield는 M:N 관계를 맺는 두 모델 어디에 위치해도 상관 없음 (단, 위치에 따라 참조 방향 주의)
4. M:N은 N:1과 달리 종속관계가 아니고 2가지 형태의 표현 가능

### ManyToManyField(to, **options)
- related_name 인자 : 역참조시 사용하는 manager name 변경 (단, 변경 후에는 변경 전 이름 사용 불가)
- symmetrical 인자 : MTM이 동일한 모델(자기 스스로)을 가리킬 때 사용
- add() method : 지정된 객체를 관련 객체 집합에 추가(이미 존재한 관계는 복제 x)
- remove() method : 관련 객체 집합에서 지정된 모델 객체 제거
```
Article : User (N:1)
N : 1에서의 역참조 -> user.article_set.all()
Article : User (N:M)
N : M에서의 역참조 -> user.article_set.all()
```
- 역참조 manage 충돌 -> related_name으로 해결
