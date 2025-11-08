# Red-Set-Protocell-Demo
Demo for Red Set Protocell - An automated AI red teaming platform feat. sniper/spotter architecture

### Recreating local runtime folders

Some folders are intentionally ignored in version control because they hold logs, sessions, or API keys. If you or a teammate accidentally deletes one of these, you can safely recreate them.

Folders to recreate:
- `logs/` and `sniper_logs/` and `spotter_logs/`  
- `sessions/` and `runs/`  
- `uploads/` and `tmp/`  
- `instance/` (Flask instance folder)

To recreate the folders and set a minimal .env template, run the included init script for your OS. After running the script, open `.env.local` and add any private keys or credentials there. Never commit `.env.local` or other secret files.
