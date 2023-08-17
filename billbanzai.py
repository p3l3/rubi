
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

# Configura el token de tu bot aquí
TOKEN = ''
bot = commands.Bot(command_prefix='!', intents=intents)

# Define el diccionario con las claves y valores
diccionario = {
    
    "Garou": [25, 15, 55, 24, 36],
    "Zerf": [30, 33, 34, 25, 52],
    "Sung": [25, 30, 20, 20, 20],
    "Ibai_Jr": [30, 30, 25, 20, 40],
    "leia": [20, 30, 20, 15, 17],
    "Akiro": [20, 22, 23, 11, 24],
    "Donquixote_Diego": [10, 20, 20, 20, 17],
    "Grimdor": [16, 21, 20, 23, 14],
    "Rafaelo": [12, 12, 12, 12, 20],
    "Marford": [12, 10, 19, 12, 10],
    "Tyron": [20, 20, 20, 13, 8],
    "Kai": [10, 10, 10, 10, 20],
    "Jack": [11, 10, 15, 10, 13],
    "Yuji": [12, 8, 8, 14, 12],
    "Capi": [11, 15, 15, 8, 8],
    "Lazaro": [8, 8, 8, 12, 13],
    "Gyro": [5, 15, 9, 6, 6],
    "Zero": [4, 10, 8, 13, 12],
    "John_Wick": [10, 10, 8, 9, 6],
    "Adan": [12, 10, 6, 5, 4],
    "Satoshi": [9, 6, 9, 7, 10],
    "Figarland_Janemba": [10, 6, 10, 10, 4],
    "Makoto": [10, 5, 5, 10, 10],
    "Illypio": [20, 20, 15, 10, 10],
    "Dante": [10, 5, 8, 4, 3],
    "Dast": [7, 7, 2, 4, 4],
    "Shinra": [8, 5, 2, 4, 2],
    "Juuji": [5, 5, 7, 1, 2],
    "Rogue": [6, 4, 4, 4, 2],
    "Belakor": [1, 1, 7, 1, 6],
    "Jackson": [2, 3, 5, 2, 4],
    "Sting": [2, 4, 4, 4, 2],
    "Qin": [6, 10, 30, 5, 20],
    "Trinity": [4, 4, 3, 3, 2],
    "Don_Egon": [4, 1, 4, 1, 4],
    "Nakato": [3, 4, 2, 1, 3],
    "Aitorren": [4, 2, 4, 1, 2],
    "Freezer": [3, 4, 2, 1, 2],
    "Tenepo": [2, 2, 2, 1, 5],
    "Dahlia": [2, 4, 3, 2, 1],
    "Sassune": [3, 2, 3, 1, 2],
    "Ibai": [1, 0, 5, 1, 3],
    "Paco": [2, 2, 2, 2, 2],
    "Shogon": [1, 4, 2, 1, 0],
    "Rimoru": [0, 3, 1, 2, 2],
    "tyki": [2, 2, 1, 1, 2],
    "Saitama": [2, 0, 4, 2, 0],
    "Samuel": [2, 2, 1, 2, 1],
    "Pabloneto": [1, 2, 2, 1, 2],
    "Ismael": [2, 2, 2, 1, 1],
    "Aki": [2, 2, 1, 2, 1],
    "Kowai": [2, 1, 2, 1, 2],
    "Zaein": [1, 3, 1, 1, 2],
    "Raymond": [2, 2, 2, 0, 2],
    "Domoku": [1, 3, 2, 1, 1],
    "Pato": [2, 0, 3, 2, 1],
    "Rey_Burrito": [1, 0, 3, 2, 2],
    "Ray": [3, 2, 1, 1, 1],
    "Nahoto": [2, 2, 2, 1, 1],
    "Cabalen": [2, 2, 1, 3, 0],
    "Yato": [2, 2, 1, 2, 1],
    "Tomoko": [2, 2, 2, 1, 1],
    "Pedro": [2, 3, 1, 1, 1],
    "Teshiwara": [0, 0, 0, 0, 0],
    "Rambo": [4, 2, 2, 1, 1],
    "Guy": [10, 60, 20, 5, 10]
    
}

@bot.event
async def on_ready():
    print(f'Conectado como {bot.user.name}')

@bot.command()
async def consultar(ctx, clave: str):
    if clave in diccionario:
        valor = diccionario[clave]
        await ctx.send(f'Las estadisticas de {clave} son: {valor}')
    else:
        await ctx.send(f'Las estadisticas de "{clave}" no fueron encontradas')

frutas = {
    'Neko_Neko_modelo_tigre_blanco': ['Zerf', 4],
    'Sal_Sal': ['Garou', 20],
    'Espacio_Espacio': ['Illipyo', 1],
    # Agrega más frutas según tus necesidades
}

@bot.command()
async def fruta(ctx, fruta: str):
    if fruta in frutas:
        info = frutas[fruta]
        color = info[0]
        nivel = info[1]
        await ctx.send(f'La fruta "{fruta}" es de {color} y tiene un nivel {nivel}.')
    else:
        await ctx.send(f'La fruta "{fruta}" no fue encontrada en el diccionario.')

npcs = {}

@bot.command()
async def ranking(ctx):
    sorted_npcs = sorted(diccionario.items(), key=lambda x: sum(x[1]), reverse=True)
    
    if sorted_npcs:
        ranking = ""
        for index, (npc, valores) in enumerate(sorted_npcs, start=1):
            total = sum(valores)
            ranking += f"{index}. {npc} - Suma de valores: {total}\n"
            if index % 10 == 0:
                await ctx.send(f'Ranking:\n{ranking}')
                ranking = ""
        if ranking:
            await ctx.send(f'Ranking:\n{ranking}')
    else:
        await ctx.send('El diccionario de NPCs está vacío.')

@bot.command()
async def agregar_npc(ctx, nombre: str, *valores: int):
    if len(valores) == 5:
        npcs[nombre] = valores
        await ctx.send(f'El NPC "{nombre}" ha sido agregado con éxito.')
    else:
        await ctx.send('Se deben proporcionar exactamente 5 valores enteros.')

@bot.command()
async def consultar_npc(ctx, nombre: str):
    if nombre in npcs:
        valores = npcs[nombre]
        await ctx.send(f'Valores del NPC "{nombre}": {valores}')
    else:
        await ctx.send(f'El NPC "{nombre}" no fue encontrado en la base de datos.')

@bot.command()
async def lista_npcs(ctx):
    if npcs:
        lista = "\n".join(npcs.keys())
        await ctx.send(f'Lista de NPCs agregados:\n{lista}')
    else:
        await ctx.send('No se han agregado NPCs.')
      

@bot.command()
async def actualizar_npc(ctx, nombre: str, *nuevos_valores: int):
    if nombre in npcs:
        if len(nuevos_valores) == 5:
            npcs[nombre] = nuevos_valores
            await ctx.send(f'Valores del NPC "{nombre}" actualizados con éxito.')
        else:
            await ctx.send('Se deben proporcionar exactamente 5 nuevos valores enteros.')
    else:
        await ctx.send(f'El NPC "{nombre}" no fue encontrado en la base de datos.')





def calcular_dado_ataque(distancia, jugador, rival):
    if distancia == "cuerpo":
        jugador_dado = max(20 + rival[4] - jugador[3] - jugador[2], 0)
    elif distancia == "pistola":
        jugador_dado = max(20 + rival[4] - jugador[3] - jugador[1], 0)
    else:
        raise ValueError("Distancia inválida")
    
    rival_dado = max(20 + jugador[4] - rival[3] - rival[2], 0)
    
    return jugador_dado, rival_dado

def calcular_ataques_multiples(velocidad_jugador, velocidad_rival):
    if velocidad_jugador >= velocidad_rival * 3:
        return 3
    elif velocidad_jugador >= velocidad_rival * 2:
        return 2
    else:
        return 1


@bot.command()
async def dados(ctx, jugador: str, rival: str, distancia: str):
    if jugador in diccionario and rival in diccionario:
        jugador_estadisticas = diccionario[jugador]
        rival_estadisticas = diccionario[rival]

        jugador_dado, rival_dado = calcular_dado_ataque(distancia, jugador_estadisticas, rival_estadisticas)

        multiplicador_ataque = calcular_ataques_multiples(jugador_estadisticas[0], rival_estadisticas[0])

        mensaje_jugador = f"Dado de ataque del jugador ({jugador}): {jugador_dado * multiplicador_ataque} (ataques: {multiplicador_ataque})"
        mensaje_rival = f"Dado de ataque del rival ({rival}): {rival_dado}"
        
        await ctx.send(mensaje_jugador)
        await ctx.send(mensaje_rival)
    else:
        await ctx.send('Jugador o rival no encontrado.')


# ID del usuario permitido para usar los comandos
USUARIO_PERMITIDO_ID = 1109958330648117248

@bot.command()
async def add_vel(ctx, key: str, puntos: int):
    if ctx.author.id == USUARIO_PERMITIDO_ID:
        if key in diccionario:
            diccionario[key][0] += puntos
            await ctx.send(f'Se añadieron {puntos} puntos a la velocidad de {key}. Valor actual: {diccionario[key][0]}')
        else:
            await ctx.send('Clave no encontrada en el diccionario.')
    else:
        await ctx.send('No tienes permiso para usar este comando.')

@bot.command()
async def add_iq(ctx, key: str, puntos: int):
    if ctx.author.id == USUARIO_PERMITIDO_ID:
        if key in diccionario:
            diccionario[key][1] += puntos
            await ctx.send(f'Se añadieron {puntos} puntos a la inteligencia de {key}. Valor actual: {diccionario[key][1]}')
        else:
            await ctx.send('Clave no encontrada en el diccionario.')
    else:
        await ctx.send('No tienes permiso para usar este comando.')

@bot.command()
async def add_fz(ctx, key: str, puntos: int):
    if ctx.author.id == USUARIO_PERMITIDO_ID:
        if key in diccionario:
            diccionario[key][2] += puntos
            await ctx.send(f'Se añadieron {puntos} puntos a la fuerza de {key}. Valor actual: {diccionario[key][2]}')
        else:
            await ctx.send('Clave no encontrada en el diccionario.')
    else:
        await ctx.send('No tienes permiso para usar este comando.')

@bot.command()
async def add_hab(ctx, key: str, puntos: int):
    if ctx.author.id == USUARIO_PERMITIDO_ID:
        if key in diccionario:
            diccionario[key][3] += puntos
            await ctx.send(f'Se añadieron {puntos} puntos a la habilidad de {key}. Valor actual: {diccionario[key][3]}')
        else:
            await ctx.send('Clave no encontrada en el diccionario.')
    else:
        await ctx.send('No tienes permiso para usar este comando.')

@bot.command()
async def add_res(ctx, key: str, puntos: int):
    if ctx.author.id == USUARIO_PERMITIDO_ID:
        if key in diccionario:
            diccionario[key][4] += puntos
            await ctx.send(f'Se añadieron {puntos} puntos a la resistencia de {key}. Valor actual: {diccionario[key][4]}')
        else:
            await ctx.send('Clave no encontrada en el diccionario.')
    else:
        await ctx.send('No tienes permiso para usar este comando.')
# Diccionario de bandas
bandas = {}

@bot.command()
async def add_band(ctx, nombre: str):
    if ctx.author.id == USUARIO_PERMITIDO_ID:
        if nombre not in bandas:
            bandas[nombre] = []
            await ctx.send(f'La banda {nombre} ha sido creada, esperamos mucho de ella.')
        else:
            await ctx.send('La banda ya existe.')
    else:
        await ctx.send('No tienes permiso para usar este comando.')

@bot.command()
async def band_register(ctx, usuario: discord.Member, nombre: str):
    if nombre in bandas:
        bandas[nombre].append(usuario)
        await ctx.send(f'Bienvenido a la banda {nombre}, {usuario.display_name}! Espero que disfrutes.')
    else:
        await ctx.send('Banda no encontrada.')

@bot.command()
async def band(ctx):
    if bandas:
        for nombre, miembros in bandas.items():
            miembros_info = '\n'.join([f'{miembro.display_name} ({miembro.id})' for miembro in miembros])
            await ctx.send(f'Miembros de la banda {nombre}:\n{miembros_info}')
    else:
        await ctx.send('No hay bandas registradas.')

@bot.command()
async def dados_npc(ctx, npc: str, distancia: str, v1: int, v2: int, v3: int, v4: int, v5: int):
    if npc in diccionario:
        jugador_estadisticas = [v1, v2, v3, v4, v5]
        rival_estadisticas = diccionario[npc]

        jugador_dado, rival_dado = calcular_dado_ataque(distancia, jugador_estadisticas, rival_estadisticas)

        multiplicador_ataque = calcular_ataques_multiples(jugador_estadisticas[0], rival_estadisticas[0])

        await ctx.send(f'Dado de ataque del npc: {jugador_dado * multiplicador_ataque} (ataques: {multiplicador_ataque})')
        await ctx.send(f'Tu dado: {rival_dado}')
    else:
        await ctx.send('NPC no encontrado en el diccionario.')

# Define las funciones de calcular_dado_ataque y calcular_ataques_multiples aquí


@bot.command()
async def comandos(ctx):
    ayuda_mensaje = (
        "Lista de comandos disponibles:\n"
        "!consultar <clave>: Consulta las estadísticas de un NPC.\n"
        "!fruta <fruta>: Muestra información sobre una fruta.\n"
        "!ranking: Muestra el ranking de NPCs basado en la suma de sus valores.\n"
        "!agregar_npc <nombre> <v1> <v2> <v3> <v4> <v5>: Agrega un NPC con valores.\n"
        "!consultar_npc <nombre>: Consulta los valores de un NPC agregado.\n"
        "!lista_npcs: Muestra la lista de NPCs agregados.\n"
        "!actualizar_npc <nombre> <v1> <v2> <v3> <v4> <v5>: Actualiza valores de un NPC.\n"
        "!dados <jugador> <rival> <distancia>: Simula un ataque entre dos NPCs.\n"
        "!add_vel <nombre> <puntos>: Añade puntos a la velocidad de un NPC.\n"
        "!add_iq <nombre> <puntos>: Añade puntos a la inteligencia de un NPC.\n"
        "!add_fz <nombre> <puntos>: Añade puntos a la fuerza de un NPC.\n"
        "!add_hab <nombre> <puntos>: Añade puntos a la habilidad de un NPC.\n"
        "!add_res <nombre> <puntos>: Añade puntos a la resistencia de un NPC.\n"
        "!add_band <nombre>: Crea una nueva banda.\n"
        "!band_register <usuario> <nombre>: Registra un usuario en una banda.\n"
        "!band: Muestra los miembros de las bandas.\n"
        "!dados_npc <npc> <distancia> <v1> <v2> <v3> <v4> <v5>: Simula un ataque de un NPC."
    )
    await ctx.send(ayuda_mensaje)
@bot.command()
async def añadir(ctx, key: str, v1: int, v2: int, v3: int, v4: int, v5: int):
    if ctx.author.id == USUARIO_PERMITIDO_ID:
        diccionario[key] = [v1, v2, v3, v4, v5]
        await ctx.send(f'Se agregó la entrada "{key}" con los valores: [{v1}, {v2}, {v3}, {v4}, {v5}] al diccionario.')
    else:
        await ctx.send('No tienes permiso para usar este comando.')

@bot.command()
async def stats_ranking(ctx):
    sorted_npcs = sorted(diccionario.items(), key=lambda x: sum(x[1]), reverse=True)
    
    if sorted_npcs:
        ranking_info = ""
        for index, (npc, valores) in enumerate(sorted_npcs, start=1):
            stats_info = f"Vel: {valores[0]}, IQ: {valores[1]}, Fz: {valores[2]}, Hab: {valores[3]}, Res: {valores[4]}"
            ranking_info += f"{index}. {npc} - {stats_info}\n"
            if index % 10 == 0:
                await ctx.send(f'Ranking:\n{ranking_info}')
                ranking_info = ""
        if ranking_info:
            await ctx.send(f'Ranking:\n{ranking_info}')
    else:
        await ctx.send('El diccionario de NPCs está vacío.')

@bot.command()
async def tier(ctx):
    sorted_npcs = sorted(diccionario.items(), key=lambda x: sum(x[1]), reverse=True)
    
    total_npcs = len(sorted_npcs)
    num_class_s_pp = int(total_npcs * 0.05)
    num_class_s_p = int(total_npcs * 0.05)
    num_class_s = int(total_npcs * 0.10)
    num_class_a = int(total_npcs * 0.10)
    num_class_b = int(total_npcs * 0.20)
    num_class_c = int(total_npcs * 0.20)
    
    class_s_pp = sorted_npcs[:num_class_s_pp]
    class_s_p = sorted_npcs[num_class_s_pp:num_class_s_pp+num_class_s_p]
    class_s = sorted_npcs[num_class_s_pp+num_class_s_p:num_class_s_pp+num_class_s_p+num_class_s]
    class_a = sorted_npcs[num_class_s_pp+num_class_s_p+num_class_s:num_class_s_pp+num_class_s_p+num_class_s+num_class_a]
    class_b = sorted_npcs[num_class_s_pp+num_class_s_p+num_class_s+num_class_a:num_class_s_pp+num_class_s_p+num_class_s+num_class_a+num_class_b]
    class_c = sorted_npcs[num_class_s_pp+num_class_s_p+num_class_s+num_class_a+num_class_b:num_class_s_pp+num_class_s_p+num_class_s+num_class_a+num_class_b+num_class_c]
    
    class_f = sorted_npcs[num_class_s_pp+num_class_s_p+num_class_s+num_class_a+num_class_b+num_class_c:]
    
    classes = {
        "S++": class_s_pp,
        "S+": class_s_p,
        "S": class_s,
        "A": class_a,
        "B": class_b,
        "C": class_c,
        "F": class_f
    }
    
    for class_name, npcs_in_class in classes.items():
        if npcs_in_class:
            npcs_list = "\n- ".join([npc[0] for npc in npcs_in_class])
            await ctx.send(f"Clase {class_name}:\n- {npcs_list}")
        else:
            await ctx.send(f"Clase {class_name}:\n- No hay NPCs en esta clase.")

# Diccionario de habilidades por usuario
habilidades_usuarios = {
    "Ibai_Jr": ["antiveneno"],
    "Qin": ["megapuño"]
}

# Diccionario de habilidades con descripciones
habilidades = {
    "antiveneno": "Pasiva de Ibai Jr: Hace que el veneno o quemaduras solo le puedan quitar su primera vida.",
    "megapuño": "Pasiva de Qin: Hace que los ataques que no sean directos fallen. Si da un ataque directo, quita dos vidas en vez de una y deja al rival sin su turno."
}

@bot.command()
async def userhab(ctx, usuario: str):
    if usuario in habilidades_usuarios:
        habilidades_usuario = habilidades_usuarios[usuario]
        habilidades_texto = ", ".join(habilidades_usuario)
        await ctx.send(f"Habilidades de {usuario}: {habilidades_texto}")
    else:
        await ctx.send(f"El usuario '{usuario}' no fue encontrado en la lista de habilidades por usuario.")

@bot.command()
async def hab(ctx, *, habilidad: str):
    if habilidad in habilidades:
        descripcion = habilidades[habilidad]
        await ctx.send(f"Descripción de la habilidad '{habilidad}': {descripcion}")
    else:
        await ctx.send(f"La habilidad '{habilidad}' no fue encontrada en la lista de habilidades.")
    
# Resto del código

bot.run(TOKEN)