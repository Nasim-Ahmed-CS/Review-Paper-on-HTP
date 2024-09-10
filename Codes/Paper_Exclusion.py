import pandas as pd
import re

def count_occurrences(column, pattern):
    regex_pattern = '|'.join(pattern)
    return column.str.contains(regex_pattern, case=False, na=False).sum()

def main():
    try:
        data = pd.read_csv('Full.csv')
    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")
        return
    except pd.errors.EmptyDataError:
        print("File is empty. Please provide a valid CSV file.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return
    
    patterns = {
        'Review': ['review'],
        'Survey': ['survey'],
        'Meta Analysis': ['meta[- ]analysis'],
        'Case Study': ['case[- ]study'],
        'Pilot Study': ['pilot[- ]study']
    }
    
    results = {}
    
    for key, pattern in patterns.items():
        results[key] = count_occurrences(data['Title'], pattern)
    
    for key, count in results.items():
        print(f'{key}: {count}')

if __name__ == "__main__":
    main()
