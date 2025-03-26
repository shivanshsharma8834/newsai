import ast
import json

data = "['https://www.gamingbible.com/news/platform/playstation/playstation-6-first-game-roasted-969641-20250320', 'https://nypost.com/2025/03/24/sports/death-of-yankees-star-brett-gardners-youngest-son-miller-under-investigation-state-dept-confirms/', 'https://cointelegraph.com/news/nvidia-stock-price-death-cross-ai-crypto-tokens-next-to-follow', 'https://people.com/brett-gardner-14-year-old-son-miller-gardner-cause-of-death-revealed-11702137', 'https://www.aljazeera.com/news/2025/3/25/japan-grants-1-4m-to-record-breaking-death-row-inmate']"

list_data = ast.literal_eval(data)
print(list_data, type(list_data))
