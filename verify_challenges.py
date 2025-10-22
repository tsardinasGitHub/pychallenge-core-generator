#!/usr/bin/env python3
"""
Challenge Database Verification Script
Verifies that all challenges are properly distributed
"""

from src.challenge_core import ChallengeGenerator, CHALLENGES_DB, get_categories

def verify_database():
    """Verify challenge database integrity"""
    print("🔍" + "="*60 + "🔍")
    print("   CHALLENGE DATABASE VERIFICATION")
    print("🔍" + "="*60 + "🔍")
    print()
    
    gen = ChallengeGenerator()
    stats = gen.get_statistics()
    
    # Total count
    print(f"📊 Total Challenges: {stats['total_challenges']}")
    print()
    
    # Difficulty distribution
    print("🔥 Difficulty Distribution:")
    for diff, count in stats['by_difficulty'].items():
        print(f"   {diff.capitalize()}: {count}")
    print()
    
    # Category distribution
    print("📂 Category Distribution:")
    categories = get_categories()
    all_valid = True
    
    for category in categories:
        cat_challenges = gen.filter_by_category(category)
        easy = [c for c in cat_challenges if c['difficulty'] == 'easy']
        medium = [c for c in cat_challenges if c['difficulty'] == 'medium']
        hard = [c for c in cat_challenges if c['difficulty'] == 'hard']
        
        total = len(cat_challenges)
        status = "✅" if total == 15 else "❌"
        
        print(f"   {status} {category.title()}: {total} total")
        print(f"      Easy: {len(easy)}, Medium: {len(medium)}, Hard: {len(hard)}")
        
        if total != 15 or len(easy) != 5 or len(medium) != 5 or len(hard) != 5:
            all_valid = False
    
    print()
    
    # Verify unique IDs
    ids = [c['id'] for c in CHALLENGES_DB]
    unique_ids = set(ids)
    
    print(f"🔑 ID Verification:")
    print(f"   Total IDs: {len(ids)}")
    print(f"   Unique IDs: {len(unique_ids)}")
    
    if len(ids) == len(unique_ids):
        print(f"   ✅ All IDs are unique!")
    else:
        print(f"   ❌ Duplicate IDs found!")
        all_valid = False
    
    print()
    
    # Final verdict
    print("="*62)
    if all_valid and stats['total_challenges'] == 165:
        print("✅ DATABASE VERIFICATION PASSED!")
        print("   All 165 challenges are properly distributed:")
        print("   - 11 categories × 15 challenges each")
        print("   - 55 easy + 55 medium + 55 hard")
        print("   - Perfect balance achieved!")
    else:
        print("❌ DATABASE VERIFICATION FAILED!")
        print("   Please check the distribution above.")
    print("="*62)

if __name__ == "__main__":
    verify_database()
