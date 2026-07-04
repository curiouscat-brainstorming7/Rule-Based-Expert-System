print("=== Health Diagnosis Expert System ===")


fever = input("Do you have fever? (yes/no): ").lower()
cough = input("Do you have cough? (yes/no): ").lower()
sore_throat = input("Do you have sore throat? (yes/no): ").lower()
headache = input("Do you have headache? (yes/no): ").lower()
body_pain = input("Do you have body pain? (yes/no): ").lower()
stomach_pain = input("Do you have stomach pain? (yes/no): ").lower()
vomiting = input("Do you have vomiting? (yes/no): ").lower()


facts = []

if fever == "yes":
    facts.append("fever")

if cough == "yes":
    facts.append("cough")

if sore_throat == "yes":
    facts.append("sore_throat")

if headache == "yes":
    facts.append("headache")

if body_pain == "yes":
    facts.append("body_pain")

if stomach_pain == "yes":
    facts.append("stomach_pain")

if vomiting == "yes":
    facts.append("vomiting")

print("\n--- Inference Steps ---")


if "fever" in facts and "cough" in facts:
    print("Rule 1 Fired -> Viral Infection")
    facts.append("viral_infection")


if "viral_infection" in facts and "sore_throat" in facts:
    print("Rule 2 Fired -> Common Cold")
    facts.append("common_cold")


if "fever" in facts and "headache" in facts and "body_pain" in facts:
    print("Rule 3 Fired -> Flu")
    facts.append("flu")


if "stomach_pain" in facts and "vomiting" in facts:
    print("Rule 4 Fired -> Food Poisoning")
    facts.append("food_poisoning")

print("\n--- Final Diagnosis ---")

if "flu" in facts:
    print("Diagnosis: Flu")
elif "common_cold" in facts:
    print("Diagnosis: Common Cold")
elif "food_poisoning" in facts:
    print("Diagnosis: Food Poisoning")
elif "viral_infection" in facts:
    print("Diagnosis: Viral Infection")
else:
    print("Diagnosis: No matching disease found.")

print("\nThank you for using the Health Diagnosis Expert System!")
