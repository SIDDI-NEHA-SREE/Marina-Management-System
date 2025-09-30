import argparse
from datetime import datetime

# Import models
from src.models.owner import Owner
from src.models.vessel import Vessel
from src.models.docking import Docking
from src.models.payment import Payment
from src.models.violation import Violation
from src.models.staff import Staff

# Import services
from src.services.owners_service import OwnersService
from src.services.vessels_service import VesselsService
from src.services.dockings_service import DockingsService
from src.services.payments_service import PaymentsService
from src.services.violations_service import ViolationsService
from src.services.staff_service import StaffService


def main():
    parser = argparse.ArgumentParser(description="CLI for Marina Management System")
    subparsers = parser.add_subparsers(dest="command")

    # --- Owners ---
    add_owner = subparsers.add_parser("add-owner")
    add_owner.add_argument("--name", required=True)
    add_owner.add_argument("--address", default="")
    add_owner.add_argument("--phone", default="")
    add_owner.add_argument("--email", default="")

    list_owners = subparsers.add_parser("list-owners")

    # --- Vessels ---
    add_vessel = subparsers.add_parser("add-vessel")
    add_vessel.add_argument("--name", required=True)
    add_vessel.add_argument("--type", required=True)
    add_vessel.add_argument("--capacity", type=int, default=0)
    add_vessel.add_argument("--owner_id", type=int, required=True)
    add_vessel.add_argument("--reg", default="")

    list_vessels = subparsers.add_parser("list-vessels")

    # --- Dockings ---
    dock_vessel = subparsers.add_parser("dock-vessel")
    dock_vessel.add_argument("--vessel_id", type=int, required=True)
    dock_vessel.add_argument("--location", required=True)
    dock_vessel.add_argument("--capacity", type=int, default=1)

    list_dockings = subparsers.add_parser("list-dockings")

    # --- Payments ---
    add_payment = subparsers.add_parser("add-payment")
    add_payment.add_argument("--vessel_id", type=int, required=True)
    add_payment.add_argument("--amount", type=float, required=True)
    add_payment.add_argument("--type", required=True)
    add_payment.add_argument("--tax", type=float, default=0.0)

    list_payments = subparsers.add_parser("list-payments")

    # --- Violations ---
    add_violation = subparsers.add_parser("add-violation")
    add_violation.add_argument("--vessel_id", type=int, required=True)
    add_violation.add_argument("--type", required=True)
    add_violation.add_argument("--details", default="")

    list_violations = subparsers.add_parser("list-violations")

    # --- Staff ---
    add_staff = subparsers.add_parser("add-staff")
    add_staff.add_argument("--name", required=True)
    add_staff.add_argument("--role", default="")
    add_staff.add_argument("--contact", default="")

    list_staff = subparsers.add_parser("list-staff")

    args = parser.parse_args()

    # --- Command Handling ---
    if args.command == "add-owner":
        service = OwnersService()
        owner = Owner(args.name, args.address, args.phone, args.email)
        print(service.create_owner(owner))

    elif args.command == "list-owners":
        service = OwnersService()
        print(service.list_owners())

    elif args.command == "add-vessel":
        service = VesselsService()
        vessel = Vessel(
            vessel_name=args.name,
            vessel_type=args.type,
            capacity=args.capacity,
            owner_id=args.owner_id,
            registration_number=args.reg,
        )
        print(service.create_vessel(vessel))

    elif args.command == "list-vessels":
        service = VesselsService()
        print(service.list_vessels())

    elif args.command == "dock-vessel":
        service = DockingsService()
        docking = Docking(
            vessel_id=args.vessel_id,
            dock_location=args.location,
            dock_capacity=args.capacity,
            arrival_time=datetime.utcnow(),
        )
        print(service.dock_vessel(docking))

    elif args.command == "list-dockings":
        service = DockingsService()
        print(service.list_dockings())

    elif args.command == "add-payment":
        service = PaymentsService()
        payment = Payment(
            vessel_id=args.vessel_id,
            amount=args.amount,
            payment_type=args.type,
            tax_amount=args.tax,
        )
        print(service.record_payment(payment))

    elif args.command == "list-payments":
        service = PaymentsService()
        print(service.list_payments())

    elif args.command == "add-violation":
        service = ViolationsService()
        violation = Violation(
            vessel_id=args.vessel_id,
            violation_type=args.type,
            details=args.details,
        )
        print(service.report_violation(violation))

    elif args.command == "list-violations":
        service = ViolationsService()
        print(service.list_violations())

    elif args.command == "add-staff":
        service = StaffService()
        staff = Staff(args.name, args.role, args.contact)
        print(service.add_staff(staff))

    elif args.command == "list-staff":
        service = StaffService()
        print(service.list_staff())

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
