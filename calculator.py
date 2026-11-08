"""두 숫자의 사칙연산을 수행하는 간단한 계산기입니다."""


def main():
    # 사용자에게 숫자 두 개를 입력받습니다.
    try:
        first_number = float(input("첫 번째 숫자를 입력하세요: "))
        second_number = float(input("두 번째 숫자를 입력하세요: "))
    except ValueError:
        print("오류: 숫자만 입력해 주세요.")
        return

    # 어떤 계산을 할지 기호로 입력받습니다.
    operator = input("연산자를 입력하세요 (+, -, *, /): ").strip()

    # 입력한 연산자에 맞는 계산을 수행합니다.
    if operator == "+":
        result = first_number + second_number
    elif operator == "-":
        result = first_number - second_number
    elif operator == "*":
        result = first_number * second_number
    elif operator == "/":
        # 나누는 수가 0이면 계산할 수 없으므로 안내하고 종료합니다.
        if second_number == 0:
            print("오류: 0으로 나눌 수 없습니다.")
            return
        result = first_number / second_number
    else:
        print("오류: 지원하지 않는 연산자입니다. +, -, *, / 중에서 입력해 주세요.")
        return

    print(f"결과: {result}")


if __name__ == "__main__":
    main()
