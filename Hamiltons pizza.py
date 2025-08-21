

#Author :Larry Grace    due :1/29/2017
#Assignment: program 1
#Hamilton's pizza
# Algorithm
# 1. How many pizzas where sold, what size were they, how many ingredients were used used
# 2. Calculate the ingredients
# 3. Output result


# Small # pizza
small_pizza = int(input ("How many small pizzas were ordered?== >"))
small_mozzarealla = 0.75
small_sauce = 0.33

# medium # pizza 
medium_pizza = int(input ("How many medium pizzas were ordered?== >"))
medium_mozzarealla = 0.5
medium_sauce = 0.5

# large # pizza
large_pizza = int(input ("How many large pizzas were ordered?== >"))
large_mozzarealla =0.7
large_sauce= 0.66

# Calculate number of ingredients
pounds_of_dough = small_pizza + medium_pizza +large_pizza+1
pounds_of_mozzarella = small_mozzarealla *small_pizza + medium_mozzarealla * \
                       medium_pizza + large_mozzarealla * large_pizza
cups_of_sauce =small_sauce * small_pizza + medium_sauce * medium_sauce\
                + large_sauce * large_sauce


# output
print()
print("You have used",\
      pounds_of_dough,"lbs of dough",pounds_of_mozzarella,\
      "lbs_of_mozzarella",cups_of_sauce,"cups_of_sauce")
