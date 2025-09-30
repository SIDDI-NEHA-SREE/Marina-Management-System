from src.services.owner_service import OwnerService
from src.services.vessel_service import VesselService
from src.services.docking_service import DockingService
from src.services.payment_service import PaymentService
from src.services.violation_service import ViolationService
from src.services.staff_service import StaffService


class MarinaCLI:
    def __init__(self):
        self.owner_service = OwnerService()
        self.vessel_service = VesselService()
        self.docking_service = DockingService()
        self.payment_service = PaymentService()
        self.violation_service = ViolationService()
        self.staff_service = StaffService()

    def run(self):
        while True:
            print("\n=== Marina Management System ===")
            print("1. Owners")
            print("2. Vessels")
            print("3. Dockings")
            print("4. Payments")
            print("5. Violations")
            print("6. Staff")
            print("7. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                self.owner_menu()
            elif choice == "2":
                self.vessel_menu()
            elif choice == "3":
                self.docking_menu()
            elif choice == "4":
                self.payment_menu()
            elif choice == "5":
                self.violation_menu()
            elif choice == "6":
                self.staff_menu()
            elif choice == "7":
                print("Exiting system. Goodbye!")
                break
            else:
                print("Invalid choice")

    # ----------------- OWNER -----------------
    def owner_menu(self):
        print("\n--- Owner Menu ---")
        print("1. Register Owner")
        print("2. View Owner Info")
        print("3. Update Owner")
        print("4. Delete Owner")
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Name: ")
            email = input("Email: ")
            phone = input("Phone: ")
            data = {"name": name, "email": email, "phone": phone}
            print(self.owner_service.register_owner(data))

        elif choice == "2":
            owner_id = int(input("Owner ID: "))
            print(self.owner_service.get_owner_info(owner_id))

        elif choice == "3":
            owner_id = int(input("Owner ID: "))
            new_email = input("New Email: ")
            print(self.owner_service.update_owner_info(owner_id, {"email": new_email}))

        elif choice == "4":
            owner_id = int(input("Owner ID: "))
            print(self.owner_service.remove_owner(owner_id))

    # ----------------- VESSEL -----------------
    def vessel_menu(self):
        print("\n--- Vessel Menu ---")
        print("1. Register Vessel")
        print("2. View Vessel Info")
        print("3. Update Vessel")
        print("4. Delete Vessel")
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Vessel Name: ")
            vtype = input("Vessel Type: ")
            capacity = int(input("Capacity: "))
            owner_id = int(input("Owner ID: "))
            data = {
                "vessel_name": name,
                "vessel_type": vtype,
                "capacity": capacity,
                "owner_id": owner_id,
                "registration_number": f"REG-{owner_id}-{name[:3].upper()}"
            }
            print(self.vessel_service.register_vessel(data))

        elif choice == "2":
            vessel_id = int(input("Vessel ID: "))
            print(self.vessel_service.get_vessel_info(vessel_id))

        elif choice == "3":
            vessel_id = int(input("Vessel ID: "))
            new_name = input("New Vessel Name: ")
            print(self.vessel_service.update_vessel_info(vessel_id, {"vessel_name": new_name}))

        elif choice == "4":
            vessel_id = int(input("Vessel ID: "))
            print(self.vessel_service.remove_vessel(vessel_id))

    # ----------------- DOCKING -----------------
    def docking_menu(self):
        print("\n--- Docking Menu ---")
        print("1. Record Docking")
        print("2. View Docking Info")
        print("3. Update Docking")
        print("4. Delete Docking")
        choice = input("Enter choice: ")

        if choice == "1":
            vessel_id = int(input("Vessel ID: "))
            dock_location = input("Dock Location: ")
            arrival_time = input("Arrival Time (YYYY-MM-DD HH:MM): ")
            data = {"vessel_id": vessel_id, "dock_location": dock_location, "arrival_time": arrival_time}
            print(self.docking_service.record_docking(data))

        elif choice == "2":
            docking_id = int(input("Docking ID: "))
            print(self.docking_service.get_docking_info(docking_id))

        elif choice == "3":
            docking_id = int(input("Docking ID: "))
            new_status = input("New Status: ")
            print(self.docking_service.update_docking(docking_id, {"status": new_status}))

        elif choice == "4":
            docking_id = int(input("Docking ID: "))
            print(self.docking_service.remove_docking(docking_id))

    # ----------------- PAYMENT -----------------
    def payment_menu(self):
        print("\n--- Payment Menu ---")
        print("1. Record Payment")
        print("2. View Payment Info")
        print("3. Update Payment")
        print("4. Delete Payment")
        choice = input("Enter choice: ")

        if choice == "1":
            vessel_id = int(input("Vessel ID: "))
            amount = float(input("Amount: "))
            payment_type = input("Payment Type (cash/card/bank): ")
            data = {"vessel_id": vessel_id, "amount": amount, "payment_type": payment_type}
            print(self.payment_service.record_payment(data))

        elif choice == "2":
            payment_id = int(input("Payment ID: "))
            print(self.payment_service.get_payment_info(payment_id))

        elif choice == "3":
            payment_id = int(input("Payment ID: "))
            new_amount = float(input("New Amount: "))
            print(self.payment_service.update_payment(payment_id, {"amount": new_amount}))

        elif choice == "4":
            payment_id = int(input("Payment ID: "))
            print(self.payment_service.remove_payment(payment_id))

    # ----------------- VIOLATION -----------------
    def violation_menu(self):
        print("\n--- Violation Menu ---")
        print("1. Report Violation")
        print("2. View Violation Info")
        print("3. Update Violation")
        print("4. Resolve Violation")
        print("5. Delete Violation")
        choice = input("Enter choice: ")

        if choice == "1":
            vessel_id = int(input("Vessel ID: "))
            vtype = input("Violation Type: ")
            details = input("Details: ")
            data = {"vessel_id": vessel_id, "violation_type": vtype, "details": details}
            print(self.violation_service.report_violation(data))

        elif choice == "2":
            violation_id = int(input("Violation ID: "))
            print(self.violation_service.get_violation_info(violation_id))

        elif choice == "3":
            violation_id = int(input("Violation ID: "))
            new_status = input("New Status: ")
            print(self.violation_service.update_violation(violation_id, {"resolved_status": new_status}))

        elif choice == "4":
            violation_id = int(input("Violation ID: "))
            print(self.violation_service.resolve_violation(violation_id))

        elif choice == "5":
            violation_id = int(input("Violation ID: "))
            print(self.violation_service.remove_violation(violation_id))

    # ----------------- STAFF -----------------
    def staff_menu(self):
        print("\n--- Staff Menu ---")
        print("1. Add Staff")
        print("2. View Staff Info")
        print("3. Update Staff")
        print("4. Delete Staff")
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Name: ")
            role = input("Role: ")
            contact = input("Contact Info: ")
            data = {"name": name, "role": role, "contact_info": contact}
            print(self.staff_service.add_staff_member(data))

        elif choice == "2":
            staff_id = int(input("Staff ID: "))
            print(self.staff_service.get_staff_info(staff_id))

        elif choice == "3":
            staff_id = int(input("Staff ID: "))
            new_role = input("New Role: ")
            print(self.staff_service.update_staff_info(staff_id, {"role": new_role}))

        elif choice == "4":
            staff_id = int(input("Staff ID: "))
            print(self.staff_service.remove_staff(staff_id))


if __name__ == "__main__":
    MarinaCLI().run()
