# 그대로 출력하기2
# 입력 받은 대로 출력하는 프로그램
# 파이썬은 받은대로 출력함
# 입력 없으면 탈출? -> sys.stdin.read()는 공백포함 문자를 받고 EOF까지 판단함
import sys
data = sys.stdin.read()
print(data, end=" ")