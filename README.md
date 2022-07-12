# DnD_bot
This a telegram bot for convenient DnD play.

## Installation
1) Install 'aiogram'.
2) Download the project to any place convenient for you.
3) Fill in the config.ini token and administrator ID.

## How to start
1) Add a bot to your conference.
2) Grant him administrator rights.
3) Create your first setting with the /create_setting command.
4) Select this setting with the /change_setting command.
5) Now you can create characters and monsters. See details below!

## Commands
### Player commands
Command | Arguments | Information
--- | --- | ---
/help | None | Shows a help message.
/info | None | Displays information about the selected setting and language.
/create_character | [STRING: name] [STRING: race] [STRING: class] [NUMBER: strength] [NUMBER: dexterity] [NUMBER: wisdom] [NUMBER: intelligence] [NUMBER: constitution] [NUMBER: charisma] [NUMBER: health] [NUMBER: gold] [NUMBER: experience] | Creates your character.
/remove_character | [STRING: character_name] | Deletes a character you've created. Only the creator or DM can delete a character.
/print_character | [STRING: character_name] | Displays information about the character.
/print_inventory | [STRING: character_name] | Displays information about the character's inventory.
/show_all_mobs | None | Displays a list of all created monsters in this setting, as well as their health and attack values.
/set_dm | None | Grants you the DM right. You cannot get DM if someone already has DM rights.
/remove_dm | None | Removes DM rights. Used to transfer rights to another user.
/roll | [NUMBER: 4/6/8/10/12/20] | Rolls the die with the maximum selected number.

### DM commands
Command | Arguments | Information
--- | --- | ---
/update_inventory | [STRING: character_name] [STRING: add/remove] [STRING: name_of_item] [NUMBER: count_of_item] | Changes the character's inventory.
/create_monster | [STRING: monster_name] [NUMBER: health] [NUMBER: attack] | Creates a monster.
/attack_monster | [STRING: monster_name] [NUMBER: damage] | Attacks a monster.
/change_monster_attack | [STRING: monster_name] [NUMBER: ±amount] | Changes the monster's attack value.
/remove_character | [STRING: character_name] | Deletes a character. Only the creator or DM can delete a character.
/change | [STRING: character_name] [STRING: strength/dexterity/wisdom/intelligence/constitution/charisma/health/gold/experience] [NUMBER: ±amount] | Changes some characteristics of the character.

### Admin commands
Command | Arguments | Information
--- | --- | ---
/change_lang | [STRING: english/russian/ukrainian] | Changes the language.
/create_setting | [STRING: setting] | Creates a new setting.
/change_setting | [STRING: setting] | Changes the setting to the desired one. When characters/monsters are created, they are assigned to the setting itself, so when changing the setting, characters and monsters that were created in setting A will not be available in setting B.
/remove_setting | [STRING: setting] | Deletes the setting.
