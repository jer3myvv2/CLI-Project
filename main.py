import os

from services.dashboard import run_dashboard


def main():
    if not os.path.exists('data'):
        os.makedirs('data')

    run_dashboard()

if __name__ == "__main__":
    main()