BASE_FEE = 5.00
TAX_RATE = 0.14
FEE_AFTER_100 = 0.03
FEE_AFTER_300 = 0.02
SENTINEL = -1

def main():
    customer_data = []

    while True:
        area_code = input("Enter area code (3 digits) or -1 to quit: ")
        if area_code == str(SENTINEL):
            break

        phone_number = input("Enter phone number (7 digits): ")
        total_messages = int(input("Enter total number of text messages sent: "))

        extra_fees = 0
        if total_messages > 100:
            if total_messages <= 300:
                extra_fees = (total_messages - 100) * FEE_AFTER_100
            else:
                extra_fees = (200 * FEE_AFTER_100) + ((total_messages - 300) * FEE_AFTER_300)

        monthly_bill_before_tax = BASE_FEE + extra_fees
        monthly_bill_after_tax = monthly_bill_before_tax * (1 + TAX_RATE)

        customer_entry = {
            'area_code': area_code,
            'phone_number': phone_number,
            'total_messages': total_messages,
            'monthly_bill_before_tax': monthly_bill_before_tax,
            'monthly_bill_after_tax': monthly_bill_after_tax
        }
        customer_data.append(customer_entry)

        if total_messages > 100 or monthly_bill_after_tax > 10:
            print(f"Area Code: {area_code}")
            print(f"Phone Number: {phone_number}")
            print(f"Total Messages Sent: {total_messages}")
            print(f"Monthly Bill Before Tax: ${monthly_bill_before_tax:.2f}")
            print(f"Monthly Bill After Tax: ${monthly_bill_after_tax:.2f}")

    report_area_code = input("Enter an area code to view bills from that area (or -1 to quit): ")
    
    while report_area_code != str(SENTINEL):
        print(f"Area Code Report for: {report_area_code}")
        for customer in customer_data:
            if customer['area_code'] == report_area_code:
                print(f"Phone Number: {customer['phone_number']}")
                print(f"Total Messages Sent: {customer['total_messages']}")
                print(f"Monthly Bill After Tax: ${customer['monthly_bill_after_tax']:.2f}")

        report_area_code = input("Enter another area code to view bills, or -1 to exit: ")

if __name__ == "__main__":
    main()
