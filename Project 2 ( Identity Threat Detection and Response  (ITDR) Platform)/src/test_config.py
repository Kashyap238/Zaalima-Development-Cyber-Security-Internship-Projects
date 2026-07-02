from config_loader import load_config

config = load_config()

print(config["risk_threshold"])
print(config["database_name"])