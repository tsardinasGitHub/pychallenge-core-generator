"""
Multilanguage Support for Challenge Generator

This module handles translations and language management for the application.
"""

import os


class LanguageManager:
    """Manages language translations and settings."""
    
    def __init__(self):
        self.current_language = "en"  # Default to English
        self.translations = {
            "en": {
                # Menu and Navigation
                "welcome_title": "🚀 PROGRAMMING CHALLENGE GENERATOR 🚀",
                "welcome_message": "🚀 Welcome to the Programming Challenge Generator!",
                "welcome_subtitle": "💡 Improve your skills with challenges designed for learning.",
                "choose_option": "👉 Choose an option: ",
                "press_enter": "⏸️  Press Enter to continue...",
                "goodbye": "👋 See you later!",
                "thanks_message": "👋 Thanks for using the Challenge Generator!",
                "keep_practicing": "💪 Keep practicing and improving your skills!",
                
                # Menu Options
                "menu_random": "1. 🎲 Get random challenge",
                "menu_difficulty": "2. 📊 Filter by difficulty",
                "menu_category": "3. 📂 Filter by category",
                "menu_search": "4. 🔍 Search specific challenge",
                "menu_statistics": "5. 📈 View statistics",
                "menu_language": "6. 🌐 Change language",
                "menu_help": "7. ❓ Help",
                "menu_exit": "0. 👋 Exit",
                
                # Challenge Display
                "challenge_title": "🎯 CHALLENGE: ",
                "description": "📝 Description: ",
                "difficulty": "🔥 Difficulty: ",
                "category": "📂 Category: ",
                "points": "⭐ Points: ",
                "example_input": "📥 Example input: ",
                "example_output": "📤 Example output: ",
                "hints": "💡 Hints:",
                "challenge_not_found": "❌ Challenge not found.",
                
                # Difficulty Levels
                "easy": "Easy",
                "medium": "Medium", 
                "hard": "Hard",
                
                # Filtering Options
                "available_difficulties": "🔥 Available difficulties:",
                "available_categories": "📂 Available categories:",
                "select_difficulty": "Select a difficulty (number): ",
                "select_category": "Select a category (number): ",
                "challenges_with_difficulty": "📋 Challenges with '{}' difficulty:",
                "challenges_in_category": "📋 Challenges in '{}' category:",
                "which_challenge": "Which challenge do you want to see? (number): ",
                "no_challenges_difficulty": "❌ No challenges with '{}' difficulty.",
                "no_challenges_category": "❌ No challenges in '{}' category.",
                
                # Search
                "enter_title": "🔍 Enter the title of the challenge to search: ",
                "enter_valid_title": "❌ Please enter a valid title.",
                
                # Statistics
                "statistics_title": "📈 DATABASE STATISTICS",
                "total_challenges": "📊 Total challenges: ",
                "by_difficulty": "🔥 By difficulty:",
                "by_category": "📂 By category:",
                
                # Language Selection
                "language_title": "🌐 LANGUAGE SELECTION",
                "current_language": "Current language: ",
                "select_language": "Select a language (number): ",
                "language_changed": "✅ Language changed successfully!",
                
                # Help
                "help_title": "❓ HELP - HOW TO USE THE GENERATOR",
                "help_random": "🎲 Random challenge: Get a random challenge to practice",
                "help_difficulty": "📊 Filter by difficulty: Choose challenges by your level",
                "help_difficulty_easy": "   • Easy: For beginners",
                "help_difficulty_medium": "   • Medium: For intermediate level",
                "help_difficulty_hard": "   • Hard: For advanced programmers",
                "help_category": "📂 Filter by category: Practice specific topics",
                "help_search": "🔍 Search specific: Find a challenge by its name",
                "help_statistics": "📈 View statistics: See what's available",
                "help_language": "🌐 Change language: Switch between English and Spanish",
                
                # Error Messages
                "invalid_option": "❌ Invalid option. Please choose a number from 0 to 7.",
                "invalid_number": "❌ Invalid number.",
                "enter_valid_number": "❌ Please enter a valid number.",
                "error_occurred": "❌ An error occurred: {}",
                "please_try_again": "🔧 Please try again.",
                "generating_random": "🎲 Generating random challenge...",
                
                # Difficulty Names (for display)
                "not_specified": "Not specified"
            },
            
            "es": {
                # Menú y Navegación
                "welcome_title": "🚀 GENERADOR DE DESAFÍOS DE PROGRAMACIÓN 🚀",
                "welcome_message": "🚀 ¡Bienvenido al Generador de Desafíos de Programación!",
                "welcome_subtitle": "💡 Perfecciona tus habilidades con desafíos diseñados para aprender.",
                "choose_option": "👉 Elige una opción: ",
                "press_enter": "⏸️  Presiona Enter para continuar...",
                "goodbye": "👋 ¡Hasta luego!",
                "thanks_message": "👋 ¡Gracias por usar el Generador de Desafíos!",
                "keep_practicing": "💪 ¡Sigue practicando y mejorando tus habilidades!",
                
                # Opciones del Menú
                "menu_random": "1. 🎲 Obtener desafío aleatorio",
                "menu_difficulty": "2. 📊 Filtrar por dificultad",
                "menu_category": "3. 📂 Filtrar por categoría",
                "menu_search": "4. 🔍 Buscar desafío específico",
                "menu_statistics": "5. 📈 Ver estadísticas",
                "menu_language": "6. 🌐 Cambiar idioma",
                "menu_help": "7. ❓ Ayuda",
                "menu_exit": "0. 👋 Salir",
                
                # Mostrar Desafío
                "challenge_title": "🎯 DESAFÍO: ",
                "description": "📝 Descripción: ",
                "difficulty": "🔥 Dificultad: ",
                "category": "📂 Categoría: ",
                "points": "⭐ Puntos: ",
                "example_input": "📥 Ejemplo entrada: ",
                "example_output": "📤 Ejemplo salida: ",
                "hints": "💡 Pistas:",
                "challenge_not_found": "❌ Desafío no encontrado.",
                
                # Niveles de Dificultad
                "easy": "Fácil",
                "medium": "Medio",
                "hard": "Difícil",
                
                # Opciones de Filtrado
                "available_difficulties": "🔥 Dificultades disponibles:",
                "available_categories": "📂 Categorías disponibles:",
                "select_difficulty": "Selecciona una dificultad (número): ",
                "select_category": "Selecciona una categoría (número): ",
                "challenges_with_difficulty": "📋 Desafíos de dificultad '{}':",
                "challenges_in_category": "📋 Desafíos en la categoría '{}':",
                "which_challenge": "¿Cuál desafío quieres ver? (número): ",
                "no_challenges_difficulty": "❌ No hay desafíos de dificultad '{}'.",
                "no_challenges_category": "❌ No hay desafíos en la categoría '{}'.",
                
                # Búsqueda
                "enter_title": "🔍 Ingresa el título del desafío a buscar: ",
                "enter_valid_title": "❌ Por favor ingresa un título válido.",
                
                # Estadísticas
                "statistics_title": "📈 ESTADÍSTICAS DE LA BASE DE DATOS",
                "total_challenges": "📊 Total de desafíos: ",
                "by_difficulty": "🔥 Por dificultad:",
                "by_category": "📂 Por categoría:",
                
                # Selección de Idioma
                "language_title": "🌐 SELECCIÓN DE IDIOMA",
                "current_language": "Idioma actual: ",
                "select_language": "Selecciona un idioma (número): ",
                "language_changed": "✅ ¡Idioma cambiado exitosamente!",
                
                # Ayuda
                "help_title": "❓ AYUDA - CÓMO USAR EL GENERADOR",
                "help_random": "🎲 Desafío aleatorio: Obtén un desafío al azar para practicar",
                "help_difficulty": "📊 Filtrar por dificultad: Elige desafíos según tu nivel",
                "help_difficulty_easy": "   • Fácil: Para principiantes",
                "help_difficulty_medium": "   • Medio: Para nivel intermedio",
                "help_difficulty_hard": "   • Difícil: Para programadores avanzados",
                "help_category": "📂 Filtrar por categoría: Practica temas específicos",
                "help_search": "🔍 Buscar específico: Encuentra un desafío por su nombre",
                "help_statistics": "📈 Ver estadísticas: Conoce qué hay disponible",
                "help_language": "🌐 Cambiar idioma: Alterna entre inglés y español",
                
                # Mensajes de Error
                "invalid_option": "❌ Opción no válida. Por favor elige un número del 0 al 7.",
                "invalid_number": "❌ Número inválido.",
                "enter_valid_number": "❌ Por favor ingresa un número válido.",
                "error_occurred": "❌ Ocurrió un error: {}",
                "please_try_again": "🔧 Por favor intenta nuevamente.",
                "generating_random": "🎲 Generando desafío aleatorio...",
                
                # Nombres de Dificultad (para mostrar)
                "not_specified": "No especificada"
            }
        }
    
    def set_language(self, language_code):
        """Set the current language."""
        if language_code in self.translations:
            self.current_language = language_code
            return True
        return False
    
    def get_text(self, key):
        """Get translated text for the current language."""
        return self.translations[self.current_language].get(key, key)
    
    def get_available_languages(self):
        """Get list of available languages."""
        return {
            "en": "English",
            "es": "Español"
        }
    
    def get_difficulty_translation(self, difficulty):
        """Get translated difficulty level."""
        difficulty_map = {
            "easy": self.get_text("easy"),
            "medium": self.get_text("medium"),
            "hard": self.get_text("hard")
        }
        return difficulty_map.get(difficulty.lower(), difficulty.title())


# Global language manager instance
language_manager = LanguageManager()