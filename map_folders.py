import os
from datetime import datetime
import argparse
import re

def generate_folder_map():
    parser = argparse.ArgumentParser(description="Mapeia pastas de um diretório alvo.")
    parser.add_argument("--path", type=str, default="..", help="Caminho alvo para listar pastas")
    args = parser.parse_args()

    script_dir = os.path.dirname(os.path.abspath(__file__))
    target_dir = os.path.abspath(args.path)
    
    # 1. Split the path into individual parts (folders)
    # We strip the drive letter and split by slashes
    raw_parts = target_dir.replace(":\\", "\\").replace(":/", "\\").split("\\")
    
    processed_parts = []
    for part in raw_parts:
        if not part: continue
        # Rule: If a folder has a dot, make it a double-dot to distinguish from hierarchy
        safe_name = part.replace(".", "..")
        processed_parts.append(safe_name)
    
    # 2. Join parts using a single dot as the hierarchy separator
    path_id = ".".join(processed_parts)
    
    # 3. Clean up any characters illegal in Windows filenames (except dots and dashes)
    path_id = re.sub(r'[^a-zA-Z0-9.-]', '', path_id)

    # 4. Final Filename Construction
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f"{path_id}__{timestamp}.md"
    save_path = os.path.join(script_dir, "maps", filename)

    if not os.path.exists(os.path.join(script_dir, "maps")):
        os.makedirs(os.path.join(script_dir, "maps"))

    try:
        folders = [f for f in os.listdir(target_dir) 
                   if os.path.isdir(os.path.join(target_dir, f)) and not f.startswith('.')]
        folders.sort()

        with open(save_path, 'w', encoding='utf-8') as md_file:
            md_file.write(f"# 📂 Folder Map: {target_dir}\n")
            md_file.write(f"*Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n\n")
            for folder in folders:
                md_file.write(f"* `{folder}`\n")

        print(f"✅ Criado: {filename}")
    except Exception as e:
        print(f"❌ Erro: {e}")

if __name__ == "__main__":
    generate_folder_map()