import requests
import pandas as pd
import matplotlib.pyplot as plt

def get_top_packages(limit=5):
    url = f"https://hugovk.github.io/top-pypi-packages/top-pypi-packages-30-days.json"
    response = requests.get(url)
    data = response.json()
    top_packages = {i+1: int(package['download_count'])
                    for i, package in enumerate(data['rows'][:limit])}
    return top_packages

def get_package_name(rank, downloads):
    url = f"https://hugovk.github.io/top-pypi-packages/top-pypi-packages-30-days.json"
    response = requests.get(url)
    data = response.json()
    for package in data['rows']:
        if int(package['download_count']) == downloads:
            return package['project']
    return f"Пакет {rank}"

def create_dataframe(packages, names):
    df = pd.DataFrame({
        'Ранг': packages.keys(),
        'Название': names.values(),
        'Загрузки': packages.values()
    })
    return df

def visualize_pypi_packages(df):
    plt.figure(figsize=(12, 6))
    plt.bar(df['Название'], df['Загрузки'] / 1_000_000, color='green')
    plt.title('Топ-5 самых популярных пакетов PyPI')
    plt.xlabel('Пакеты')
    plt.ylabel('Миллионы загрузок')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def main():
    top_5_packages = get_top_packages(5)
    print("Топ-5 пакетов по загрузкам:", top_5_packages)

    package_names = {rank: get_package_name(rank, downloads)
                     for rank, downloads in top_5_packages.items()}
    print("Названия пакетов:", package_names)

    df = create_dataframe(top_5_packages, package_names)
    print(df)

    visualize_pypi_packages(df)

if __name__ == "__main__":
    main()
