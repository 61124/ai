class ExpertSystem:
    def __init__(self):
        self.symptoms = []
        # Mapping individual symptoms to diagnoses
        self.diagnoses = {
            "fever": "You might have an infection. Consult a doctor if it persists.",
            "cough": "It could be a common cold or flu. Rest and stay hydrated.",
            "chest pain": "Seek immediate medical attention, it might be a heart issue.",
            "headache": "It could be due to stress or dehydration. Drink water and rest."
        }
        # Adding rules for multi-symptom diagnoses
        self.multi_symptom_rules = {
            frozenset(["fever", "cough"]): "You might have the flu. Get plenty of rest and hydrate.",
            frozenset(["fever", "chest pain"]): "You might have a serious heart condition. Seek immediate medical attention.",
            frozenset(["headache", "fever"]): "It could be a viral infection. Drink fluids and rest."
        }

    def add_symptom(self, symptom):
        """Add a symptom to the list of symptoms."""
        self.symptoms.append(symptom.lower())

    def diagnose(self):
        """Diagnose based on the symptoms entered by the user."""
        if not self.symptoms:
            return "No symptoms provided. Please enter your symptoms."
        
        # Create a frozenset of the user's symptoms for multi-symptom diagnosis
        symptom_set = frozenset(self.symptoms)

        # Check for multi-symptom diagnoses first
        if symptom_set in self.multi_symptom_rules:
            return f"Diagnosis: {self.multi_symptom_rules[symptom_set]}"

        # If no multi-symptom match, proceed with individual symptom diagnoses
        results = []
        for symptom in self.symptoms:
            if symptom in self.diagnoses:
                results.append(f"Symptom: {symptom} -> {self.diagnoses[symptom]}")
            else:
                results.append(f"Symptom: {symptom} -> No diagnosis found. Consult a doctor.")
        
        return "\n".join(results)

if __name__ == "__main__":
    expert_system = ExpertSystem()
    print("Welcome to the Medical Expert System")
    while True:
        symptom = input("Enter a symptom (or type 'exit' to quit): ")
        if symptom.lower() == 'exit':
            break
        expert_system.add_symptom(symptom)
    
    print("\nDiagnosis Result:")
    print(expert_system.diagnose())
