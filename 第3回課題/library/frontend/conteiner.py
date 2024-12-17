import flet as ft

def create_weather_card(date, area_name, weather, weather_image_url, wind, wave):
    # 波高を表示する行
    wave_row = None
    if wave != 0:
        wave_row = ft.Row(
            [
                ft.Text("波高", size=12),
                ft.Text(str(wave), size=12),  # 数値を文字列に変換
            ],
            alignment="center",
        )

    # コンテンツを動的に作成し、None を除外
    content_items = [
        ft.Text(date, size=14, weight="bold"),
        ft.Text(area_name, size=12, color=ft.colors.GREY),
        ft.Image(src=weather_image_url, width=50, height=50, fit=ft.ImageFit.CONTAIN),
        ft.Text(weather, size=12),
        ft.Text(wind, size=12),
        make_yazirushi(wind),
    ]

    # wave_row が None でない場合のみ追加
    if wave_row is not None:
        content_items.append(wave_row)

    return ft.Container(
        content=ft.Column(
            content_items,  # 動的に作成したリストを使用
            alignment="center",
            horizontal_alignment="center",
        ),
        width=120,
        height=300,
        border=ft.border.all(1, ft.colors.GREY),
        border_radius=ft.border_radius.all(10),
        padding=10,
    )


def generate_weather_cards(data):
    cards = []
    for key, weather_info in data.items():
        # 天気コードが存在する場合のみカードを生成
        try:
            if weather_info["weather_code"]:
                date = weather_info["day"]
                area_name = weather_info["area_name"]
                weather = weather_data[weather_info["weather_code"]]["short_name"]
                weather_image_url = create_link(weather_info["weather_code"],weather_info["Time"])
                # アイコンURL生成
                wind = weather_info["wind"].split("の")[0]
                try:
                    wave = weather_info["wave"].split(" 後")[0]
                except:
                    wave = 0
                cards.append(create_weather_card(date, area_name, weather, weather_image_url, wind, wave))
        except:
            pass
    return cards