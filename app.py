from flask import Flask, jsonify
from flask_cors import CORS
import random
from slugify import slufigy

app = Flask(__name__)
CORS(app)

quotes = [
    {"text": "Keep thy mind in hell, and despair not.", "author": "St. Silouan the Athonite", "author_slug": "st-silouan-the-athonite", "tags": ["spirituality", "resilience"]},
    {"text": "Animus debes mutare, non caelum.", "author": "Lucio Anneo Seneca", "author_slug": "lucio-anneo-seneca", "tags": ["philosophy", "self-improvement"]},
    {"text": "The challenge is to resist circumstances. Any idiot can be happy in a happy place, but moral courage is required to be happy in a hellhole.", "author": "Joyce Carol Oates", "author_slug": "joyce-carol-oates", "tags": ["courage", "resilience"]},
    {"text": "Man is an animal, and his happiness depends upon his physiology more than he likes to think. This is a humble conclusion, but I cannot make myself disbelieve it. Unhappy businessmen, I am convinced, would increase their happiness more by walking six miles every day than by any conceivable change of philosophy.", "author": "Bertrand Russell", "author_slug": "bertrand-russell", "tags": ["philosophy", "happiness"]},
    {"text": "Not one of us knows what effect his life produces, and what he gives to others; that is hidden from us and must remain so, though we are often allowed to see some little fraction of it, so that we may not lose courage. The way in which power works is a mystery.", "author": "Albert Schweitzer", "author_slug": "albert-schweitzer", "tags": ["life", "mystery"]},
    {"text": "Man is a rational animal — so at least I have been told. Throughout a long life, I have looked diligently for evidence in favor of this statement, but so far I have not had the good fortune to come across it.", "author": "Bertrand Russell", "author_slug": "bertrand-russell", "tags": ["philosophy", "humanity"]},
    {"text": "There is no man, however wise, who has not at some period in his youth said things, or lived in a way the consciousness of which is so unpleasant to him in later life that he would gladly, if he could, expunge it from his memory.", "author": "Marcel Proust", "author_slug": "marcel-proust", "tags": ["wisdom", "memory"]},
    {"text": "Modern man is afraid of silence because in silence he might hear God.", "author": "Metropolitan Tikhon Shevkunov", "author_slug": "metropolitan-tikhon-shevkunov", "tags": ["spirituality", "silence"]},
    {"text": "We are as forlorn as children lost in the woods. When you stand in front of me and look at me, what do you know of the griefs that are in me and what do I know of yours? And if I were to cast myself down before you and weep and tell you, what more would you know about me than you know about Hell when someone tells you it is hot and dreadful? For that reason alone we human beings ought to stand before one another as reverently, as reflectively, as lovingly, as we would before the entrance to Hell.", "author": "Franz Kafka", "author_slug": "franz-kafka", "tags": ["humanity", "empathy"]},
    {"text": "There are no ordinary people. You have never talked to a mere mortal. Nations, cultures, arts, civilizations - these are mortal, and their life is to ours as the life of a gnat. But it is immortals whom we joke with, work with, marry, snub and exploit - immortal horrors or everlasting splendors.", "author": "C.S. Lewis", "author_slug": "cs-lewis", "tags": ["spirituality", "humanity"]},
    {"text": "None of us has all the qualities to be a good observer of his age.", "author": "George Kennan", "author_slug": "george-kennan", "tags": ["wisdom", "observation"]},
    {"text": "It is the task of the university to prepare men for the formation of their prejudices, not to impregnate them with its own.", "author": "George Kennan", "author_slug": "george-kennan", "tags": ["education", "philosophy"]},
    {"text": "Ce ne sont que les Français qui puissent faire une si belle ruine.", "author": "George Kennan’s German uncle", "author_slug": "george-kennans-german-uncle", "tags": ["culture", "humor"]},
    {"text": "I suddenly became aware that I had a reputable and appointed place in the proceedings: I was now responsible for the well-being of others. For this reason, I was something more than my usual self. I no longer had to relate myself to others as a species of naked intruder on the human scene. I had a role to play, a useful, necessary, legitimate role, helpful to others, requiring no justification or apology.", "author": "George Kennan", "author_slug": "george-kennan", "tags": ["fatherhood", "responsibility"]},
    {"text": "Dearest, I beg of you, sleep properly and go for walks.", "author": "Franz Kafka", "author_slug": "franz-kafka", "tags": ["care", "well-being"]},
    {"text": "For the Christians are distinguished from other men neither by country, nor language, nor the customs which they observe. For they neither inhabit cities of their own, nor employ a peculiar form of speech, nor lead a life which is marked out by any singularity.", "author": "The Epistle of Mathetes to Diognetus", "author_slug": "the-epistle-of-mathetes-to-diognetus", "tags": ["spirituality", "identity"]},
    {"text": "An honest man falls in love with an honest woman; he wishes, therefore to marry her, to be the father of her children, to secure her and himself. All systems of government should be tested by whether he can do this.", "author": "G.K. Chesterton", "author_slug": "gk-chesterton", "tags": ["family", "justice"]},
    {"text": "If you’re afraid, you’re already a slave.", "author": "Grzegorz Braun", "author_slug": "grzegorz-braun", "tags": ["courage", "freedom"]},
    {"text": "It is sometimes so bitterly cold in the winter that one says, 'The cold is too awful for me to care whether summer is coming or not; the harm outdoes the good.' But with or without our approval, the severe weather does come to an end eventually and one fine morning the wind changes and there is a thaw.", "author": "Vincent Van Gogh", "author_slug": "vincent-van-gogh", "tags": ["hope", "resilience"]},
    {"text": "How often people speak of art and science as though they were two entirely different things, with no interconnection. An artist is emotional, they think, and uses only his intuition; he sees all at once and has no need of reason. A scientist is cold, they think, and uses only his reason; he argues carefully step by step, and needs no imagination. That is all wrong.", "author": "Isaac Asimov", "author_slug": "isaac-asimov", "tags": ["art", "science"]},
    {"text": "In the middle of the journey of our life I came to myself within a dark wood where the straight way was lost. Ah, how hard a thing it is to tell what a wild, and rough, and stubborn wood this was, which in my thought renews the fear!", "author": "Dante Alighieri", "author_slug": "dante-alighieri", "tags": ["life", "struggle"]},
    {"text": "There is no path. The path is made by walking.", "author": "Antonio Machado", "author_slug": "antonio-machado", "tags": ["life", "action"]},
    {"text": "Blessed is that man who finds his work", "author": "Thomas Carlyle", "author_slug": "thomas-carlyle", "tags": ["work", "purpose"]},
    {"text": "Those who will not slip beneath the still surface on the well of grief, turning down through its black water to the place we cannot breathe, will never know the source from which we drink, the secret water, cold and clear, nor find in the darkness glimmering, the small round coins, thrown by those who wished for something else.", "author": "David Whyte", "author_slug": "david-whyte", "tags": ["grief", "wisdom"]},
    {"text": "My religious belief teaches me to feel as safe in battle as in bed. God has fixed the time for my death. I do not concern myself about that, but to be always ready, no matter when it may overtake me.", "author": "Stonewall Jackson", "author_slug": "stonewall-jackson", "tags": ["faith", "courage"]},
    {"text": "Stand at the brink of despair, and when you see that you cannot bear it anymore, draw back a little, and have a cup of tea.", "author": "Sophrony Sakharov", "author_slug": "sophrony-sakharov", "tags": ["resilience", "spirituality"]},
    {"text": "Gradually it was disclosed to me that the line separating good and evil passes not through states, nor between classes, nor between political parties either—but right through every human heart—and through all human hearts.", "author": "Aleksandr Solzhenitsyn", "author_slug": "aleksandr-solzhenitsyn", "tags": ["morality", "humanity"]},
    {"text": "Man, as long as he lives, must always struggle. And his first fight is to defeat himself.", "author": "St. Ephraim of Katounakia", "author_slug": "st-ephraim-of-katounakia", "tags": ["spirituality", "struggle"]},
    {"text": "Since limits make us what we are, the idea of absolute freedom is bound to be terroristic.", "author": "Terry Eagleton", "author_slug": "terry-eagleton", "tags": ["philosophy", "freedom"]},
    {"text": "People in those old times had convictions; we moderns only have opinions. And it needs more than a mere opinion to erect a Gothic cathedral.", "author": "Heinrich Heine", "author_slug": "heinrich-heine", "tags": ["conviction", "history"]},
    {"text": "The freedom to love presupposes the responsibility to be a channel of reconciliation.", "author": "Stavros Kofinas", "author_slug": "stavros-kofinas", "tags": ["love", "responsibility"]},
    {"text": "A man who is unable to bear chastisement is unable to be healed.", "author": "Fr Paul Truebenbach", "author_slug": "fr-paul-truebenbach", "tags": ["spirituality", "healing"]},
    {"text": "If the world is against the truth, then I am against the world.", "author": "St. Athanasios the Great", "author_slug": "st-athanasios-the-great", "tags": ["truth", "faith"]},
    {"text": "When one falsity has been let in, infinite others follow.", "author": "Baruch Spinoza", "author_slug": "baruch-spinoza", "tags": ["truth", "philosophy"]},
    {"text": "Before you act, you should pray, for action before prayer is pride.", "author": "St. Paisios of Mt. Athos", "author_slug": "st-paisios-of-mt-athos", "tags": ["spirituality", "humility"]},
    {"text": "Nobody is equal to anybody. Even the same man is not equal to himself on different days.", "author": "Thomas Sowell", "author_slug": "thomas-sowell", "tags": ["equality", "individuality"]},
    {"text": "The same Greek word (pathos) that is translated as suffering can also mean the passions (e.g., anger, lust, pride, despair).", "author": "Daniel B. Hinshaw", "author_slug": "daniel-b-hinshaw", "tags": ["language", "spirituality"]},
    {"text": "Be at peace with your soul and heaven and earth will be at peace with you. Endeavor to enter the treasury within you and you will see the treasury which is in heaven…The ladder of that kingdom is hidden…within your soul.", "author": "St. Isaac of Nineveh", "author_slug": "st-isaac-of-nineveh", "tags": ["spirituality", "peace"]},
    {"text": "The doing of things from duty is but a stage on the road to the kingdom of truth and love.", "author": "George MacDonald", "author_slug": "george-macdonald", "tags": ["duty", "love"]},
    {"text": "‘I have led a toothless life,' he thought. 'A toothless life. I have never bitten into anything. I was waiting. I was reserving myself for later on—and I have just noticed that my teeth have gone.’", "author": "Jean-Paul Sartre", "author_slug": "jean-paul-sartre", "tags": ["life", "regret"]},
    {"text": "It is the habit of tyrants to prefer the company of aliens. Citizens they feel are enemies, but aliens will offer no opposition.", "author": "Aristotle", "author_slug": "aristotle", "tags": ["politics", "tyranny"]},
    {"text": "However, he who makes himself a worm cannot complain afterwards that he gets stepped on.", "author": "Immanuel Kant", "author_slug": "immanuel-kant", "tags": ["responsibility", "philosophy"]},
    {"text": "These are days when the Christian is expected to praise every creed but his own.", "author": "G.K. Chesterton", "author_slug": "gk-chesterton", "tags": ["faith", "culture"]},
    {"text": "Tolerance is the virtue of people who do not believe in anything.", "author": "G.K. Chesterton", "author_slug": "gk-chesterton", "tags": ["tolerance", "belief"]},
    {"text": "Just as the tadpole already breathes, though with different organs from those of the frog, so the child acts like the adult, but employing a mentality whose structure varies according to the stages of its development.", "author": "Jean Piaget", "author_slug": "jean-piaget", "tags": ["development", "psychology"]},
    {"text": "The patient should give some indication of wanting not only change but to change, that is, of dissatisfaction with something that resides in the self.", "author": "Otto Kernberg", "author_slug": "otto-kernberg", "tags": ["psychology", "change"]},
    {"text": "The goal is not simply to avoid sin but to rise spiritually.", "author": "Saint Paisios", "author_slug": "saint-paisios", "tags": ["spirituality", "growth"]},
    {"text": "Tradition is not the worship of ashes, but the preservation of fire.", "author": "Roman Maxim", "author_slug": "roman-maxim", "tags": ["tradition", "wisdom"]},
    {"text": "There are always plenty of rivals to our work. We are always falling in love or quarreling, looking for jobs or fearing to lose them, getting ill and recovering, following public affairs. If we let ourselves, we shall always be waiting for some distraction or other to end before we can really get down to our work.", "author": "C.S. Lewis", "author_slug": "cs-lewis", "tags": ["work", "focus"]},
    {"text": "There is a God-shaped vacuum in every man that only Christ can fill.", "author": "St. Augustine", "author_slug": "st-augustine", "tags": ["spirituality", "faith"]},
    {"text": "The soul is healed by being with children.", "author": "Fyodor Dostoevsky", "author_slug": "fyodor-dostoevsky", "tags": ["children", "healing"]},
    {"text": "When you pray to God in time of temptation do not say, 'Take this or that away from me', but pray like this: 'O Jesus Christ, sovereign Master, help me and do not let me sin against Thee...'", "author": "Abba Isaiah", "author_slug": "abba-isaiah", "tags": ["prayer", "spirituality"]},
    {"text": "We must not mind insulting men, if by respecting them we offend God.", "author": "St. John Chrysostom", "author_slug": "st-john-chrysostom", "tags": ["faith", "courage"]},
    {"text": "No matter how just your words may be, you ruin everything when you speak with anger.", "author": "St. John Chrysostom", "author_slug": "st-john-chrysostom", "tags": ["anger", "wisdom"]},
    {"text": "There are two kinds of truth: the truth that lights the way and the truth that warms the heart. The first of these is science, and the second is art. Neither is independent of the other or more important than the other.", "author": "Raymond Chandler", "author_slug": "raymond-chandler", "tags": ["truth", "art", "science"]},
    {"text": "Everything written with vitality expresses that vitality: there are no dull subjects, only dull minds.", "author": "Raymond Chandler", "author_slug": "raymond-chandler", "tags": ["writing", "vitality"]},
    {"text": "I remember a psychiatrist telling me that I gamble in order to escape the reality of life, and I told him that’s why everyone does everything.", "author": "Norm MacDonald", "author_slug": "norm-macdonald", "tags": ["life", "humor"]},
    {"text": "The only thing an old man can tell a young man is that it goes fast, real fast, and if you’re not careful it’s too late. Of course, the young man will never understand this truth.", "author": "Norm MacDonald", "author_slug": "norm-macdonald", "tags": ["life", "time"]},
    {"text": "No one can heal my disease except He Who knows the depths of the heart.", "author": "St. Ephraim the Syrian", "author_slug": "st-ephraim-the-syrian", "tags": ["spirituality", "healing"]},
    {"text": "A healthy person has a thousand dreams but a sick person has only one dream.", "author": "Robert F. Kennedy Jr.", "author_slug": "robert-f-kennedy-jr", "tags": ["health", "dreams"]},
    {"text": "There’s no vocabulary For love within a family, love that’s lived in But not looked at, love within the light of which All else is seen, the love within which All other love finds speech. This love is silent.", "author": "T.S. Eliot", "author_slug": "ts-eliot", "tags": ["love", "family"]},
    {"text": "Mystery does not imply muddled thinking. On the other hand, thinking you could be clear about something which in its nature is essentially mysterious is muddled thinking.", "author": "Iain McGilchrist", "author_slug": "iain-mcgilchrist", "tags": ["mystery", "philosophy"]},
    {"text": "What did you do as a child that made the hours pass like minutes? Herein lies the key to your earthly pursuits.", "author": "Carl Jung", "author_slug": "carl-jung", "tags": ["purpose", "psychology"]},
    {"text": "Abstract love of humanity is nearly always love of self.", "author": "Fyodor Dostoevsky", "author_slug": "fyodor-dostoevsky", "tags": ["love", "self"]},
    {"text": "To try too hard to make people good, is one way to make them worse; … the only way to make them good is to be good—remembering well the beam and the mote.", "author": "George MacDonald", "author_slug": "george-macdonald", "tags": ["goodness", "example"]},
    {"text": "Marriage is a matter of justice for children.", "author": "Katy Faust", "author_slug": "katy-faust", "tags": ["marriage", "justice"]},
    {"text": "There is no coming to consciousness without pain.", "author": "Carl Jung", "author_slug": "carl-jung", "tags": ["consciousness", "pain"]},
    {"text": "Let everything happen to you: beauty and terror. Just keep going. No feeling is final.", "author": "Rainer Maria Rilke", "author_slug": "rainer-maria-rilke", "tags": ["life", "resilience"]},
    {"text": "Man is fond of counting his troubles, but he does not count his joys.", "author": "Fyodor Dostoevsky", "author_slug": "fyodor-dostoevsky", "tags": ["happiness", "perspective"]},
    {"text": "We do not merely study the past: we inherit it, and inheritance brings with it not only the rights of ownership, but the duties of trusteeship.", "author": "Roger Scruton", "author_slug": "roger-scruton", "tags": ["history", "responsibility"]},
    {"text": "My argument against God was that the universe seemed so cruel and unjust. But how had I got this idea of just and unjust? A man does not call a line crooked unless he has some idea of a straight line.", "author": "C.S. Lewis", "author_slug": "cs-lewis", "tags": ["faith", "justice"]},
    {"text": "By not being aware of having a shadow, you declare a part of your personality to be non-existent. Then it enters the kingdom of the non-existent, which swells up and takes on enormous proportions…", "author": "Carl Jung", "author_slug": "carl-jung", "tags": ["psychology", "shadow"]},
    {"text": "The faster that you do the hard things you want to avoid, the faster you will receive the good things you actually want", "author": "Anonymous", "author_slug": "anonymous", "tags": ["action", "motivation"]},
    {"text": "The search for happiness is one of the chief sources of unhappiness.", "author": "Eric Hoffer", "author_slug": "eric-hoffer", "tags": ["happiness", "philosophy"]},
    {"text": "Nature loves courage. You make the commitment and nature will respond to that commitment by removing impossible obstacles. Dream the impossible dream and the world will not grind you under, it will lift you up.", "author": "Terence McKenna", "author_slug": "terence-mckenna", "tags": ["courage", "nature"]},
    {"text": "The foundation of all mental illness is the unwillingness to experience legitimate suffering.", "author": "Carl Jung", "author_slug": "carl-jung", "tags": ["psychology", "suffering"]}
]

# Endpoint 1: Random quote from the whole list
@app.route('/quote', methods=['GET'])
def get_random_quote():
    quote = random.choice(quotes)
    return jsonify(quote)

# Endpoint 2: Random quote by author
@app.route('/quote/author/<author>', methods=['GET'])
def get_quote_by_author(author):
    author_quotes = [q for q in quotes if q['author_slug'].lower() == author.lower()]
    if not author_quotes:
        return jsonify({"error": "Author not found"}), 404
    quote = random.choice(author_quotes)
    return jsonify(quote)

# Endpoint 3: Random quote by theme/tag
@app.route('/quote/theme/<theme>', methods=['GET'])
def get_quote_by_theme(theme):
    theme_quotes = [q for q in quotes if theme.lower() in [t.lower() for t in q['tags']]]
    if not theme_quotes:
        return jsonify({"error": "Theme not found"}), 404
    quote = random.choice(theme_quotes)
    return jsonify(quote)

# Endpoint 4: Full list of quotes
@app.route('/quotes', methods=['GET'])
def get_all_quotes():
    return jsonify(quotes)

if __name__ == '__main__':
    app.run(debug=True)