# Djeeta.py
A bot made using Rapptz's Discord API. Made for the intention of practicing Python, as well as providing utility to Granblue Fantasy players. Mostly for my own personal use. Currently Utilizes the following libraries:

    discord
    asyncio
    json
    requests
    "datetime" from package datetime
    "timezone" from package pytz
    
Djeeta can perform the following actions from the following categories:
    
**Granblue Fantasy:**

    !wiki - Performs a http://gbf.wiki search using the given query.
        Syntax: !wiki [Search Query]
    !exp - Calculates the EXP needed to reach the desired Weapon/Summon Level. 
        Type 'char' into the [Char] to calculate Character EXP instead.
        Syntax: !exp [Desired Lvl] [Current Lvl] [EXP to next Lvl] [Char]
    !skill - Returns the suggested skill fodder based on Rarity and Current Skill Level. 
        Rarity accepts keywords 'SR', 'SSR', 'Bahamut' and 'Seraph'.
        Syntax: !skill [Rarity] [Current Skill Level]
    !events - Fetches the current events from http://gbf.wiki, and returns them.
    !servertime - Return the current Server Time.
    
**General Utility:**
    
    !google - Performs a http://www.google.com search using the given query. Returns the relevant URL.

Special Thanks to the following for assisting me:

    @Nyaskpi
