import re
import jaconv

content_champ = "!ahri"

def change_champion_name(content_champ):
    kanchome_string = ""
    lol_champion_list = ["Aatrox", "Ahri", "Akali", "Alistar", "Amumu", "Anivia", "Annie", "Aphelios", "Ashe", "AurelionSol", "Azir", "Bard", "Blitzcrank", "Brand", "Braum", "Caitlyn", "Camille", "Cassiopeia", "ChoGath", "Corki", "Darius", "Diana", "DrMundo", "Draven", "Ekko", "Elise", "Evelynn", "Ezreal", "Fiddlesticks", "Fiora", "Fizz", "Galio", "Gangplank", "Garen", "Gnar", "Gragas", "Graves", "Gwen", "Hecarim", "Heimerdinger", "Illaoi", "Irelia", "Ivern", "Janna", "JarvanIV", "Jax", "Jayce", "Jhin", "Jinx", "KaiSa", "Kalista", "Karma", "Karthus", "Kassadin", "Katarina", "Kayle", "Kayn", "Kennen", "KhaZix", "Kindred", "Kled", "KogMaw", "LeBlanc", "LeeSin", "Leona", "Lillia", "Lissandra", "Lucian", "Lulu", "Lux", "Malphite", "Malzahar", "Maokai", "MasterYi", "MissFortune", "Mordekaiser", "Morgana", "Nami", "Nasus", "Nautilus", "Neeko", "Nidalee", "Nocturne", "Nunu", "Olaf", "Orianna", "Ornn", "Pantheon", "Poppy", "Pyke", "Qiyana", "Quinn", "Rakan", "Rammus", "RekSai", "Rell", "Renekton", "Rengar", "Riven", "Rumble", "Ryze", "Samira", "Sejuani", "Senna", "Seraphine", "Sett", "Shaco", "Shen", "Shyvana", "Singed", "Sion", "Sivir", "Skarner", "Sona", "Soraka", "Swain", "Sylas", "Syndra", "TahmKench", "Taliyah", "Talon", "Taric", "Teemo", "Thresh", "Tristana", "Trundle", "Tryndamere", "TwistedFate", "Twitch", "Udyr", "Urgot", "Varus", "Vayne", "Veigar", "VelKoz", "Vi", "Viego", "Viktor", "Vladimir", "Volibear", "Warwick", "monkeyking", "Xayah", "Xerath", "XinZhao", "Yasuo", "Yone", "Yorick", "Yuumi", "Zac", "Zed", "Ziggs", "Zilean", "Zoe", "Zyra"]
    content_champ = jaconv.kata2hira(content_champ)
    content_champ = re.sub("aatrox|えいとろくっす|えいとろ", "Aatrox", content_champ)
    content_champ = re.sub("ahri|あーり", "Ahri", content_champ)
    content_champ = re.sub("akali|あかり", "Akali", content_champ)
    content_champ = re.sub("alistar|ありすたー", "Alistar", content_champ)
    content_champ = re.sub("amumu|あむむ", "Amumu", content_champ)
    content_champ = re.sub("anivia|あにびあ", "Anivia", content_champ)
    content_champ = re.sub("あにー", "Annie", content_champ)
    content_champ = re.sub("あふぇ", "Aphelios", content_champ)
    content_champ = re.sub("あっしゅ|あしぇ", "Ashe", content_champ)
    content_champ = re.sub("おれそる|おれりおんそる", "AurelionSol", content_champ)
    content_champ = re.sub("あじーる|うらじみーる", "Azir", content_champ)
    content_champ = re.sub("ばーど", "Bard", content_champ)
    content_champ = re.sub("ぶりっつくらんく", "Blitzcrank", content_champ)
    content_champ = re.sub("ぶらんど", "Brand", content_champ)
    content_champ = re.sub("ぶらうむ", "Braum", content_champ)
    content_champ = re.sub("けいとりん", "Caitlyn", content_champ)
    content_champ = re.sub("かみーる", "Camille", content_champ)
    content_champ = re.sub("かしおぺあ", "Cassiopeia", content_champ)
    content_champ = re.sub("ちょがす|ちょ=がす", "ChoGath", content_champ)
    content_champ = re.sub("こーき", "Corki", content_champ)
    content_champ = re.sub("だりうす", "Darius", content_champ)
    content_champ = re.sub("だいあな", "Diana", content_champ)
    content_champ = re.sub("どくたーむんど|むんど", "DrMundo", content_champ)
    content_champ = re.sub("どれいぶん", "Draven", content_champ)
    content_champ = re.sub("えこー", "Ekko", content_champ)
    content_champ = re.sub("えりす", "Elise", content_champ)
    content_champ = re.sub("いぶりん", "Evelynn", content_champ)
    content_champ = re.sub("えずりある|えず", "Ezreal", content_champ)
    content_champ = re.sub("ふぃどるすてぃっく|ふぃどる", "Fiddlesticks", content_champ)
    content_champ = re.sub("ふぃおら", "Fiora", content_champ)
    content_champ = re.sub("ふぃず", "Fizz", content_champ)
    content_champ = re.sub("がりお", "Galio", content_champ)
    content_champ = re.sub("がんくぷらんく", "Gangplank", content_champ)
    content_champ = re.sub("がれん", "Garen", content_champ)
    content_champ = re.sub("なー", "Gnar", content_champ)
    content_champ = re.sub("ぐらがす", "Gragas", content_champ)
    content_champ = re.sub("ぐれいぶす", "Graves", content_champ)
    content_champ = re.sub("ぐうぇん|はさみおんな", "Gwen", content_champ)
    content_champ = re.sub("へかりむ", "Hecarim", content_champ)
    content_champ = re.sub("はいまーでぃんがー|はいまー", "Heimerdinger", content_champ)
    content_champ = re.sub("いらおい|吉田沙保里", "Illaoi", content_champ)
    content_champ = re.sub("いれりあ", "Irelia", content_champ)
    content_champ = re.sub("あいばーん", "Ivern", content_champ)
    content_champ = re.sub("じゃんな", "Janna", content_champ)
    content_champ = re.sub("じゃーばんIV|じゃーばん", "JarvanIV", content_champ)
    content_champ = re.sub("じゃっくす", "Jax", content_champ)
    content_champ = re.sub("じぇいす", "Jayce", content_champ)
    content_champ = re.sub("じんくす", "Jinx", content_champ)
    content_champ = re.sub("じん", "Jhin", content_champ)
    content_champ = re.sub("かいさ|かい＝さ", "KaiSa", content_champ)
    content_champ = re.sub("かりすた", "Kalista", content_champ)
    content_champ = re.sub("かるま", "Karma", content_champ)
    content_champ = re.sub("かーさす", "Karthus", content_champ)
    content_champ = re.sub("かさでぃん", "Kassadin", content_champ)
    content_champ = re.sub("かたりな", "Katarina", content_champ)
    content_champ = re.sub("けいる", "Kayle", content_champ)
    content_champ = re.sub("けいん", "Kayn", content_champ)
    content_champ = re.sub("けねん", "Kennen", content_champ)
    content_champ = re.sub("か＝じっくす|かじっくす", "KhaZix", content_champ)
    content_champ = re.sub("きんどれっど|きんど", "Kindred", content_champ)
    content_champ = re.sub("くれっど", "Kled", content_champ)
    content_champ = re.sub("こぐ＝まう|こぐまう|こぐ", "KogMaw", content_champ)
    content_champ = re.sub("るぶらん|る＝ぶらん", "LeBlanc", content_champ)
    content_champ = re.sub("りーしん|りー・しん", "LeeSin", content_champ)
    content_champ = re.sub("れおな|くそおんな", "Leona", content_champ)
    content_champ = re.sub("りりあ", "Lillia", content_champ)
    content_champ = re.sub("りさんどら", "Lissandra", content_champ)
    content_champ = re.sub("るしあん", "Lucian", content_champ)
    content_champ = re.sub("るる", "Lulu", content_champ)
    content_champ = re.sub("らっくす", "Lux", content_champ)
    content_champ = re.sub("まるふぁいと", "Malphite", content_champ)
    content_champ = re.sub("まるざはーる", "Malzahar", content_champ)
    content_champ = re.sub("まおかい", "Maokai", content_champ)
    content_champ = re.sub("ますたーいー|いー", "MasterYi", content_champ)
    content_champ = re.sub("みすふぉーちゅん|ふぉーちゅん", "MissFortune", content_champ)
    content_champ = re.sub("もるでかいざー|もるで", "Mordekaiser", content_champ)
    content_champ = re.sub("もるがな", "Morgana", content_champ)
    content_champ = re.sub("なみ", "Nami", content_champ)
    content_champ = re.sub("なさす", "Nasus", content_champ)
    content_champ = re.sub("のーちらす", "Nautilus", content_champ)
    content_champ = re.sub("にーこ", "Neeko", content_champ)
    content_champ = re.sub("にだりー", "Nidalee", content_champ)
    content_champ = re.sub("のくたーん|のく", "Nocturne", content_champ)
    content_champ = re.sub("ぬぬ", "Nunu", content_champ)
    content_champ = re.sub("おらふ", "Olaf", content_champ)
    content_champ = re.sub("おりあな|おりあんな", "Orianna", content_champ)
    content_champ = re.sub("おーん|かじしんのよびごえ", "Ornn", content_champ)
    content_champ = re.sub("ぱんておん", "Pantheon", content_champ)
    content_champ = re.sub("ぽっぴー", "Poppy", content_champ)
    content_champ = re.sub("ぱいく|ぺぇく", "Pyke", content_champ)
    content_champ = re.sub("きあな|きやな", "Qiyana", content_champ)
    content_champ = re.sub("くいーん|くいん", "Quinn", content_champ)
    content_champ = re.sub("らかん", "Rakan", content_champ)
    content_champ = re.sub("らむす", "Rammus", content_champ)
    content_champ = re.sub("れくさい|れく=さい", "RekSai", content_champ)
    content_champ = re.sub("れる", "Rell", content_champ)
    content_champ = re.sub("れねくとん|れねく", "Renekton", content_champ)
    content_champ = re.sub("れんがー", "Rengar", content_champ)
    content_champ = re.sub("りべん", "Riven", content_champ)
    content_champ = re.sub("らんぶる", "Rumble", content_champ)
    content_champ = re.sub("らいず", "Ryze", content_champ)
    content_champ = re.sub("さみーら", "Samira", content_champ)
    content_champ = re.sub("せじゅあに|せじゅ", "Sejuani", content_champ)
    content_champ = re.sub("せな", "Senna", content_champ)
    content_champ = re.sub("せらふぃーん", "Seraphine", content_champ)
    content_champ = re.sub("せと", "Sett", content_champ)
    content_champ = re.sub("しゃこ", "Shaco", content_champ)
    content_champ = re.sub("しぇん", "Shen", content_champ)
    content_champ = re.sub("しばーな|しゔぁーな", "Shyvana", content_champ)
    content_champ = re.sub("しんじど|はげぱんちまん", "Singed", content_champ)
    content_champ = re.sub("さいおん", "Sion", content_champ)
    content_champ = re.sub("しゔぃあ", "Sivir", content_champ)
    content_champ = re.sub("すかーな", "Skarner", content_champ)
    content_champ = re.sub("そな", "Sona", content_champ)
    content_champ = re.sub("そらか", "Soraka", content_champ)
    content_champ = re.sub("すうぇいん", "Swain", content_champ)
    content_champ = re.sub("さいらす", "Sylas", content_champ)
    content_champ = re.sub("しんどら", "Syndra", content_champ)
    content_champ = re.sub("たむけんち|たむ=けんち|たむけん", "TahmKench", content_champ)
    content_champ = re.sub("たりあ|たりや", "Taliyah", content_champ)
    content_champ = re.sub("たろん", "Talon", content_champ)
    content_champ = re.sub("たりっく", "Taric", content_champ)
    content_champ = re.sub("てぃーも", "Teemo", content_champ)
    content_champ = re.sub("すれっしゅ", "Thresh", content_champ)
    content_champ = re.sub("とりすたーな|とりす", "Tristana", content_champ)
    content_champ = re.sub("とらんどる", "Trundle", content_champ)
    content_champ = re.sub("とりんだめあ", "Tryndamere", content_champ)
    content_champ = re.sub("つぃすてっど・ふぇいと|つぃすてっどふぇいと|ふぇいと|TF", "TwistedFate", content_champ)
    content_champ = re.sub("つうぃっち|ついっち", "Twitch", content_champ)
    content_champ = re.sub("うでぃあ|うでぃーる", "Udyr", content_champ)
    content_champ = re.sub("あーごっと|あーごっど", "Urgot", content_champ)
    content_champ = re.sub("ゔぁるす", "Varus", content_champ)
    content_champ = re.sub("ゔぇいん", "Vayne", content_champ)
    content_champ = re.sub("ゔぇいがー|べいがー", "Veigar", content_champ)
    content_champ = re.sub("ゔぇるこず|ゔぇる=こず", "VelKoz", content_champ)
    content_champ = re.sub("ゔぁい", "Vi", content_champ)
    content_champ = re.sub("ゔぇいご", "Viego", content_champ)
    content_champ = re.sub("びくたー|ゔぃくたー", "Viktor", content_champ)
    content_champ = re.sub("ぶらっどみあ|ぶらっど", "Vladimir", content_champ)
    content_champ = re.sub("ぼりべあ", "Volibear", content_champ)
    content_champ = re.sub("わーうぃっく", "Warwick", content_champ)
    content_champ = re.sub("うーこんぐ|うーこん", "Wukong", content_champ)
    content_champ = re.sub("ざや", "Xayah", content_champ)
    content_champ = re.sub("ぜらす", "Xerath", content_champ)
    content_champ = re.sub("しんじゃお|しん=じゃお", "XinZhao", content_champ)
    content_champ = re.sub("やすお", "Yasuo", content_champ)
    content_champ = re.sub("よね", "Yone", content_champ)
    content_champ = re.sub("よりっく", "Yorick", content_champ)
    content_champ = re.sub("ゆーみ", "Yuumi", content_champ)
    content_champ = re.sub("ざっく", "Zac", content_champ)
    content_champ = re.sub("ぜど", "Zed", content_champ)
    content_champ = re.sub("じぐす", "Ziggs", content_champ)
    content_champ = re.sub("じりあん", "Zilean", content_champ)
    content_champ = re.sub("ぞーい", "Zoe", content_champ)
    content_champ = re.sub("ざいら|せかいいちかわいいおんなのこ|いばらのゆりかご|茨のゆりかご|茨の楽園", "Zyra", content_champ)
    for champion_name in lol_champion_list:
        if content_champ == "!" + champion_name:
            kanchome_string = "https://jp.op.gg/champion/" + champion_name + "/statistics/"
    return kanchome_string
