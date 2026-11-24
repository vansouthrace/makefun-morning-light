import os

ENTRY = 'Dawn pours through the blinds,\nand the dust turns to gold on its way down.'


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
