taxi,groups,children = [0] * 5,int(input()),list(map(int, input().split()))
for i in children:taxi[i] += 1
print(taxi[4] + taxi[3] + taxi[2] // 2 + (max(0, taxi[1] - taxi[3] - 2 * (taxi[2] % 2)) - 1) // 4 + 1 + taxi[2] % 2)