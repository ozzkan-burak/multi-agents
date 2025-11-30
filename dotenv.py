import os

def load_dotenv(dotenv_path='.env'):
    """Basit .env dosyası yükleyici"""
    if not os.path.exists(dotenv_path):
        return
    
    with open(dotenv_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                value = value.strip()
                # Tırnak işaretlerini kaldır
                if value.startswith('"') and value.endswith('"'):
                    value = value[1:-1]
                elif value.startswith("'") and value.endswith("'"):
                    value = value[1:-1]
                os.environ[key.strip()] = value