# [BOJ]/[1992]쿼드트리

### -분할정복(DIVIDE & CONQUER)-

* `QuadTree()`: 주어진 영상정보 배열`map[][]`에서 지정한 범위 내에 숫자가 모두 같은지 확인하는 메소드
  * `s_x`: 범위 시작의 x좌표
  * `s_y`: 범위 시작의 y좌표
  * `N`: 해당 범위의 가로/세로 크기
  * :arrow_forward:내부 숫자가 하나의 숫자만(0또는 1)으로 이루어져 있다면 그 수 출력
  * :arrow_forward:내부에 0과 1이 같이 존재한다면 왼쪽 위`(s_x, s_y)`, 오른쪽 위`(s_x, s_y+halfN)`, 왼쪽 아래`(s_x+halfN, s_y)`, 오른쪽 아래`(s_x+halfN, s_y+halfN)`의 범위 시작점과 원래 범위의 절반크기인 `halfN`을 이용해 재귀로 호출



(:heavy_plus_sign:문제를 작은 부분으로 나눠서 똑같은 규칙이 적용된다면 '분할정복'사용하기!

​		=> 재귀 호출 이용해 계산)









