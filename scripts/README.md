# Scripts de Verificación y Pruebas

Esta carpeta contiene scripts útiles para verificar y probar el sistema del generador de desafíos.

## 📋 Scripts Disponibles

### 🔍 verify_challenges.py
**Propósito**: Verificación de base de datos original

**Qué hace**:
- Verifica total de desafíos
- Valida distribución por categoría
- Valida distribución por dificultad
- Muestra detalles de cada categoría

**Ejecutar**:
```bash
python scripts/verify_challenges.py
```

---

### 🔍 verify_spanish_db.py
**Propósito**: Verificación completa de la base de datos en español

**Qué hace**:
- Verifica que ambas bases de datos (EN/ES) tengan 165 desafíos
- Comprueba que todos los IDs estén presentes
- Valida la distribución por categorías y dificultad
- Muestra ejemplos de traducciones
- Confirma que todos los campos requeridos estén presentes

**Ejecutar**:
```bash
python scripts/verify_spanish_db.py
```

---

### 🧪 test_bilingual.py
**Propósito**: Pruebas funcionales del sistema bilingüe

**Qué hace**:
- Prueba generador en inglés y español
- Verifica el mismo desafío en ambos idiomas
- Prueba cambio dinámico de idioma
- Valida filtrado por categoría en español
- Valida filtrado por dificultad
- Muestra estadísticas en español

**Ejecutar**:
```bash
python scripts/test_bilingual.py
```

---

### 📊 show_summary.py
**Propósito**: Muestra resumen visual de la implementación

**Qué hace**:
- Estadísticas generales del sistema
- Lista de categorías EN → ES
- Distribución por dificultad
- Ejemplos de traducciones
- Archivos modificados
- Características implementadas
- Instrucciones de uso

**Ejecutar**:
```bash
python scripts/show_summary.py
```

---

### ⚡ quick_test.py
**Propósito**: Prueba rápida de funcionalidad

**Qué hace**:
- Desafío aleatorio en español
- Filtrado por categoría (Matemáticas)
- Filtrado por dificultad (Fácil)
- Estadísticas básicas
- Cambio a inglés

**Ejecutar**:
```bash
python scripts/quick_test.py
```

---

### 📝 doc_update_summary.py
**Propósito**: Resumen de actualizaciones de documentación

**Qué hace**:
- Muestra archivos de documentación actualizados
- Lista contenido agregado al CHANGELOG
- Lista actualizaciones en README
- Muestra información destacada
- Lista nuevos scripts documentados
- Muestra características clave

**Ejecutar**:
```bash
python scripts/doc_update_summary.py
```

---

## 🚀 Ejecución Rápida de Todos los Scripts

### Windows (PowerShell):
```powershell
# Ejecutar todos en secuencia
python scripts/verify_spanish_db.py
python scripts/test_bilingual.py
python scripts/show_summary.py
python scripts/quick_test.py
```

### Linux/macOS:
```bash
# Ejecutar todos en secuencia
python3 scripts/verify_spanish_db.py
python3 scripts/test_bilingual.py
python3 scripts/show_summary.py
python3 scripts/quick_test.py
```

---

## 📦 Dependencias

Todos estos scripts usan únicamente:
- Python 3.8+ (biblioteca estándar)
- Módulos del proyecto: `src.challenge_core`

No requieren dependencias externas.

**Nota sobre imports**: Todos los scripts incluyen configuración automática de rutas, por lo que no es necesario configurar `PYTHONPATH` manualmente. Simplemente ejecútalos desde la raíz del proyecto.

---

## ✅ Uso Recomendado

1. **Después de cambios en la base de datos**: `verify_spanish_db.py`
2. **Antes de un release**: `test_bilingual.py` + `show_summary.py`
3. **Para prueba rápida**: `quick_test.py`
4. **Para documentación**: `doc_update_summary.py`

---

🔧 **Mantenimiento**: Estos scripts se actualizan junto con el sistema principal.
