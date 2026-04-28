import sys
try:
    import server
    print("SUCCESS")
except Exception as e:
    print(f"FAILED: {e}")
