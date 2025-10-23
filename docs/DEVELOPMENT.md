# Guía de Desarrollo - Challenge Generator v4.0

## 📖 Documentación Técnica Completa

Esta guía proporciona información técnica detallada sobre la arquitectura y el funcionamiento del sistema.

---

## 🏗️ Arquitectura del Sistema

### Estructura de Directorios

```
pychallenge-core-generator/
├── src/
│   └── challenge_core/
│       ├── __init__.py           # Paquete principal
│       ├── data.py               # Bases de datos bilingües
│       ├── generator.py          # Lógica del generador
│       └── language.py           # Sistema de idiomas
├── scripts/                      # Scripts de verificación
│   ├── README.md                 # Documentación de scripts
│   ├── verify_spanish_db.py      # Verificación BD española
│   ├── test_bilingual.py         # Pruebas funcionales
│   ├── show_summary.py           # Resumen de implementación
│   ├── quick_test.py             # Prueba rápida
│   └── doc_update_summary.py     # Resumen documentación
├── docs/                         # Documentación
│   ├── CHANGELOG.md              # Historial de cambios
│   └── DEVELOPMENT.md            # Esta guía
├── main.py                       # Punto de entrada
├── README.md                     # Documentación principal
└── requirements.txt              # Dependencias (vacío)
```

---

## 🗄️ Sistema de Bases de Datos

### Bases de Datos Duales

El sistema utiliza **dos bases de datos separadas** para mejor rendimiento y claridad:

#### `CHALLENGES_DB_EN` (Inglés)
- 165 desafíos en inglés
- Categorías en inglés: `mathematics`, `strings`, `algorithms`, etc.
- Ubicación: `src/challenge_core/data.py` (líneas 10-1848)

#### `CHALLENGES_DB_ES` (Español)
- 165 desafíos en español
- Categorías en español: `matemáticas`, `cadenas`, `algoritmos`, etc.
- Ubicación: `src/challenge_core/data.py` (líneas 1850-3688)

### Estructura de un Desafío

```python
{
    "id": 1,                           # Único, 1-165
    "title": "Challenge Title",        # Nombre del desafío
    "description": "Description...",   # Descripción detallada
    "difficulty": "easy|medium|hard",  # Nivel de dificultad
    "category": "category_name",       # Categoría
    "points": 10-35,                   # Puntos (10=easy, 20=medium, 30-35=hard)
    "example_input": "input",          # Ejemplo de entrada
    "example_output": "output",        # Ejemplo de salida esperada
    "hints": ["hint1", "hint2", ...]   # Lista de pistas
}
```

### Distribución de Desafíos

```
Total: 165 desafíos por idioma
├── 11 Categorías × 15 desafíos cada una
└── Por dificultad:
    ├── Easy: 55 desafíos (5 por categoría)
    ├── Medium: 55 desafíos (5 por categoría)
    └── Hard: 55 desafíos (5 por categoría)
```

---

## 🔧 Componentes Principales

### 1. ChallengeGenerator (generator.py)

**Clase principal** para gestionar desafíos.

#### Constructor
```python
def __init__(self, language: str = 'en'):
    """
    Inicializa el generador con idioma especificado.
    
    Args:
        language: 'en' para inglés, 'es' para español
    """
```

#### Métodos Principales

```python
# Cambiar idioma dinámicamente
generator.set_language('es')

# Obtener desafío aleatorio
challenge = generator.get_random_challenge()

# Filtrar por dificultad
easy_challenges = generator.filter_by_difficulty('easy')

# Filtrar por categoría
math_challenges = generator.filter_by_category('matemáticas')

# Buscar desafío específico
challenge = generator.search_challenge('Suma de Dos Números')

# Obtener estadísticas
stats = generator.get_statistics()
```

### 2. Sistema de Idiomas (language.py)

**LanguageManager**: Gestiona traducciones de la interfaz.

```python
# Cambiar idioma
language_manager.set_language('es')

# Obtener texto traducido
text = language_manager.get_text('welcome_message')

# Obtener idioma actual
current = language_manager.current_language  # 'en' o 'es'
```

### 3. Funciones de Datos (data.py)

```python
# Obtener base de datos según idioma
db = get_challenges_db('es')  # Retorna CHALLENGES_DB_ES

# Obtener categorías en idioma especificado
categories = get_categories('es')

# Obtener dificultades en idioma especificado
difficulties = get_difficulties('en')
```

---

## 🌐 Sistema Bilingüe

### Mapeo de Categorías

| Inglés                    | Español                       |
|---------------------------|-------------------------------|
| mathematics               | matemáticas                   |
| strings                   | cadenas                       |
| algorithms                | algoritmos                    |
| comprension de listas     | comprension de listas         |
| lambdas                   | lambdas                       |
| expresiones regulares     | expresiones regulares         |
| manejo de ficheros        | manejo de ficheros            |
| manejo de paquetes        | manejo de paquetes            |
| fechas                    | fechas                        |
| tipos de error            | tipos de error                |
| funciones de orden superior | funciones de orden superior |

### Flujo de Cambio de Idioma

```
Usuario selecciona idioma
        ↓
language_manager.set_language(nuevo_idioma)
        ↓
main.py retorna nuevo idioma
        ↓
generator.set_language(nuevo_idioma)
        ↓
generator.challenges = get_challenges_db(nuevo_idioma)
        ↓
Interfaz y desafíos actualizados
```

---

## 🧪 Testing y Verificación

### Scripts Disponibles

1. **verify_spanish_db.py**: Verificación completa
   - Compara ambas bases de datos
   - Valida integridad
   - Muestra estadísticas

2. **test_bilingual.py**: Pruebas funcionales
   - Prueba ambos idiomas
   - Verifica cambio dinámico
   - Valida filtros

3. **quick_test.py**: Prueba rápida
   - Verificación básica
   - Ideal para desarrollo

### Ejecutar Pruebas

```bash
# Verificación completa
python scripts/verify_spanish_db.py

# Pruebas funcionales
python scripts/test_bilingual.py

# Prueba rápida
python scripts/quick_test.py
```

---

## 🔨 Agregar Nuevos Desafíos

### Paso 1: Agregar en CHALLENGES_DB_EN

```python
CHALLENGES_DB_EN = [
    # ... desafíos existentes
    {
        "id": 166,  # Siguiente ID disponible
        "title": "New Challenge",
        "description": "Challenge description in English",
        "difficulty": "medium",
        "category": "mathematics",
        "points": 20,
        "example_input": "5",
        "example_output": "25",
        "hints": ["Hint 1", "Hint 2"]
    }
]
```

### Paso 2: Agregar traducción en CHALLENGES_DB_ES

```python
CHALLENGES_DB_ES = [
    # ... desafíos existentes
    {
        "id": 166,  # MISMO ID que en inglés
        "title": "Nuevo Desafío",
        "description": "Descripción del desafío en español",
        "difficulty": "medium",
        "category": "matemáticas",
        "points": 20,
        "example_input": "5",
        "example_output": "25",
        "hints": ["Pista 1", "Pista 2"]
    }
]
```

### Paso 3: Verificar

```bash
python scripts/verify_spanish_db.py
```

### ⚠️ Reglas Importantes

- ✅ **Mismo ID** en ambas bases de datos
- ✅ **Misma dificultad** y puntos
- ✅ **Mantener balance**: agregar misma cantidad a cada dificultad
- ✅ **Categoría traducida** correctamente
- ✅ **Todos los campos** requeridos presentes

---

## 🎨 Personalizar Interfaz

### Agregar Nuevos Textos

Editar `src/challenge_core/language.py`:

```python
'en': {
    'new_text_key': 'Text in English',
    # ...
},
'es': {
    'new_text_key': 'Texto en Español',
    # ...
}
```

Usar en código:
```python
text = language_manager.get_text('new_text_key')
```

### Agregar Nuevo Idioma

1. Agregar traducciones en `language.py`
2. Crear nueva base de datos (ej: `CHALLENGES_DB_FR`)
3. Actualizar `get_challenges_db()` en `data.py`
4. Actualizar menú de idiomas en `main.py`

---

## 📊 Estadísticas del Sistema

```python
stats = generator.get_statistics()

# Retorna:
{
    'total_challenges': 165,
    'by_difficulty': {
        'easy': 55,
        'medium': 55,
        'hard': 55
    },
    'by_category': {
        'matemáticas': 15,
        'cadenas': 15,
        # ... (11 categorías)
    }
}
```

---

## 🐛 Debugging

### Problemas Comunes

#### Error: "Import could not be resolved"
- **Causa**: Linter de VS Code
- **Solución**: Ignorar (el código funciona correctamente)

#### Desafíos no traducidos
- **Causa**: ID no coincide o falta en CHALLENGES_DB_ES
- **Solución**: Verificar con `verify_spanish_db.py`

#### Categoría no aparece
- **Causa**: Nombre de categoría no coincide
- **Solución**: Usar nombres exactos del mapeo de categorías

### Modo Debug

```python
# Imprimir información del generador
print(f"Idioma actual: {generator.language}")
print(f"Total desafíos cargados: {len(generator.challenges)}")
print(f"Primer desafío: {generator.challenges[0]['title']}")
```

---

## 🚀 Deployment

### Pre-deployment Checklist

- [ ] Ejecutar `verify_spanish_db.py` sin errores
- [ ] Ejecutar `test_bilingual.py` sin errores
- [ ] Verificar que ambas BD tengan mismo número de desafíos
- [ ] Actualizar CHANGELOG.md
- [ ] Actualizar README.md si hay nuevas características
- [ ] Probar cambio de idioma en la aplicación

### Release

1. Actualizar versión en documentación
2. Crear tag de git
3. Actualizar CHANGELOG con fecha
4. Verificar todos los scripts funcionan

---

## 📝 Convenciones de Código

### Python
- PEP 8 style guide
- Type hints en funciones públicas
- Docstrings en formato Google

### Commits
- Mensajes en inglés
- Formato: `tipo: descripción breve`
- Tipos: `feat`, `fix`, `docs`, `refactor`, `test`

Ejemplos:
```
feat: add new math challenges
fix: correct category translation
docs: update README with v4.0 info
refactor: improve generator performance
test: add bilingual system tests
```

---

## 🤝 Contribuir

1. Fork el proyecto
2. Crear rama (`git checkout -b feature/NewFeature`)
3. Agregar cambios con commits descriptivos
4. Ejecutar scripts de verificación
5. Push a la rama (`git push origin feature/NewFeature`)
6. Abrir Pull Request

---

## 📞 Soporte

Para problemas o preguntas:
1. Revisar esta guía
2. Revisar README.md
3. Ejecutar scripts de verificación
4. Revisar CHANGELOG.md para cambios recientes

---

**Última actualización**: v4.0.0 - Octubre 23, 2025  
**Mantenedor**: Challenge Generator Team
