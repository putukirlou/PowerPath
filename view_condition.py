import os
import sqlite3
from functools import wraps
from flask import Flask, render_template, request, current_app, redirect

def condition(cursor, connection, args):
    args["title"] = "Список состояния станций заряда для электромобилей"

    query = (
        f"SELECT * FROM atm;"
    )
    cursor.execute(query)
    condition = cursor.fetchall()
    args["condition"] = condition

    if request.method == "GET":
        return render_template("condition.html", args=args)
    elif request.method == "POST":
        return render_template("condition.html", args=args)