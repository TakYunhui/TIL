# GIT 이란...
> 분산 버전 관리 시스템

## Git의 3가지 영역
1. Working Area
  - 실제 작업 영역
2. Staging Area

3. Repository
 - 버전(commit) 이력과 파일들이 영구적으로 저장되는 영역, 모든 버전과 변경 이록이 기록됨 
### git 초기화
```bash
$ git init
```
#### 숨겨진 폴더 보기 
```bash
$ ls -a
```
### 상태 확인 명령어
```bash
$ git status
```
### staging area에 추가
```bash
$ git add {path} <folder_name>/{file_name}
```
### Repository에 저장하기
```bash
$ git commit -m "commit message"
```
### git 기초 설정
```bash
$ git config --global user.email "gwalgwal98@naver.com"
$ git config --global user.name "탁윤희"
$ git config --global --list
```

### 커밋 기록 확인하기
```bash
$ git log
```
### 직전 커밋 수정 
```bash
$ git commit --amend 
# vim에서 커밋 내용 수정 
# 1. insert를 눌러서 삽입 상태로 만든다
# 2. 커밋 메시지를 수정한다
# 3. ESC를 눌러 삽입 상태를 종료한다
# 4. :wq를 입력해서 저장하고 종료한다
```
