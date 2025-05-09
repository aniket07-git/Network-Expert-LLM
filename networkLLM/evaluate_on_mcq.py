import json
import subprocess
import re
import shlex

# Load the MCQ questionnaire from the JSON file
def load_questions(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Function to extract the answer from the LLM's response
def extract_answer(llm_response):
    # Using a regex to find the final answer after 'Answer' with optional colon
    match = re.search(r"(?i)\banswer\s*:?\s*(is\s*)?([A-D])\b", llm_response)
    if match:
        return match.group(2)
    return None

# Function to clean the options by removing None or empty values
def clean_options(options):
    # Filter out None or empty strings
    return [option for option in options if option not in (None, "")]

# Function to call torchtune and get the LLM's response
def generate_llm_response(question, options):
    # Universal prompt to be used before every question
    prompt = ("Answer the following multiple choice question. First provide a short reasoning. "
              "After this conclude with Answer in a single string whose values can be one of the 4 alphabets A, B, C, or D. "
              "For example, Answer option number in alphabet. Do not forget to give the final answer in the end from either A, B, C or D.")
    
    # Adding the question and options to the prompt
    prompt += f"\n\nQuestion: {question}\n"
    prompt += "Options:\n"
    for i, option in enumerate(options):
        prompt += f"{option}\n"
    
    # Safely escape the prompt to prevent YAML parsing issues
    safe_prompt = shlex.quote(prompt)
    
    # Command to run the LLM generation using torchtune
    command = [
        "tune", "run", "generate", 
        "--config", "configs/custom_generation_config.yaml", 
        f"prompt[user]={safe_prompt}"  # Pass the prompt as a safe quoted string
    ]
    
    # Run the subprocess and capture the error messages (stderr)
    try:
        print(f"Running torchtune command: {' '.join(command)}")
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        
        # If stderr has the generated response, return it
        if result.stderr:
            print(result.stderr.strip())
            return result.stderr.strip()
        else:
            print(f"Error: No output generated. STDERR is empty.")
            return None
    except subprocess.CalledProcessError as e:
        print(f"Error executing torchtune command: {e}")
        print(f"STDOUT: {e.stdout}")
        print(f"STDERR: {e.stderr}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

# Function to calculate the score for all questions
def calculate_score(questions):
    score = 0
    total_questions = len(questions)
    
    for question in questions[:]:
        question["options"] = clean_options(question["options"])
        # Get the correct answer from the question
        correct_answer = question['correct_option']
        
        # Generate the LLM response based on the question and options
        llm_response = generate_llm_response(question['question'], question['options'])
        
        if llm_response is None:
            print(f"Skipping question due to error: {question['question']}")
            continue
        
        # Extract the answer from the LLM's response
        llm_answer = extract_answer(llm_response)
        
        if llm_answer == correct_answer:
            score += 1
        
        # Optionally print each question and LLM answer for debugging
        print(f"Question: {question['question']}")
        print(f"Options: {', '.join(question['options'])}")
        print(f"Correct Answer: {correct_answer}")
        print(f"LLM Answer: {llm_answer}")
        print("-" * 50)
    
    # Calculate the final score as a percentage
    score_percentage = (score / total_questions) * 100
    print(f"Final Score: {score_percentage}% ({score}/{total_questions})")

# Main function to execute the scoring
def main():
    # Load the MCQ questions from the file
    questions = load_questions('mcq_questions.json')
    
    # Calculate the score for the LLM's answers
    calculate_score(questions)

if __name__ == "__main__":
    main()
