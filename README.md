# service-configurator
> A command-line environment provisioning utility for distributed microservices architectures.

## Overview
Managing environment variables across a multi-service backend introduces significant friction during local bootstrapping and container orchestration setup. Coordinating database credentials, persistence layers, caching endpoints, and authentication keys manually across isolated services often leads to configuration drift and syntax errors. `service-configurator` eliminates this operational overhead by providing a streamlined interactive setup routine that validates, formats, and persists production-aligned configuration files directly into the workspace.

## How It Works
The execution pipeline operates via a synchronous command-line interface designed around standard input and file serialization workflows:
1. **Interactive Prompting:** Captures administrator inputs for database parameters (`DB_USER`, `DB_PASSWORD`, `DB_NAME`), authentication secrets (`JWT_SECRET`), and container routing hosts with sensible fallback defaults.
2. **Sanitization & Formatting:** Applies string stripping routines to sanitize user input and constructs a standardized key-value environment payload mapped to specific container hooks.
3. **Safe Serialization:** Utilizes secure file context managers (`open(..., "w")`) to write the `.env` configuration file while isolating exceptions and routing diagnostic error messages to standard error streams.

## Key Features
* **Interactive Credential Capture:** Prompts for essential database and authentication variables with intelligent default fallbacks.
* **Standard Library Architecture:** Zero third-party package requirements, ensuring instant execution and zero dependency installation friction.
* **Robust Error Handling:** Intercepts runtime exceptions during file serialization, providing descriptive diagnostic feedback and non-zero exit codes.
* **Container-Ready Output:** Automatically binds service host variables (`POSTGRES_HOST`, `REDIS_HOST`) tailored for Docker Compose networks.

## Tech Stack & Core Dependencies Breakdown
* **Language:** Python 3.8+ (Target runtime)
* **Standard Library Modules:** 
  * `os`: Interfacing with system environments and file paths.
  * `sys`: Managing standard error streams and process termination status codes (`sys.exit`).

## Environment & Web-Based Quick Start
You can run this project instantly using GitHub Codespaces or a local Python environment without installing external dependencies.

### GitHub Codespaces
1. Open the repository on GitHub and click **Code** -> **Codespaces** -> **Create codespace on main**.
2. Once the terminal initializes, execute the setup script:
   ```bash
   python3 main.py
   ```
### Local Virtual Environment (venv)
1. Clone or download the repository workspace.
2. Create and activate a virtual environment:
  ```bash
  python3 -m venv venv
  source venv/bin/activate  # On Windows use: venv\Scripts\activate
  ```

3. Run the configuration script:
   ```bash
    python main.py
   ```

## Repository Structure
```bash
service-configurator/
├── .github/
│   └── workflows/
│       └── ci.yml
├── .gitignore
├── README.md
└── main.py
```

## Roadmap
**[ ] JSON/YAML Export Support:** Extend the utility to export configuration profiles into structured JSON or YAML formats for Kubernetes ConfigMap integration.

**[ ] CLI Argument Parsing:** Integrate Python's argparse module to support non-interactive execution flags and automated CI pipeline overrides.

**[ ] Interactive Validation:** Implement regex-based validation rules for database credentials and secret key entropy checks prior to file writing.
