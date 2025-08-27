# Hospital Ward Management List - Ordered collections for patient beds
# Ward 4A Patient Beds (Ordered by proximity to nurses' station)
ward_4a = ["Bed1: Robert", "Bed2: Fatima", "Bed3: James"]

# New admission
ward_4a.append("Bed4: Aisha")
ward_4a.append("Bed5: Zomo")
print("Ward 4A:", ward_4a) 
 #output: Ward 4A: ['Bed1: Robert', 'Bed2: Fatima', 'Bed3: James', 'Bed4: Aisha', 'Bed5: Zomo']
 # Discharge patient
discharged = ward_4a.pop(1)
print(f"Discharged: {discharged} → Remaining: {ward_4a}")  
# Output: Discharged: Bed2: Fatima → Remaining: ['Bed1: Robert', 'Bed3: James', 'Bed4: Aisha']