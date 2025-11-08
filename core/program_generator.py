import json
from core.mistral_client import query_mistral

def generate_workout_plan(user_goal: str):
    base_programs = json.load(open("data/programs.json"))
    
    # Select base plan
    if "strength" in user_goal.lower():
        base = base_programs["strength"]
    elif "weight" in user_goal.lower():
        base = base_programs["weight_loss"]
    else:
        base = base_programs["general_fitness"]
    
    # Optional: refine with Mistral
    messages = [
        {"role": "system", "content": "You are an expert gym trainer. Create structured workout plans."},
        {"role": "user", "content": f"User goal: {user_goal}\nBase plan: {base}\nMake it personalized and easy to follow."},
    ]
    
    response = query_mistral(messages)
    return response
