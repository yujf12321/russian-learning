from flask import Flask, render_template, jsonify, request 
import json
import os

app = Flask(__name__)

def load_articles():
    """从JSON文件加载文章数据"""
    try:
        with open('data/articles.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def load_translations():
    """从JSON文件加载翻译词典"""
    try:
        with open('data/translations.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# 确保data目录存在
def ensure_data_directory():
    if not os.path.exists('data'):
        os.makedirs('data')

# 初始化数据文件（如果不存在）
def init_data_files():
    ensure_data_directory()
    
    # 如果文章文件不存在，创建默认文章
    if not os.path.exists('data/articles.json'):
        default_articles = [
            {
                "id": 1,
                "title": "Путешествие в Санкт-Петербург",
                "content": """Санкт-Петербург - один из самых красивых городов мира. Его часто называют культурной столицей России. Город был основан Петром Первым в 1703 году и более двухсот лет был столицей Российской империи.

В Санкт-Петербурге находится множество известных достопримечательностей. Эрмитаж, расположенный в Зимнем дворце, является одним из крупнейших музеев мира. В его коллекции представлены шедевры Леонардо да Винчи, Рафаэля, Рембрандта и других великих художников.

Петергоф, известный как "Русский Версаль", поражает своими фонтанами и садами. Каждый год тысячи туристов приезжают сюда, чтобы увидеть знаменитый Большой каскад и полюбоваться видом на Финский залив.

Невский проспект - главная улица города. Здесь можно увидеть Казанский собор, храм Спаса на Крови и множество других исторических зданий. Вечером, когда включается подсветка, город выглядит особенно прекрасно.

В Санкт-Петербурге также много театров. Мариинский театр известен во всём мире своими балетными и оперными постановками. Каждый год здесь проходит международный фестиваль "Звёзды белых ночей".""",
                "translation": """圣彼得堡是世界上最美丽的城市之一。它常被称为俄罗斯的文化之都。这座城市由彼得大帝于1703年建立，在超过两百年的时间里一直是俄罗斯帝国的首都。

圣彼得堡拥有众多著名的景点。位于冬宫的艾尔米塔什博物馆是世界上最大的博物馆之一。其收藏包括达芬奇、拉斐尔、伦勃朗等伟大艺术家的杰作。

彼得宫城被称为"俄罗斯的凡尔赛宫"，以其喷泉和花园而闻名。每年都有成千上万的游客来到这里，欣赏著名的大瀑布和芬兰湾的景色。

涅瓦大街是这座城市的主要街道。在这里可以看到喀山大教堂、救世主滴血教堂和许多其他历史建筑。当夜幕降临，灯光亮起时，这座城市显得格外美丽。

圣彼得堡还拥有众多剧院。马林斯基剧院以其芭蕾舞和歌剧表演而闻名于世。每年这里都会举办"白夜之星"国际艺术节。"""
            }
        ]
        with open('data/articles.json', 'w', encoding='utf-8') as f:
            json.dump(default_articles, f, ensure_ascii=False, indent=4)
    
    # 如果翻译文件不存在，创建默认翻译词典
    if not os.path.exists('data/translations.json'):
        default_translations = {
            "Санкт-Петербург": "圣彼得堡",
            "культурной": "文化的",
            "столицей": "首都",
            "основан": "建立",
            "достопримечательностей": "景点",
            "Эрмитаж": "艾尔米塔什博物馆",
            "расположенный": "位于",
            "дворце": "宫殿",
            "крупнейших": "最大的",
            "музеев": "博物馆",
            "коллекции": "收藏",
            "шедевры": "杰作",
            "фонтанами": "喷泉",
            "садами": "花园",
            "туристов": "游客",
            "каскад": "瀑布",
            "проспект": "大街",
            "собор": "大教堂",
            "храм": "教堂",
            "театров": "剧院",
            "балетными": "芭蕾舞",
            "оперными": "歌剧",
            "постановками": "表演",
            "фестиваль": "艺术节"
        }
        with open('data/translations.json', 'w', encoding='utf-8') as f:
            json.dump(default_translations, f, ensure_ascii=False, indent=4)

# 初始化数据文件
init_data_files()

@app.route('/')
def index():
    """渲染主页，显示文章列表"""
    articles = load_articles()
    return render_template('index.html', articles=articles)

@app.route('/translate', methods=['POST'])
def translate():
    """处理单词翻译请求"""
    word = request.json.get('word', '')
    translations = load_translations()
    translation = translations.get(word, '')
    return jsonify({'translation': translation})

if __name__ == '__main__':
    app.run(debug=True) 