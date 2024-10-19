import random


def generate_test_case(n, m):
    operations = []
    for _ in range(m):
        op_type = random.choice(["update", "buy"])
        item_id = random.randint(1, n)
        money = random.randint(50, 500)
        operations.append(f"{op_type} {item_id} {money}")

    return f"{n} {m}\n" + "\n".join(operations)


# 示例生成测试用例
n = 10 ** 4  # 商品总数
m = 10 ** 4  # 日志行数
test_case = generate_test_case(n, m)

with open("test_case.txt", "w") as f:
    f.write(test_case)

print("测试用例已写入 test_case.txt")