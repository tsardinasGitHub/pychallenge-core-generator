"""
Challenge Core Package

This package contains the main logic for generating and selecting programming challenges.
"""

from .generator import ChallengeGenerator
from .data import CHALLENGES_DB, get_categories, get_difficulties
from .language import language_manager

__all__ = ['ChallengeGenerator', 'CHALLENGES_DB', 'get_categories', 'get_difficulties', 'language_manager']