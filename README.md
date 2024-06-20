Update Server Configuration Script
This Python script helps update the configuration file whenever there are maximum threshold issues. The script reads the file content, updates the specified key with the new value, and ensures an exact match for the key.

How It Works
Read the file content: The script first reads the file and saves its content to a variable.
Write mode: It then opens the file in write mode to check for string matches and update the configuration accordingly.

Important Notes
Avoid hard-coding: Pass the file path, key, and value as arguments to the function instead of hard-coding them.
Exact string match: The function uses line.strip().startswith(key + "=") to ensure an exact match for the key (e.g., MAX_CONNECTIONS). This prevents bugs that may arise from partial matches (e.g., MAX_CONN matching MAX_CONNECTIONS).
