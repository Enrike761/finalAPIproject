def calcular_fuerza_un_pokemon(df, nombre_pokemon):
    pokemon = df[df['name'].str.lower() == nombre_pokemon.lower()]
    

    pokemon['puntuacion'] = (
        pokemon['hp'] * 1 + 
        pokemon['defense'] * 1 + 
        pokemon['attack'] * 1.3 + 
        pokemon['special-attack'] * 1.3 + 
        pokemon['special-defense'] * 1 +
        pokemon['speed'] * 1.5
    )
    
    return pokemon[['name', 'puntuacion']]


def strongest_pokemon(df):
    df['puntuacion'] = (
        df['hp'] * 1 + 
        df['defense'] * 1 + 
        df['attack'] * 1.3 + 
        df['special-attack'] * 1.3 + 
        df['special-defense'] * 1 +
        df['speed'] * 1.5
    )
    return df.nlargest(10, 'puntuacion') #nlargest(n, column) devuelve un DataFrame que contiene las n filas con los valores más altos de la columna especificada (column).

pokemon_mas_fuerte = strongest_pokemon(concat_df)

print(pokemon_mas_fuerte) #mewtwo is the strongest pokemon with a punctuation of 842, followed by ho-oh, lugia, dragonite and mew