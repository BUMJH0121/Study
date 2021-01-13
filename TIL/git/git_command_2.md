### git



​	**repos**에 다른 사람을 **초대**하여 협업할 수 있다.

​	협업 중 발생한 merge상황에 다른사람과 상의하여 정리 후 commit



#### pull

 - **github**에 올라가 있는 데이터를 **local 컴퓨터**로 가져와 동기화

   `git pull origin(url) branch이름`

#### clone

​	**github**에서 **repos**를 복사해옴

​	`git clone repos주소`

​	**clone**과 **zip파일 다운로드**의 차이점

		- **clone**은 **commit**기록까지 전부 다운 받지만 **zip파일**은 파일만 다운받음



#### switch(checkout)

​	**branch**를 이동

​	`git switch 이동할 branch 이름`



#### branch

​	**branch**를 관리

​	`git branch` : branch이름들을 확인

​	`git branch -d branch이름`: branch를 삭제

​	`git branch 이름` : 새로운 branch 생성



#### merge

​	branch끼리 병합

​	`git merge branch이름`: 현재 활성화된 branch에 branch이름의 branch를 병합



#### restore

​	commit하기 전 unstage시키는 명령어

​	`git restore --staged 파일이름`



#### amend

​	바로 전 commit의 메세지를 수정

​	`git commit -amend`



#### reset

​	마지막 commit을 취소

​	`git reset HEAD^`

​	^갯수 : 취소하고 싶은 commit 갯수



### git-scm.com

​	공식사이트