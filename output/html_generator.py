def export_html(timetable):
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="utf-8">
    <title>Timetable</title>
    </head>
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
