- 시뮬레이션

경우의 수(cur 기준)
1. 평지
2. (활주로 없고) 한 칸 낮아진 경우
3. (활주로 없고) 한 칸 높아진 경우(지나 온 길에 활주로가 없어야함)
4. 그 밖의 경우

재귀로 풀려고하다가 한 줄을 자르면 리턴값이 달라진다는 것을 깨닫고 한줄씩 완전탐색 했습니다.

1. main함수에서 한줄씩 보내주는 역할을 합니다.
<pre>
<code>
for i in range(n):
      answer += check(array[i], x)
      tmp = []
      for j in range(n):
        tmp.append(array[j][i])
      answer += check(tmp, x)
</code>
</pre>

2. check함수에서 활주로건설 가능/불가능을 리턴해줍니다.
위의 경우의 수를 고려하여 네개의 if문으로 구성했지만 난항을 겪었습니다.

그 이유는 바로바로.. 괄호로 표시했듯, 활주로가 이미 건설됐는지아닌지를 고려하지 않았기때문입니다..

그래서 활주로 건설 표시 배열도 생성해줌으로써 활주로가 있는지 없는지까지 고려하였습니다. - 요부분은 어떻게 활주로 건설여부를 효율적으로 체크할지 떠오르지 않아서 다른 분들의 코드를 보고 도움을 좀 받았습니다. 

활주로건설여부를 표시한 후에도 새로 건설할 때 고려할 것이 또 있었습니다...

고려할 때에 중요하게 생각한 것은 높이가 높아질때와 낮아질 때의 경우가 다르다는 것입니다.

낮아진 경우는 인덱스 값을 늘려가면서 체크하면 되지만

높아진 경우는 뒤를 고려해야하기때문에 활주로 체크를 cur과 그 다음 것 동시에 모두 해줘야했습니다.
<pre>
<code>
elif cur-prev == 1:
      if i-x >= 0:
        for j in range(1,x):
          if const[i-j] != 1 and const[i-j-1] != 1:
            if arr[i-j] != arr[i-j-1] or const[i-j] == 1:
              re = -1
              break
            else:
              const[i-j] = 1
          else:
              re = -1
              break
        if re == -1:
          flag = False
          break
        else:
          const[i-x] = 1
          prev = cur
      else:
        flag = False
        break
</code>
</pre>
***
길고 복잡하게 짠 것 같아 마음이 착잡합니다.. 다음에 시뮬레이션을 푼다면, 문제의 경우의 수를 빨리 파악하여 풀어야겠습니다.
