# For Classes, Objects, Inheritance:
# • Use python shell, which displays menu, asks user
# 1. Add customer
# 2. Add rental booking
# 3. See customer list
# 4. See rental booking list
# 5. See inventory of vehicles available
# • Once the user selects an option, relevant operation needs to be displayed
# • Predefine the vehicle list in dictionary or list

import datetime

# id for booking transaction
id = 1
# customer id for customer details
cid = 2

# Declaration
vehicle = {"bike": 2, "car": 4}  # for count the vehicle availabel
namelist = ["NILESH", "ADARSH"]  # use to booking
# customer details
customerdetails = {1: {'Name': 'NILESH', 'Phone Number': '7620223325', 'Email': 'nileshkapse@gamil.com'}}
booking_details = {}  # booking details


# Adding customer class

class addcutomer:
    def takedetails(self):
        print("Enter Customer Name : ")
        name = input().upper()
        namelist.append(name)
        print("Enter Customer Phone Number : ")
        phonenum = input()
        print("Enter Customer Email : ")
        email = input()
        global cid
        global customerdetails
        customerdetails[cid] = {"Name": name, "Phone Number": phonenum, "Email": email}
        cid = cid + 1
        print("Sucessfully Added Details")


# date Converter
def dateconvert(date):
    date1 = datetime.datetime.strptime(date, '%d/%m/%Y').date()
    date1 = date1.strftime('%d/%m/%Y')
    return date1


# reduce the vehicle count
def reducevehi(invehi):
    for key, value in vehicle.items():
        if key == invehi:
            red = vehicle[invehi]
            if red > 1:
                vehicle[key] = red - 1
            else:
                print


# Adding the Booking
class addrentalbooking:
    def Customername(self):
        print("Enter Valid Name :")
        name = input().upper()
        if namelist.__contains__(name):  # checking is customer is register or not

            print("Enter Rental Dates in (DD/MM/YYYY ie. 01/01/2022) : ")
            date = input()
            rdate = dateconvert(date)
            # n = len(rental_date)
            # rental_date.insert(n, rdate)
            print("Enter Return Date : ")
            re_date = input()
            redate = dateconvert(re_date)
            # return_date.insert(n, redate)
            print("Enter Vehicle Type from Below List : ")
            print(vehicle)
            invehicle = input()
            global id
            global booking_details
            booking_details[id] = {'name': name, 'vehicle_type': invehicle, 'rentaldate': rdate, 'returndate': redate}
            id = id + 1
            reducevehi(invehicle)  # reduce the vehicle which is rented
            print("Vehicle Rental successfully done")

        else:
            print("Name Not found Add Customer Details")


# Customer List display

class custlist:
    def display(self):
        print("Customer Details :")
        print()
        print("CId", "  ", "Name", "      ", "Phone Number", "      ", "Email")
        for key, value in customerdetails.items():
            print(key, "  ", customerdetails[key]['Name'], "  ", customerdetails[key]['Phone Number'], "  ",
                  customerdetails[key]['Email'], "  ")


# Rental Details Display
class rentallist:
    def display(self):
        print("booking details")
        print()
        print("Id     ", "Name     ", "Vehicle     ", "Rental Date     ", "Return Date")
        for key, value in booking_details.items():
            print(key, "     ", booking_details[key]['name'], "     ", booking_details[key]['vehicle_type'], "     ",
                  booking_details[key]['rentaldate'], "     ", booking_details[key]['returndate'])


# Printing The available Vehicle
class availability:
    def available(self):
        print(vehicle)


# Option Selection Class
class switch:
    def selectedoption(self, option):
        default = "Invalid Input"

        return getattr(self, 'case_' + str(option), lambda: default)()

    def case_1(self):
        addc = addcutomer()
        addc.takedetails()

    def case_2(self):
        renb = addrentalbooking()
        renb.Customername()

    def case_3(self):
        obj = custlist()
        obj.display()

    def case_4(self):
        abc = rentallist()
        abc.display()

    def case_5(self):
        obj = availability()
        obj.available()


# Main Menu Display Class

def menu():
    while 1:
        print()
        print("******************************************************")
        print("For Quit or Exit type * 'exit' * ")
        print("......................................................")
        print("1. Add customer ")
        print("2. Add rental booking")
        print("3. See customer list")
        print("4. See rental booking list")
        print("5. See inventory of vehicles available")
        print("......................................................")
        print("Enter Input Here : ")
        a = input()
        print()
        if a != "exit":
            myswitch = switch()
            myswitch.selectedoption(a)
        else:
            break


# Main Function
def main():
    print()
    print("Welcome to Rental System ")
    print("Choose the Following Option :")
    if __name__ == "__main__":
        menu()


main()
