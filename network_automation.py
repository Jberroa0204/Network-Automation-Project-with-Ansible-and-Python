import subprocess
import sys

def run_playbook(playbook_path):
    try:
        subprocess.run(['ansible-playbook', '-i', '/Users/tito/networkautomation/hosts', playbook_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}", file=sys.stderr)

def main():
    # Run configuration playbook
    print("Running configuration playbook...")
    run_playbook('configure_cisco.yml')

    # Run show commands playbook
    print("Running show commands playbook...")
    run_playbook('show_commands.yml')
    
    # Run Ping command playbook
    print("Running ping command playbook...")
    run_playbook('ping_device.yml')

if __name__ == "__main__":
    main()

