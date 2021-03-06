def main():
    n = int(input())  # 테스트케이스 갯수
    for i in range(n):
        answer = 0
        m, bc = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))  # a,b 이동경로 저장
        charger = []
        for j in range(bc):
            charger.append(list(map(int, input().split())))
        tmp_a = []
        tmp_b = []
        cur_a = [1, 1]
        cur_b = [10, 10]
        for k in charger:
            loc = (k[0], k[1])
            if abs(cur_a[0] - loc[0]) + abs(cur_a[1] - loc[1]) <= k[2]:
                tmp_a.append(k[3])
            else:
                tmp_a.append(-1)
            if abs(cur_b[0] - loc[0]) + abs(cur_b[1] - loc[1]) <= k[2]:
                tmp_b.append(k[3])
            else:
                tmp_b.append(-1)
        if max(tmp_a) != -1:
            answer += max(tmp_a)
        if max(tmp_b) != -1:
            answer += max(tmp_b)

        for j in range(m):
            if a[j] == 1:  # 시시각각 변하는 a의 위치...
                cur_a[1] -= 1
            elif a[j] == 2:
                cur_a[0] += 1
            elif a[j] == 3:
                cur_a[1] += 1
            elif a[j] == 4:
                cur_a[0] -= 1

            if b[j] == 1:  # 동시에 변하는 b의 위치..
                cur_b[1] -= 1
            elif b[j] == 2:
                cur_b[0] += 1
            elif b[j] == 3:
                cur_b[1] += 1
            elif b[j] == 4:
                cur_b[0] -= 1
            pos_a = []
            pos_b = []
            for k in charger:  # 효율적인 bc선정을 위해 bc정보 모두 저장...
                loc = (k[0], k[1])
                if abs(cur_a[0] - loc[0]) + abs(cur_a[1] - loc[1]) <= k[2]:
                    pos_a.append(k[3])
                else:
                    pos_a.append(-1)
                if abs(cur_b[0] - loc[0]) + abs(cur_b[1] - loc[1]) <= k[2]:
                    pos_b.append(k[3])
                else:
                    pos_b.append(-1)

            maxa = max(pos_a)
            maxb = max(pos_b)
            tmpmaxa = []
            tmpmaxb = []
            if maxa != -1 and maxb != -1:  # 최선의 bc를 찾는 중...
                if pos_a.index(maxa) == pos_b.index(maxb):
                    answer += maxa
                    for sb in pos_a:
                        if sb != maxa and sb != -1:
                            tmpmaxa.append(sb)
                    for sb in pos_b:
                        if sb != maxb and sb != -1:
                            tmpmaxb.append(sb)
                    tmp = tmpmaxa + tmpmaxb
                    if tmp:
                        answer += max(tmp)
                else:
                    answer += maxa + maxb

            else:
                if maxa != -1:
                    answer += maxa
                if maxb != -1:
                    answer += maxb

        print("#", end="")
        print(i + 1, end=" ")
        print(answer)


main()
