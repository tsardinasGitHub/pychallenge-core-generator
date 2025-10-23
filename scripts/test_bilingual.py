"""
Script para probar el sistema bilingüe.
"""

import sys
from pathlib import Path

# Agregar el directorio raíz al path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.challenge_core import ChallengeGenerator, language_manager

def test_bilingual_system():
    """Prueba el sistema bilingüe."""
    
    print("=" * 80)
    print("PRUEBA DEL SISTEMA BILINGÜE")
    print("=" * 80)
    
    # Crear generador en inglés
    print("\n1. PROBANDO EN INGLÉS")
    print("-" * 80)
    gen_en = ChallengeGenerator('en')
    challenge_en = gen_en.get_random_challenge()
    print(f"ID: {challenge_en['id']}")
    print(f"Título: {challenge_en['title']}")
    print(f"Categoría: {challenge_en['category']}")
    print(f"Dificultad: {challenge_en['difficulty']}")
    print(f"Descripción: {challenge_en['description'][:100]}...")
    
    # Crear generador en español
    print("\n2. PROBANDO EN ESPAÑOL")
    print("-" * 80)
    gen_es = ChallengeGenerator('es')
    challenge_es = gen_es.get_random_challenge()
    print(f"ID: {challenge_es['id']}")
    print(f"Título: {challenge_es['title']}")
    print(f"Categoría: {challenge_es['category']}")
    print(f"Dificultad: {challenge_es['difficulty']}")
    print(f"Descripción: {challenge_es['description'][:100]}...")
    
    # Buscar el mismo desafío en ambos idiomas
    print("\n3. PROBANDO MISMO DESAFÍO EN AMBOS IDIOMAS (ID=1)")
    print("-" * 80)
    
    challenges_en = gen_en.challenges
    challenges_es = gen_es.challenges
    
    challenge_1_en = next(c for c in challenges_en if c['id'] == 1)
    challenge_1_es = next(c for c in challenges_es if c['id'] == 1)
    
    print("\nINGLÉS:")
    print(f"  Título: {challenge_1_en['title']}")
    print(f"  Categoría: {challenge_1_en['category']}")
    print(f"  Descripción: {challenge_1_en['description']}")
    
    print("\nESPAÑOL:")
    print(f"  Título: {challenge_1_es['title']}")
    print(f"  Categoría: {challenge_1_es['category']}")
    print(f"  Descripción: {challenge_1_es['description']}")
    
    # Probar cambio de idioma
    print("\n4. PROBANDO CAMBIO DE IDIOMA")
    print("-" * 80)
    gen = ChallengeGenerator('en')
    print(f"Idioma inicial: en")
    print(f"Total de desafíos: {len(gen.challenges)}")
    print(f"Primer desafío: {gen.challenges[0]['title']}")
    
    gen.set_language('es')
    print(f"\nIdioma cambiado a: es")
    print(f"Total de desafíos: {len(gen.challenges)}")
    print(f"Primer desafío: {gen.challenges[0]['title']}")
    
    # Probar filtrado por categoría
    print("\n5. PROBANDO FILTRADO POR CATEGORÍA EN ESPAÑOL")
    print("-" * 80)
    gen_es = ChallengeGenerator('es')
    math_challenges = gen_es.filter_by_category('matemáticas')
    print(f"Desafíos de matemáticas: {len(math_challenges)}")
    print("Primeros 3:")
    for i, ch in enumerate(math_challenges[:3], 1):
        print(f"  {i}. {ch['title']} ({ch['difficulty']})")
    
    # Probar filtrado por dificultad
    print("\n6. PROBANDO FILTRADO POR DIFICULTAD EN ESPAÑOL")
    print("-" * 80)
    easy_challenges = gen_es.filter_by_difficulty('easy')
    print(f"Desafíos fáciles: {len(easy_challenges)}")
    print("Primeros 3:")
    for i, ch in enumerate(easy_challenges[:3], 1):
        print(f"  {i}. {ch['title']} - {ch['category']}")
    
    # Estadísticas
    print("\n7. ESTADÍSTICAS EN ESPAÑOL")
    print("-" * 80)
    stats = gen_es.get_statistics()
    print(f"Total de desafíos: {stats['total_challenges']}")
    print("\nPor dificultad:")
    for diff, count in sorted(stats['by_difficulty'].items()):
        print(f"  {diff}: {count}")
    print("\nPor categoría:")
    for cat, count in sorted(stats['by_category'].items()):
        print(f"  {cat}: {count}")
    
    print("\n" + "=" * 80)
    print("✅ TODAS LAS PRUEBAS COMPLETADAS EXITOSAMENTE")
    print("=" * 80)

if __name__ == "__main__":
    test_bilingual_system()
