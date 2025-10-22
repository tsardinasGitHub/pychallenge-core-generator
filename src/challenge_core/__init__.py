"""
Challenge Core Package

This package contains the main logic for generating and selecting programming challenges.
"""

from .generator import ChallengeGenerator
from .data import CHALLENGES_DB
from .language import language_manager

__all__ = ['ChallengeGenerator', 'CHALLENGES_DB', 'language_manager']