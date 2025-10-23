# Programming Challenge Generator / Generador de Desafíos de Programación

An interactive **fully bilingual** programming challenge generator to practice and improve coding skills. / Un generador interactivo **completamente bilingüe** de desafíos de programación para practicar y mejorar habilidades de codificación.

## 🌟 NEW in v4.0: Complete Bilingual System!

🎉 **All 165 challenges are now available in both English and Spanish!**
- ✅ Separate databases for English and Spanish
- ✅ Full translations: titles, descriptions, hints, and categories
- ✅ Real-time language switching with instant challenge updates
- ✅ No runtime translation needed - pre-translated content for best performance

## 🚀 Features / Características

- **🎲 Random challenges**: Get a random challenge to practice / Obtén un desafío aleatorio para practicar
- **📊 Difficulty filtering**: Choose between easy, medium, or hard based on your level / Filtra por fácil, medio o difícil según tu nivel
- **📂 Category filtering**: Practice specific course topics / Practica temas específicos del curso
- **🔍 Specific search**: Find challenges by name / Busca desafíos por nombre
- **📈 Statistics**: See what challenges are available / Ve qué desafíos están disponibles
- **🌐 **Full bilingual support**: Switch between English and Spanish with complete challenge translations / Soporte completamente bilingüe con traducciones completas de desafíos
- **💻 User-friendly interface**: Colorful and easy-to-use CLI / Interfaz colorida y fácil de usar
- **⚡ Dynamic language switching**: Changes apply immediately to all challenges / Cambio de idioma dinámico que se aplica inmediatamente

## 📁 Project Structure / Estructura del Proyecto

```
pychallenge-core-generator/
├── src/
│   └── challenge_core/
│       ├── __init__.py           # Paquete principal
│       ├── data.py               # Bases de datos bilingües (165 EN + 165 ES)
│       ├── generator.py          # Lógica del generador con soporte de idioma
│       └── language.py           # Sistema multiidioma
├── scripts/                      # Scripts de verificación y pruebas
│   ├── README.md                 # Documentación de scripts
│   ├── verify_challenges.py      # Verificación BD original
│   ├── verify_spanish_db.py      # Verificación BD española
│   ├── test_bilingual.py         # Pruebas sistema bilingüe
│   ├── show_summary.py           # Resumen implementación
│   ├── quick_test.py             # Prueba rápida
│   └── doc_update_summary.py     # Resumen documentación
├── docs/                         # Documentación técnica
│   ├── INDEX.md                  # Índice de documentación
│   ├── CHANGELOG.md              # Historial de cambios
│   ├── DEVELOPMENT.md            # Guía de desarrollo completa
│   └── IMPLEMENTACION_BILINGUE.md # Detalles implementación bilingüe
├── main.py                       # Punto de entrada CLI
├── setup_dev.py                  # Setup automático entorno desarrollo
├── setup.bat                     # Script setup Windows
├── setup.sh                      # Script setup Unix/Linux
├── .gitignore                    # Archivos ignorados por git
├── requirements.txt              # Dependencias del proyecto
└── README.md                     # Este archivo
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

### 🎓 Course Topics / Temas del Curso (165 challenges total):
Each category has **15 challenges** with balanced difficulty levels (5 easy + 5 medium + 5 hard) / Cada categoría tiene **15 desafíos** con niveles de dificultad balanceados (5 fácil + 5 medio + 5 difícil):

1. **📐 Mathematics / Matemáticas** (15 challenges): Basic operations, prime numbers, complex calculations, matrix operations, number theory
2. **🔤 Strings** (15 challenges): Character counting, palindromes, advanced manipulation, pattern matching, text analysis
3. **⚙️ Algorithms / Algoritmos** (15 challenges): Linear search, merge sort, bubble sort, quicksort, dynamic programming
4. **📋 List Comprehensions / Comprensión de Listas** (15 challenges): Filtering, nested structures, transformations, matrix operations
5. **λ Lambdas** (15 challenges): Simple operations, map/filter/reduce, advanced combinations, currying
6. **🔍 Regular Expressions / Expresiones Regulares** (15 challenges): Pattern matching, phone extraction, email validation, log parsing
7. **📂 File Handling / Manejo de Ficheros** (15 challenges): Reading files, word counting, JSON management, CSV processing, binary files
8. **📦 Package Management / Manejo de Paquetes** (15 challenges): Basic imports, system info, advanced integration, threading
9. **📅 Dates / Fechas** (15 challenges): Simple operations, calculations, business day processing, timezone handling
10. **⚠️ Error Types / Tipos de Error** (15 challenges): Basic handling, multiple exceptions, robust systems, custom exceptions
11. **🔄 Higher Order Functions / Funciones de Orden Superior** (15 challenges): Function parameters, composition, pipelines, decorators

### Distribution Summary:
- **Total Challenges**: 165
- **Easy Challenges**: 55 (5 per category)
- **Medium Challenges**: 55 (5 per category)
- **Hard Challenges**: 55 (5 per category)
- **Categories**: 11 programming topics
- **Perfect Balance**: Each category has exactly the same distribution

### Example Challenges by Difficulty:

#### Easy / Fácil (55 total):
- **Sum of Two Numbers**: Basic mathematical operations
- **Simple Lambda Operations**: Introduction to lambda functions
- **Basic Exception Handling**: Simple error management
- **String Reverser**: String manipulation basics
- **Linear Search**: Basic algorithm implementation

#### Medium / Medio (55 total):
- **Palindrome**: String processing and logic
- **Date Calculator**: Working with datetime module
- **File Word Counter**: File operations and text processing
- **Binary Search**: Efficient searching algorithms
- **Lambda Functions with Map**: Functional programming

#### Hard / Difícil (55 total):
- **Email Validation with Regex**: Complex pattern matching
- **Advanced Package Integration**: Multiple module coordination
- **Higher Order Functions**: Function pipelines and decorators
- **Dynamic Programming - Knapsack**: Advanced algorithms
- **Lazy Evaluation Pipeline**: Generator-based processing

## 🌐 Multilingual Support / Soporte Multiidioma

The application supports **complete bilingual functionality** with separate challenge databases for each language:

- **🇺🇸 English**: Complete database with 165 challenges
- **🇪🇸 Español**: Complete database with 165 challenges (fully translated)

### Bilingual Features / Características Bilingües:
- **✅ Dual Databases**: Separate `CHALLENGES_DB_EN` and `CHALLENGES_DB_ES`
- **✅ Complete Translations**: All titles, descriptions, hints, and categories translated
- **✅ Real-time switching**: Change language without restarting
- **✅ Instant updates**: Challenges immediately reflect selected language
- **✅ Category translation**: 
  - mathematics → matemáticas
  - strings → cadenas
  - algorithms → algoritmos
  - list comprehensions → comprension de listas
  - lambdas → lambdas
  - regular expressions → expresiones regulares
  - file handling → manejo de ficheros
  - package management → manejo de paquetes
  - dates → fechas
  - error types → tipos de error
  - higher order functions → funciones de orden superior
- **✅ Persistent selection**: Language choice maintained during session
- **✅ Consistent interface**: Emojis and formatting preserved
- **✅ Pre-translated content**: No runtime translation overhead

### How to change language / Cómo cambiar el idioma:
1. Select option **6** from the main menu / Selecciona la opción **6** del menú principal
2. Choose your preferred language / Elige tu idioma preferido
   - 1 = English (165 challenges)
   - 2 = Español (165 desafíos)
3. All challenges immediately update to selected language / Todos los desafíos se actualizan inmediatamente al idioma seleccionado

### Example / Ejemplo:
```
English Challenge:
  ID: 1
  Title: Sum of Two Numbers
  Category: mathematics
  Description: Create a function that takes two numbers and returns their sum.

Spanish Challenge (same ID):
  ID: 1
  Título: Suma de Dos Números
  Categoría: matemáticas
  Descripción: Escribe una función que sume dos números y devuelva el resultado.
```

## 🔧 Customization / Personalización

### Adding new challenges / Agregar nuevos desafíos

You need to add the challenge to **both databases** (English and Spanish) in `src/challenge_core/data.py`:

```python
# In CHALLENGES_DB_EN:
{"id": 166, "title": "Your Challenge", "category": "mathematics", ...}

# In CHALLENGES_DB_ES (same ID):
{"id": 166, "title": "Tu Desafío", "category": "matemáticas", ...}
```

⚠️ **Important**: Keep the same ID in both databases!

📚 **For complete customization guide**, see [Development Guide](docs/DEVELOPMENT.md)  
📚 **Para guía completa de personalización**, ver [Guía de Desarrollo](docs/DEVELOPMENT.md)

### Adding new languages / Agregar nuevos idiomas:
Edit the `src/challenge_core/language.py` file and add new language dictionaries to the `translations` object.

### Modifying the interface:
The `main.py` file contains all the user interface logic. You can customize:
- Messages and emojis
- Colors and formatting
- New menu options
- Navigation flow

## 🧪 Testing / Pruebas

### Quick Test / Prueba Rápida
```bash
# Quick functionality test / Prueba rápida de funcionalidad
python scripts/quick_test.py
```

### Verification Scripts / Scripts de Verificación
```bash
# Verify Spanish database / Verificar base de datos española
python scripts/verify_spanish_db.py

# Test bilingual system / Probar sistema bilingüe  
python scripts/test_bilingual.py

# Show implementation summary / Mostrar resumen de implementación
python scripts/show_summary.py
```

### Using in Code / Uso en Código
```python
from src.challenge_core import ChallengeGenerator

# Create generator in Spanish / Crear generador en español
gen = ChallengeGenerator('es')

# Get random challenge / Obtener desafío aleatorio
challenge = gen.get_random_challenge()

# Change language / Cambiar idioma
gen.set_language('en')
```

📚 **For detailed testing and development information**, see [Development Guide](docs/DEVELOPMENT.md)  
📚 **Para información detallada de testing y desarrollo**, ver [Guía de Desarrollo](docs/DEVELOPMENT.md)

## 📈 Statistics / Estadísticas

The generator includes a comprehensive statistics system that shows:
- **Total challenges**: 165 challenges across all categories
- **Distribution by difficulty**: 55 Easy, 55 Medium, 55 Hard
- **Distribution by category**: 15 challenges per category (perfectly balanced learning)
- **Course coverage**: All programming course topics included with extensive practice

### Current Database Stats:
```
📊 Total challenges: 165
🔥 By difficulty:
   Easy/Fácil: 55
   Medium/Medio: 55  
   Hard/Difícil: 55
📂 By category: 11 categories × 15 challenges each
   - 5 Easy per category
   - 5 Medium per category
   - 5 Hard per category
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
- ✅ **165 challenges** covering all course topics (5x expansion!)
- ✅ **Perfectly balanced difficulty** (55 easy + 55 medium + 55 hard)
- ✅ **5 challenges per difficulty level** per category for extensive practice
- ✅ **Complete bilingual system** with separate databases (English + Spanish)
- ✅ **Full translations** of all 165 challenges in Spanish
- ✅ **Real-time language switching** with instant challenge updates
- ✅ **Enhanced user interface** with difficulty indicators
- ✅ **Comprehensive course coverage** (11 programming topics)
- ✅ **Professional naming** (English naming conventions)
- ✅ **Scalable architecture** for future expansions
- ✅ **Pre-translated content** for optimal performance

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

### v4.0.0 - Complete Bilingual System (2025-10-23)
- ✅ **165 challenges fully translated to Spanish**
- ✅ Separate databases: `CHALLENGES_DB_EN` and `CHALLENGES_DB_ES`
- ✅ Complete translations: titles, descriptions, hints, categories
- ✅ Dynamic language switching with `set_language()` method
- ✅ Language-aware functions: `get_challenges_db()`, `get_categories()`, `get_difficulties()`
- ✅ Real-time challenge updates when changing language
- ✅ Verification and testing scripts added
- ✅ Pre-translated content for optimal performance
- ✅ Perfect distribution maintained in both languages

### v3.0.0 - Massive Expansion (2025-10-22)
- ✅ Expanded from 33 to 165 challenges (5x increase!)
- ✅ 5 challenges per difficulty level per category
- ✅ Perfect balance: 55 easy, 55 medium, 55 hard
- ✅ Comprehensive coverage of all programming topics
- ✅ Enhanced challenge variety and complexity
- ✅ Improved learning progression

### v2.0.0 - Multilingual & Complete Course Coverage
- ✅ Added Spanish language support (interface only)
- ✅ Expanded to 33 challenges (11 per difficulty level)
- ✅ Complete course topic coverage (11 categories)
- ✅ Real-time language switching for interface
- ✅ Enhanced user interface

### v1.0.0 - Initial Release
- ✅ Basic challenge generator
- ✅ English interface only
- ✅ 15 challenges across basic categories

---

## 📚 Documentation / Documentación

- **[Development Guide](docs/DEVELOPMENT.md)** - Complete technical documentation / Documentación técnica completa
  - Architecture and components / Arquitectura y componentes
  - Adding challenges / Agregar desafíos
  - Bilingual system details / Detalles del sistema bilingüe
  - Testing and debugging / Testing y debugging
  - Contribution guidelines / Guías de contribución

- **[Changelog](docs/CHANGELOG.md)** - Version history / Historial de versiones

- **[Scripts Documentation](scripts/README.md)** - Verification scripts guide / Guía de scripts de verificación

---

🚀 **Happy programming and enjoy solving challenges!** 🚀  
🚀 **¡Feliz programación y disfruta resolviendo desafíos!** 🚀

*Built with ❤️ for the programming learning community*  
*Construido con ❤️ para la comunidad de aprendizaje de programación*