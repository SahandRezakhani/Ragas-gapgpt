import os
import sys
from dotenv import load_dotenv
from rich import print
load_dotenv()

def main():
    api_key = os.getenv("GAPGPT_API_KEY")
    if not api_key:
        print("❌ Error: GAPGPT_API_KEY environment variable is not set.")
        print("Please create a .env file with: GAPGPT_API_KEY=your_key_here")
        sys.exit(1)

    print("\n[bold green blink2]API key found. Running evaluation examples...[/]\n")

    # Import and run the simple evaluation example
    print("[bold cyan]=[/]" * 60)
    print("[bold red blink2]1. Running 'example1' for evaluate Faithfulness[/]")
    print("[bold cyan]=[/]" * 60)
    import examples.example1
    print()

    print("[bold cyan]=[/]" * 60)
    print("[bold red blink2]1. Running 'example2' for evaluate Faithfulness[/]")
    print("[bold cyan]=[/]" * 60)
    import examples.example2
    print()

    print("[bold cyan]=[/]" * 60)
    print("[bold red blink2]1. Running 'example3' for evaluate Faithfulness[/]")
    print("[bold cyan]=[/]" * 60)
    import examples.example3

if __name__ == "__main__":
    main()