from selenium import webdriver
from datetime import datetime


def crawling_top_apps(
    web_driver,
    category: str = '',
    paid: str = '',
    limit: int = 10
):
    category_url = f'/category/{category}'
    free_app_rank_url = f'https://play.google.com/store/apps/category/GAME{category_url}' \
                        f'/collection/topselling_{paid}'

    web_driver.get(free_app_rank_url)
    top_app_details = web_driver.find_elements_by_class_name('details')

    for idx, app in enumerate(top_app_details[:limit]):
        content = app.text.split('. ')[-1]

        app_title = content.split('\n')[0]
        corp = content.split('\n')[-1]

        print(f'{idx + 1}위 {app_title} - {corp}')


if __name__ == '__main__':
    top_n = 10
    categories = [
        'HEALTH_AND_FITNESS',
        'FINANCE',
        'SHOPPING'
    ]
    paid = 'free'

    driver = webdriver.Chrome('C:/chromedriver')

    today = datetime.now().strftime('%Y-%m-%d')

    for category in categories:
        print('-' * 60)
        print(f'{today} Top {top_n} {paid} Apps in {category}')
        print('-' * 60)
        crawling_top_apps(driver, category, paid, top_n)