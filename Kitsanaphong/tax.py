
def calculate_tax(income):
    brackets = [
        (150000, 0.00),
        (300000, 0.05),
        (500000, 0.10),
        (750000, 0.15),
        (1000000, 0.20),
        (2000000, 0.25),
        (5000000, 0.30),
        (float('inf'), 0.35),
    ]

    total_tax = 0
    lower = 0
    details = []  # เก็บรายละเอียดภาษีแต่ละขั้น

    for upper, rate in brackets:
        if income > lower:
            taxable = min(income, upper) - lower
            tax = taxable * rate
            total_tax += tax
            if taxable > 0:
                details.append((lower, min(income, upper), rate, tax))
            lower = upper
        else:
            break

    return total_tax, details

def show_result(name, income):
    total_tax, details = calculate_tax(income)
    after_tax = income - total_tax
    effective_rate = (total_tax / income * 100) if income > 0 else 0 

    print(f"\n=== Tax calculation results{name} ===")
    print("\nTax details")
    print()
    for lower, upper, rate, tax in details:
        print(f"{lower:,.0f} - {upper:,.0f}\t\t{tax:,.0f} บาท")

    print(f"\nภาษีรวม\t\t{total_tax:,.0f} บาท")
    print(f"รายได้หลังหักภาษี\t{after_tax:,.0f} บาท")
    print(f"Effective Tax Rate = {effective_rate:.2f}%")

    return total_tax, after_tax, effective_rate


def calculate_single():
    income = float(input("กรอกเงินได้สุทธิ : "))
    show_result("", income)


def calculate_multiple():
    n = int(input("กรอกจำนวนคน : "))
    summary = []

    for i in range(1, n + 1):
        income = float(input(f"กรอกเงินได้สุทธิของคนที่ {i} : "))
        total_tax, after_tax, effective_rate = show_result(f" (คนที่ {i})", income)
        summary.append((i, income, total_tax, after_tax, effective_rate))

    # สรุปผลรวมทุกคน
    print("\n=== สรุปผลทุกคน ===")
    print(f"{'คนที่':<8}{'เงินได้สุทธิ':>15}{'ภาษีรวม':>15}{'รายได้หลังหักภาษี':>20}{'Effective Rate':>18}")
    for i, income, total_tax, after_tax, effective_rate in summary:
        print(f"{i:<8}{income:>15,.0f}{total_tax:>15,.0f}{after_tax:>20,.0f}{effective_rate:>17.2f}%")


def main():
    print("=== โปรแกรมคำนวณภาษีเงินได้บุคคลธรรมดา ===")
    print("1. คำนวณภาษีคนเดียว")
    print("2. คำนวณภาษีหลายคน")
    choice = input("เลือกเมนู (1/2) : ").strip()

    if choice == "1":
        calculate_single()
    elif choice == "2":
        calculate_multiple()
    else:
        print("กรุณาเลือก 1 หรือ 2 เท่านั้น")


if __name__ == "__main__":
    main()