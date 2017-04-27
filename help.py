def help(message):
    """Returns relevant help information based on number provided.
    :return: Help text"""
    string = message.split()
    if len(string) == 1:
        text = "Hi, I'm Djeeta Bot! \n" \
               "Please use `!help number` to know more about a category. \n \n" \
               "**Commands** \n" \
               "`1. Granblue Fantasy \n" \
               "2. General Utilities`"
        return text
    elif len(string) == 2:
        if "1" in string:
            text = "**Granblue Fantasy** \n \n" \
                   "`!wiki - Performs a gbf.wiki search using the given search request. \n" \
                   "   Syntax: !wiki [Search Query] \n" \
                   "!events - Fetches the current events from http://gbf.wiki's front page. \n" \
                   "!exp - Calculates the EXP needed to reach the desired Weapon/Summon Level. Type 'char' in [Char Modifier] to calculate Character EXP instead. \n" \
                   "   Syntax: !exp [Desired Lvl] [Current Lvl] [EXP to next Lvl] [Char Modifier] \n" \
                   "!skill - Returns the suggested skill fodder based on Rarity and Current Skill Level. Rarity accepts keywords 'SR', 'SSR', 'Bahamut' and 'Seraph'. \n" \
                   "   Syntax: !skill [Rarity] [Current Skill Level]`"
            return text
        elif "2" in string:
            text = "**General Utility** \n \n" \
                   "`!google - Performs a Google search using the given search request.`"
            return text