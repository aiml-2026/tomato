import streamlit as st
import os

# Set page layout to wide
st.set_page_config(layout="wide")

# Add custom CSS to set the background color to white
st.markdown(
    """
    <style>
    body {
        background-color: white;
    }
    </style>
    """, unsafe_allow_html=True
)

# List of filenames for your ZIP files
zip_files = ["1.zip", "2.zip", "3.zip", "4.zip", "5.zip",
             "6.zip", "7.zip", "8.zip","9.zip", "10.zip", "11.zip",
             "12.zip", "13.zip", "14.zip", "15.zip","16.zip","17.zip","18.zip","19.zip","20.zip"]

# List of new names for the downloaded files
download_names = ["A junior developer in your team has trouble setting up Node.js and npm on their system. How would you guide them through the installation and verify their setup using a simple script.zip", 
		  "Your team needs a lightweight server for testing API endpoints. Explain how you would create and deploy a basic Node.js server that responds with for incoming HTTP requests on port 4000.zip", 
                  "A client requests a simple API to differentiate GET and POST requests. Design a solution where the server returns GET request received for GET and POST request received for POST.zip",
		  "The team wants to fetch user data from an API and display it on a React page. How would you achieve this using the use Effect hook to fetch data only when the component is mounted.zip", 
                  "Your product manager wants a global theme switcher for light and dark modes. How would you implement this feature using React Context API.zip",
		  "A new React-based website needs separate pages for Home, About, and Contact. Explain how you would structure the application using React Router.zip", 
		  "Your project requires reading a configuration file asynchronously. Demonstrate the difference between callbacks and promises to achieve this, highlighting the pros and cons of each method.zip", 
                  "A team member needs a static website hosted on an Express.js application. How would you configure an Express server to serve files from a 'public' directory and handle routes for / and /about.zip", 
                  "The marketing team wants a Hello, React! banner on the company website. Create a React component for this requirement, explaining the process step-by-step.zip",
                  "Your task is to build a user profile card. How would you design a React component to display user details passed via props and toggle additional information using state.zip",
                  "A developer on your team needs to debug React lifecycle phases. Create a React component that logs specific messages during the mounting, updating, and unmounting phases.zip",
		  "Your application requires showing a warning message only when a specific condition is met. Build a React component with a button to toggle the message visibility using Boolean state.zip", 
		  "Build a counter component for a task tracker application. Include increment, decrement, and reset functionalities. How would you implement this using the useState hook.zip", 
                  "Design a RESTful API for a clock management system. Include endpoints to create, read, update, and delete clocks. How would you structure your code to ensure scalability and clarity.zip",
		  "Extend the clock management API to store data in MongoDB. How would you use Mongoose to define schemas, validate data, and implement CRUD operation.zip",
   	   	  "Build a full-stack application with a React frontend consuming data from your clock management REST API. How would you test the integration between the frontend and backend.zip",
		  "Your REST API frequently encounters errors when connecting to MongoDB. Implement middleware in Express to handle errors gracefully and log them for debugging.zip",
		  "You are working on a new development machine. After installing Node.js and npm, you run a script that prints Node.js is installed but receive an error saying node: command not found. What steps will you take to resolve the issue.zip",
                  "A QA engineer on your team requests unit tests for the counter component. How would you write tests for its increment, decrement, and reset functionalities.zip",
		  "Your team is ready to deploy the clock management app to production. What steps would you follow to build a RESTful API for managing a collection of clocks. Implement endpoints for creating, reading, updating, and deleting books.zip"]

# Directory where your ZIP files are stored
zip_directory = "./"  # Adjust this path

# Function to create download buttons for each file in two columns
def create_download_buttons():
    col1, col2 = st.columns(2)  # Create two columns for the layout
    for i, (zip_file, new_name) in enumerate(zip(zip_files, download_names)):
        zip_path = os.path.join(zip_directory, zip_file)
        
        if os.path.exists(zip_path):
            # Alternate between columns for each button
            column = col1 if i % 2 == 0 else col2

            with column:
                with open(zip_path, "rb") as f:
                    st.download_button(
                        label=f"{new_name}",
                        data=f,
                        file_name=new_name,
                        mime="application/zip"
                    )

# Streamlit app layout
st.title("NODE JS")  # Change the title
st.write("Click the buttons below to download the ZIP files:")

# Create individual buttons for each file in two columns
create_download_buttons()
