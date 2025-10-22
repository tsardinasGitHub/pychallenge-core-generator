# Programming Challenge Generator / Generador de Desafíos de Programación

An interactive multilingual programming challenge generator to practice and improve coding skills. / Un generador interactivo multiidioma de desafíos de programación para practicar y mejorar habilidades de codificación.

## 🚀 Features / Características

- **🎲 Random challenges**: Get a random challenge to practice / Obtén un desafío aleatorio para practicar
- **📊 Difficulty filtering**: Choose between easy, medium, or hard based on your level / Filtra por fácil, medio o difícil según tu nivel
- **📂 Category filtering**: Practice specific course topics / Practica temas específicos del curso
- **🔍 Specific search**: Find challenges by name / Busca desafíos por nombre
- **📈 Statistics**: See what challenges are available / Ve qué desafíos están disponibles
- **🌐 Multilingual support**: Switch between English and Spanish / Alterna entre inglés y español
- **💻 User-friendly interface**: Colorful and easy-to-use CLI / Interfaz colorida y fácil de usar

## 📁 Project Structure / Estructura del Proyecto

```
pychallenge-core-generator/
├── src/
│   └── challenge_core/
│       ├── __init__.py            # Makes 'challenge_core' a package
│       ├── generator.py           # Main selection and filtering logic
│       ├── data.py                # Challenge database with 33 challenges
│       └── language.py            # Multilingual support system
├── main.py                        # Entry point and CLI
├── setup_dev.py                   # Automated development environment setup
├── setup.bat                      # Windows quick setup script
├── setup.sh                       # Unix/Linux quick setup script
├── .gitignore                     # Files to ignore in git
├── requirements.txt               # Project dependencies
└── README.md                      # This file
```

## 🛠️ Installation & Setup

### Prerequisites / Prerrequisitos
- **Python 3.8+** (recommended: Python 3.10 or higher)
- **Git** (for cloning the repository)

### Basic Installation / Instalación Básica

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd pychallenge-core-generator
   ```

2. **Run directly** (no external dependencies required):
   ```bash
   python main.py
   ```

### 🏗️ Development Environment Setup (Recommended)

#### 🚀 Quick Setup (Automated)

We provide automated setup scripts for easy environment creation:

**Windows:**
```powershell
# Option 1: Run batch file
setup.bat

# Option 2: Run Python setup script
python setup_dev.py
```

**macOS/Linux:**
```bash
# Option 1: Run shell script
chmod +x setup.sh
./setup.sh

# Option 2: Run Python setup script
python3 setup_dev.py
```

#### 🛠️ Manual Setup

If you prefer manual setup, follow these steps:

**Windows:**
```powershell
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Verify Python version
python --version

# Run the application
python main.py

# Deactivate when done (optional)
deactivate
```

**macOS/Linux:**
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate

# Verify Python version
python --version

# Run the application
python main.py

# Deactivate when done (optional)
deactivate
```

### 📦 Why Use Virtual Environment?

Even though this project has **no external dependencies**, using a virtual environment is considered best practice because:

- **🔒 Isolation**: Keeps your project isolated from system Python
- **📋 Reproducibility**: Ensures consistent Python version across environments
- **🔄 Version control**: Easy to manage different Python versions
- **🛡️ Future-proofing**: Ready for when you add dependencies later
- **👥 Team consistency**: Ensures all developers use the same environment
- **🧪 Testing**: Safer testing without affecting system Python

### Quick Start (No Setup Required)

If you prefer to run immediately without virtual environment:
```bash
python main.py
```

### Install Dependencies (Currently None)

```bash
pip install -r requirements.txt
```

Note: The `requirements.txt` file is currently empty as this project uses only Python standard library.

## 🎯 Usage

### Run the program:
```bash
python main.py
```

### Menu options / Opciones del menú:
- **1**: Get random challenge / Obtener desafío aleatorio
- **2**: Filter by difficulty (easy, medium, hard) / Filtrar por dificultad (fácil, medio, difícil)
- **3**: Filter by category / Filtrar por categoría
- **4**: Search for a specific challenge by name / Buscar desafío específico por nombre
- **5**: View database statistics / Ver estadísticas de la base de datos
- **6**: Change language (English ⇄ Spanish) / Cambiar idioma (Inglés ⇄ Español)
- **7**: View help / Ver ayuda
- **0**: Exit the program / Salir del programa

## 📚 Challenge Categories / Categorías de Desafíos

### 🎓 Course Topics / Temas del Curso (33 challenges total):
Each category has 3 difficulty levels (Easy, Medium, Hard) / Cada categoría tiene 3 niveles de dificultad (Fácil, Medio, Difícil):

1. **📐 Mathematics / Matemáticas**: Basic operations, prime numbers, complex calculations
2. **🔤 Strings**: Character counting, palindromes, advanced manipulation
3. **⚙️ Algorithms / Algoritmos**: Linear search, merge sort, bubble sort
4. **📋 List Comprehensions / Comprensión de Listas**: Filtering, nested structures, transformations
5. **λ Lambdas**: Simple operations, map/filter, advanced combinations
6. **🔍 Regular Expressions / Expresiones Regulares**: Pattern matching, phone extraction, email validation
7. **📂 File Handling / Manejo de Ficheros**: Reading files, word counting, JSON management
8. **📦 Package Management / Manejo de Paquetes**: Basic imports, system info, advanced integration
9. **📅 Dates / Fechas**: Simple operations, calculations, business day processing
10. **⚠️ Error Types / Tipos de Error**: Basic handling, multiple exceptions, robust systems
11. **🔄 Higher Order Functions / Funciones de Orden Superior**: Function parameters, composition, pipelines

### Example Challenges by Difficulty:

#### Easy / Fácil:
- **Sum of Two Numbers**: Basic mathematical operations
- **Simple Lambda Operations**: Introduction to lambda functions
- **Basic Exception Handling**: Simple error management

#### Medium / Medio:
- **Palindrome**: String processing and logic
- **Date Calculator**: Working with datetime module
- **File Word Counter**: File operations and text processing

#### Hard / Difícil:
- **Email Validation with Regex**: Complex pattern matching
- **Advanced Package Integration**: Multiple module coordination
- **Higher Order Functions**: Function pipelines and decorators

## 🌐 Multilingual Support / Soporte Multiidioma

The application supports two languages with real-time switching:

- **🇺🇸 English**: Default language with full interface
- **🇪🇸 Español**: Complete Spanish translation

### Language Features:
- **Real-time switching**: Change language without restarting
- **Complete translation**: All menus, messages, and difficulty levels
- **Persistent selection**: Language choice maintained during session
- **Consistent interface**: Emojis and formatting preserved

### How to change language:
1. Select option **6** from the main menu
2. Choose your preferred language (1=English, 2=Español)
3. Interface immediately updates to selected language

## 🔧 Customization / Personalización

### Adding new challenges / Agregar nuevos desafíos:
Edit the `src/challenge_core/data.py` file and add new elements to the `CHALLENGES_DB` array:

```python
{
    "id": 34,
    "title": "Your New Challenge",
    "description": "Challenge description",
    "difficulty": "easy|medium|hard",
    "category": "your_category",
    "points": 20,
    "example_input": "example",
    "example_output": "result",
    "hints": ["hint1", "hint2"]
}
```

### Adding new languages / Agregar nuevos idiomas:
Edit the `src/challenge_core/language.py` file and add new language dictionaries to the `translations` object.

### Modifying the interface:
The `main.py` file contains all the user interface logic. You can customize:
- Messages and emojis
- Colors and formatting
- New menu options
- Navigation flow

## 🧪 Testing / Pruebas

To test the main functionalities:

```python
from src.challenge_core import ChallengeGenerator, language_manager

# Create instance / Crear instancia
gen = ChallengeGenerator()

# Test methods / Probar métodos
challenge = gen.get_random_challenge()
easy_challenges = gen.filter_by_difficulty("easy")
math_challenges = gen.filter_by_category("mathematics")
stats = gen.get_statistics()

# Test multilingual support / Probar soporte multiidioma
language_manager.set_language("es")  # Switch to Spanish
spanish_text = language_manager.get_text("welcome_message")

language_manager.set_language("en")  # Switch to English
english_text = language_manager.get_text("welcome_message")
```

### Quick Test Commands:
```bash
# Test application / Probar aplicación
python main.py

# Test specific category / Probar categoría específica
python -c "
from src.challenge_core import ChallengeGenerator
gen = ChallengeGenerator()
challenges = gen.filter_by_category('lambdas')
print(f'Lambda challenges: {len(challenges)}')
for c in challenges: print(f'- {c[\"title\"]} ({c[\"difficulty\"]})')
"
```

## 📈 Statistics / Estadísticas

The generator includes a comprehensive statistics system that shows:
- **Total challenges**: 33 challenges across all categories
- **Distribution by difficulty**: 11 Easy, 11 Medium, 11 Hard
- **Distribution by category**: 3 challenges per category (balanced learning)
- **Course coverage**: All programming course topics included

### Current Database Stats:
```
📊 Total challenges: 33
🔥 By difficulty:
   Easy/Fácil: 11
   Medium/Medio: 11  
   Hard/Difícil: 11
📂 By category: 11 categories × 3 challenges each
```

## 🤝 Contributions

Contributions are welcome! To contribute:

1. Fork the project
2. Create a branch for your feature (`git checkout -b feature/NewFeature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

## 📝 Development Notes / Notas de Desarrollo

- **Python 3.6+** required / requerido
- No external dependencies / Sin dependencias externas
- **Modular architecture** for easy extension / Arquitectura modular para fácil extensión
- **Multilingual system** with centralized translations / Sistema multiidioma con traducciones centralizadas
- **Clear separation** between logic, data, and presentation / Separación clara entre lógica, datos y presentación
- **Scalable design** for adding new languages and challenges / Diseño escalable para agregar idiomas y desafíos

### Key Improvements Made:
- ✅ **33 challenges** covering all course topics
- ✅ **Balanced difficulty** (11 easy + 11 medium + 11 hard)
- ✅ **Multilingual support** (English ⇄ Spanish)
- ✅ **Real-time language switching**
- ✅ **Enhanced user interface** with difficulty indicators
- ✅ **Comprehensive course coverage** (11 programming topics)
- ✅ **Professional naming** (English naming conventions)

## 🎓 Educational Purpose / Propósito Educativo

This project is designed for / Este proyecto está diseñado para:
- **👨‍🎓 Students** who want to practice programming / Estudiantes que quieren practicar programación
- **👩‍🏫 Teachers** who need exercises for their classes / Profesores que necesitan ejercicios para sus clases
- **👨‍💻 Developers** who want to review algorithms / Desarrolladores que quieren repasar algoritmos
- **🌍 Spanish speakers** learning programming / Hispanohablantes aprendiendo programación
- **🎯 Anyone** interested in improving coding skills / Cualquiera interesado en mejorar habilidades de programación

### Learning Path:
1. **Start with Easy challenges** to build confidence
2. **Progress to Medium challenges** for skill building  
3. **Tackle Hard challenges** for advanced concepts
4. **Use your preferred language** (English or Spanish)
5. **Practice specific topics** using category filters

## 📄 License

This project is open source and available under the MIT License.

## 🚀 Version History / Historial de Versiones

### v2.0 - Multilingual & Complete Course Coverage
- ✅ Added Spanish language support
- ✅ Expanded to 33 challenges (11 per difficulty level)
- ✅ Complete course topic coverage (11 categories)
- ✅ Real-time language switching
- ✅ Enhanced user interface

### v1.0 - Initial Release
- ✅ Basic challenge generator
- ✅ English interface only
- ✅ 15 challenges across basic categories

---

🚀 **Happy programming and enjoy solving challenges!** 🚀
🚀 **¡Feliz programación y disfruta resolviendo desafíos!** 🚀

*Built with ❤️ for the programming learning community*
*Construido con ❤️ para la comunidad de aprendizaje de programación*