def min_max_finder():
    print("=== Min–Max Finder ===")
    
    # Take input from user
    user_input = input("Enter numbers separated by spaces: ")
    
    # Convert to list of integers
    try:
        numbers = list(map(int, user_input.split()))
    except ValueError:
        print("Error: Please enter only valid integers.")
        return
    
    if not numbers:
        print("Error: The list is empty.")
        return

    # Calculate min, max, and range
    minimum = min(numbers)
    maximum = max(numbers)
    num_range = maximum - minimum

    # Get indices
    min_index = numbers.index(minimum)
    max_index = numbers.index(maximum)

    # Display results
    print("\n--- Results ---")
    print(f"Input List: {numbers}")
    print(f"Minimum Value: {minimum} (Index: {min_index})")
    print(f"Maximum Value: {maximum} (Index: {max_index})")
    print(f"Range (max - min): {num_range}")

# Run the program
min_max_finder()
