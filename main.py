# 그리디01 동전 거슬러주기 문제
n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]

for coin in coin_types:
  count += n // coin
  n %= coin

print(count)

# 그리디02 큰 수의 법칙 문제 #내가 푼거
n, m, k = map(int, input().split())
given_numbers = list(map(int, input().split()))
data = given_numbers.sort()

data[-1]
data[-2]

result = 0
count1 = 0
count2 = 0

if m >= k:
  count1 += m // (k + 1)
  count2 += m % (k + 1)
  result = (data[-1] * k * (count1 + count2)) + (data[-2] * count1)
  print(result)
else:
  print(m * data[-1])

# 그리디02 #답안예시
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[-1]
second = data[2]

count = int(m // (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first
result += (m - count) * second
print(result)

# 그리디03 # 숫자 카드 게임 # 내가 푼 풀이
n, m = map(int, input().split())
min_list = []
result = 0

for _ in range(n):
  data = list(map(int, input().split()))
  min_list.append(data[min])
print(min_list(sum))

# 그리디03 # 숫자 카드 게임 # 이중 for문을 이용해보자
n, m = map(int, input().split())
result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
  data = list(map(int, input().split()))
  min_value = 10001
  for a in data:
    min_value = min(min_value, a)
  result = max(result, min_value)  #max 가장 큰수 구하기를 이렇게?

print(result)

# 그리디04 # 1이 될때까지 #내가 푼 문제
n, k = map(int, input().split())
count = 0

while n >= k:
  if n % k == 0:
    n = n // k
    count += 1
    if n == 1:
      print(count)
      break
  else:
    n -= 1
    count += 1
    if n == 1:
      print(count)
      break

if n < k:
  count = n - 1
  print(count)

# 그리디04 #1이 될때까지 #답안예시
n, k = map(int, input().split())
result = 0

while True:
  target = (n // k) * k
  result += (n - target)
  n = target
  if n < k:
    break
  result += 1
  n //= k

result += (n - 1)
print(result)

# 그리디04 #1이 될때까지 #단순하게 풀기
n, k = map(int, input().split())
result = 0

while n >= k:
  while n % k != 0:
    n -= 1
    result += 1
  n = n // k
  result += 1

#n이 k보다 작아지면 (n < k)
while n > 1:
  n -= 1
  result += 1

print(result)
