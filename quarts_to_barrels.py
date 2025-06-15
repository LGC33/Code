# Convert quarts to barrels and ounces

QUARTS_PER_BARREL = 168
OUNCES_PER_QUART = 32

def main() -> None:
    total_quarts = int(input("Enter number of quarts: "))
    barrels = total_quarts // QUARTS_PER_BARREL
    remaining_quarts = total_quarts % QUARTS_PER_BARREL
    total_ounces = total_quarts * OUNCES_PER_QUART

    print(f"{total_quarts} quarts is {barrels} barrel(s) and {remaining_quarts} quart(s).")
    print(f"That's {total_ounces} ounces.")

if __name__ == "__main__":
    main()
