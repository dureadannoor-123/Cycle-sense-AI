from supabase import create_client
from datetime import datetime
from postgrest.exceptions import APIError
from config import url, key
import warnings
class MCT_DB:
    def __init__(self):
        warnings.filterwarnings("ignore")

        self.Client = create_client(url, key)
    def sign_up_database(self, name: str, email: str, password: str,age:int,weight:float,height:float,marital_status:str):
        try:
            # Check if email already exists in authentication system
            user_response = self.Client.table("USER").select("*").eq("email", email).execute()
           # print(user_response)
            if user_response.data:
                return {"status":"error","message":"Email already exists! Please use a different email."}
            # Sign up with Supabase authentication
            response = self.Client.auth.sign_up({"email": email, "password": password})
           # print(response)
            if response.user:  # Check if sign-up was successful
                user_data = {
                    "name": name,
                    "age":age,
                    "weight":weight,
                    "height":height,
                    "email": email,
                    "password": password,
                    "marital_status":marital_status
                }
                self.Client.table("USER").insert(user_data).execute()  #  Insert into DB
                return {"status":"success","message":f"Account created successfully!"}

            return {"status":"error","message":"Sign-up failed. Please try again."}
        except Exception as e:
            return {"status":"error","message":f"An error occurred: {str(e)}"}
    def Log_In_database(self,email:str,password:str):
            try:
                self.user_response = self.Client.table("USER").select("*").eq("email", email).execute()
                if self.user_response.data:  # Check if any user exists
                    self.user = self.user_response.data[0]  # First matched user
                    if self.user["password"]==password:
                        self.logged_in_email = email
                        return {"status":"success","message":"Account logged in successfully!"}
                    else:
                        return {"status":"error","message":"Incorrect password. Please enter the correct password."}
                else:
                    return {"status":"error","message":"Create a new account as your email does not exist."}
            except Exception as e:  # Catch any errors
                return {"status": "error", "message": f"An error occurred: {str(e)}"}
    def Forgot_Password(self, email: str, new_password: str):
        try:
            # Check if the email exists in the database
            user_response = self.Client.table("USER").select("*").eq("email", email).execute()
            if not user_response.data:
                return {"status": "error", "message": "Email  not found."}
            else:
                # Email exists, update the password
                updated_data = {
                    "password": new_password
                }
                # Update the password for the existing user
                update_response = self.Client.table("USER").update(updated_data).eq("email", email).execute()
                return {"status": "success", "message": "Password successfully updated."}
        except Exception as e:
            return {"status": "error", "message": f"An error occurred: {str(e)}"}

    def periodtracker(self,
                      user_email: str,  # user_email must exist in the User table
                      last_menstrual_date: datetime.date,
                      previous_menstrual_date_1: datetime.date,
                      previous_menstrual_date_2: datetime.date,
                      previous_menstrual_date_3: datetime.date,
                      period_length_days: int,
                      ):
        try:
            # Check if the user exists in the User table
            response = self.Client.table("USER").select("email").eq("email", user_email).execute()
            if not response.data:
                print(f"ERROR: User with email {user_email} does not exist in the User table.")
                return {"status": "error", "message": f"User with email {user_email} does not exist in the User table."}

            # Check if the email already exists in the PeriodTracker table
            existing_period_response = self.Client.table("PeriodTracker").select("*").eq("user_email",
                                                                                         user_email).execute()

            menstrual_data = {
                "user_email": user_email,
                "last_menstrual_date": last_menstrual_date.isoformat(),
                "previous_menstrual_date_1": previous_menstrual_date_1.isoformat(),
                "previous_menstrual_date_2": previous_menstrual_date_2.isoformat(),
                "previous_menstrual_date_3": previous_menstrual_date_3.isoformat(),
                "period_length_days": period_length_days,
            }

            print(menstrual_data)

            if existing_period_response.data:
                # If the user already has an entry, update the existing one
                update_response = self.Client.table("PeriodTracker").update(menstrual_data).eq("user_email",
                                                                                               user_email).execute()
                if update_response.data:
                    print(update_response.data)
                    return {"status": "success", "message": "Period data updated successfully!"}
                else:
                    return {"status": "error", "message": "Failed to update period data."}
            else:
                # If the user does not have an entry, insert a new one
                try:
                    response = self.Client.table("PeriodTracker").insert(menstrual_data).execute()
                    print("Response data:", response.data)  # Check the actual response data
                    return {"status": "success", "message": "Period data inserted successfully!"}
                except Exception as e:
                    print("ERROR:", e)
                    return {"status": "error", "message": f"An error occurred while inserting data: {str(e)}"}

        except Exception as e:
            print("ERROR:", e)
            return {"status": "error", "message": f"An error occurred: {str(e)}"}

    def test_connection(self):
        try:
            response = self.Client.table("USER").select("*").execute()
            if response and response.data:
                print("Connected to Supabase! Users:", response.data)
            else:
                print("Connected to Supabase! Users: None")
        except Exception as e:
            print("Connection Error:", str(e))
# Run the test
mct=MCT_DB()
mct.test_connection()
"""m=mct.Forgot_Password("numl-s23-31963@numls.edu.pk","21AFNAN249")
print(m)

r=mct.Log_In_database("afnann","numl-s23-31963@numls.edu.pk","21nov25633")
print(r)res=mct.sign_up_database("afnann","numl-s23-31963@numls.edu.pk","21nov25633")
print(res)
response2=  mct.sign_up_database("afnan e", "afnan@example.com", "876543")"""

"""res=mct.sign_up_database("afnan","afnanshoukat011@gmail.com","21nov2003",21,47,150,"Single")"""

# Convert string inputs to datetime.date format
pt = mct.periodtracker(
    "afnanshoukat011@gmail.com",
    datetime.strptime("2024-12-7", "%Y-%m-%d").date(),
    datetime.strptime("2025-01-29", "%Y-%m-%d").date(),
    datetime.strptime("2025-03-12", "%Y-%m-%d").date(),
    datetime.strptime("2025-04-15", "%Y-%m-%d").date(),
    7
)


