def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")

    reversed_list = fruit_list.reverse()
    print(f"reversed: {reversed_list}")
    
    fruit_list.append("orange")
    print(f"appended: {fruit_list}")
    
    fruit_list.insert(fruit_list.index("apple"), "cherry")
    print(f"added cherry: {fruit_list}")
    
    fruit_list.remove("banana")
    print(f"removed banana: {fruit_list}")
    
    popped_item = fruit_list.pop()
    print(f"popped item: {popped_item}")
    print(f"new list: {fruit_list}")
    
    fruit_list.sort()
    print(f"sorted list: {fruit_list}")
    
    fruit_list.clear()
    print(f"cleared list: {fruit_list}")

main()