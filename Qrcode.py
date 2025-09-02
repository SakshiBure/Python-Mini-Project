import qrcode  # type: ignore

# Taking UPI ID as input
upi_id = input("Enter your UPI ID: ")

# Payment URL template (customize amount, currency, message)
amount = "10"   # Example amount
currency = "INR"
note = "Test Payment"

# Defining payment URLs
upi_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&am={amount}&cu={currency}&tn={note}"

# Create QR codes for each app (all use same UPI standard)
phonepe_qr = qrcode.make(upi_url)
paytm_qr = qrcode.make(upi_url)
google_pay_qr = qrcode.make(upi_url)

# Save the QR codes as image files
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')

# Display the QR codes
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()
