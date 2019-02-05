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

    def create_parking_lot(self, slot_count):
        slot_count = int(slot_count)
        if slot_count < 1:
            print("Invalid slot count")
            return
        for i in range(1, slot_count):
            self.slots[i] = Slot(slot_no=i, is_available=True)

        return

    def get_slot_if_available(self):
        for i in self.slots:
            if self.slots[i].is_available:
                return self.slots[i]
        return None

    def park(self, registration_nog, color):
        slot = self.get_slot_if_available()
        if not slot:
            print("Sorry, parking lot is full")
        slot.car = Car(registration_nog, color)
        slot.is_available = False
        return

    def registration_numbers_for_cars_with_colour(self, color):
        registration_nos = []
        for i in self.slots.values():
            if i.car and i.car.color == color:
                registration_nos.append(i.car.registration_no, )
        print(", ".join(registration_nos)) if registration_nos else print("Not found")