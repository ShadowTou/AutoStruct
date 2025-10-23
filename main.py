import os
import subprocess
import platform

def system_info():
    """Menampilkan sistem yang detail"""
    print("=== SYSTEM INFORMATION ===")

    # Informasi platform
    print(f"OS: {platform.system} Version: {platform.version}")
    print(f"Arch: {platform.architecture()}")
    print(f"Processor: {platform.processor()}")


    # Informasi direktori
    print(f"Current directory: {os.getcwd()}")
    print(f"Home directory: {os.path.expanduser("~")}")

    # Berjalan jika os windows
    if platform.system() == "Windows":
        #disk process in windows
        result = subprocess.run(["wmic", "logicaldisk", "get", "size,freespace,caption"], capture_output=True, text=True)
        print("\nDisk Information:\n")
        print(result.stdout)
    # Berjalan jika os unix-like
    else:
        result = subprocess.run(["df", "-h"], capture_output=True, text=True)
        print("\nDisk Information:")
        print(result.stdout)

def create_project_structure(project_name):
    """Membuat Struktur Folder Otomatis"""
    #membuat template folder yang nantinya bakal otomatis muncul disaat aplikasi dijalankan
    folders = ["src", "tests", "docs", "models", "controllers", "views", "config"]
    # membuat folder dengan parameter project_name
    os.makedirs(project_name, exist_ok=True)
    # change directory ke project_name yang telah dibuat
    os.chdir(project_name)

    # Membuat folder template di project_name
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"Created: {folder}\n")
    
    # Membuat readme untuk membutuhkan client memahami program kita
    with open("readme.md", "w") as create:
        create.write(f"# {project_name}\n\nProject Description Here!")

    print(f"\nProject '{project_name}' created successfully!")


# Demo Aplikasi
if __name__ == "__main__":
    system_info()
    create_project_structure("Acil")
        