"""
Script para verificar la base de datos de desafíos en español.
"""

import sys
from pathlib import Path

# Agregar el directorio raíz al path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.challenge_core.data import CHALLENGES_DB_EN, CHALLENGES_DB_ES, get_categories, get_difficulties

def verify_spanish_database():
    """Verifica que la base de datos en español esté completa y correcta."""
    
    print("=" * 80)
    print("VERIFICACIÓN DE BASE DE DATOS EN ESPAÑOL")
    print("=" * 80)
    
    # Verificar número de desafíos
    print(f"\n✓ Desafíos en inglés: {len(CHALLENGES_DB_EN)}")
    print(f"✓ Desafíos en español: {len(CHALLENGES_DB_ES)}")
    
    if len(CHALLENGES_DB_EN) == len(CHALLENGES_DB_ES):
        print("✅ Ambas bases de datos tienen el mismo número de desafíos")
    else:
        print("❌ ERROR: Las bases de datos tienen diferente número de desafíos")
        return
    
    # Verificar que todos los IDs estén presentes
    ids_en = {challenge['id'] for challenge in CHALLENGES_DB_EN}
    ids_es = {challenge['id'] for challenge in CHALLENGES_DB_ES}
    
    if ids_en == ids_es:
        print(f"✅ Todos los IDs (1-{len(CHALLENGES_DB_EN)}) están presentes en ambas bases de datos")
    else:
        missing_en = ids_es - ids_en
        missing_es = ids_en - ids_es
        if missing_en:
            print(f"❌ IDs faltantes en inglés: {missing_en}")
        if missing_es:
            print(f"❌ IDs faltantes en español: {missing_es}")
        return
    
    # Verificar categorías
    print("\n" + "=" * 80)
    print("CATEGORÍAS")
    print("=" * 80)
    
    categories_en = get_categories('en')
    categories_es = get_categories('es')
    
    print(f"\nCategorías en inglés ({len(categories_en)}):")
    for cat in categories_en:
        count = sum(1 for c in CHALLENGES_DB_EN if c['category'] == cat)
        print(f"  - {cat}: {count} desafíos")
    
    print(f"\nCategorías en español ({len(categories_es)}):")
    for cat in categories_es:
        count = sum(1 for c in CHALLENGES_DB_ES if c['category'] == cat)
        print(f"  - {cat}: {count} desafíos")
    
    # Verificar dificultades
    print("\n" + "=" * 80)
    print("NIVELES DE DIFICULTAD")
    print("=" * 80)
    
    difficulties_en = get_difficulties('en')
    difficulties_es = get_difficulties('es')
    
    print(f"\nDificultades en inglés: {difficulties_en}")
    for diff in difficulties_en:
        count = sum(1 for c in CHALLENGES_DB_EN if c['difficulty'] == diff)
        print(f"  - {diff}: {count} desafíos")
    
    print(f"\nDificultades en español: {difficulties_es}")
    for diff in difficulties_es:
        count = sum(1 for c in CHALLENGES_DB_ES if c['difficulty'] == diff)
        print(f"  - {diff}: {count} desafíos")
    
    # Verificar distribución por categoría y dificultad
    print("\n" + "=" * 80)
    print("DISTRIBUCIÓN POR CATEGORÍA Y DIFICULTAD (ESPAÑOL)")
    print("=" * 80)
    
    for cat in categories_es:
        print(f"\n{cat.upper()}:")
        for diff in ['easy', 'medium', 'hard']:
            count = sum(1 for c in CHALLENGES_DB_ES 
                       if c['category'] == cat and c['difficulty'] == diff)
            print(f"  - {diff}: {count} desafíos")
    
    # Verificar que todos los desafíos tienen los campos necesarios
    print("\n" + "=" * 80)
    print("VERIFICACIÓN DE CAMPOS")
    print("=" * 80)
    
    required_fields = ['id', 'title', 'description', 'difficulty', 'category', 'points', 'example_input', 'example_output', 'hints']
    
    missing_fields = []
    for challenge in CHALLENGES_DB_ES:
        for field in required_fields:
            if field not in challenge:
                missing_fields.append(f"ID {challenge.get('id', '?')}: falta campo '{field}'")
    
    if missing_fields:
        print("❌ Campos faltantes:")
        for msg in missing_fields:
            print(f"  - {msg}")
    else:
        print("✅ Todos los desafíos tienen los campos requeridos")
    
    # Mostrar algunos ejemplos de traducciones
    print("\n" + "=" * 80)
    print("EJEMPLOS DE TRADUCCIONES")
    print("=" * 80)
    
    for i in [1, 30, 60, 90, 120, 150, 165]:
        challenge_en = next(c for c in CHALLENGES_DB_EN if c['id'] == i)
        challenge_es = next(c for c in CHALLENGES_DB_ES if c['id'] == i)
        
        print(f"\nID {i}:")
        print(f"  EN: {challenge_en['title']}")
        print(f"  ES: {challenge_es['title']}")
        print(f"  Categoría EN: {challenge_en['category']}")
        print(f"  Categoría ES: {challenge_es['category']}")
    
    print("\n" + "=" * 80)
    print("✅ VERIFICACIÓN COMPLETADA EXITOSAMENTE")
    print("=" * 80)

if __name__ == "__main__":
    verify_spanish_database()
