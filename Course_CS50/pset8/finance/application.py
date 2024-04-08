import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    user_id = session.get("user_id")
    all_rows = db.execute("SELECT symbol, SUM(amount) AS total_amount FROM shares WHERE id = :id GROUP BY symbol", id=user_id)
    rows = [row for row in all_rows if row['symbol'] != 'add cash']
    for row in rows:
        symbol = row["symbol"]
        # Отримання current_price за допомогою функції
        quote = lookup(symbol)
        if quote == None:
            return apology("Invalid symbol!", 400)
        else:
            current_price = quote["price"]
            #symbol = quote["symbol"]
            name = symbol #добавлена назва компанії на випадок корегування форми запиту котировок щоб повертала назву компанії
            # Додавання значень до рядка в результаті запиту
            amount = row["total_amount"]
            summ = current_price * amount
            row["current_price"] = current_price
            row["company"] = name
            row["summ"] = summ

    total_summ_shares = sum(row["summ"] for row in rows)
    rowsusers = db.execute("SELECT cash, username FROM users WHERE id = :id", id=user_id)
    cash = rowsusers[0]["cash"]
    username = rowsusers[0]["username"]
    total = cash + total_summ_shares
    # Передача результату на сторінку HTML для побудови таблиці
    return render_template('index.html', rows=rows, cash=cash, username=username, total=total, current_time=datetime.now())


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not (request.form.get("symbol") or request.form.get("shares")):
            return apology("must provide symbol and amount shares", 400)

        # Check if shares was a positive integer
        try:
            amount = int(request.form.get("shares"))
        except:
            return apology("shares must be a positive integer", 400)
        # Check if # of shares requested was 0
        if amount <= 0:
            return apology("can't buy less than or 0 shares", 400)
        
        symbol = request.form.get("symbol")
        quote = lookup(symbol)
        if quote == None:
            return apology("Invalid symbol!", 400)
        price = quote["price"]
        #symbol = quote["symbol"]
        name = quote["name"] #добавлена назва компанії на випадое корегування форми запиту котировок
        user_id = session.get("user_id")
        rows = db.execute("SELECT cash FROM users WHERE id = :id", id=user_id)
        cash = rows[0]["cash"]
        summ = price * amount
        if (cash - summ) < 0:
            return apology("you have no enough money", 400)
        else:
            new_cash = cash - summ
            db.execute("UPDATE users SET cash = :new_cash WHERE id = :user_id", new_cash=new_cash, user_id=user_id)
            db.execute("INSERT INTO shares (id, company, symbol, amount, price, summ, cash) VALUES (:id, :company, :symbol, :amount, :price, :summ, :cash)",
                        id=user_id, company=name, symbol=symbol, amount=amount, price=price, summ= -summ, cash=new_cash)
            return redirect("/")
    else:
        user_id = session.get("user_id")
        userrows = db.execute("SELECT username, cash FROM users WHERE id = :id", id=user_id)
        cash = userrows[0]["cash"]
        username = userrows[0]["username"]
        return render_template("buy.html", username=username, cash=cash)


@app.route("/check", methods=["GET"])
def check():
    """Return true if username available, else false, in JSON format"""
    username = request.args.get("username")
    rows = db.execute("SELECT * FROM users WHERE username = :username", username=username)
    if username.strip() and len(rows) == 0: #користувача з таким ім'ям не існує
        return jsonify(True)
    else:
        return jsonify(False)


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_id = session.get("user_id")
    rows_user = db.execute("SELECT username FROM users WHERE id = :id", id=user_id)
    username = rows_user[0]["username"]
    rows = db.execute("SELECT * FROM shares WHERE id = :id", id=user_id)
    for row in rows:
        amount = row["amount"]
        if amount <= 0:
            row["sell"] = -amount
        else:
            row["buy"] = amount

    return render_template('history.html', rows=rows, username=username, current_time=datetime.now())

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "GET":
        return render_template("quote.html")
    elif request.method == "POST":
        symbol = request.form.get("symbol")
        if not request.form.get("symbol"):
            return apology("Please, provide symbol", 400)
        quote = lookup(symbol)
        if quote == None:
            return apology("Invalid symbol!", 400)
        #price = date["price"]
        #symbol = date["symbol"]
        price = quote["price"]
        return render_template("quoted.html", price=price, symbol=symbol)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

     # Forget any user_id
    session.clear()

    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        username = request.form.get("username")
        if not request.form.get("username"):
            return apology("must provide username", 400)
        rows = db.execute("SELECT * FROM users WHERE username = :username", username=username)
        if len(rows) != 0: #користувач з таким ім'ям вже існує
            return apology("Username already taken", 400)
        # користувач з таким ім'ям не існує
        password = request.form.get("password")
        if not request.form.get("password"):
            return apology("must provide password", 400)
        confirm_password = request.form.get("confirmation")
        # Перевірка, чи обидва паролі співпадають
        if password != confirm_password:
            return "Passwords do not match", 400
        hashed_password = generate_password_hash(password)
            # Збереження нового користувача
        db.execute("INSERT INTO users (username, hash) VALUES (:username, :hash)", username=username, hash=hashed_password)
        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))
        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]
    return redirect("buy")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        # Ensure username was submitted
        if not (request.form.get("symbol") and request.form.get("shares")):
            return apology("must provide symbol and amount shares", 400)
        symbol = request.form.get("symbol")
        quote = lookup(symbol)
        if quote == None:
            return apology("Invalid symbol!", 400)
        price = quote["price"]
        #symbol = quote["symbol"]
        name = symbol
        amount=float(request.form.get("shares"))
        if amount <= 0:
            return apology("you must provide integer number", 400)
        # Виконання SQL-запиту на підрахунок наявності необхідної кількості певних акцій
        user_id = session.get("user_id")
        rows = db.execute("SELECT SUM(amount) AS total_amount FROM shares WHERE id = :id AND symbol = :symbol",
                  id=user_id, symbol=symbol)
        # Отримання суми значення amount для визначеного id та symbol
        total_amount = rows[0]["total_amount"] if rows else None
        if total_amount < amount:
            return apology("you don't have enough shares", 400)
        else:
            summ = price * amount
            rows = db.execute("SELECT cash FROM users WHERE id = :id", id=user_id)
            cash = rows[0]["cash"]
            new_cash = cash + summ
            db.execute("UPDATE users SET cash = :new_cash WHERE id = :user_id", new_cash=new_cash, user_id=user_id)
            db.execute("INSERT INTO shares (id, company, symbol, amount, price, summ, cash) VALUES (:id, :company, :symbol, :amount, :price, :summ, :cash)",
                        id=user_id, company=name, symbol=symbol, amount= -amount, price=price, summ=summ, cash=new_cash)
            return redirect("/")
    else:
        user_id = session.get("user_id")
        all_rows = db.execute("SELECT symbol FROM shares WHERE id = :id GROUP BY symbol", id=user_id)
        rows = [row for row in all_rows if row['symbol'] != 'add cash']
        return render_template("sell.html", rows=rows)

@app.route("/add", methods=["GET", "POST"])
@login_required
def add():
    """Add cash"""
    if request.method == "POST":
        # Ensure add was submitted
        if not (request.form.get("positive_number")):
            return apology("must provide summ of cash", 400)
        addcash = float(request.form.get("positive_number"))
        print(addcash)
        user_id = session.get("user_id")
        rows = db.execute("SELECT cash FROM users WHERE id = :id", id=user_id)
        cash = rows[0]["cash"]
        new_cash = cash + addcash
        db.execute("UPDATE users SET cash = :new_cash WHERE id = :user_id", new_cash=new_cash, user_id=user_id)
        db.execute("INSERT INTO shares (id, company, symbol, amount, price, summ, cash) VALUES (:id, :company, :symbol, :amount, :price, :summ, :cash)",
                        id=user_id, company="Add cash", symbol="add cash", amount= 0, price=0, summ=addcash, cash=new_cash)
        return redirect("/")
    else:
        user_id = session.get("user_id")
        userrows = db.execute("SELECT username, cash FROM users WHERE id = :id", id=user_id)
        cash = userrows[0]["cash"]
        username = userrows[0]["username"]
        return render_template("add.html", username=username, cash=cash)


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
