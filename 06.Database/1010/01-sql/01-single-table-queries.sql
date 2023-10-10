-- 01. Querying data (SELECT)
-- 1. 단일 필드 조회 
SELECT
  LastName
FROM
  employees;

-- 2. 여러 개의 필드 조회
SELECT
  LastName, FirstName
FROM
  employees;

-- 3. 전체 조회 
SELECT
  *
FROM
  employees;

-- 4. 열이름 수정하여 출력
SELECT
  FirstName AS '이름'
FROM
  employees;

-- 5. 필드 데이터 조건(연산)
SELECT 
  Name, Milliseconds / 60000 AS '재생 시간(분)'
FROM
  tracks;

-- 02. Sorting data (ORDER BY)
-- 1. 오름차순 정렬
SELECT
  FirstName 
FROM
  employees
ORDER BY 
  FirstName;

-- 2. 내림차순 정렬
SELECT
  FirstName 
FROM
  employees

ORDER BY 
  FirstName DESC;

-- 3. 하나 이상의 컬럼으로 결과 정렬
SELECT 
  Country, City
FROM 
  customers
ORDER BY
  Country DESC,
  City ASC;

-- 4. 조건 + 정렬
SELECT 
  Name, Milliseconds / 60000 AS '재생 시간(분)'
FROM
  tracks
ORDER BY 
  Milliseconds DESC;

-- NULL 정렬 예시
-- NULL 오름차순 정렬에서 가장 먼저 출력
SELECT
  ReportsTo
FROM
  employees
ORDER BY
  ReportsTo;

-- 03. Filtering data (WHERE)
-- 1. 중복 제거
SELECT DISTINCT
  Country
FROM
  customers
ORDER BY
  Country;

-- 2. 조회 조건 지정
SELECT 
  LastName, FirstName, City
FROM 
  customers
WHERE
  City = 'Prague';

-- 3. 여러 조건 지정
SELECT 
  LastName, FirstName, Company, Country
FROM 
  customers
WHERE
  -- NULL 조회
  Company IS NULL
  AND Country = 'USA';

SELECT 
  Name, Bytes
FROM 
  tracks
WHERE
  -- 숫자 데이터 범위 지정
  Bytes BETWEEN 100000 AND 500000;

SELECT 
  Name, Bytes
FROM 
  tracks
WHERE
  Bytes BETWEEN 100000 AND 500000
ORDER BY
  Bytes;

SELECT 
  LastName, FirstName, Country
FROM 
  customers
WHERE
  -- 해당하면 출력 
  -- 부정형 NOT IN
  Country IN ('Canada', 'Germany', 'France');

SELECT 
  LastName, FirstName
FROM 
  customers
WHERE
  -- 특정한 문자열로 끝나는 조건
  LastName LIKE '%son';

SELECT 
  LastName, FirstName
FROM 
  customers
WHERE
  -- 특정한 문자열로 끝나는 조건 + 필드 자리 수 
  FirstName LIKE '___a';

-- 조회하는 레코드 수 제한
SELECT 
  TrackId, Name, Bytes
FROM 
  tracks
ORDER BY
  Bytes DESC
LIMIT 7;

SELECT 
  TrackId, Name, Bytes
FROM 
  tracks
ORDER BY
  Bytes DESC
-- OFFSET 상쇄
LIMIT 3, 4;


-- 04. Grouping data
SELECT
  Country
FROM
  customers
GROUP BY
  Country;

SELECT 
  Composer, AVG(Bytes)
FROM
  tracks
GROUP BY
  Composer
ORDER BY
  AVG(Bytes) DESC;

SELECT 
  Composer,
  AVG(Milliseconds / 60000) AS avgOfMinute
FROM
  tracks
GROUP BY
  Composer
-- 집계 항목에 대한 세부 조건 지정 
HAVING
  avgOfMinute < 10;

-- 에러


-- 에러 해결
