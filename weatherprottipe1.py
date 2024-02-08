import requests
import json

# JSONファイルを読み込む。検証ツールで取得した天気コード
weather_code_file_path = "weathercode.json"
with open(weather_code_file_path, encoding="utf-8") as f:
    weather_codes = json.load(f)

url = "https://www.jma.go.jp/bosai/forecast/data/forecast/110000.json"

def get_weather_info(code):
    """天気コードに基づいて説明とアイコンファイル名を取得します。"""
    code_str = str(code)
    default_value = {"description": "不明な天気コード", "icon": "unknown.png"}
    return weather_codes.get(code_str, default_value)

def get_weather_forecast():
    response = requests.get(url)
    data = response.json()

    # HTMLコンテンツの開始部分
    html_content = """
    <!DOCTYPE html>
    <html lang="ja">
    <head>
        <meta charset="UTF-8">
        <title>天気予報ビューア</title>
    </head>
    <body>
        <h1>天気予報</h1>
    """

    for item in data:
        for series in item["timeSeries"]:
            if "areas" in series:
                for area in series["areas"]:
                    html_content += f"<h2>----{area['area']['name']}----</h2>"
                    if "weatherCodes" in area:
                        for i, code in enumerate(area["weatherCodes"]):
                            weather_info = get_weather_info(code)
                            html_content += f"<p>{series['timeDefines'][i]}: {weather_info['description']} (アイコン: <img src='{weather_info['icon']}' alt='{weather_info['description']}' style='width: 50px;'>)</p>"
    
    # HTMLコンテンツの終了部分
    html_content += """
    </body>
    </html>
    """

    # HTMLファイルとして保存
    with open("weather_forecast.html", "w", encoding="utf-8") as file:
        file.write(html_content)

get_weather_forecast()
