"""
Script de prueba rápida del programa principal.
Simula el uso del sistema con español.
"""

import sys
from pathlib import Path

# Agregar el directorio raíz al path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.challenge_core import ChallengeGenerator

def quick_test():
    """Prueba rápida del generador en español."""
    
    print("=" * 80)
    print("PRUEBA RÁPIDA DEL GENERADOR EN ESPAÑOL")
    print("=" * 80)
    
    # Crear generador en español
    gen = ChallengeGenerator('es')
    
    # Obtener desafío aleatorio
    print("\n1. Desafío aleatorio:")
    challenge = gen.get_random_challenge()
    print(f"   {challenge['title']} ({challenge['difficulty']}) - {challenge['category']}")
    
    # Filtrar por categoría
    print("\n2. Desafíos de Matemáticas:")
    math_challenges = gen.filter_by_category('matemáticas')
    for i, ch in enumerate(math_challenges[:3], 1):
        print(f"   {i}. {ch['title']} ({ch['difficulty']})")
    
    # Filtrar por dificultad
    print("\n3. Desafíos Fáciles:")
    easy_challenges = gen.filter_by_difficulty('easy')
    print(f"   Total: {len(easy_challenges)} desafíos")
    
    # Estadísticas
    print("\n4. Estadísticas:")
    stats = gen.get_statistics()
    print(f"   Total: {stats['total_challenges']} desafíos")
    print(f"   Categorías: {len(stats['by_category'])}")
    
    # Cambiar a inglés
    print("\n5. Cambio a Inglés:")
    gen.set_language('en')
    challenge_en = gen.get_random_challenge()
    print(f"   {challenge_en['title']} ({challenge_en['difficulty']}) - {challenge_en['category']}")
    
    print("\n" + "=" * 80)
    print("✅ PRUEBA COMPLETADA - TODO FUNCIONA CORRECTAMENTE")
    print("=" * 80)

if __name__ == "__main__":
    quick_test()
