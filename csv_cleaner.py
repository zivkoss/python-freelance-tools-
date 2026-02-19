import pandas as pd
import argparse
import sys

def clean_csv(input_file, output_file, sort_col="price"):
    try:
        df = pd.read_csv(input_file)
        df = df.dropna()
        df = df.drop_duplicates()
        df = df.sort_values(by=sort_col)
        df.to_csv(output_file, index=False)
        print(f"Готово! Обрађено {len(df)} редова. Излаз: {output_file}")
    except FileNotFoundError:
        print(f"Грешка: Не нађен фајл {input_file}")
        sys.exit(1)
    except KeyError:
        print(f"Грешка: Колона '{sort_col}' не постоји.")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CSV Cleaner алат")
    parser.add_argument("input", help="Улазни CSV фајл")
    parser.add_argument("-o", "--output", default="cleaned.csv", help="Излазни CSV фајл")
    parser.add_argument("-s", "--sort", default="price", help="Колона за сортирање")
    args = parser.parse_args()
    clean_csv(args.input, args.output, args.sort)
