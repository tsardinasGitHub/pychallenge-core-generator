#!/usr/bin/env python3
"""
Development Environment Setup Script
Creates virtual environment and sets up the development environment
"""

import os
import sys
import subprocess
import platform
from pathlib import Path

def print_header():
    """Print setup header"""
    print("🚀" + "="*60 + "🚀")
    print("    PROGRAMMING CHALLENGE GENERATOR - DEV SETUP")
    print("🚀" + "="*60 + "🚀")
    print()

def check_python_version():
    """Check if Python version meets requirements"""
    version = sys.version_info
    print(f"🐍 Python version detected: {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Error: Python 3.8 or higher is required!")
        print("   Please install a newer version of Python.")
        return False
    
    print("✅ Python version is compatible!")
    return True

def create_virtual_environment():
    """Create virtual environment"""
    print("\n📦 Creating virtual environment...")
    
    if Path("venv").exists():
        print("⚠️  Virtual environment 'venv' already exists!")
        response = input("   Do you want to recreate it? (y/n): ").lower().strip()
        if response != 'y':
            print("   Skipping virtual environment creation.")
            return True
    
    try:
        subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
        print("✅ Virtual environment created successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error creating virtual environment: {e}")
        return False

def get_activation_command():
    """Get the correct activation command for the current platform"""
    system = platform.system()
    if system == "Windows":
        return "venv\\Scripts\\activate"
    else:
        return "source venv/bin/activate"

def show_next_steps():
    """Show next steps for the user"""
    activation_cmd = get_activation_command()
    
    print("\n🎯 Setup completed successfully!")
    print("\n📋 Next steps:")
    print("   1. Activate the virtual environment:")
    
    if platform.system() == "Windows":
        print(f"      {activation_cmd}")
    else:
        print(f"      {activation_cmd}")
    
    print("   2. Run the application:")
    print("      python main.py")
    print("\n   3. When finished, deactivate the environment:")
    print("      deactivate")
    
    print("\n💡 Pro tips:")
    print("   - The virtual environment ensures clean isolation")
    print("   - You can safely add dependencies to requirements.txt")
    print("   - Use 'python --version' to verify you're in the right environment")
    
def test_installation():
    """Test if the main application can be imported"""
    print("\n🧪 Testing installation...")
    
    try:
        # Add current directory to Python path
        sys.path.insert(0, str(Path.cwd()))
        
        # Try to import the main components
        from src.challenge_core import ChallengeGenerator, CHALLENGES_DB, language_manager
        
        # Quick functionality test
        generator = ChallengeGenerator()
        stats = generator.get_statistics()
        total_challenges = stats.get('total_challenges', 0)
        
        print(f"✅ Successfully imported challenge_core package!")
        print(f"✅ Challenge database loaded: {total_challenges} challenges")
        print(f"✅ Language manager initialized: {language_manager.current_language}")
        
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("   The application might not run correctly.")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def main():
    """Main setup function"""
    print_header()
    
    # Check Python version
    if not check_python_version():
        return 1
    
    # Create virtual environment
    if not create_virtual_environment():
        return 1
    
    # Test installation
    test_installation()
    
    # Show next steps
    show_next_steps()
    
    print("\n🚀 Development environment setup completed!")
    print("   Happy coding! 🎉")
    
    return 0

if __name__ == "__main__":
    try:
        exit_code = main()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print("\n\n⚠️  Setup interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error during setup: {e}")
        sys.exit(1)