# Thoughtful-Robot-Automation
Thoughful - Platform Technical Screen
⸻

Objective

This project simulates a robotic dispatch function used in Thoughtful’s automation factory. The goal is to classify packages into proper handling stacks based on their volume and mass.

Rules

A package is classified as:
	•	Bulky if:
	•	Volume (Width × Height × Length) ≥ 1,000,000 cm³, or
	•	Any single dimension ≥ 150 cm
	•	Heavy if:
	•	Mass ≥ 20 kg

Package Stack Assignment:

Condition	Stack
Neither bulky nor heavy	STANDARD
Either bulky or heavy	SPECIAL
Both bulky and heavy	REJECTED


⸻

Function Signature with Arguments

def sort(width, height, length, mass):
    ...

	•	Parameters:
	•	width (int): in centimeters
	•	height (int): in centimeters
	•	length (int): in centimeters
	•	mass (int): in kilograms
	•	Returns:
	•	str: one of "STANDARD", "SPECIAL", or "REJECTED"

⸻

Example Usage

print(sort(50, 50, 50, 10))       # STANDARD
print(sort(100, 100, 100, 10))    # SPECIAL (bulky due to volume)
print(sort(120, 120, 120, 25))    # REJECTED
print(sort(151, 40, 40, 10))      # SPECIAL (bulky due to dimension)
print(sort(30, 30, 30, 25))       # SPECIAL (heavy only)


⸻

Testing

To run tests, simply run the Python script in your terminal or any IDE:

python3 sort_packages.py
