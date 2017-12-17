import feedparser
import flask

app = flask.Flask(__name__)

RSS_FEEDS = {
    "bbc": "http://feeds.bbci.co.uk/news/rss.xml",
    "cnn": "http://rss.cnn.com/rss/edition.rss",
    "fox": "http://feeds.foxnews.com/foxnews/latest",
    "iol": "http://www.iol.co.za/cmlink/1.640"
}


@app.route("/")
@app.route("/<publication>")
def get_news(publication="bbc"):
    feed = feedparser.parse(RSS_FEEDS[publication])
    first_article = feed["entries"][0]
    return """
    <html>
    <body>
        <h1>Headlines</h1>
        <b>{title}</b></br>
        <i>{published}</i></br>
        <p>{summary}</p></br>
    </body>
    </html>
    """.format(title=first_article.get("title"), published=first_article.get("published"), summary=first_article.get("summary"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
