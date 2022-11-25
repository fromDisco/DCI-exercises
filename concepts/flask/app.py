from flask import Flask, jsonify, request, session, redirect
import psycopg2


# instantiating a class (Flask)
app = Flask(__name__)


def db_connection(request):
    try: 
        connection = psycopg2.connect(
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432",
            database="flask_intro1",
        )

        return connection, connection.cursor()

    except psycopg2.OperationalError as db_error:
        print("#########################")
        print("#########################")
        print(request.access_route)
        print("#########################")
        print("#########################")
        redirect(request.access_route, db_error) 
        # feedback = db_error 
        # print("_________________")
        # print(feedback)
        # print("_________________")
        # connection = None
        # return feedback, 9


@app.route("/")
def index():
    connection, cur = db_connection()

    # Fetch all the reminders from the database
    cur.execute("SELECT id, title, description FROM reminders")
    reminder_data = cur.fetchall()
    reminder_data = [
        {"id": item[0], "title": item[1], "description": item[2]}
        for item in reminder_data
    ]

    return jsonify({"reminders": reminder_data})


# Decorator -- URL path call add-reminder
@app.route("/add-reminder", methods=["POST"])
def add_reminder():
    connection, cur = db_connection()

    try:
        title = request.json["title"]
    except KeyError:
        title = None

    # handle the exception (error handling)
    try:
        description = request.json["description"]
    except KeyError:
        description = None
    cur.execute(
        f"INSERT INTO reminders (title, description) VALUES('{title}', '{description}') RETURNING id, title, description;"
    )
    connection.commit()
    values = cur.fetchone()

    values_dict = {"id": values[0], "title": values[1], "description": values[2]}
    # change the return value from empty list to have REMINDERS instead
    return jsonify(values_dict)


@app.route("/reminders/<int:id>")
def reminder(id):
    connection, cur = db_connection()

    cur.execute(f"SELECT title, description FROM reminders WHERE id = {id};")
    reminder_data = cur.fetchone()

    if not reminder_data:
        return jsonify({"message": "Reminder not found"}), 404
    try:
        reminder_dict = {
            "id": id,
            "title": reminder_data[0],
            "description": reminder_data[1],
        }
        return jsonify(reminder_dict)
    except:
        return jsonify({"message": "Sorry something bad happened"}), 500


# DELETE
@app.route("/reminders/<int:id>", methods=["DELETE"])
def delete_reminder(id):
    connection, cur = db_connection()
    cur.execute(f"DELETE FROM reminders WHERE id={id};")
    # commit the changes
    connection.commit()
    return jsonify({"message": "Successfully deleted!"})


@app.route("/reminders/<int:id>/update", methods=["PUT"])
def update_reminder(id):

    connection, cur = db_connection(request)

    # reads all column names of table
    list_table_column_names = """SELECT column_name FROM 
    information_schema.columns WHERE table_name='reminders'"""
    cur.execute(list_table_column_names)

    # flatten the response tuple
    # response is a list of tuples in following pattern:
    # ('column_name', ), so element[0] reads first element
    table_rows_list = [element[0] for element in cur.fetchall()]

    # if there are errors, feedback gives information
    feedback = {"expected_columns": [row for row in table_rows_list]}

    # if key_error stays false, feedback can be deleted
    key_error = False

    # check if every row of table list has its counterpart in response.json
    for row in table_rows_list:
        if "id" in row:
            # jump over 'id'
            # id is given as an argument, not through request
            continue

        try:
            request.json[row]
        except KeyError:
            feedback.update(
                {"--> ERROR missing declaration for row": {row: request.json.get(row)}}
            )
            key_error = True
            continue

    # check if request.json contains an invalid column
    for key in request.json.keys():
        if key not in table_rows_list:
            feedback.update({"--> ERROR no such key": {key: "Column not recognized."}})
            key_error = True

    # if any errors accured, return with error message
    if key_error:
        return jsonify(feedback), 500

    # empty feedback, because missing user has different error message
    feedback = {}

    cur.execute(
        f"""
        UPDATE reminders
        SET title='{request.json.get('title')}', 
        description='{request.json.get('description')}'
        WHERE id={id} RETURNING id, title, description
    """
    )

    values = cur.fetchone()
    connection.commit()

    if not values:
        feedback.update({"--> ERROR 400": f"no user id=={id}"})
        return jsonify(feedback)

    return jsonify({"id": values[0], "title": values[1], "description": values[2]})


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5050)  # port for flask
