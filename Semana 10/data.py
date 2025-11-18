import json

def export_to_json(students):
    try:
        if len(students) > 0:
            filename = 'students_data.json'

            with open(filename, 'w') as json_file:
                json.dump(students, json_file, indent=4)
            
            print(f"Students data successfully exported to {filename}")
        else:
            print("No student data to export.")
        input("Press enter key to exit")

    except TypeError as e:
        print(f"Error exporting to JSON: {e}")
        input("Press enter key to exit")


def import_from_json(filename):
    try:
        with open(filename, 'r') as json_file:
            data_dict = json.load(json_file)
        print(data_dict)
        input("Press enter key to exit")
        return data_dict
    except FileNotFoundError as e:
        print(f"Error: File not found. {e}")
        input("Press enter key to exit")
        return []
