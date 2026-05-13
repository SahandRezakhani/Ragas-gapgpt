"""
RAGAs - Automated Evaluation of Retrieval Augmented Generation
Implementation based on the paper: "RAGAs: Automated Evaluation of Retrieval Augmented Generation"
arXiv:2309.15217

License: MIT
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def main():
    # Check if API key is set
    api_key = os.getenv("GAPGPT_API_KEY")
    if not api_key:
        print("❌ Error: GAPGPT_API_KEY environment variable is not set.")
        print("Please create a .env file with: GAPGPT_API_KEY=your_key_here")
        sys.exit(1)

    print("✅ API key found. Running evaluation examples...\n")

    # Import and run the simple evaluation example
    print("=" * 60)
    print("1. Running Simple Evaluation Example")
    print("=" * 60)
    import examples.simple_evaluation

    print("\n" + "=" * 60)
    print("2. Running WikiEval Demo Example")
    print("=" * 60)
    import examples.wikeval_demo

if __name__ == "__main__":
    main()