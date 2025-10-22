"""
Challenge Generator - Terminal Interface (CLI)

This is the main entry point for the application.
Provides a command line interface to interact with the challenge generator.
"""

import sys
import os

# Add the src directory to path to import challenge_core
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from challenge_core import ChallengeGenerator, language_manager
from challenge_core.data import get_categories, get_difficulties


def show_menu():
    """Display the main options menu."""
    print("\n" + "="*50)
    print("   " + language_manager.get_text("welcome_title"))
    print("="*50)
    print(language_manager.get_text("menu_random"))
    print(language_manager.get_text("menu_difficulty"))
    print(language_manager.get_text("menu_category"))
    print(language_manager.get_text("menu_search"))
    print(language_manager.get_text("menu_statistics"))
    print(language_manager.get_text("menu_language"))
    print(language_manager.get_text("menu_help"))
    print(language_manager.get_text("menu_exit"))
    print("="*50)


def show_challenge(challenge):
    """
    Display a challenge in formatted way.
    
    Args:
        challenge (dict): Dictionary with challenge information.
    """
    if not challenge:
        print(language_manager.get_text("challenge_not_found"))
        return
    
    print("\n" + "="*60)
    print(f"{language_manager.get_text('challenge_title')}{challenge.get('title', 'No title')}")
    print("="*60)
    print(f"{language_manager.get_text('description')}{challenge.get('description', 'No description')}")
    
    difficulty = challenge.get('difficulty', 'not_specified')
    translated_difficulty = language_manager.get_difficulty_translation(difficulty)
    print(f"{language_manager.get_text('difficulty')}{translated_difficulty}")
    
    print(f"{language_manager.get_text('category')}{challenge.get('category', language_manager.get_text('not_specified')).title()}")
    print(f"{language_manager.get_text('points')}{challenge.get('points', 0)}")
    print(f"{language_manager.get_text('example_input')}{challenge.get('example_input', 'Not available')}")
    print(f"{language_manager.get_text('example_output')}{challenge.get('example_output', 'Not available')}")
    
    hints = challenge.get('hints', [])
    if hints:
        print(f"\n{language_manager.get_text('hints')}")
        for i, hint in enumerate(hints, 1):
            print(f"   {i}. {hint}")
    
    print("="*60)


def filter_by_difficulty(generator):
    """Handle filtering by difficulty."""
    difficulties = get_difficulties()
    
    print(f"\n{language_manager.get_text('available_difficulties')}")
    for i, diff in enumerate(difficulties, 1):
        translated_diff = language_manager.get_difficulty_translation(diff)
        print(f"{i}. {translated_diff}")
    
    try:
        option = int(input(f"\n{language_manager.get_text('select_difficulty')}")) - 1
        if 0 <= option < len(difficulties):
            chosen_difficulty = difficulties[option]
            challenges = generator.filter_by_difficulty(chosen_difficulty)
            
            if challenges:
                translated_diff = language_manager.get_difficulty_translation(chosen_difficulty)
                print(f"\n{language_manager.get_text('challenges_with_difficulty').format(translated_diff)}")
                for i, challenge in enumerate(challenges, 1):
                    difficulty = challenge.get('difficulty', 'unknown')
                    translated_difficulty = language_manager.get_difficulty_translation(difficulty)
                    print(f"{i}. {challenge.get('title', 'No title')} ({translated_difficulty})")
                
                try:
                    selection = int(input(f"\n{language_manager.get_text('which_challenge')}")) - 1
                    if 0 <= selection < len(challenges):
                        show_challenge(challenges[selection])
                    else:
                        print(language_manager.get_text("invalid_number"))
                except ValueError:
                    print(language_manager.get_text("enter_valid_number"))
            else:
                translated_diff = language_manager.get_difficulty_translation(chosen_difficulty)
                print(language_manager.get_text("no_challenges_difficulty").format(translated_diff))
        else:
            print(language_manager.get_text("invalid_option"))
    except ValueError:
        print(language_manager.get_text("enter_valid_number"))


def filter_by_category(generator):
    """Handle filtering by category."""
    categories = get_categories()
    
    print(f"\n{language_manager.get_text('available_categories')}")
    for i, cat in enumerate(categories, 1):
        print(f"{i}. {cat.title()}")
    
    try:
        option = int(input(f"\n{language_manager.get_text('select_category')}")) - 1
        if 0 <= option < len(categories):
            chosen_category = categories[option]
            challenges = generator.filter_by_category(chosen_category)
            
            if challenges:
                print(f"\n{language_manager.get_text('challenges_in_category').format(chosen_category.title())}")
                for i, challenge in enumerate(challenges, 1):
                    difficulty = challenge.get('difficulty', 'unknown')
                    translated_difficulty = language_manager.get_difficulty_translation(difficulty)
                    print(f"{i}. {challenge.get('title', 'No title')} ({translated_difficulty})")
                
                try:
                    selection = int(input(f"\n{language_manager.get_text('which_challenge')}")) - 1
                    if 0 <= selection < len(challenges):
                        show_challenge(challenges[selection])
                    else:
                        print(language_manager.get_text("invalid_number"))
                except ValueError:
                    print(language_manager.get_text("enter_valid_number"))
            else:
                print(language_manager.get_text("no_challenges_category").format(chosen_category))
        else:
            print(language_manager.get_text("invalid_option"))
    except ValueError:
        print(language_manager.get_text("enter_valid_number"))


def search_specific_challenge(generator):
    """Handle searching for a specific challenge."""
    title = input(f"\n{language_manager.get_text('enter_title')}").strip()
    if title:
        challenge = generator.search_challenge(title)
        show_challenge(challenge)
    else:
        print(language_manager.get_text("enter_valid_title"))


def show_statistics(generator):
    """Display database statistics."""
    stats = generator.get_statistics()
    
    print("\n" + "="*40)
    print(language_manager.get_text("statistics_title"))
    print("="*40)
    print(f"{language_manager.get_text('total_challenges')}{stats['total_challenges']}")
    
    print(f"\n{language_manager.get_text('by_difficulty')}")
    for diff, count in stats['by_difficulty'].items():
        translated_diff = language_manager.get_difficulty_translation(diff)
        print(f"   {translated_diff}: {count}")
    
    print(f"\n{language_manager.get_text('by_category')}")
    for cat, count in stats['by_category'].items():
        print(f"   {cat.title()}: {count}")
    
    print("="*40)


def show_language_menu():
    """Show language selection menu."""
    languages = language_manager.get_available_languages()
    current_lang_name = languages[language_manager.current_language]
    
    print("\n" + "="*40)
    print(language_manager.get_text("language_title"))
    print("="*40)
    print(f"{language_manager.get_text('current_language')}{current_lang_name}")
    print()
    
    for i, (code, name) in enumerate(languages.items(), 1):
        print(f"{i}. {name}")
    
    try:
        option = int(input(f"\n{language_manager.get_text('select_language')}")) - 1
        lang_codes = list(languages.keys())
        if 0 <= option < len(lang_codes):
            new_lang = lang_codes[option]
            if language_manager.set_language(new_lang):
                print(f"\n{language_manager.get_text('language_changed')}")
            else:
                print(language_manager.get_text("invalid_option"))
        else:
            print(language_manager.get_text("invalid_option"))
    except ValueError:
        print(language_manager.get_text("enter_valid_number"))


def show_help():
    """Show help information."""
    print("\n" + "="*50)
    print(language_manager.get_text("help_title"))
    print("="*50)
    print(language_manager.get_text("help_random"))
    print(language_manager.get_text("help_difficulty"))
    print(language_manager.get_text("help_difficulty_easy"))
    print(language_manager.get_text("help_difficulty_medium"))
    print(language_manager.get_text("help_difficulty_hard"))
    print(language_manager.get_text("help_category"))
    print(language_manager.get_text("help_search"))
    print(language_manager.get_text("help_statistics"))
    print(language_manager.get_text("help_language"))
    print("="*50)


def main():
    """Main function that handles the program flow."""
    generator = ChallengeGenerator()
    
    print(language_manager.get_text("welcome_message"))
    print(language_manager.get_text("welcome_subtitle"))
    
    while True:
        try:
            show_menu()
            option = input(f"\n{language_manager.get_text('choose_option')}").strip()
            
            if option == "1":
                print(f"\n{language_manager.get_text('generating_random')}")
                challenge = generator.get_random_challenge()
                show_challenge(challenge)
            
            elif option == "2":
                filter_by_difficulty(generator)
            
            elif option == "3":
                filter_by_category(generator)
            
            elif option == "4":
                search_specific_challenge(generator)
            
            elif option == "5":
                show_statistics(generator)
            
            elif option == "6":
                show_language_menu()
            
            elif option == "7":
                show_help()
            
            elif option == "0":
                print(f"\n{language_manager.get_text('thanks_message')}")
                print(language_manager.get_text("keep_practicing"))
                break
            
            else:
                print(language_manager.get_text("invalid_option"))
            
            # Pause before continuing
            input(f"\n{language_manager.get_text('press_enter')}")
            
        except KeyboardInterrupt:
            print(f"\n\n{language_manager.get_text('goodbye')}")
            break
        except Exception as e:
            print(f"\n{language_manager.get_text('error_occurred').format(e)}")
            print(language_manager.get_text("please_try_again"))


if __name__ == "__main__":
    main()