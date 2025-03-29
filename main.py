
#from langchain_openai import OpenAI
from dotenv import load_dotenv

from agents import Agent, InputGuardrail,GuardrailFunctionOutput, Runner, ItemHelpers, TResponseInputItem, trace
from pydantic import BaseModel
import asyncio
from typing import Literal
from dataclasses import dataclass

# Load environment variables from .env file
load_dotenv()
# This code sets up a multi-agent system to generate and validate a diet plan based on user input.


members = ['nutritionist', 'diet_validator']
options = members + ['FINISH']

@dataclass
class DietQuery(BaseModel):
    """User query for diet plan"""
    is_diet_query: bool

@dataclass
class NutritionistOutput(BaseModel):
    """Output from the nutritionist"""
    diet_plan: str

@dataclass
class DietValidatorOutput(BaseModel):
    """Output from the diet validator"""
    feedback: str
    plan_approved: bool

guardrail_agent = Agent(
    name="Guardrail check",
    instructions="Check if the user is asking about diet plans.",
    output_type=DietQuery,
)

nutritionist_agent = Agent(
    name="Nutritionist",
    handoff_description="Specialist agent for creating diet plans",
    instructions="You are a nutritionist. Create a diet plan based on the user's needs.",
    output_type=NutritionistOutput,
)
diet_validator_agent = Agent(
    name="Diet Validator",
    handoff_description="Specialist agent for validating diet plans meets user health needs and dietary restrictions",
    instructions="You are a diet validator. Validate the diet plan created by the nutritionist meets the needs of the user, and provide feedback.",
    output_type=DietValidatorOutput,
)

def main():
    query = "I am 9 years old, I am male, average height and weight for my age, I want to gain strength and muscle, please suggest a diet plan for 1 day that is only vegetarian options (no meat, no fish, no eggs)only 6 unique items in a day and I can repeat the items unlimited times in a day"
    input_items: list[TResponseInputItem] = [{"content" : msg, "role" : "user"} for msg in [query]]
    nutritionist_output: NutritionistOutput | None = None
    max_tries = 3 
    with trace("LLM as a judge"):
        while True:
            nutritionist = asyncio.run(Runner.run(nutritionist_agent, input_items))
            nutritionist_output = nutritionist.final_output_as(NutritionistOutput)
            print("Nutritionist output: ", nutritionist_output)
            input_items = input_items + [{"content" : nutritionist_output.diet_plan, "role" : "assistant"}]
            if nutritionist_output is None:
                print("No diet plan generated, exiting...")
                return nutritionist_output
            max_tries -= 1
            if max_tries <= 0:
                print("Max tries reached, use latest generated diet plan, exiting...")
                return nutritionist_output
            print("Diet plan generated, sending to validator...")
            
            diet_validator = asyncio.run(Runner.run(diet_validator_agent, input_items))
            diet_validator_output = diet_validator.final_output_as(DietValidatorOutput)
            print("Diet Validator output: ", diet_validator_output)
            if diet_validator_output.plan_approved:
                print("Diet plan approved!")
                return nutritionist_output
            else:
                print("Diet plan not approved, updating...")
                print("Feedback: ", diet_validator_output.feedback)
                input_items = input_items + [{"content" : diet_validator_output.feedback, "role" : "assistant"}]
                continue


if __name__ == "__main__":
    main()
