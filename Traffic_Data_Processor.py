# Task A: Input Validation
import tkinter as tk


def validate_date_input():
    """
    Prompts the user for a date in DD MM YYYY format, validates the input for:
    - Correct data type
    - Correct range for day, month, and year
    """
    day = 0
    month = 0
    year = 0

    # loop for day
    while True:
        try:
            day = int(
                input("\nPlease enter the day of the survey in the format DD: "))
            if day not in range(1, 32):
                print('Out of range - values must be in the range 1 and 31')
                continue
            break
        except ValueError:
            print('Integer required')

    # loop for month
    while True:
        try:
            month = int(
                input("Please enter the month of the survey in the format MM: "))
            if month not in range(1, 13):
                print('Out of range - values must be in the range 1 and 12')
                continue
            break
        except ValueError:
            print('Integer required')

    # loop for year
    while True:
        try:
            year = int(
                input("Please enter the year of the survey in the format YYYY: "))
            if year not in range(2000, 2025):
                print('Out of range - values must be in the range 2000 and 2024')
                continue
            break
        except ValueError:  # 1.(www.turing.com, n.d.)
            print('Integer required')

    # formatting values into 2 digits
    day = f"{day:02d}"
    month = f"{month:02d}"
    year = f"{year:04d}"
    histogram_date = (f"{day}/{month}/{year}")
    csv_file_name = (f"traffic_data{day}{month}{year}.csv")

    return (csv_file_name, histogram_date)


def validate_continue_input():
    """
    Prompts the user to decide whether to load another dataset:
    - Validates "Y" or "N" input
    """
    # getting user input
    choice = input(
        "Do you want to select another data file for a different date?(Y/N): ")
    choice = choice.upper()

    return (choice)

# Task B: Processed Outcomes


def process_data(csv_file_name):
    """
    Processes the CSV data for the selected date and extracts data
    """

    # intializing variables and dictionary to store requested data
    total_vehicles = 0
    total_trucks = 0
    total_electric_vehicles = 0
    total_two_wheeled_vehicles = 0
    busses_northElm_heading_north = 0
    vehicles_going_straight = 0
    truck_percentage = 0
    total_bicycles = 0
    avg_bicycles = 0
    over_limit_count = 0
    total_vehicles_elm_rabbit_road = 0
    total_vehicles_hanley_westway_road = 0
    scooter_percentage = 0
    scooter_count = 0
    rain_hours_list = []
    rain_hours = 0
    hourly_counts_Hanley = {}
    hourly_counts_Elm = {}
    outcomes = []

    # error handling if the file does not exist
    try:
        # importing data from the CSV file
        csv_file = open(f"{csv_file_name}", "r")
        data_set = csv_file.readlines()  # 2.(www.w3schools.com, n.d.)
        csv_file.close()

        # removing newline characters & splitting data into list
        for i in range(len(data_set)):
            data_set[i] = data_set[i].strip()
            data_set[i] = data_set[i].split(",")   # 3.(ChatGPT, 2024)

        # removing header
        data_set.pop(0)

        # looping through traffic data
        for i in data_set:
            # total number of vehicles
            total_vehicles += 1

            # total number of trucks
            if i[8] == 'Truck':
                total_trucks += 1

            # tot of electric vehicles
            if i[9] == 'True':
                total_electric_vehicles += 1

            # tot of two-wheeled vehicles
            if i[8] == "Motorcycle" or i[8] == "Bicycle" or i[8] == "Scooter":
                total_two_wheeled_vehicles += 1

            # tot of Busses leaving Elm Avenue/Rabbit Road heading North
            if i[8] == "Buss" and i[0] == "Elm Avenue/Rabbit Road" and i[4] == "N":
                busses_northElm_heading_north += 1

            # tot of Vehicles through both junctions not turning left or right
            if i[3] == i[4]:
                vehicles_going_straight += 1

            # avg of bicycles
            if i[8] == "Bicycle":
                total_bicycles += 1

            # over the limit count
            if int(i[7]) > int(i[6]):
                over_limit_count += 1

            # total only Elm Avenue/Rabbit Road
            if i[0] == "Elm Avenue/Rabbit Road":
                total_vehicles_elm_rabbit_road += 1

            # total only Hanley Highway/Westway
            if i[0] == "Hanley Highway/Westway":
                total_vehicles_hanley_westway_road += 1

            # perc of scooters going through Elm Avenue/Rabbit Road
            if i[0] == "Elm Avenue/Rabbit Road" and i[8] == "Scooter":
                scooter_count += 1
                scooter_percentage = int(
                    (scooter_count/total_vehicles_elm_rabbit_road)*100)

            # saving hour and vehicle count into a dictionary
            if i[0] == "Hanley Highway/Westway":
                hour = i[2].split(":")[0]  # learned from chatgpt
                if hour not in hourly_counts_Hanley:
                    hourly_counts_Hanley[hour] = 1
                else:
                    hourly_counts_Hanley[hour] += 1

            if i[0] == "Elm Avenue/Rabbit Road":
                hour = i[2].split(":")[0]  # learned from chatgpt
                if hour not in hourly_counts_Elm:
                    hourly_counts_Elm[hour] = 1
                else:
                    hourly_counts_Elm[hour] += 1

            # The total number of hours of rain on the selected date
            if i[5] == 'Light Rain' or i[5] == "Heavy Rain":
                rain_hour = i[2].split(":")[0]
                if rain_hour not in rain_hours_list:
                    rain_hours_list.append(rain_hour)

        # truck percentage
        truck_percentage = round((total_trucks/total_vehicles)*100)

        # total of bicycles
        avg_bicycles = int(round((total_bicycles/24), 2))

        # getting the peak hour vehicle count
        # 4.(note.nkmk.me, 2023)
        max_vehicles_in_hour = max(hourly_counts_Hanley.values())

        # getting the peak hour
        # 5.(note.nkmk.me, 2023)
        peak_hour = int(
            max(hourly_counts_Hanley, key=hourly_counts_Hanley.get))
        peak_time = (f"{peak_hour}:00 and {peak_hour+1}:00")

        # getting rain hours count
        rain_hours = len(rain_hours_list)

        # saving all output into a list
        outcomes = [total_vehicles, total_trucks, total_electric_vehicles, total_two_wheeled_vehicles, busses_northElm_heading_north, vehicles_going_straight, truck_percentage, avg_bicycles, over_limit_count,
                    total_vehicles_elm_rabbit_road, total_vehicles_hanley_westway_road, scooter_percentage, peak_time, max_vehicles_in_hour, rain_hours, csv_file_name, hourly_counts_Hanley, hourly_counts_Elm]

    except FileNotFoundError:
        outcomes = "error"
        print(f"\nThe file {
              csv_file_name} was not found in the specified location. Please check for the correct date and try again.\n")
    except ZeroDivisionError:
        outcomes = "error"
        print("\nThe file is empty. Please check for the correct date and try again.\n")
    except ValueError:
        outcomes = "error"
        print("\nThe file is not in the correct format . Please check the file and try again.\n")
    return outcomes


def display_outcomes(outcomes):
    """
    Displays the calculated outcomes in a clear and formatted way.
    """

    # assigning all output to a variable
    print_to_idle = (f"""

data file selected is: {outcomes[15]}


The total number of vehicles recorded for this date is: {outcomes[0]}
The total number of trucks recorded for this date is: {outcomes[1]}
The total number of electric vehicles for this date is: {outcomes[2]}
The total number of two-wheeled vehicles for this date is: {outcomes[3]}
The total number of Busses leaving Elm Avenue/Rabbit Road heading North is: {outcomes[4]}
The total number of Vehicles through both junctions not turning left or right is: {outcomes[5]}
The percentage of total vehicles recorded that are trucks for this date is: {outcomes[6]}%
the average number of Bikes per hour for this date is: {outcomes[7]}
The total number of Vehicles recorded as over the speed limit for this date is: {outcomes[8]}
The total number of vehicles recorded through Elm Avenue/Rabbit Road junction is: {outcomes[9]}
The total number of vehicles recorded through Hanley Highway/Westway junction is: {outcomes[10]}
{outcomes[11]}% of vehicles recorded through Elm Avenue/Rabbit Road are scooters.
The highest number of vehicles in an hour on Hanley Highway/Westway is {outcomes[13]}
The most vehicles through Hanley Highway/Westway were recorded between {outcomes[12]}
The number of hours of rain for this date is: {outcomes[14]}

*******************************************************************************************************
""")

    print(print_to_idle)

    return print_to_idle

# Task C: Save Results to Text File


def save_results_to_file(print_to_idle):
    """
    Saves the processed outcomes to a text file and appends if the program loops.
    """
    # saving the output list line by line to a list
    save_to_text = print_to_idle.splitlines()  # 6.(ChatGPT, 2024)

    # opening file to write data
    results = open("results.txt", "a")

    # writing the data into the text file
    for i in save_to_text:
        results.write(i+"\n")

    # closing the file
    results.close()

    return ()


# Task D: Histogram Display


class HistogramApp:
    def __init__(self, traffic_data, date):
        """
        Initializes the histogram application with the traffic data and selected date.
        """
        # asssigning the data to variables
        self.traffic_data = traffic_data
        self.date = date

        # creating a tkinter window and title
        self.root = tk.Tk()
        self.root.title("Traffic Histogram")
        self.canvas = None

        # bringing the window to the front
        self.root.lift()
        self.root.attributes('-topmost', True)  # 7.(GeeksforGeeks, 2024)
        self.root.attributes('-topmost', False)  # 7.(GeeksforGeeks, 2024)

        # calling functions to setup the window, draw the histogram and add legend
        self.setup_window()
        self.draw_histogram()
        self.add_legend()

    def setup_window(self):
        """
        Sets up the Tkinter window and canvas for the histogram.
        """
        self.canvas = tk.Canvas(self.root, width=1000, height=570, bg='white')
        self.canvas.pack(fill='both', expand=True)  # 8.(GeeksforGeeks, 2019)

    def draw_histogram(self):
        """
        Draws the histogram with axes, labels, and bars.
        """
        # setting canvas size and margins
        margin = 100
        width = 1000
        height = 520
        bar_width = 30

        # getiing data from traffic_data dictionary
        elm_avenue_data = self.traffic_data.get(
            'Elm Avenue/Rabbit Road', [0] * 24)
        henley_highway_data = self.traffic_data.get(
            'Henley Highway/Westway', [0] * 24)

        # finding max value to scale the bars
        max_value = max(max(elm_avenue_data), max(henley_highway_data))
        scale_factor = (height - 2 * margin) / \
            max_value if max_value > 0 else 1  # (ChatGPT, 2024)

        # adjusting bar spacing to remove useless space
        bar_spacing = (width - 2 * margin) / (23)

        # drawing X axis
        self.canvas.create_line(margin, height - margin,
                                width - margin, height - margin, width=2)

        # drawing bars and labels
        for i in range(24):
            x = margin + i * bar_spacing  # Base x-position for this hour

            # Elm Avenue bars (green)
            elm_height = elm_avenue_data[i] * scale_factor
            self.canvas.create_rectangle(
                x - bar_width / 2, height - margin - elm_height,
                x, height - margin,
                fill='#95e895',
                outline='#05A205'
            )

            # value label for Elm Avenue
            self.canvas.create_text(
                x - bar_width / 4, height - margin - elm_height - 10,
                text=str(elm_avenue_data[i]),
                font=('Arial', 8, 'bold'),
                fill='#05A205'
            )

            # Henley Highway bars (blue)
            henley_height = henley_highway_data[i] * scale_factor
            self.canvas.create_rectangle(
                x, height - margin - henley_height,
                x + bar_width / 2, height - margin,
                fill='#2ca4f3',
                outline='#00568F'
            )

            # value label for Henley Highway
            self.canvas.create_text(
                x + bar_width / 4, height - margin - henley_height - 10,
                text=str(henley_highway_data[i]),
                font=('Abadi', 8, 'bold'),
                fill='#2ca4f3'
            )

            # drawing hour labels
            self.canvas.create_text(
                x, height - margin + 20,
                text=str(i),
                font=('Abadi', 8)
            )

        # chart title
        self.canvas.create_text(
            300, 30,
            text=f'Histogram of Vehicle Frequency per Hour ({self.date})',
            font=('Abadi', 15, 'bold')
        )

        # label for X-axis
        self.canvas.create_text(
            width / 2, height - 20,
            text='Hours 00:00 to 23:00',
            font=('Abadi', 11, 'bold'),
            fill='#4b4d4b'
        )

    def add_legend(self):
        """
        Adds a legend to the histogram to indicate which bar corresponds to which junction.
        """
        # setting the initial position for the legend
        legend_x = 70
        legend_y = 60

        # Elm Avenue
        self.canvas.create_rectangle(
            legend_x, legend_y, legend_x + 20, legend_y + 20,
            fill='#95e895', outline='#05A205'
        )
        self.canvas.create_text(
            legend_x + 30, legend_y + 10,
            text='Elm Avenue/Rabbit Road',
            anchor='w',
            font=('Abadi', 11)
        )
        # Henley Highway
        self.canvas.create_rectangle(
            legend_x, legend_y + 30, legend_x + 20, legend_y + 50,
            fill='#2ca4f3', outline='#00568F'
        )
        self.canvas.create_text(
            legend_x + 30, legend_y + 40,
            text='Henley Highway/Westway',
            anchor='w',
            font=('Abadi', 11)
        )

    def run(self):
        """
        Runs the Tkinter main loop to display the histogram.
        """
        # start the Tkinter main event loop
        self.root.mainloop()  # 9.(Welcome to python-forum.io, 2016)

# Task E: Code Loops to Handle Multiple CSV Files


class MultiCSVProcessor:
    def __init__(self):
        """
        Initializes the application for processing multiple CSV files.
        """
        self.traffic_data = None  # stores vehicle count data for each junction
        self.histogram_date = None  # date for the histogram

    def load_csv_file(self):
        """
        Loads a CSV file and processes its data.
        """
        # getting user inputs
        csv_file_name, histogram_date = validate_date_input()

        # processing the data from the CSV file
        outcomes = process_data(csv_file_name)

        # restart if the file is not found
        if outcomes == "error":
            return self.load_csv_file()

        # extracting the vehicle count data for each junction
        vehicle_count_hanley, vehicle_count_elm = outcomes[16], outcomes[17]

        # updating traffic data with extracted values
        self.traffic_data = {
            "Elm Avenue/Rabbit Road": list(vehicle_count_elm.values()),
            "Henley Highway/Westway": list(vehicle_count_hanley.values())
        }

        # updating the histogram date
        self.histogram_date = histogram_date

        # display and save the processed outcomes
        print_to_idle = display_outcomes(outcomes)
        save_results_to_file(print_to_idle)

        return self.traffic_data, self.histogram_date

    def clear_previous_data(self):
        """
        Clears data from the previous run to process a new dataset.
        """
        # reset the data for the next run
        self.traffic_data = None
        self.histogram_date = None

    def handle_user_interaction(self):
        """
        Handles user input for processing multiple files.
        """
        # prompts user to continue or quit
        choice = validate_continue_input()

        if choice == "N":
            print("\nProgram terminated.")
            return False

        elif choice == "Y":
            # clear previous data before processing new files
            self.clear_previous_data()
            return True

        else:
            print("\nInvalid input. Please enter Y or N")
            return self.handle_user_interaction()

    def process_files(self):
        """
        Main loop for handling multiple CSV files until the user decides to quit.
        """
        while True:
            self.traffic_data, self.histogram_date = self.load_csv_file()
            print("Close the histogram window to continue.\n")
            app = HistogramApp(self.traffic_data, self.histogram_date)
            app.run()
            print("Results saved to the text file.\n")

            if not self.handle_user_interaction():
                break


# Starting the program
if __name__ == "__main__":
    processor = MultiCSVProcessor()
    processor.process_files()

# Rereferences
"""
 1. www.turing.com. (n.d.). What is ValueError in Python & How to fix it.
  [online] Available at: https://www.turing.com/kb/valueerror-in-python-and-how-to-fix.
  [Accessed 25 November 2024]

 2. www.w3schools.com. (n.d.). Python File readlines() Method.
  [online] Available at: https://www.w3schools.com/python/ref_file_readlines.asp.
  [Accessed 28 November 2024]

 3. ChatGPT. (2024). ChatGPT - Split string into list.
  [online] Available at: https://chatgpt.com/share/67542855-90d4-800c-a288-276cdf2d0132 
  [Accessed 31 November 2024].

 4. note.nkmk.me. (2023). Get maximum/minimum values and keys in Python dictionaries | note.nkmk.me.
  [online] Available at: https://note.nkmk.me/en/python-dict-value-max-min/.
  [Accessed 31 November 2024].

‌ 5. note.nkmk.me. (2023). Get maximum/minimum values and keys in Python dictionaries | note.nkmk.me.
  [online] Available at: https://note.nkmk.me/en/python-dict-value-max-min/.
  [Accessed 22 November 2024].

‌ 6. ChatGPT. (2024). ChatGPT - Split string into list.
  [online] Available at: https://chatgpt.com/share/67542855-90d4-800c-a288-276cdf2d0132 
  [Accessed 20 November 2024].

 7. GeeksforGeeks (2024). Make a Tkinter Window Jump to the Front.
  [online] GeeksforGeeks. Available at: https://www.geeksforgeeks.org/make-a-tkinter-window-jump-to-the-front/?utm_source=chatgpt.com
  [Accessed 5 Dec. 2024].

 8. GeeksforGeeks (2019). Python | pack() method in Tkinter.
  [online] GeeksforGeeks. Available at: https://www.geeksforgeeks.org/python-pack-method-in-tkinter/?utm_source=chatgpt.com 
  [Accessed 5 Dec. 2024].
 
 9.‌ Welcome to python-forum.io. (2016). main lop in python tkinter.
  [online] Available at: https://python-forum.io/thread-36168.html 
  [Accessed 11 Dec. 2024].
‌‌"""
