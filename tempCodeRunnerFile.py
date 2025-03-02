        if orientation == -1:  
                print("Ship has no orientation")
                
                if len(ship_position) > 2:  # Ensure that there are at least 3 elements in ship_position
                    ai_col_guess = ship_position[1 + 1]  # Access the third element if available
                else:
                    # If ship_position doesn't have enough elements, handle the situation
                    ai_row_guess = ship_position[0]  # Default to the first element in ship_position
                    ai_col_guess = ship_position[1] if len(ship_position) > 1 else 0  # Default to 0 if there's only one element

                if is_ocean(ship_position[0] + 1, ship_position[1], ai_radar):
                    ai_row_guess = ship_position[0] + 1
                    ai_col_guess = ship_position[1]
                elif is_ocean(ship_position[0] - 1, ship_position[1], ai_radar):
                    ai_row_guess = ship_position[0] - 1
                    ai_col_guess = ship_position[1]
                elif is_ocean(ship_position[0], ship_position[1] - 1, ai_radar):
                    ai_row_guess = ship_position[0]
                    ai_col_guess = ship_position[1] - 1
                else:
                    ai_row_guess = randint(0, rows - 1)
                    ai_col_guess = randint(0, cols - 1)