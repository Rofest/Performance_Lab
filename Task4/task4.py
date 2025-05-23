import sys

def main():
    if len(sys.argv) != 2:
        print("Использование: python task4.py numbers.txt")
        sys.exit(1)

    try:
        with open(sys.argv[1], encoding='utf-8') as f:
            nums = list(map(int, f.read().split()))
    except Exception:
        print("Ошибка чтения или неверный формат файла", file=sys.stderr)
        sys.exit(1)

    if not nums:
        print("Файл не содержит чисел", file=sys.stderr)
        sys.exit(1)

    nums.sort()
    med = nums[len(nums) // 2]
    moves = sum(abs(x - med) for x in nums)
    print(moves)

main()