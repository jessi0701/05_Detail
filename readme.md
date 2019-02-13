# readme

### 1.Django setting

  별다른 어려움 없었습니다.

### 2.base.html 구성

  navbar를 만들 때 왼쪽 오른쪽 으로 구역을 나눠서 왼쪽은 왼쪽 정렬, 오른쪽은 오른쪽 정렬을 하였습니다.

### 3. 페이지 구성

1. / : header 부분은 css를 활용하여 높이와 배경화면을 설정하였습니다. 배경화면은 반복하지 않고 너비 높이 100%를 줘서 꽉차게 만들었습니다.

2. signup/ : 그림부분이랑 SignUp부분을 row col을 활용해서 분리시켰습니다.

3. mypage/ : signup과 마찬가지인데 카드는 절대위치에 위치해야되는걸 몰랐는데 검색해보니 position:fixed; 라는 기능을 활용해서 고정시켰습니다.

4. qna/ : 먼저 제목인 Q&A를 영역을 할당하여 가운데 정렬한 후, 제목과 이메일은 col-md-6 mb-3을 각각 줘서 2등분 할수 있도록 하고 내용은 textarea속성을 활용해서 구성했습니다.

5. <str:not_found>/ : variable routing 을 잘 몰랐었는데 전에 한 수업내용을 참고하여 작성하였습니다. str값을 주소에서 받아와 에러페이지를 수정할때 이용했습니다.