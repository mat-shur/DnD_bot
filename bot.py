from random import randint

# DATABASE
import sqlite3

conn = sqlite3.connect('dnd_bot.db', check_same_thread=False)
conn.row_factory = lambda k, l: {c[0]: l[i] for i, c in enumerate(k.description)}
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS settings(
        name TEXT
    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS characters(
        player_id INT,
        player_name TEXT,
        setting TEXT,
        name TEXT,
        race TEXT,
        class TEXT,
        strength INT,
        dexterity INT,
        wisdom INT,
        intelligence INT,
        constitution INT,
        charisma INT,
        health INT,
        gold INT,
        experience INT
    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS characters_inventory(
        setting TEXT,
        name TEXT,
        item TEXT,
        count_of_item INT
    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS dms(
        dm_id INT,
        chat_id INT
    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS mobs(
        setting TEXT,
        name TEXT,
        health INT,
        attack INT
    )
""")
# DATABASE

# BOT SETTINGS
import os
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
# BOT SETTINGS

# LANGUAGE
current_lang = config['bot']['language']
dict_of_lang = {
    'english': {
        'roll': 'You rolled number',
        'change_lang': 'The language has been successfully changed to',
        'dm_exist': 'DM is already exist in this chat!',
        'dm_assign': 'was assigned to DM.',
        'dm_remove': 'refused DM.',
        'dm_havens': 'You are not a DM!',
        'only_for_admins': 'Only for administrator!',
        'setting_exist': 'This setting already exist! Use /change_setting [STRING: setting_name].',
        'setting_created': 'Successfully created new setting',
        'setting_not_exist': 'This setting was not found, create it using the /create_new_setting command or choose another from the following list:',
        'setting_changed': 'Successfully changed the setting to',
        'setting_removed': 'Successfully removed the setting',
        'character_created': 'Successfully created new character',
        'character_exist': 'A character with this name has already been created!',
        'character_player_have': 'You already have a character!',
        'character_not_exist': 'A character with that name does not exist!',
        'character_changed': 'The character was successfully changed!',
        'character_removed': 'The character was successfully deleted!',
        'character_not_your': 'This is not your character!',
        'mob_created': 'Monster successfully created!',
        'mobs_not_exist': 'There are no monsters yet!',
        'mob_exist': 'A monster with that name already exists!',
        'mob_not_exist': 'A monster with that name not exists!',
        'mob_attacked': 'After the hit, the monster has life left',
        'mob_dead': 'After the impact, the monster died.',
        'inventory_item_not_exist': 'The character does not have this item!',
        'inventory_updated': 'Character inventory successfully updated.',
        'inventory_empty': 'The character`s inventory is empty!',
        'dm_only': 'You need to be a DM for this command!',
        'mob_attack_changed': 'The monster`s attack value has been successfully changed!',
        'setting_no_choosen': 'Before using this command, you need to select a setting! Use /change_setting.'
    },
    'russian': {
        # русня - не люди
        'roll': 'Тебе выпало число',
        'change_lang': 'Язык успешно изменен на',
        'dm_exist': 'ДМ уже есть в этом чате!',
        'dm_assign': 'назначено ДМ.',
        'dm_remove': 'отказался от ДМ.',
        'dm_have_no': 'Ты не ДМ!',
        'only_for_admins': 'Только для администраторов!',
        'setting_exist': 'Этот сеттинг уже существует! Используйте /change_setting [STRING: setting_name].',
        'setting_created': 'Успешно создано новый сеттинг',
        'setting_not_exist': 'Этот сеттинг не найден, создайте его, используя команду /create_new_setting или выберите другой из следующего списка:',
        'setting_changed': 'Успешно изменено сеттинг на',
        'setting_removed': 'Успешно удалено сеттинг',
        'character_created': 'Успешно создан новый персонаж',
        'character_exist': 'Персонаж с таким именем уже существует!',
        'character_player_have': 'У вас уже есть персонаж!',
        'character_not_exist': 'Персонажа с таким именем не существует!',
        'character_changed': 'Персонаж был успешно изменен!',
        'character_removed': 'Персонаж был успешно удален!',
        'character_not_your': 'Это не твой персонаж!',
        'mob_created': 'Монстр успешно создан!',
        'mobs_not_exist': 'Монстров пока нет!',
        'mob_exist': 'Монстр с таким именем уже есть!',
        'mob_not_exist': 'Монстра с таким именем нету!',
        'mob_attacked': 'После удара у монстра осталась жизней',
        'mob_dead': 'После удара монстр умер.',
        'inventory_item_not_exist': 'Этого предмета нет у персонажа!',
        'inventory_updated': 'Инвентарь персонажа успешно обновлен.',
        'inventory_empty': 'Инвентарь персонажа пустой!',
        'dm_only': 'Для этой команды нужно быть ДМ!',
        'mob_attack_changed': 'Значение атаки монстра успешно изменено!',
        'setting_no_choosen': 'Перед тем, как использовать эту команду, нужно выбрать сеттинг! Используйте /change_setting.'
    },
    'ukrainian': {
        'roll': 'Тобі випало число',
        'change_lang': 'Мову успішно змінено на',
        'dm_exist': 'ДМ вже є в цьому чаті!',
        'dm_assign': 'доручено ДМ.',
        'dm_remove': 'відмовився від ДМ.',
        'dm_have_no': 'Ти не є ДМ!',
        'only_for_admins': 'Лише для адміністраторів!',
        'setting_exist': 'Цей сеттінг вже існує! Використайте /change_setting [STRING: setting_name].',
        'setting_created': 'Успішно створено новий сеттінг',
        'setting_not_exist': 'Цього сеттінгу не знайдено, створіть його, використовуючи команду /create_new_setting або оберіть інший з наступного списку:',
        'setting_changed': 'Успішно змінено сеттінг на',
        'setting_removed': 'Успішно видалено сеттінг',
        'character_created': 'Успішно створений новий персонаж',
        'character_exist': 'Персонаж з таким ім`ям вже створений!',
        'character_player_have': 'У вас вже є персонаж!',
        'character_not_exist': 'Персонажа з таким іменем не існує!',
        'character_changed': 'Персонажа було успішно змінено!',
        'character_removed': 'Персонажа було успішно видалено!',
        'character_not_your': 'Це не твій персонаж!',
        'mob_created': 'Монстр успішно створений!',
        'mobs_not_exist': 'Монстрів поки немає!',
        'mob_exist': 'Монстр з таким іменем вже існує!',
        'mob_not_exist': 'Монстра з таким іменем не існує!',
        'mob_attacked': 'Після удару у монстра залишилось життя',
        'mob_dead': 'Після удару монстр вмер.',
        'inventory_item_not_exist': 'Цього предмету немає в персонажа!',
        'inventory_updated': 'Інвентар персонажа успішно оновлено.',
        'inventory_empty': 'Інвентар персонажа пустий!',
        'dm_only': 'Для цієї команди потрібно бути ДМ!',
        'mob_attack_changed': 'Значення атаки монстра було успішно змінено!',
        'setting_no_choosen': 'Перед тим як використати цю команду потрібно обрати сеттінг! Використайте /change_setting.'
    }
}
# LANGUAGE

# BOT
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

token = config['options']['token']
bot = Bot(token=token)
dp = Dispatcher(bot, storage=MemoryStorage())

admin_id = int(config['options']['admin_id'])


@dp.message_handler(commands=['info'])
async def info(message):
    info_str = f"→ Setting: {config['bot']['setting']}\n→ Language: {config['bot']['language']}"
    await bot.send_message(chat_id=message.chat.id, text=info_str)


@dp.message_handler(commands=['print_inventory'])
async def print_inventory(message):
    # name
    character_name = message.text.replace('/print_inventory ', '')

    if character_name == '/print_inventory':
        await bot.send_message(chat_id=message.chat.id, text="/print_inventory [STRING: character_name]")
        return

    cur.execute(f"SELECT * FROM 'characters' WHERE name = ? AND setting = ?", (character_name, config['bot']['setting'],))
    character = cur.fetchone()

    if not character:
        await bot.send_message(chat_id=message.chat.id, text=dict_of_lang[current_lang]['character_not_exist'])
        return

    cur.execute(f"SELECT * FROM 'characters_inventory' WHERE name = ? AND setting = ?", (character_name, config['bot']['setting'],))
    character_items = cur.fetchall()

    if not character_items:
        await bot.send_message(chat_id=message.chat.id, text=dict_of_lang[current_lang]['inventory_empty'])
        return

    invetory_list = \
        f"→ [{character['player_name']}`s]:\n" + \
        f"\t\t\t➥ {character['name']} inventory:\n"
    for item in character_items:
        invetory_list += f"● {item['item']}: {item['count_of_item']}\n"

    await bot.send_message(chat_id=message.chat.id, text=invetory_list)


@dp.message_handler(commands=['update_inventory'])
async def update_inventory(message):
    # name add/remove item count_of_item
    cur.execute(f"SELECT * FROM 'dms' WHERE dm_id = ? AND chat_id = ?", (message.from_user.id, message.chat.id,))
    dm = cur.fetchone()

    if not dm:
        await bot.send_message(chat_id=message.chat.id, text=dict_of_lang[current_lang]['dm_only'])
        return

    inventory_array = message.text.replace('/update_inventory ', '').split(' ')

    if len(inventory_array) == 4 and inventory_array[1] in ['add', 'remove'] and inventory_array[3].isdigit():
        cur.execute(f"SELECT * FROM 'characters' WHERE name = ? AND setting = ?", (inventory_array[0], config['bot']['setting'],))
        character = cur.fetchone()

        if not character:
            await bot.send_message(chat_id=message.chat.id, text=dict_of_lang[current_lang]['character_not_exist'])
            return

        cur.execute(f"SELECT * FROM 'characters_inventory' WHERE name = ? AND setting = ? AND item = ?", (inventory_array[0], config['bot']['setting'], inventory_array[2],))
        item = cur.fetchone()

        if item:
            state = '-' if inventory_array[1] == 'remove' else '+'
            cur.execute(f"UPDATE 'characters_inventory' SET count_of_item = count_of_item {state} {inventory_array[3]} WHERE name = ? AND setting = ? AND item = ?;", (inventory_array[0], config['bot']['setting'], inventory_array[2],))
            conn.commit()

            if state == '-':
                cur.execute(f"SELECT * FROM 'characters_inventory' WHERE name = ? AND setting = ? AND item = ?", (inventory_array[0], config['bot']['setting'], inventory_array[2],))
                item = cur.fetchone()

                if item['count_of_item'] <= 0:
                    cur.execute(f"DELETE FROM 'characters_inventory' WHERE name = ? AND setting = ? AND item = ?", (inventory_array[0], config['bot']['setting'], inventory_array[2],))
                    conn.commit()
            await bot.send_message(chat_id=message.chat.id, text=dict_of_lang[current_lang]['inventory_updated'])
        elif not item and inventory_array[1] == 'remove':
            await bot.send_message(chat_id=message.chat.id, text=dict_of_lang[current_lang]['inventory_item_not_exist'])
        elif not item and inventory_array[1] == 'add':
            cur.execute("INSERT INTO 'characters_inventory' (setting, name, item, count_of_item) VALUES (?, ?, ?, ?);", (config['bot']['setting'], inventory_array[0], inventory_array[2], inventory_array[3],))
            conn.commit()
            await bot.send_message(chat_id=message.chat.id, text=dict_of_lang[current_lang]['inventory_updated'])
    else:
        await bot.send_message(chat_id=message.chat.id, text='/update_inventory [STRING: character_name] [STRING: add/remove] [STRING: name_of_item] [NUMBER: count_of_item]')


@dp.message_handler(commands=['show_all_mobs'])
async def show_all_mobs(message):
    cur.execute(f"SELECT * FROM 'mobs'")
    mobs = cur.fetchall()

    if not mobs:
        await bot.send_message(chat_id=message.chat.id, text=dict_of_lang[current_lang]['mobs_not_exist'])
        return

    mobs_list = ''

    for mob in mobs:
        mobs_list += f"→ {mob['name']}\n\t\t\t● Health: {mob['health']}\n\t\t\t● Attack: {mob['attack']}\n\n"

    await bot.send_message(chat_id=message.chat.id, text=mobs_list)


@dp.message_handler(commands=['change_monster_attack'])
async def change_monster_attack(message):
    # name amount
    cur.execute(f"SELECT * FROM 'dms' WHERE dm_id = ? AND chat_id = ?", (message.from_user.id, message.chat.id,))
    dm = cur.fetchone()

    if not dm:
        await bot.send_message(chat_id=message.chat.id, text=dict_of_lang[current_lang]['dm_only'])
        return

    attack_array = message.text.replace('/attack_monster ', '').split(' ')

    if len(attack_array) == 2 and attack_array[1].isdigit():
        cur.execute(f"SELECT * FROM 'mobs' WHERE name = ? AND setting = ?", (attack_array[0], config['bot']['setting'],))
        mob = cur.fetchone()

        if not mob:
            await bot.send_message(chat_id=message.chat.id, text=dict_of_lang[current_lang]['mob_not_exist'])
            return

        cur.execute(f"UPDATE 'mobs' SET attack = attack + {attack_array[1]} WHERE name = ? AND setting = ?;", (attack_array[0], config['bot']['setting'],))
        conn.commit()

        await bot.send_message(chat_id=message.chat.id, text=dict_of_lang[current_lang]['mob_attack_changed'])
    else:
        await bot.send_message(chat_id=message.chat.id, text='/change_monster_attack [STRING: monster_name] [NUMBER: ±amount]')


@dp.message_handler(commands=['attack_monster'])
async def attack_monster(message):
    # name dmg
    cur.execute(f"SELECT * FROM 'dms' WHERE dm_id = ? AND chat_id = ?", (message.from_user.id, message.chat.id,))
    dm = cur.fetchone()

    if not dm:
        await bot.send_message(chat_id=message.chat.id, text=dict_of_lang[current_lang]['dm_only'])
        return

    damage_array = message.text.replace('/attack_monster ', '').split(' ')

    if len(damage_array) == 2 and damage_array[1].isdigit():
        cur.execute(f"SELECT * FROM 'mobs' WHERE name = ? AND setting = ?", (damage_array[0], config['bot']['setting'],))
        mob = cur.fetchone()

        if not mob:
            await bot.send_message(chat_id=message.chat.id, text=dict_of_lang[current_lang]['mob_not_exist'])
            return

        cur.execute(f"UPDATE 'mobs' SET health = health - {damage_array[1]} WHERE name = ? AND setting = ?;", (damage_array[0], config['bot']['setting'],))
        conn.commit()

        cur.execute(f"SELECT * FROM 'mobs' WHERE name = ? AND setting = ?", (damage_array[0], config['bot']['setting'],))
        mob = cur.fetchone()

        if mob['health'] <= 0:
            cur.execute(f"DELETE FROM 'mobs' WHERE name = ? AND setting = ?", (damage_array[0], config['bot']['setting'],))
            conn.commit()
            await bot.send_message(chat_id=message.chat.id, text=dict_of_lang[current_lang]['mob_dead'])
        else:
            await bot.send_message(chat_id=message.chat.id, text=f"{dict_of_lang[current_lang]['mob_attacked']} {mob['health']}.")
    else:
        await bot.send_message(chat_id=message.chat.id, text='/attack_monster [STRING: monster_name] [NUMBER: damage]')


@dp.message_handler(commands=['create_monster'])
async def create_monster(message):
    # name health attack
    cur.execute(f"SELECT * FROM 'dms' WHERE dm_id = ? AND chat_id = ?", (message.from_user.id, message.chat.id,))
    dm = cur.fetchone()

    if not dm:
        await bot.send_message(chat_id=message.chat.id, text=dict_of_lang[current_lang]['dm_only'])
        return

    if config['bot']['setting'] == 'none':
        await bot.send_message(chat_id=message.chat.id, text=dict_of_lang[current_lang]['setting_no_choosen'])
        return

    monster_array = message.text.replace('/create_monster ', '').split(' ')

    if len(monster_array) == 3 and monster_array[1].isdigit() and monster_array[2].isdigit():
        cur.execute(f"SELECT * FROM 'mobs' WHERE name = ? AND setting = ?", (monster_array[0], config['bot']['setting'],))
        mob = cur.fetchall()

        if mob:
            await bot.send_message(chat_id=message.chat.id, text=dict_of_lang[current_lang]['mob_exist'])
            return

        cur.execute("INSERT INTO 'mobs' (setting, name, health, attack) VALUES (?, ?, ?, ?);", (config['bot']['setting'], monster_array[0], monster_array[1], monster_array[2],))
        conn.commit()
        await bot.send_message(chat_id=message.chat.id, text=dict_of_lang[current_lang]['mob_created'])
    else:
        await bot.send_message(chat_id=message.chat.id, text='/create_monster [STRING: monster_name] [NUMBER: health] [NUMBER: attack]')


@dp.message_handler(commands=['remove_character'])
async def remove_character(message):
    # name
    character_name = message.text.replace('/remove_character ', '')

    if character_name == '/remove_character':
        await bot.send_message(chat_id=message.chat.id, text="/remove_character [STRING: character_name]")
        return

    cur.execute(f"SELECT * FROM 'characters' WHERE name = ? AND setting = ?", (character_name, config['bot']['setting'],))
    character = cur.fetchone()

    if not character:
        await bot.send_message(chat_id=message.chat.id, text=dict_of_lang[current_lang]['character_not_exist'])
        return

    cur.execute(f"SELECT * FROM 'dms' WHERE dm_id = ? AND chat_id = ?", (message.from_user.id, message.chat.id,))
    dm = cur.fetchone()

    if character['player_id'] == message.from_user.id or dm:
        cur.execute(f"DELETE FROM 'characters' WHERE name = ? AND setting = ?", (character_name, config['bot']['setting'],))
        conn.commit()
        await bot.send_message(chat_id=message.chat.id, text=dict_of_lang[current_lang]['character_removed'])
    else:
        await bot.send_message(chat_id=message.chat.id, text=dict_of_lang[current_lang]['character_not_your'])


@dp.message_handler(commands=['change'])
async def change_character(message):
    # name type amount
    cur.execute(f"SELECT * FROM 'dms' WHERE dm_id = ? AND chat_id = ?", (message.from_user.id, message.chat.id,))
    dm = cur.fetchone()

    if not dm:
        await bot.send_message(chat_id=message.chat.id, text=dict_of_lang[current_lang]['dm_only'])
        return

    change_array = message.text.replace('/change ', '').split(' ')

    if len(change_array) == 3 and change_array[1] in ['strength', 'dexterity', 'wisdom', 'intelligence', 'constitution', 'charisma', 'health', 'gold', 'experience'] and change_array[2].isdigit():
        cur.execute(f"SELECT * FROM 'characters' WHERE name = ? AND setting = ?", (change_array[0], config['bot']['setting'],))
        character = cur.fetchone()

        if not character:
            await bot.send_message(chat_id=message.chat.id, text=dict_of_lang[current_lang]['character_not_exist'])
            return

        cur.execute(f"UPDATE 'characters' SET {change_array[1]} = {change_array[1]} + {change_array[2]} WHERE name = ? AND setting = ?;", (change_array[0], config['bot']['setting'],))
        conn.commit()
        await bot.send_message(chat_id=message.chat.id, text=dict_of_lang[current_lang]['character_changed'])
    else:
        await bot.send_message(chat_id=message.chat.id, text='/change [STRING: character_name] [STRING: strength/dexterity/wisdom/intelligence/constitution/charisma/health/gold/experience] [NUMBER: ±amount]')


@dp.message_handler(commands=['print_character'])
async def print_character(message):
    # name
    character_name = message.text.replace('/print_character ', '')

    if character_name == '/print_character':
        await bot.send_message(chat_id=message.chat.id, text="/print_character [STRING: character_name]")
        return

    cur.execute(f"SELECT * FROM 'characters' WHERE name = ? AND setting = ?", (character_name, config['bot']['setting'],))
    character = cur.fetchone()

    if character:
        character_stat = \
            f"→ [{character['player_name']}`s]:\n" + \
            f"\t\t\t➥ {character['name']}\n" + \
            f"\t\t\t\t\t\t▬▬▬\n" + \
            f"● Race: {character['race']}\n" + \
            f"● Class: {character['class']}\n" + \
            f"\t\t\t\t\t\t▬▬▬\n" + \
            f"● Strength: {character['strength']}\n" + \
            f"● Dexterity: {character['dexterity']}\n" + \
            f"● Wisdom: {character['wisdom']}\n" + \
            f"● Intelligence: {character['intelligence']}\n" + \
            f"● Constitution: {character['constitution']}\n" + \
            f"● Charisma: {character['charisma']}\n" + \
            f"\t\t\t\t\t\t▬▬▬\n" + \
            f"● Health: {character['health']}\n" + \
            f"● Gold: {character['gold']}\n" + \
            f"● Experience: {character['experience']}"
        await bot.send_message(chat_id=message.chat.id, text=character_stat)
    else:
        await bot.send_message(chat_id=message.chat.id, text=dict_of_lang[current_lang]['character_not_exist'])


@dp.message_handler(commands=['create_character'])
async def create_character(message):
    # name race class strength dexterity wisdom intelligence constitution charisma health gold experience
    new_character = message.text.replace('/create_character ', '').split(' ')

    if config['bot']['setting'] == 'none':
        await bot.send_message(chat_id=message.chat.id, text=dict_of_lang[current_lang]['setting_no_choosen'])
        return

    if len(new_character) == 12:
        for i in range(3, 12):
            if not new_character[i].isdigit():
                await bot.send_message(chat_id=message.chat.id, text='/create_character [STRING: name] [STRING: race] [STRING: class] [NUMBER: strength] [NUMBER: dexterity] [NUMBER: wisdom] [NUMBER: intelligence] [NUMBER: constitution] [NUMBER: charisma] [NUMBER: health] [NUMBER: gold] [NUMBER: experience]')
                return

        cur.execute(f"SELECT * FROM 'characters' WHERE name = ? AND setting = ?", (new_character[0], config['bot']['setting'],))
        character = cur.fetchone()

        if character:
            await bot.send_message(chat_id=message.chat.id, text=dict_of_lang[current_lang]['character_exist'])
            return

        cur.execute(f"SELECT * FROM 'characters' WHERE player_id = ? AND setting = ?", (message.from_user.id, config['bot']['setting'],))
        character = cur.fetchone()

        if character:
            await bot.send_message(chat_id=message.chat.id, text=dict_of_lang[current_lang]['character_player_have'])
            return

        cur.execute("""
            INSERT INTO 'characters' 
                (player_id, player_name, setting, name, race, class, strength, dexterity, wisdom, intelligence, constitution, charisma, health, gold, experience) 
            VALUES 
                (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);""",
                (message.from_user.id, message.from_user.first_name, config['bot']['setting'], new_character[0], new_character[1], new_character[2], new_character[3], new_character[4], new_character[5], new_character[6], new_character[7], new_character[8], new_character[9], new_character[10], new_character[11])
        )
        conn.commit()

        await bot.send_message(chat_id=message.chat.id, text=f"{dict_of_lang[current_lang]['character_created']} {new_character[0]}.")
    else:
        await bot.send_message(chat_id=message.chat.id, text='/create_character [STRING: name] [STRING: race] [STRING: class] [NUMBER: strength] [NUMBER: dexterity] [NUMBER: wisdom] [NUMBER: intelligence] [NUMBER: constitution] [NUMBER: charisma] [NUMBER: health] [NUMBER: gold] [NUMBER: experience]')


@dp.message_handler(commands=['create_setting'])
async def create_new_setting(message):
    # setting
    if message.from_user.id == admin_id:
        new_setting = message.text.replace('/create_setting ', '')

        if new_setting == '/create_setting':
            await bot.send_message(chat_id=message.chat.id, text="/create_setting [STRING: setting]")
            return

        cur.execute(f"SELECT * FROM 'settings' WHERE name = ?", (new_setting,))
        setting = cur.fetchone()

        if setting:
            await bot.send_message(chat_id=message.chat.id, text=dict_of_lang[current_lang]['setting_exist'])
        else:
            await bot.send_message(chat_id=message.chat.id, text=f"{dict_of_lang[current_lang]['setting_created']} {new_setting}.")
            cur.execute("INSERT INTO 'settings' (name) VALUES (?);", (new_setting,))
            conn.commit()
    else:
        await bot.send_message(chat_id=message.chat.id, text=dict_of_lang[current_lang]['only_for_admins'])


@dp.message_handler(commands=['change_setting'])
async def change_setting(message):
    # setting
    if message.from_user.id == admin_id:
        new_setting = message.text.replace('/change_setting ', '')

        if new_setting == '/change_setting':
            await bot.send_message(chat_id=message.chat.id, text="/change_setting [STRING: setting]")
            return

        cur.execute(f"SELECT * FROM 'settings' WHERE name = ?", (new_setting,))
        setting = cur.fetchone()

        if setting:
            config.set('bot', 'setting', new_setting)

            with open('config.ini', 'w') as configfile:
                config.write(configfile)

            await bot.send_message(chat_id=message.chat.id, text=f"{dict_of_lang[current_lang]['setting_changed']} {new_setting}.")
        else:
            cur.execute(f"SELECT * FROM 'settings'")
            settings = cur.fetchall()
            settings_list = ''

            for setting in settings:
                settings_list += f"\t\t\t{setting['name']}\n"

            await bot.send_message(chat_id=message.chat.id, text=f"{dict_of_lang[current_lang]['setting_not_exist']}\n{settings_list}")
    else:
        await bot.send_message(chat_id=message.chat.id, text=dict_of_lang[current_lang]['only_for_admins'])


@dp.message_handler(commands=['remove_setting'])
async def remove_setting(message):
    # setting
    if message.from_user.id == admin_id:
        remove_setting_ = message.text.replace('/remove_setting ', '')

        if remove_setting_ == '/remove_setting':
            await bot.send_message(chat_id=message.chat.id, text="/remove_setting [STRING: setting]")
            return

        cur.execute(f"SELECT * FROM 'settings' WHERE name = ?", (remove_setting_,))
        setting = cur.fetchone()

        if setting:
            cur.execute(f"DELETE FROM 'settings' WHERE name = ?;", (remove_setting_,))
            conn.commit()

            if config['bot']['setting'] == remove_setting_:
                config.set('bot', 'setting', 'none')

                with open('config.ini', 'w') as configfile:
                    config.write(configfile)

            await bot.send_message(chat_id=message.chat.id, text=f"{dict_of_lang[current_lang]['setting_removed']} {remove_setting_}.")
        else:
            cur.execute(f"SELECT * FROM 'settings'")
            settings = cur.fetchall()
            settings_list = ''

            for setting in settings:
                settings_list += f"\t\t\t{setting['name']}\n"

            await bot.send_message(chat_id=message.chat.id, text=f"{dict_of_lang[current_lang]['setting_not_exist']}\n{settings_list}")
    else:
        await bot.send_message(chat_id=message.chat.id, text=dict_of_lang[current_lang]['only_for_admins'])


@dp.message_handler(commands=['set_dm'])
async def set_dm(message):
    cur.execute(f"SELECT * FROM 'dms' WHERE chat_id = ?", (message.chat.id,))
    dm = cur.fetchone()

    if dm:
        await bot.send_message(chat_id=message.chat.id, text=dict_of_lang[current_lang]['dm_exist'])
    else:
        cur.execute("INSERT INTO 'dms' (dm_id, chat_id) VALUES (?, ?);", (message.from_user.id, message.chat.id,))
        conn.commit()
        mention = "[" + message.from_user.first_name + "](tg://user?id=" + str(message.from_user.id) + ")"
        await bot.send_message(chat_id=message.chat.id, text=f"{mention} {dict_of_lang[current_lang]['dm_assign']}", parse_mode='Markdown')


@dp.message_handler(commands=['remove_dm'])
async def remove_dm(message):
    cur.execute(f"SELECT * FROM 'dms' WHERE dm_id = ? AND chat_id = ?", (message.from_user.id, message.chat.id, ))
    dm = cur.fetchone()

    if dm:
        mention = "[" + message.from_user.first_name + "](tg://user?id=" + str(message.from_user.id) + ")"
        await bot.send_message(chat_id=message.chat.id, text=f"{mention} {dict_of_lang[current_lang]['dm_remove']}", parse_mode='Markdown')
        cur.execute(f"DELETE FROM 'dms' WHERE dm_id = ? AND chat_id = ?;", (message.from_user.id, message.chat.id,))
        conn.commit()
    else:
        await bot.send_message(chat_id=message.chat.id, text=dict_of_lang[current_lang]['dm_have_no'])


@dp.message_handler(commands=['change_lang'])
async def change_lang(message):
    global current_lang
    # lang: english/russian/ukrainian
    if message.from_user.id == admin_id:
        new_lang = message.text.replace('/change_lang ', '')

        if new_lang == '/change_lang':
            await bot.send_message(chat_id=message.chat.id, text="/change_lang [STRING: english/russian/ukrainian]")
            return

        if new_lang in ['english', 'russian', 'ukrainian']:
            config.set('bot', 'language', new_lang)

            with open('config.ini', 'w') as configfile:
                config.write(configfile)

            current_lang = config['bot']['language']

            await bot.send_message(chat_id=message.chat.id, text=f"{dict_of_lang[current_lang]['change_lang']} {new_lang}.")
        else:
            await bot.send_message(chat_id=message.chat.id, text="/change_lang [STRING: english/russian/ukrainian]")
    else:
        await bot.send_message(chat_id=message.chat.id, text=dict_of_lang[current_lang]['only_for_admins'])


@dp.message_handler(commands=['roll'])
async def roll_dice(message):
    # number: 4/6/8/10/12/20
    dice_number = message.text.replace('/roll ', '')

    if dice_number == '/roll':
        await bot.send_message(chat_id=message.chat.id, text="/roll [NUMBER: 4, 6, 8, 10, 12, 20]")
        return

    if dice_number.isdigit() and dice_number in ['4', '6', '8', '10', '12', '20']:
        result = randint(1, int(dice_number))
        await bot.send_message(chat_id=message.chat.id, text=f"{dict_of_lang[current_lang]['roll']} {result}.")
    else:
        await bot.send_message(chat_id=message.chat.id, text="/roll [NUMBER: 4/6/8/10/12/20]")


@dp.message_handler(commands=['help'])
async def help(message):
    help_str = ''

    if config['bot']['language'] == 'english':
        help_str = '''
+=+ HELP MESSAGE +=+

Player commands:
/help - Shows a help message.
/info - Displays information about the selected setting and language.
/create_character [STRING: name] [STRING: race] [STRING: class] [NUMBER: strength] [NUMBER: dexterity] [NUMBER: wisdom] [NUMBER: intelligence] [NUMBER: constitution] [NUMBER: charisma] [NUMBER: health] [NUMBER: gold] [NUMBER: experience] - Creates your character.
/remove_character [STRING: character_name] - Deletes a character you've created. Only the creator or DM can delete a character.
/print_character [STRING: character_name] - Displays information about the character.
/print_inventory [STRING: character_name] - Displays information about the character's inventory.
/show_all_mobs - Displays a list of all created monsters in this setting, as well as their health and attack values.
/set_dm - Grants you the DM right. You cannot get DM if someone already has DM rights.
/remove_dm - Removes DM rights. Used to transfer rights to another user.
/roll [NUMBER: 4/6/8/10/12/20] - Rolls the die with the maximum selected number.

DM commands:
/update_inventory [STRING: character_name] [STRING: add/remove] [STRING: name_of_item] [NUMBER: count_of_item] - Changes the character's inventory.
/create_monster [STRING: monster_name] [NUMBER: health] [NUMBER: attack] - Creates a monster.
/attack_monster [STRING: monster_name] [NUMBER: damage] - Attacks a monster.
/change_monster_attack [STRING: monster_name] [NUMBER: ±amount] - Changes the monster's attack value.
/remove_character [STRING: character_name] - Deletes a character. Only the creator or DM can delete a character.
/change [STRING: character_name] [STRING: strength/dexterity/wisdom/intelligence/constitution/charisma/health/gold/experience] [NUMBER: ±amount] - Changes some characteristics of the character.

Admin commands:
/change_lang [STRING: english/russian/ukrainian] - Changes the language.
/create_setting [STRING: setting] - Creates a new setting.
/change_setting [STRING: setting] - Changes the setting to the desired one. When characters/monsters are created, they are assigned to the setting itself, so when changing the setting, characters and monsters that were created in setting A will not be available in setting B.
/remove_setting [STRING: setting] - Deletes the setting.
        '''
    elif config['bot']['language'] == 'russian':
        help_str = '''
+=+ ПОМОЩЬ +=+

Команды игрока:
/help - Показывает справочное сообщение.
/info — Отображает информацию о выбранном сеттинге и языке.
/create_character [STRING: name] [STRING: race] [STRING: class] [NUMBER: strength] [NUMBER: dexterity] [NUMBER: wisdom] [NUMBER: intelligence] [NUMBER: constitution] [NUMBER: charisma] [NUMBER: health] [NUMBER: gold] [NUMBER: experience] - Создает вашего персонажа.
/remove_character [STRING: character_name] — Удаляет созданного вами персонажа. Только создатель или ДМ может удалить персонажа.
/print_character [STRING: character_name] — Отображает информацию о персонаже.
/print_inventory [STRING: character_name] — Отображает информацию об инвентаре персонажа.
/show_all_mobs — Отображает список всех созданных монстров в этом параметре, а также их значения здоровья и атаки.
/set_dm - Предоставляет вам право ДМ. Вы не можете получить ДМ, если у кого-то уже есть права ДМ.
/remove_dm - Удаляет права ДМ. Используется для передачи прав другому пользователю.
/roll [NUMBER: 4/6/8/10/12/20] — Бросает кубик с максимальным выбранным числом.

Команды ДМ:
/update_inventory [STRING: character_name] [STRING: add/remove] [STRING: name_of_item] [NUMBER: count_of_item] — Изменяет инвентарь персонажа.
/create_monster [STRING: monster_name] [NUMBER: health] [NUMBER: attack] — Создает монстра.
/attack_monster [STRING: monster_name] [NUMBER: damage] — Атакует монстра.
/change_monster_attack [STRING: monster_name] [NUMBER: ±amount] — Изменяет значение атаки монстра.
/remove_character [STRING: character_name] — Удаляет персонажа. Только создатель или ДМ может удалить персонажа.
/change [STRING: character_name] [STRING: strength/dexterity/wisdom/intelligence/constitution/charisma/health/gold/experience] [NUMBER: ±amount] - Изменяет характеристику персонажа.

Команды администратора:
/change_lang [STRING: english/russian/ukrainian] - Изменяет язык.
/create_setting [STRING: setting] — Создает новый сеттинг.
/change_setting [STRING: setting] — Изменяет сеттинг на нужный. При создании персонажей/монстров они назначаются самому сеттингу, поэтому при изменении сеттинга персонажи и монстры, созданные в сеттинге А, не будут доступны в сеттинге Б.
/remove_setting [STRING: setting] — Удаляет сеттинг.
        '''
    elif config['bot']['language'] == 'ukrainian':
        help_str = '''
+=+ ПОВІДОМЛЕННЯ ДОПОМОГИ +=+

Команди гравця:
/help - Показує довідкове повідомлення.
/info - Відображає інформацію про вибране налаштування та мову.
/create_character [STRING: name] [STRING: race] [STRING: class] [NUMBER: strength] [NUMBER: dexterity] [NUMBER: wisdom] [NUMBER: intelligence] [NUMBER: constitution] [NUMBER: charisma] [NUMBER: health] [NUMBER: gold] [NUMBER: experience] - Створює вашого персонажа.
/remove_character [STRING: character_name] - Видаляє персонажа, якого ви створили. Лише автор персонажа або ДМ може видалити персонажа.
/print_character [STRING: character_name] - Відображає інформацію про символ.
/print_inventory [STRING: character_name] - Відображає інформацію про інвентар персонажа.
/show_all_mobs - Відображає список усіх створених монстрів у цьому параметрі, а також їхнє здоров'я та значення атаки.
/set_dm - Надає вам право ДМ. Ви не можете отримати DM, якщо хтось уже має права на ДМ.
/remove_dm - Видаляє права ДМ. Використовується для передачі прав іншому користувачеві.
/roll [NUMBER: 4/6/8/10/12/20] - Кидає кубик із максимальним вибраним числом.

Команди ДМ:
/update_inventory [STRING: character_name] [STRING: add/remove] [STRING: name_of_item] [NUMBER: count_of_item] - Змінює інвентар персонажа.
/create_monster [STRING: monster_name] [NUMBER: health] [NUMBER: attack] - Створює монстра.
/attack_monster [STRING: monster_name] [NUMBER: damage] - Атакує монстра.
/change_monster_attack [STRING: monster_name] [NUMBER: ±amount] - Змінює значення атаки монстра.
/remove_character [STRING: character_name] - Видаляє персонажа. Лише автор персонажа або ДМ може видалити персонажа.
/change [STRING: character_name] [STRING: strength/dexterity/wisdom/intelligence/constitution/charisma/health/gold/experience] [NUMBER: ±amount] - Змінює деякі характеристики персонажа.

Команди адміністратора:
/change_lang [STRING: english/russian/ukrainian] - Змінює мову.
/create_setting [STRING: setting] - Створює нове сеттінг.
/change_setting [STRING: setting] - Змінює сеттінг на потрібне. Коли створюються персонажі/монстри, вони призначаються самому сеттінгу, тому під час зміни сеттінгу персонажі та монстри, створені у сеттінгу A, не будуть доступні в сеттінгу B.
/remove_setting [STRING: setting] - Видаляє сеттінг.
        '''

    await bot.send_message(chat_id=message.chat.id, text=help_str)


if __name__ == "__main__":
    while True:
        try:
            executor.start_polling(dp)
        except:
            pass
# BOT
