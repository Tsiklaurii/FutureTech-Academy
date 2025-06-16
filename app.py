from flask import Flask, render_template

app = Flask(__name__)

courses = [
    {"id": 0, "name": "Python კურსი", "price": 3200, "prof": "დავით ინანაშვილი", "img":"https://i.pinimg.com/736x/f6/7f/be/f67fbe635aa1c06e99b90e66def65761.jpg", "description":"სწავლა იწყება საფუძვლებიდან და გეხმარება ნაბიჯ-ნაბიჯ გადახვიდე პრაქტიკულ ცოდნაზე. კურსი მოიცავს ისეთ თემებს, როგორებიცაა: ცვლადები, პირობითი ოპერატორები, ციკლები, ფუნქციები, ფაილური სისტემასთან მუშაობა და ობიექტზე ორიენტირებული პროგრამირება. დავალებები აგებულია რეალურ მაგალითებზე, ხოლო პროექტები გეხმარება პორტფოლიოს შექმნაში.", "date":"1 აგვისტო - 30 მაისი"},
    {"id": 1, "name": "ვებ-დეველოპმენტის კურსი", "price": 800, "prof": "გიორგი თამარაშვილი", "img":"https://i.pinimg.com/736x/42/ca/3f/42ca3f46f4cee593361ac54785cda7d8.jpg", "description":"ეს კურსი გაძლევს საშუალებას შექმნა თანამედროვე, რეაგირებადი ვებსაიტები HTML, CSS და JavaScript-ის გამოყენებით. ნაბიჯ-ნაბიჯ შეისწავლი სტრუქტურირებას, სტილიზაციას და ინტერაქციულ ფუნქციებს. კურსის ბოლოს შეგეძლება შექმნა საკუთარი პორტფოლიოს ვებსაიტი და დაამზადო მცირე პროექტები რეალური დიზაინის მიხედვით." , "date":"3 ივლისი - 30 დეკემბერი"},
    {"id": 2, "name": "ციფრული მარკეტინგის კურსი", "price": 2000, "prof": "ლიკა კიკნაძე", "img":"https://i.pinimg.com/736x/82/d5/62/82d562e85a3d9cbd1f0570ce404836b6.jpg", "description":"ეს კურსი გასწავლით როგორ გამოიყენო სოციალური მედია, საძიებო სისტემები და რეკლამა ონლაინ სივრცეში ბიზნესის გასაზრდელად. სწავლობთ SEO-ს, Google Ads-ს, Meta Ads-ს, იმეილ მარკეტინგსა და ანალიტიკას. კურსის ბოლოს შეძლებთ კამპანიების დაგეგმვას, შესრულებას და შედეგების გაზომვას.", "date":"3 აგვისტო - 3 მარტი"},
    {"id": 3, "name": "ინტერიერის დიზაინის კურსი", "price": 900, "prof": "ლადო კერესელიძე", "img":"https://i.pinimg.com/736x/06/8c/66/068c6667b3661966c151e511727e64b2.jpg", "description":"აღმოაჩინე სივრცის დიზაინის სამყარო! კურსი გასწავლის ფერთა თეორიას, განლაგების წესებს, განათებისა და მასალების შერჩევას. შეისწავლი როგორც ხელით ესკიზების შექმნას, ისე პროგრამებით მუშაობას (AutoCAD, SketchUp). კურსის ბოლოს შეძლებ მოამზადო საკუთარი დიზაინ-პროექტი რეალურ სივრცეზე დაფუძნებით.", "date":"11 ივნისი - 1 იანვარი"},
]

@app.route("/")
def index():
    return render_template("index.html", courses=courses)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/blogdetails")
def blogdetails():
    return render_template("blogdetails.html")

@app.route("/career")
def career():
    return render_template("career.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/registration")
def registration():
    return render_template("registration.html")

@app.route("/view/<int:courses_index>")
def view_course(courses_index):
    chosen_course = courses[courses_index]
    return render_template("view_course.html", course=chosen_course)

app.run(debug=True)