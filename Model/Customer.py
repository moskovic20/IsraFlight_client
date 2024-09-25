class Customer:
    def __init__(self, customer_id, password, full_name, email, phone_number, is_manager):  # שים לב ל-m הקטנה
        self.customer_id = customer_id
        self.password = password
        self.full_name = full_name
        self.email = email
        self.phone_number = phone_number
        self.is_manager = is_manager  # שים לב ל-m הקטנה

    def __repr__(self):
        return (f"Customer(ID={self.customer_id}, "
                f"FullName='{self.full_name}', Email='{self.email}', PhoneNumber='{self.phone_number}'), IsManager='{self.is_manager}'")
