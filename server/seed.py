#!/usr/bin/env python3

from app import app
from models import db, Plant

def seed_data():
    plants = [
        Plant(name="Aloe", image="./images/aloe.jpg", price=11.50, is_in_stock=True),
        Plant(name="Snake Plant", image="./images/snake.jpg", price=18.99, is_in_stock=True),
        Plant(name="Pothos", image="./images/pothos.jpg", price=12.00, is_in_stock=False),
    ]

    db.session.add_all(plants)
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        print("Seeding database...")
        db.drop_all()
        db.create_all()
        seed_data()
        print("Done!")
