def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def get_positive_integer(prompt):
    # Get and validate a positive integer from user input
    while True:
        try:
            value = input(prompt).strip()
            
            # Check if input is empty
            if not value:
                print("Error: Please enter a number.")
                continue
            
            # Convert to integer
            num = int(value)
            
            # Check if positive
            if num <= 0:
                print("Error: Please enter a positive integer (greater than 0).")
                continue
            
            return num
            
        except ValueError:
            print("Error: Please enter a valid integer.")
        except Exception as e:
            print(f"Error: An unexpected error occurred: {e}")

def find_primes_in_range(start, end):
    # Find all prime numbers in the given range (inclusive)
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def display_primes(primes, start, end):
    # Display primes in formatted output (10 per line)
    if not primes:
        print(f"\nNo prime numbers found in the range {start} to {end}.")
        return
    
    print(f"\nPrime numbers between {start} and {end}:")
    print("-" * 50)
    
    # Display 10 numbers per line
    for i, prime in enumerate(primes):
        if i % 10 == 0 and i > 0:
            print()  # New line after every 10 numbers
        print(f"{prime:4d}", end=" ")
    
    print()  # Final newline
    print(f"\nTotal prime numbers found: {len(primes)}")

def main():
    print("Prime Number Finder")
    print("=" * 30)
    
    try:
        # Get range start
        start = get_positive_integer("Enter the start of range: ")
        
        # Get range end
        end = get_positive_integer("Enter the end of range: ")
        
        # Validate that start <= end
        if start > end:
            print("Error: Start value cannot be greater than end value.")
            return
        
        # Find primes in the range
        primes = find_primes_in_range(start, end)
        
        # Display results
        display_primes(primes, start, end)
        
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user.")
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()