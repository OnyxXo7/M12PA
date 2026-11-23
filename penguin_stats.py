# penguin_stats.py
# Sergio Sasso
# 11/15/2026
# Functions for calculating and classifying penguin statistics

def calculate_percentage(count, total):
    return count / total * 100

def classify_species(percent):
    if percent < 25:
        return "small"
    elif percent >= 25 and percent < 40:
        return "medium"
    else:
        return "large"

def get_position_description(selected_species, largest_species, smallest_species):
    if selected_species == largest_species:
        return "largest"
    elif selected_species == smallest_species:
        return "smallest"
    else:
        return "middle-sized"
