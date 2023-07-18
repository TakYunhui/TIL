# Type Conversion
### 명시적 형변환
- 개발자가 직접 형변환을 하는 것

   - str -> integer: 형식에 맞는 숫자만 가능
   - integer -> str: 모두 가능 
   - range, dict로 바꾸기 불가 
   - dict는 str 제외 key값만 바꾸기 가능 
   - 나머지는 다 됨

### 암시적 형변환
- 파이썬이 자동으로 형변환을 하는 것
   
   Boolean과 Numeric type에서만 가능
  - 0 = False, 0이 아닌 다른 수 = True

### 연산자 
1. 산술 연산자 
2. 복합 연산자
- 연산과 할당이 함께 이뤄짐
  - a+= i  -> a = a + i
3. 비교 연산자
- is 비교 연산자: 메모리 내에서 같은 객체를 참조하는지 확인
  - ==(동등성: equality), is(식별성: identity)
  - is 연산자는 되도록 None, True, False 등을 비교
4. 논리 연산자 
- and, or, not
 > 단축평가: 논리 연산에서 두 번째 피연산자를 평가하지 않고 결과를 결정하는 동작

    - F and T -> 앞에서 F가 나왔으므로 F로 평가 끝
    - T or F -> 앞에서 T가 나왔으므로 T로 평가 끝