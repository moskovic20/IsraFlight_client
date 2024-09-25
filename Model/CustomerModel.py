import requests
from Model.Customer import Customer

class CustomerModel:
    def __init__(self):
        self.base_url = "http://localhost:5034/api/Customer"  # יש לעדכן לכתובת ה-API שלך

    def get_all_customers(self):
        response = requests.get(self.base_url)
        if response.status_code == 200:
            customers_data = response.json()
            customers = [Customer(
                customer_id=customer['customerId'],
                password=customer['password'],
                full_name=customer['fullName'],
                email=customer['email'],
                phone_number=customer['phoneNumber'],
                is_manager=customer['isManager']  # הוסף את השדה isManager
            ) for customer in customers_data]
            return customers
        else:
            raise Exception(f"Failed to get customers: {response.status_code}")

    def get_customer_by_id(self, customer_id):
        url = f"{self.base_url}/{customer_id}"
        response = requests.get(url)
        if response.status_code == 200:
            customer_data = response.json()
            return Customer(
                customer_id=customer_data['customerId'],
                password=customer_data['password'],
                full_name=customer_data['fullName'],
                email=customer_data['email'],
                phone_number=customer_data['phoneNumber'],
                is_manager=customer_data['isManager']  # הוסף את השדה isManager
            )
        else:
            raise Exception(f"Failed to get customer: {response.status_code}")

    def get_customer_by_email(self, email):
        url = f"{self.base_url}/Email/{email}"  # יש לעדכן את ה-URL בהתאם לשרת שלך
        try:
            response = requests.get(url)
            if response.status_code == 200:
                customer_data = response.json()
                return Customer(
                    customer_id=customer_data['customerId'],
                    password=customer_data['password'],
                    full_name=customer_data['fullName'],
                    email=customer_data['email'],
                    phone_number=customer_data['phoneNumber'],
                    is_manager=customer_data['isManager']  # הוסף את השדה isManager
                )
            elif response.status_code == 404:
                return None
            else:
                raise Exception(f"Unexpected response from server: {response.status_code}")
        except requests.exceptions.RequestException as e:
            raise Exception(f"Communication error with server: {e}")
        
    def is_email_exists(self, email):
        try:
            customer = self.get_customer_by_email(email)
            if customer is not None:
                return True  # נמצא משתמש עם אותו אימייל
            return False  # לא נמצא משתמש עם אותו אימייל
        except Exception as e:
            raise Exception(str(e))

    # יצירת לקוח חדש
    def create_customer(self, customer):
        customer_data = {
            "customerId": 0,
            "password": customer.password,
            "fullName": customer.full_name,
            "email": customer.email,
            "phoneNumber": customer.phone_number,
            "isManager": customer.is_manager  # הוסף את השדה isManager
        }
        response = requests.post(self.base_url, json=customer_data)
        if response.status_code == 201:  # 201 Created
            return response.json()
        else:
            raise Exception(f"Failed to create customer: {response.status_code}")

    # עדכון פרטי לקוח קיים
    def update_customer(self, customer_id, customer):
        url = f"{self.base_url}/{customer_id}"
        customer_data = {
            "customerId": customer.customer_id,
            "password": customer.password,
            "fullName": customer.full_name,
            "email": customer.email,
            "phoneNumber": customer.phone_number,
            "isManager": customer.is_manager  # הוסף את השדה isManager
        }
        response = requests.put(url, json=customer_data)
        if response.status_code == 204:  # 204 No Content
            return True
        else:
            raise Exception(f"Failed to update customer: {response.status_code}")

    # מחיקת לקוח
    def delete_customer(self, customer_id):
        url = f"{self.base_url}/{customer_id}"
        response = requests.delete(url)
        if response.status_code == 204:  # 204 No Content
            return True
        else:
            raise Exception(f"Failed to delete customer: {response.status_code}")
