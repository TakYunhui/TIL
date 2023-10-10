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
-> SQLite 사용 
-> 프로그램 별 함수, 데이터 타입 등은 다를 수 있다

## DQL
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


## DDL
### CREATE 
- 테이블 생성 : CREATE TABLE
```
[데이터 타입]
1. NULL : 아무런 값도 포함하지 않음
2. INTEGER : 정수
3. REAL : 부동 소수점
4. TEXT : 문자열
5. BLOB : 이미지, 동영상, 문서 등 바이너리 데이터
```
```
[제약 조건]
1. PRIMARY KEY : 기본 키 지정
2. NOT NULL : 해당 필드에 NULL 값 허용 X  
3. FOREIGN KEY : 다른 테이블과의 외래 키 관계 정의
```

### ALTER
- 테이블 및 필드 조작 : ALTER TABLE
```
1. ADD COLUMN : 필드 추가
2. RENAME COLUMN : 필드 이름 변경
3. DROP COLUMN : 필드 삭제
- PK 가 아니며 UNIQUE 제약 조건이 없는 경우에만 작동 
4. RENAME TO : 테이블 이름 변경
```


## DML
### INSERT
- 테이블 레코드 삽입 : INSERT INTO
```SQL
INSERT INTO
  테이블명 (title, content, createdAt)
VALUES 
  ('title1', 'content1', '1900-01-01'),
  ('title2', 'content2', '1800-01-01'),
  ('title3', 'content3', '1700-01-01');
```

### DELETE
- 테이블 레코드 삭제 : DELETE FROM

### UPDATE
- 테이블 레코드 수정 
```SQL
UPDATE tablename
SET 세부사항
WHERE 조건
```

### JOIN
#### INNER JOIN
- 두 테이블에서 값이 일치하는 레코드에 대해서만 결과 반환
- 회원이 작성한 모든 게시글의 제목과 작성자명 조회
#### LEFT JOIN
- 오른쪽 테이블의 일치하는 레코드와 함께 왼쪽 테이블의 모든 레코드 반환
- 게시글을 작성한 이력이 없는(NULL) 회원정보 조회 

##### 계정 비활성화
- 계정이 완전 삭제된 것이 아니라 대체할 어떤 정보로 만들어 둔다
- 데이터 저장 안 해두면 복구 안 됨