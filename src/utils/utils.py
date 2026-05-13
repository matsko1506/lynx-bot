import discord

def read_file(filename):
    with open(filename, encoding="utf-8") as file:
        lines = file.readlines()
    return lines

def format_weather_message(data, arg):
    print(f"{data}")
    current = data['current_weather']
    temp_now = current['temperature']
    wind_now = current['windspeed']
    daily = data['daily']
    temp_max = daily['temperature_2m_max'][0]
    temp_min = daily['temperature_2m_min'][0]
    uv_today = daily['uv_index_max'][0]
    rain_chance = daily['precipitation_probability_max'][0]

    if temp_now < 10:
        embed_color = discord.Color.blue()
    elif temp_now > 25:
        embed_color = discord.Color.red()
    else:
        embed_color = discord.Color.green()

    embed = discord.Embed(
        title=f"WEATHER FORECAST FOR {arg}",
        color=embed_color
    )

    embed.add_field(name="[TEMP]:", value=f"{temp_now}°C", inline=True)
    embed.add_field(name="[TEMP RANGE]:", value=f"{temp_min}-{temp_max}°C", inline=True)
    embed.add_field(name="[WIND]:", value=f"{wind_now}km/h", inline=True)
    embed.add_field(name="[RAIN PROBABILITY]:", value=f"{rain_chance}%", inline=True)
    embed.add_field(name="[UV INDEX]:", value=f"{uv_today}", inline=True)

    return embed