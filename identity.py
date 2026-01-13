import psutil

def get_logged_in_users():
    # psutil.users() returns a list of named tuples
    users = psutil.users()
    
    # Get the count
    user_count = len(users)
    
    print(f"--- System User Report ---")
    print(f"Total users currently logged in: {user_count}")
    print("-" * 26)
    
    if user_count > 0:
        print(f"{'Username':<15} {'Terminal':<12} {'Host':<15}")
        for user in users:
            # Each user object has: name, terminal, host, started, and pid
            print(f"{user.name:<15} {user.terminal:<12} {user.host:<15}")
    else:
        print("No users detected.")

if __name__ == "__main__":
    get_logged_in_users()