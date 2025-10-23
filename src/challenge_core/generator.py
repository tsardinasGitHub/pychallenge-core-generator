"""
Challenge Generator

This module contains the main logic for selecting and filtering programming challenges.
"""

import random
from typing import List, Dict, Any, Optional
from .data import get_challenges_db


class ChallengeGenerator:
    """
    Main class for generating challenges based on different criteria.
    """
    
    def __init__(self, language: str = 'en'):
        """
        Initialize the generator with the challenges database.
        
        Args:
            language (str): Language code ('en' for English, 'es' for Spanish).
        """
        self.language = language
        self.challenges = get_challenges_db(language)
    
    def set_language(self, language: str):
        """
        Change the language and reload the challenges database.
        
        Args:
            language (str): Language code ('en' or 'es').
        """
        self.language = language
        self.challenges = get_challenges_db(language)
    
    def get_random_challenge(self) -> Dict[str, Any]:
        """
        Get a random challenge from the database.
        
        Returns:
            Dict[str, Any]: A randomly selected challenge.
        """
        return random.choice(self.challenges)
    
    def filter_by_difficulty(self, difficulty: str) -> List[Dict[str, Any]]:
        """
        Filter challenges by difficulty level.
        
        Args:
            difficulty (str): Difficulty level ('easy', 'medium', 'hard')
            
        Returns:
            List[Dict[str, Any]]: List of challenges filtered by difficulty.
        """
        return [challenge for challenge in self.challenges 
                if challenge.get('difficulty', '').lower() == difficulty.lower()]
    
    def filter_by_category(self, category: str) -> List[Dict[str, Any]]:
        """
        Filter challenges by category.
        
        Args:
            category (str): Challenge category
            
        Returns:
            List[Dict[str, Any]]: List of challenges filtered by category.
        """
        return [challenge for challenge in self.challenges 
                if challenge.get('category', '').lower() == category.lower()]
    
    def search_challenge(self, title: str) -> Optional[Dict[str, Any]]:
        """
        Search for a specific challenge by title.
        
        Args:
            title (str): Title of the challenge to search for
            
        Returns:
            Optional[Dict[str, Any]]: The found challenge or None if it doesn't exist.
        """
        for challenge in self.challenges:
            if challenge.get('title', '').lower() == title.lower():
                return challenge
        return None
    
    def get_statistics(self) -> Dict[str, Any]:
        """
        Get statistics about the challenges database.
        
        Returns:
            Dict[str, Any]: Dictionary with statistics.
        """
        total = len(self.challenges)
        difficulties = {}
        categories = {}
        
        for challenge in self.challenges:
            # Count by difficulty
            diff = challenge.get('difficulty', 'Unclassified')
            difficulties[diff] = difficulties.get(diff, 0) + 1
            
            # Count by category
            cat = challenge.get('category', 'No category')
            categories[cat] = categories.get(cat, 0) + 1
        
        return {
            'total_challenges': total,
            'by_difficulty': difficulties,
            'by_category': categories
        }