import sys
import os

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.orchestrator.orchestrator import Orchestrator


def main():
    if len(sys.argv) < 2:
        print("❗ ERROR: You must pass a query.")
        print('Example: python src/run.py "Analyze ROAS drop in last 7 days"')
        sys.exit(1)

    user_query = sys.argv[1]
    print("\n🚀 Starting Agentic System...\n")

    orchestrator = Orchestrator()
    orchestrator.run(user_query)


if __name__ == "__main__":
    main()
