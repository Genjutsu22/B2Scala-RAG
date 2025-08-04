import ollama
from retriever import retrieve_context
import os


# You are an expert in B2Scala code generation. Your task is to generate valid B2Scala code from a structured protocol draft.
# Use the following examples and documentation as a guide to ensure correct syntax and patterns.
    
def load_structured_draft(file_path):
    """
    Loads a structured protocol draft from a text file.
    """
    with open(file_path, 'r') as f:
        return f.read()

def generate_b2scala_code(draft, context):
    """
    Uses the local Ollama LLM to generate B2Scala code based on the draft and retrieved context.
    """
    prompt = f"""
    
    ---
    Documentation & Examples:
    {context}
    ---
    
    Protocol Draft:
    {draft}
    ---
    You a sofware engineer specialized in c++ code generation.
    Generate the c++ code for this protocol draft. The code should be fully functional and ready to be compiled.
    """
    
    print("Sending prompt to local LLM for code generation...")
    try:
        response = ollama.chat(
            model='llama3.1',  # Or the model you installed (e.g., 'llama3')
            messages=[{'role': 'user', 'content': prompt}]
        )
        return response['message']['content']
    except Exception as e:
        return f"An error occurred with the LLM: {e}"

if __name__ == "__main__":
    draft_file = "structured_draft.txt"
    output_file = os.path.join("Generated", "generated_code.scala")

    if not os.path.exists(draft_file):
        print(f"Error: Draft file '{draft_file}' not found. Please create one.")
    else:
        # Load the structured draft
        protocol_draft = load_structured_draft(draft_file)

        # Retrieve relevant context from the knowledge base
        retrieved_context = retrieve_context(protocol_draft)
        
        # Generate the code
        generated_code = generate_b2scala_code(protocol_draft, "\n\n".join(retrieved_context))
        
        # Save the generated code
        os.makedirs("Generated", exist_ok=True)
        with open(output_file, "w") as f:
            f.write(generated_code)
        
        print("\n--- Generated B2Scala Code ---")
        print(generated_code)
        print(f"\nCode saved to {output_file}")