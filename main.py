import os
import sys

def configure_environment():
    print("=== E-Commerce Microservices Setup ===")
    try:
        db_user = input("Enter PostgreSQL username [postgres]: ").strip() or "postgres"
        db_pass = input("Enter PostgreSQL password [secret]: ").strip() or "secret"
        db_name = input("Enter PostgreSQL database name [ecommerce]: ").strip() or "ecommerce"
        jwt_secret = input("Enter JWT Secret Key [super-secret-key]: ").strip() or "super-secret-key"

        env_content = f"""DB_USER={db_user}
DB_PASSWORD={db_pass}
DB_NAME={db_name}
JWT_SECRET={jwt_secret}
POSTGRES_HOST=postgres
REDIS_HOST=redis
"""

        with open(".env", "w") as f:
            f.write(env_content)
        print("\n[+] Successfully generated .env configuration file.")
    except Exception as e:
        print(f"[-] Error writing configuration: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    configure_environment()