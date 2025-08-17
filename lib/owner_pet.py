# lib/owner_pet.py

class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if not isinstance(name, str) or not name.strip():
            raise Exception("Pet name must be a non-empty string")
        self.name = name

        if not isinstance(pet_type, str) or pet_type.lower() not in Pet.PET_TYPES:
            raise Exception(f"pet_type must be one of {Pet.PET_TYPES}")
        self.pet_type = pet_type.lower()

        if owner is not None and not isinstance(owner, Owner):
            raise Exception("owner must be an Owner instance or None")
        self.owner = owner

        Pet.all.append(self)

    def __repr__(self):
        return f"<Pet name={self.name!r} type={self.pet_type!r} owner={self.owner.name if self.owner else 'None'}>"


class Owner:
    def __init__(self, name):
        if not isinstance(name, str) or not name.strip():
            raise Exception("Owner name must be a non-empty string")
        self.name = name

    def pets(self):
        return [p for p in Pet.all if p.owner is self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("add_pet requires a Pet instance")
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda p: p.name.lower())
