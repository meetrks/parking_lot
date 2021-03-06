#!/usr/bin/env python3


class Car:
    def __init__(self, registration_no, color):
        self.registration_no = registration_no
        self.color = color


class Slot:
    def __init__(self, slot_no, is_available=False):
        self.car = None
        self.slot_no = slot_no
        self.is_available = is_available


class ParkingLot:

    def __init__(self):
        self.slots = {}

    def is_parking_lot_created(self):
        return True if self.slots else False

    def create_parking_lot(self, slot_count):
        if self.is_parking_lot_created():
            print("Parking lot already created")
            return

        slot_count = int(slot_count)
        if slot_count < 1:
            print("Invalid slot count")
            return
        for i in range(1, slot_count + 1):
            self.slots[i] = Slot(slot_no=i, is_available=True)
        print("Created a parking lot with {slot_count} slots".format(slot_count=str(slot_count)))
        return

    def get_slot_if_available(self):
        for i in self.slots:
            if self.slots[i].is_available:
                return self.slots[i]
        return None

    def park(self, registration_nog, color):
        if not self.is_parking_lot_created():
            return

        slot = self.get_slot_if_available()
        if not slot:
            print("Sorry, parking lot is full")
            return
        slot.car = Car(registration_nog, color)
        slot.is_available = False
        print("Allocated slot number: {slot_no}".format(slot_no=slot.slot_no))
        return

    def registration_numbers_for_cars_with_colour(self, color):
        if not self.is_parking_lot_created():
            return

        registration_nos = []
        for i in self.slots:
            if self.slots[i].car and self.slots[i].car.color == color:
                registration_nos.append(self.slots[i].car.registration_no, )
        print(", ".join(registration_nos)) if registration_nos else print("Not found")

    def slot_numbers_for_cars_with_colour(self, color):
        if not self.is_parking_lot_created():
            return

        slot_numbers = []
        for i in self.slots:
            if self.slots[i].car and self.slots[i].car.color == color:
                slot_numbers.append(str(i))
        print(", ".join(slot_numbers)) if slot_numbers else print("Not found")

    def slot_number_for_registration_number(self, registration_no):
        if not self.is_parking_lot_created():
            return

        for i in self.slots:
            if self.slots[i].car and self.slots[i].car.registration_no == registration_no:
                print(i)
                return
        print("Not found")

    def leave(self, slot_no):
        if not self.is_parking_lot_created():
            return

        slot_no = int(slot_no)
        if slot_no in self.slots:
            slot_obj = self.slots[slot_no]
            if slot_obj.is_available:
                print("Not Found")
                return
            slot_obj.car = None
            slot_obj.is_available = True
            print("Slot number {slot_no} is free".format(slot_no=str(slot_no)))

    def status(self):
        if not self.is_parking_lot_created():
            return

        print("Slot No.  Registration No\t Color")
        for i in self.slots:
            if self.slots[i].car and not self.slots[i].is_available:
                print(i, "\t ", self.slots[i].car.registration_no, "\t", self.slots[i].car.color)
