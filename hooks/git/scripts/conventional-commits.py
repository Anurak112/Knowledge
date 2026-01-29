#!/usr/bin/env python3
import sys
import re

def validate_commit_message(msg):
    # Conventional Commits regex
    # type(scope): description
    pattern = r'^(feat|fix|docs|style|refactor|perf|test|chore|ci|build|revert)(\(.+\))?:\s.+'
    
    if not re.match(pattern, msg):
        print(f"❌ Invalid commit message format: {msg}")
        print("Expected format: type(scope): description")
        print("Types: feat, fix, docs, style, refactor, perf, test, chore, ci, build, revert")
        return False
    
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: conventional-commits.py <commit_message_file>")
        sys.exit(1)
        
    msg_file = sys.argv[1]
    with open(msg_file, 'r') as f:
        msg = f.read().strip()
        
    if not validate_commit_message(msg):
        sys.exit(1)
        
    print("✅ Commit message valid")
    sys.exit(0)
