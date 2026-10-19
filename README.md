# test-station-sim
Test station for myself


"hello"

## Setup

Requires Python 3.12 and Git.

Step 1. Clone the repo and open the folder:

In powershell:
    git clone https://github.com/jessem10210/test-station-sim.git
   cd test-station-sim

Step 2. Create virtual enviroment:

In powershell:
    python -m venv .venv

Step 3. Activate it:

In powershell:
    .venv\Scripts\Activate.ps1

If powershell refuses to run the script run this once and try again

In powershell:
    Set-ExecutionPolicy -Scope CurrentUser RemoteSigned

Your prompt should now start with .venv

Step 4. Install the dependencies:

In powershell:
    pip install -r requirements.txt

Step 5. Run the sample script from the repo root:

In powershell:
    python scripts/summarize_csv.py

To leave the enviroment, run 'deactivate'

##