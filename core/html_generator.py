import os

def export_html(timetable):
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="utf-8">
    <title>Timetable</title>
    </head>
    <style>
    table {
    border-collapse: collapse;
    margin-bottom: 30px;
    }

    th, td {
        border: 1px solid black;
        padding: 8px;
        text-align: center;
        vertical-align: middle;
        padding: 8px;
    }

    th {
        background-color: #f0f0f0;
    }
    
    h1{
        margin-top: 30px;
        font-size: 24px;
    </style>
    <body>
    
    """

    for sections, schedule in timetable.items():
        html += f"<h1>{sections}</h1>"
        html += "<table border='1'>\n"
        html += """
            <tr>
            <th>Day</th>
            <th>P1</th>
            <th>P2</th>
            <th>P3</th>
            <th>P4</th>
            <th>P5</th>
            <th>P6</th>
            <th>P7</th>
            <th>P8</th>
            </tr>
        """

        for day, periods in schedule.items():
            html += f"<tr><td>{day}</td>\n"

            for period in periods:
                subject, teacher = periods[period]
                html += f"<td>{subject}<br>{teacher}</td>\n"

            html += "</tr>"
        html += "</table>"

    html += """
        </body>
        </html>
    """

    with open("timetable.html" , "w") as file:
        file.write(html)


def send_file(file, destination):
    source_file = file
    destination_dir = destination
    file_name = os.path.basename(source_file)

    destination_file = os.path.join(destination_dir, file_name)

    try:
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)

        os.replace(source_file, destination_file)
        print(f"Successfully moved to {destination_file}")

    except FileNotFoundError:
        print("The source file does not exist.")
    except PermissionError:
        print("Permission denied.")

