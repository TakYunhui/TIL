# Databse
#### 관계형 데이터베이스

> SSAFY 10기 Databse 과정 라이브 강의 코드

| 진행일 | 주제                    |
| ------ | ----------------------- |
| 10/10  | SQL  |
| 10/11  | Many to one relationships 1 |
| 10/12 | Many to one relationships 2 |
| 10/16 | Many to many relationships 1 |
| 10/17 | Many to many relationships 2 |


## 231010: DQL
### Query
- 데이터베이스로부터 정보를 요청
- SQL 작성 코드 => 쿼리문(SQL문)

### DQL(Data Query Language)

### SELECT statement 실행 순서
1. 테이블에서(FROM)
2. 조회(SELECT)
3. 정렬(ORDER BY)
#### 레코드 조회
- 레코드 검색 : SELECT
```sql
SELECT 
  statement 
FROM
  table_name;
```
- SELECT 이후 레코드를 선택하려는 필드 하나 이상 지정
- FROM 이후 레코드를 선택하려는 테이블의 이름 지정
- enter 영향 x, ';' 종료가 중요
- 쿼리문 오른쪽 마우스 클릭 후 Run Selected Query (선택된 쿼리문만 실행)

#### 레코드 정렬
- 조회 결과 레코드 정렬 : ORDER BY
```sql
ORDER BY 
  column1 [ASC|DESC],
  column2 [ASC|DESC]
```
- SELECT 문 이후에 작성 
- column을 기준으로 결과를 오름차순(ASC, 기본값), 내림차순(DESC) 정렬

#### Filtering
- DISTINCT : 중복 제거 
- WHERE : 조회 시 특정 조건 지정
- ORDER BY 는 WHERE 절보다 뒤쪽에 위치
```
[비교 연산자]
=, >=, <=, != 
IS : NULL 타입과 함께 사용하여 일치 여부 확인
LIKE : 값이 특정 패턴에 일치하는지 확인(Wildcards 와 함께 사용)
 (*) Wildcard 
    1. % : 0 개 이상의 문자열과 일치하는지 확인
    2. _ : 단일 문자와 일치하는지 확인
IN : 값이 특정 목록 안에 있는지 확인
BETWEEN, AND
[논리 연산자]
AND(&&), OR(||), NOT(!)
```
- LIMIT : 조회 제한

#### 레코드 그룹화 
- 레코드를 그룹화하여 요약본 생성 : GROUP BY
- 집계 함수와 함께 사용
- 집계 함수 : SUM, AVG, MAX, MIN, COUNT